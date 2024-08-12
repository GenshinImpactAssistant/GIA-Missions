from source.mission.template.mission_combat import MissionCombat

tlp2m_default_value = {'start_position': [684.14, -1511.84], 'end_position': [803.39, -1452.34], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [684.14, -1511.84], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [775.92, -1488.27], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [803.39, -1452.34], 'special_key': None}], 'break_position': [[684.14, -1511.84], [775.92, -1488.27], [803.39, -1452.34]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[802.03, -1460.3]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '采集璃月云来海海边雷萤术士'}, 'author': 'GIA', 'tags': {'zh_CN': ['战斗'], 'en_US': ['Combat']}, 'local_edit_mission': '采集璃月云来海海边雷萤术士', 'description': '', 'note': ''}

class MissionMain(MissionCombat):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",is_circle_search_enemy=True,)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

