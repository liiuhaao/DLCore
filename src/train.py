import os


def run(cfg):
    for dataset in os.listdir(cfg["path"]["data"]):
        if dataset.startswith("."):
            continue
        if "dataset" in cfg and dataset != cfg["dataset"]:
            continue
