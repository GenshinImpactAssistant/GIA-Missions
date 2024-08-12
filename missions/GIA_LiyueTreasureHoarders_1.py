from source.mission.template.mission_combat import MissionCombat

tlp2m_default_value = {'start_position': [-635.61, 308.16], 'end_position': [-908.6, 367.66], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-635.61, 308.16], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-527.05, 479.69], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [-541.27, 538.53], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [-561.61, 542.16], 'special_key': None}, {'id': 5, 'motion': 'ANY', 'position': [-583.11, 584.91], 'special_key': None}, {'id': 6, 'motion': 'ANY', 'position': [-616.29, 531.28], 'special_key': None}, {'id': 7, 'motion': 'ANY', 'position': [-651.86, 523.16], 'special_key': None}, {'id': 8, 'motion': 'ANY', 'position': [-719.47, 505.62], 'special_key': None}, {'id': 9, 'motion': 'ANY', 'position': [-732.35, 428.65], 'special_key': None}, {'id': 10, 'motion': 'ANY', 'position': [-767.66, 454.57], 'special_key': None}, {'id': 11, 'motion': 'ANY', 'position': [-815.88, 422.63], 'special_key': None}, {'id': 12, 'motion': 'ANY', 'position': [-908.6, 367.66], 'special_key': None}], 'break_position': [[-635.61, 308.16], [-527.05, 479.69], [-541.27, 538.53], [-561.61, 542.16], [-583.11, 584.91], [-616.29, 531.28], [-651.86, 523.16], [-719.47, 505.62], [-732.35, 428.65], [-767.66, 454.57], [-815.88, 422.63], [-908.6, 367.66]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[-564.25, 552.49], [-583.5, 588.0], [-650.24, 514.03], [-732.74, 431.74], [-816.27, 425.72], [-909.0, 370.75]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '盗宝团-璃月璃沙郊若干'}, 'author': 'GIA', 'tags': {'zh_CN': ['战斗'], 'en_US': ['Combat']}, 'local_edit_mission': '盗宝团-璃月璃沙郊若干', 'description': '', 'note': ''}

class MissionMain(MissionCombat):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",is_circle_search_enemy=True,)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

