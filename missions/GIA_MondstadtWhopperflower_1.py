from source.mission.template.mission_combat import MissionCombat

tlp2m_default_value = {'start_position': [3057.89, -4424.09], 'end_position': [3240.14, -4335.84], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [3057.89, -4424.09], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [3082.49, -4490.2], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [3129.06, -4502.47], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [3135.89, -4483.59], 'special_key': None}, {'id': 5, 'motion': 'ANY', 'position': [3233.08, -4416.3], 'special_key': None}, {'id': 6, 'motion': 'ANY', 'position': [3240.14, -4335.84], 'special_key': None}], 'break_position': [[3057.89, -4424.09], [3082.49, -4490.2], [3129.06, -4502.47], [3135.89, -4483.59], [3233.08, -4416.3], [3240.14, -4335.84]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[3135.5, -4480.5], [3239.75, -4332.75]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '采集蒙德苍风高地附近2个骗骗花'}, 'author': 'GIA', 'tags': {'zh_CN': ['战斗'], 'en_US': ['Combat']}, 'local_edit_mission': '采集蒙德苍风高地附近2个骗骗花', 'description': '', 'note': ''}

class MissionMain(MissionCombat):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name")

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

