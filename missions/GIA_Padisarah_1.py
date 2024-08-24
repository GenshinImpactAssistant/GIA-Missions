from source.mission.template.mission_just_collect import MissionJustCollect

tlp2m_default_value = {'start_position': [-5457.57, 925.91], 'end_position': [-5669.56, 980.76], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-5457.57, 925.91], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-5522.55, 909.36], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [-5528.17, 910.11], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [-5511.62, 947.91], 'special_key': None}, {'id': 5, 'motion': 'ANY', 'position': [-5522.84, 993.35], 'special_key': None}, {'id': 6, 'motion': 'ANY', 'position': [-5572.11, 1032.66], 'special_key': None}, {'id': 7, 'motion': 'ANY', 'position': [-5586.23, 1026.44], 'special_key': None}, {'id': 8, 'motion': 'ANY', 'position': [-5639.25, 998.11], 'special_key': None}, {'id': 9, 'motion': 'ANY', 'position': [-5669.56, 987.14], 'special_key': None}, {'id': 10, 'motion': 'ANY', 'position': [-5669.56, 980.76], 'special_key': None}], 'break_position': [[-5457.57, 925.91], [-5522.55, 909.36], [-5528.17, 910.11], [-5511.62, 947.91], [-5522.84, 993.35], [-5572.11, 1032.66], [-5639.25, 998.11], [-5669.56, 987.14], [-5669.56, 980.76]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[-5528.57, 913.19], [-5522.94, 912.44], [-5583.38, 1030.88], [-5673.16, 983.52]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '帕蒂沙兰采集'}, 'author': 'GIA', 'tags': {'zh_CN': ['采集'], 'en_US': ['Collect']}, 'local_edit_mission': '帕蒂沙兰采集', 'description': '', 'note': ''}

class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

