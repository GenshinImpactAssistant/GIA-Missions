from source.mission.template.mission_combat import MissionCombat

tlp2m_default_value = {'start_position': [-635.61, 308.16], 'end_position': [-1060.11, 469.41], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-635.61, 308.16], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-663.04, 431.99], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [-758.69, 410.8], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [-882.78, 363.95], 'special_key': None}, {'id': 5, 'motion': 'ANY', 'position': [-1040.61, 455.91], 'special_key': None}, {'id': 6, 'motion': 'ANY', 'position': [-1060.11, 469.41], 'special_key': None}], 'break_position': [[-635.61, 308.16], [-663.04, 431.99], [-758.69, 410.8], [-882.78, 363.95], [-1040.61, 455.91], [-1060.11, 469.41]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[-1041.0, 459.0], [-1060.5, 472.5]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '丘丘暴徒-璃月璃沙郊2个'}, 'author': 'GIA', 'tags': {'zh_CN': ['战斗'], 'en_US': ['Combat']}, 'local_edit_mission': '丘丘暴徒-璃月璃沙郊2个', 'description': '', 'note': ''}

class MissionMain(MissionCombat):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",is_circle_search_enemy=True,)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

