import os, json
from tqdm import tqdm
from scripts.utils import load_cfg

def main():
    cfg = load_cfg("configs/nim_config.yaml")
    paths = cfg["DATA_PATHS"]
    out_path = paths["COMBINED"]
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    print("🔄 Loading datasets from config ...")
    dist = json.load(open(paths["DISTILLED"])) if os.path.exists(paths["DISTILLED"]) else []
    struct = json.load(open(paths["STRUCTURED"])) if os.path.exists(paths["STRUCTURED"]) else []

    print(f"  → {len(dist)} distilled pairs")
    print(f"  → {len(struct)} structured pairs")

    combined = []
    for ex in dist:
        combined.append({
            "question": ex.get("question"),
            "answer": ex.get("teacher", ex.get("answer")),
            "meta": {"source": "distilled"}
        })
    for ex in struct:
        combined.append({
            "question": ex.get("question"),
            "answer": ex.get("answer"),
            "meta": {"source": "structured", **ex.get("meta", {})}
        })

    print(f"✅ Total merged examples: {len(combined)}")
    json.dump(combined, open(out_path, "w"), indent=2)
    print(f"💾 Saved merged dataset → {out_path}")

if __name__ == "__main__":
    main()
