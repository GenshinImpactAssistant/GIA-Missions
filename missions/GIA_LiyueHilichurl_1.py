from source.mission.template.mission_combat import MissionCombat

tlp2m_default_value = {'start_position': [286.39, -3795.34], 'end_position': [178.78, -3913.71], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [286.39, -3795.34], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [276.17, -3862.53], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [239.08, -3897.95], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [204.78, -3919.14], 'special_key': None}, {'id': 5, 'motion': 'ANY', 'position': [178.78, -3913.71], 'special_key': None}], 'break_position': [[286.39, -3795.34], [276.17, -3862.53], [239.08, -3897.95], [204.78, -3919.14], [178.78, -3913.71]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[180.56, -3917.91]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '采集荻花洲西北丘丘人'}, 'author': 'GIA', 'tags': {'zh_CN': ['战斗'], 'en_US': ['Combat']}, 'local_edit_mission': '采集荻花洲西北丘丘人', 'description': '', 'note': ''}

class MissionMain(MissionCombat):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",is_circle_search_enemy=True,)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

