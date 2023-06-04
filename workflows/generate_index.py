from util import *
import ast
import os
import json
from datetime import datetime
import pytz

language = ["zh_CN", "en_US"]
tag_multi_lang = {
        "collect": {
            "en_US": "Collect",
            "zh_CN": "采集"
        },
        "combat": {
            "en_US": "Combat",
            "zh_CN": "战斗"
        },
        "daily": {
            "en_US": "Daily",
            "zh_CN": "日常"
        },
        "artifact": {
            "en_US": "Artifact",
            "zh_CN": "圣遗物"
        }
    }
tag_lang_find = {}

def init():
    global tag_lang_find
    tag_lang_find = {value: tag for tag, item in tag_multi_lang.items() for value in item.values()}
        
def get_tag_name(tag, lang):
    global tag_lang_find
    if tag in tag_lang_find:
        return tag_multi_lang[tag_lang_find[tag]][lang]
    else:
        return tag

def get_default_value(value: dict):
    # Priority: en_US > zh_CN > first value
    if "en_US" in value:
        return value["en_US"]
    elif "zh_CN" in value:
        return value["zh_CN"]
    else:
        return list(value.values())[0]

def get_value_for_lang(lang, key, meta_value):
    if key not in meta_value:
        if key in ["tags"]:
            return []
        elif key in ["name", "author", "title", "description", "note"]:
            return ""
        else:
            return None
    value = meta_value[key]

    # Special case for tags
    if key == "tags":
        if isinstance(value, dict):
            value = get_default_value(value)
        return [get_tag_name(tag, lang) for tag in value]

    if not isinstance(value, dict):
        return value
    if lang in value:
        return value[lang]
    else:
        get_default_value(value)

def main():
    MISSIONS_FOLDER = os.path.join(ROOT_PATH, "missions")

    opts = get_opts()
    update_files = opts.input
    # Get the file name from the path
    update_files = [os.path.basename(f).replace(".py", "") for f in update_files if f.endswith(".py")]

    all_authors = set()

    source_index = {}
    source_index_dict = {}
    for lang in language:
        source_index[lang] = json.loads(open(os.path.join(ROOT_PATH, f"index_{lang}.json"), "r", encoding="utf-8").read())
        source_index_dict[lang] = {m["name"]: m for m in source_index[lang]["missions"]}
    target_index = {}
    for lang in language:
        target_index[lang] = {
            "about": source_index[lang]["about"],
            "tags": source_index[lang]["tags"],
            "missions": []
        }
    for mission_file in os.listdir(MISSIONS_FOLDER):
        if os.path.isfile(os.path.join(MISSIONS_FOLDER, mission_file)) and mission_file.endswith(".py"):
            name = mission_file[:-3]
            mission_file = Path(os.path.join(MISSIONS_FOLDER, mission_file))
            with open(mission_file, "rb") as f:
                source = f.read()
            module = ast.parse(source)
            meta_value = None
            for node in module.body:
                if isinstance(node, ast.Assign) and len(node.targets) == 1 and node.targets[0].id == 'META':
                    meta_value = ast.literal_eval(node.value)
                    break
            # Make dict for each mission with each language
            now_time = datetime.now(pytz.utc).strftime("%Y-%m-%d %H:%M:%S")

            # Add the author to all_authors
            if "author" in meta_value:
                all_authors.update(set([_.strip() for _ in meta_value["author"].split(",")]))

            for lang in language:
                mission_dict = {}
                mission_dict["name"] = name
                mission_dict["url"] = f"{SOURCE_REPO}/blob/{SOURCE_BRANCH}/missions/{name}.py"
                mission_dict["title"] = get_value_for_lang(lang, "name", meta_value)
                direct_info = ["author", "tags", "description", "note"]
                for key in direct_info:
                    mission_dict[key] = get_value_for_lang(lang, key, meta_value)
                if name in update_files:
                    mission_dict["last_update"] = now_time
                else:
                    mission_dict["last_update"] = source_index_dict[lang][name]["last_update"]
                if name in source_index_dict[lang]:
                    mission_dict["create_time"] = source_index_dict[lang][name]["create_time"]
                else:
                    mission_dict["create_time"] = mission_dict["last_update"]
                target_index[lang]["missions"].append(mission_dict)
    for lang in language:
        print(f"Generating index for index_{lang}.json")
        target_index[lang]["missions"] = sorted(target_index[lang]["missions"], key=lambda x: x["create_time"])
        with open(os.path.join(ROOT_PATH, f"index_{lang}.json"), "w", encoding='utf-8') as f:
            f.write(json.dumps(target_index[lang], indent=4, ensure_ascii=False))
    
    # index.json is the same as index_en_US.json
    with open(os.path.join(ROOT_PATH, "index.json"), "w", encoding='utf-8') as f:
        f.write(json.dumps(target_index["en_US"], indent=4, ensure_ascii=False))

    all_authors = ", ".join(sorted(all_authors))
    # set environment variable for GitHub Actions, exec in shell
    env_file = os.getenv('GITHUB_ENV')
    with open(env_file, "a") as f:
        f.write(f"ALL_AUTHORS={all_authors}")

if __name__ == "__main__":
    init()
    main()