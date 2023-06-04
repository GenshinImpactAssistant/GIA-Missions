import json
from util import *

def main():
    language = ["", "_zh_CN", "_en_US"]
    for lang in language:
        source_index = json.loads(get_source_repo_file(f"index{lang}.json"))
        this_index_path = os.path.join(ROOT_PATH, f"index{lang}.json")
        this_index = json.loads(open(this_index_path, "r", encoding="utf-8").read())
        # print(source_index)
        # print(this_index)
        assert "missions" in this_index, "index.json should have a 'missions' key"
        assert source_index["missions"] == this_index["missions"], "'missions' in index.json should not be modified manually"

if __name__ == "__main__":
    main()