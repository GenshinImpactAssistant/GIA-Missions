from source.mission.template.mission_combat import MissionCombat

tlp2m_default_value = {'start_position': [1169.39, -3164.34], 'end_position': [1300.89, -3036.09], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [1169.39, -3164.34], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [1149.53, -3127.47], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [1206.69, -3094.29], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [1300.89, -3036.09], 'special_key': None}], 'break_position': [[1169.39, -3164.34], [1149.53, -3127.47], [1206.69, -3094.29], [1300.89, -3036.09]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[1298.59, -3030.2]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '采集璃月琼玑野1个遗迹守卫'}, 'author': 'GIA', 'tags': {'zh_CN': ['战斗'], 'en_US': ['Combat']}, 'local_edit_mission': '采集璃月琼玑野1个遗迹守卫', 'description': '', 'note': ''}

class MissionMain(MissionCombat):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",is_circle_search_enemy=True,)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

