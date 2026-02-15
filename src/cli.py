import argparse
from pathlib import Path
import yaml

def _load_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def main() -> None:
    p = argparse.ArgumentParser(description="Water consumption analysis CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    train = sub.add_parser("train", help="Run processing/training step (optional)")
    train.add_argument("--config", required=True)

    pred = sub.add_parser("predict", help="Run forecast/prediction step (optional)")
    pred.add_argument("--config", required=True)

    args = p.parse_args()
    cfg = _load_config(args.config)

    if args.cmd == "train":
        print("TRAIN with config:", cfg.get("project", {}))
    else:
        print("PREDICT with config:", cfg.get("project", {}))

if __name__ == "__main__":
    main()
