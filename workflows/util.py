import requests
import os
from pathlib import Path
import argparse

SOURCE_REPO = "https://github.com/moulai/GIA-Missions"
SOURCE_BRANCH = "main"
ROOT_PATH = Path(__file__).parent.parent

def get_opts() -> argparse.Namespace:
    oparser = argparse.ArgumentParser()
    oparser.add_argument(
        "--input", "-i", nargs='+', default="/dev/stdin", required=True
    )
    return oparser.parse_args()

def get_source_repo_file(path):
    return requests.get(f"{SOURCE_REPO}/raw/{SOURCE_BRANCH}/{path}").text