import yaml
from openai import OpenAI

def load_cfg(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def nim_client(cfg, role):
    base = cfg.get("NIM_BASE").rstrip("/")
    model = cfg[f"{role}_MODEL"]
    api_key = cfg["NIM_API_KEY"]
    base_url = f"{base}/nim/{model}"
    return OpenAI(base_url=base_url, api_key=api_key)
