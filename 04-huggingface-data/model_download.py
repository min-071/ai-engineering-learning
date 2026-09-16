from huggingface_hub import hf_hub_download, snapshot_download

# Download and cache one model file
model_path = hf_hub_download(
    repo_id="sentence-transformers/all-MiniLM-L6-v2",
    filename="config.json"
)

print(f"Cached at: {model_path}")

# Download and cache the full model
model_dir = snapshot_download(
    "sentence-transformers/all-MiniLM-L6-v2"
)

print(f"Full model at: {model_dir}")

