from source.mission.template.mission_combat import MissionCombat

tlp2m_default_value = {'start_position': [1840.81, -5598.66], 'end_position': [1816.89, -5644.59], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [1840.81, -5598.66], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [1816.89, -5644.59], 'special_key': None}], 'break_position': [[1840.81, -5598.66], [1816.89, -5644.59]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[1816.5, -5641.5]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '采集蒙德苍风高地附近1个丘丘萨满'}, 'author': 'GIA', 'tags': {'zh_CN': ['战斗'], 'en_US': ['Combat']}, 'local_edit_mission': '采集蒙德苍风高地附近1个丘丘萨满', 'description': '', 'note': ''}

class MissionMain(MissionCombat):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name")

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

