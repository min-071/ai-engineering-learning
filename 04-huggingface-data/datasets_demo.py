from datasets import load_dataset

# 1. Load the IMDb training dataset
dataset = load_dataset("stanfordnlp/imdb", split="train")

print(f"Total examples: {len(dataset)}")

# 2. Create train, validation, and test splits
split = dataset.train_test_split(test_size=0.2, seed=42)
train_val = split["train"].train_test_split(test_size=0.125, seed=42)

train_ds = train_val["train"]
val_ds = train_val["test"]
test_ds = split["test"]

print(f"Train: {len(train_ds)}")
print(f"Validation: {len(val_ds)}")
print(f"Test: {len(test_ds)}")

# 3. Stream Wikipedia instead of downloading the entire dataset
wiki = load_dataset(
    "wikimedia/wikipedia",
    "20231101.en",
    split="train",
    streaming=True
)

print("\nFirst 5 Wikipedia articles:")

for i, example in enumerate(wiki):
    print(example["title"])

    if i >= 4:
        break

