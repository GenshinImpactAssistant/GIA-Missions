from source.mission.template.mission_just_collect import MissionJustCollect

META={'name': {'zh_CN': '采集湖光铃兰'}, 'author': 'GIA', 'tags': {'zh_CN': ['采集'], 'en_US': ['Collect']}, 'local_edit_mission': '采集湖光铃兰', 'description': '采集伊黎耶林区传送锚点附近3个湖光铃兰，试试新版GIA任务生成功能', 'note': '干就完了'}

class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name")

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

tlp2m_default_value = {'start_position': [-6457.11, -9352.21], 'end_position': [-6417.36, -9315.34], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-6457.11, -9352.21], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-6433.36, -9355.34], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [-6427.11, -9353.09], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [-6417.36, -9315.34], 'special_key': None}], 'break_position': [[-6457.11, -9352.21], [-6433.36, -9355.34], [-6427.11, -9353.09], [-6417.36, -9315.34]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[-6428.98, -9359.15], [-6412.36, -9316.62]], 'generate_from': 'path recorder 1.0'}
