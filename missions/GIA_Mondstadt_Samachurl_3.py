from source.mission.template.mission_combat import MissionCombat

tlp2m_default_value = {'start_position': [3853.24, -5188.79], 'end_position': [3754.89, -5625.84], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [3853.24, -5188.79], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [3850.89, -5397.84], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [3736.74, -5447.62], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [3741.84, -5528.49], 'special_key': None}, {'id': 5, 'motion': 'ANY', 'position': [3754.89, -5625.84], 'special_key': None}], 'break_position': [[3853.24, -5188.79], [3850.89, -5397.84], [3736.74, -5447.62], [3741.84, -5528.49], [3754.89, -5625.84]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[3850.5, -5394.75], [3754.5, -5622.75]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '采集蒙德坠星山谷，向北2个丘丘萨满'}, 'author': 'GIA', 'tags': {'zh_CN': ['战斗'], 'en_US': ['Combat']}, 'local_edit_mission': '采集蒙德坠星山谷，向北2个丘丘萨满', 'description': '', 'note': ''}

class MissionMain(MissionCombat):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name")

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

