import argparse
import importlib
import os
import shutil
import sys
import time
from pprint import pprint

import yaml


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config/default.yaml", type=str)
    parser.add_argument("--dataset", type=str)
    parser.add_argument("--backup", action="store_true", default=False)
    parser.add_argument("--no-backup", action="store_false", dest="backup")
    parser.add_argument("--name", default=time.strftime("%y%m%d%H%M%S", time.localtime()), type=str)

    parser.add_argument("--data", type=str)
    parser.add_argument("--src", type=str)
    parser.add_argument("--log", type=str)
    parser.add_argument("--output", type=str)

    args = parser.parse_args()
    return args


def load_config(args):
    with open(args.config, "r") as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)

    for key, value in vars(args).items():
        if value is not None:
            if key in ["name", "dataset"]:
                cfg[key] = value
            if key in ["config", "src", "data", "log", "output"]:
                cfg["path"][key] = value
    if args.backup:
        cfg["name"] = os.path.basename(args.output) if args.output else args.name
        cfg["path"]["output"] = args.output if args.output else os.path.join(cfg["path"]["log"], args.name)
    else:
        cfg["path"].pop("log")
    return cfg


def backup(cfg):
    os.makedirs(cfg["path"]["output"], exist_ok=True)

    shutil.rmtree(os.path.join(cfg["path"]["output"], "src"), ignore_errors=True)
    shutil.copytree(cfg["path"]["src"], os.path.join(cfg["path"]["output"], "src"))
    shutil.copyfile("main.py", os.path.join(cfg["path"]["output"], "main.py"))

    with open(os.path.join(cfg["path"]["output"], "config.yaml"), "w") as file:
        yaml.dump(cfg, file, default_flow_style=False)


def main():
    args = parse_arguments()
    cfg = load_config(args)
    pprint(cfg)

    if args.backup:
        backup(cfg)

    if cfg["path"]["src"] not in sys.path:
        sys.path.append(cfg["path"]["src"])

    train_module = importlib.import_module("train")
    train_module.run(cfg)


if __name__ == "__main__":
    main()
