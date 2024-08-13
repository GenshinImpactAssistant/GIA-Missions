from source.mission.template.mission_combat import MissionCombat

tlp2m_default_value = {'start_position': [3057.89, -4424.09], 'end_position': [3289.09, -4426.28], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [3057.89, -4424.09], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [3289.09, -4426.28], 'special_key': None}], 'break_position': [[3057.89, -4424.09], [3289.09, -4426.28]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[3288.7, -4423.19]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '深渊法师-蒙德苍风高地西侧1个'}, 'author': 'GIA', 'tags': {'zh_CN': ['战斗'], 'en_US': ['Combat']}, 'local_edit_mission': '深渊法师-蒙德苍风高地西侧1个', 'description': '', 'note': ''}

class MissionMain(MissionCombat):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",is_circle_search_enemy=True,)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

