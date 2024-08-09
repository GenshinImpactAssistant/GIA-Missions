from source.mission.template.mission_combat import MissionCombat

tlp2m_default_value = {'start_position': [1561.34, -5829.61], 'end_position': [1725.77, -5805.09], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [1561.34, -5829.61], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [1725.77, -5805.09], 'special_key': None}], 'break_position': [[1561.34, -5829.61], [1725.77, -5805.09]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[1717.61, -5801.69]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '采集蒙德苍风高地，邻近悬崖附近1个丘丘萨满'}, 'author': 'GIA', 'tags': {'zh_CN': ['战斗'], 'en_US': ['Combat']}, 'local_edit_mission': '采集蒙德苍风高地，邻近悬崖附近1个丘丘萨满', 'description': '', 'note': ''}

class MissionMain(MissionCombat):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name")

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

