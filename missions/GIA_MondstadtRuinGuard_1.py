from source.mission.template.mission_combat import MissionCombat

tlp2m_default_value = {'start_position': [1662.14, -6400.84], 'end_position': [1524.25, -6666.71], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [1662.14, -6400.84], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [1614.44, -6597.87], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [1524.25, -6666.71], 'special_key': None}], 'break_position': [[1662.14, -6400.84], [1614.44, -6597.87], [1524.25, -6666.71]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[1523.85, -6663.62]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '采集蒙德明冠峡1个遗迹守卫'}, 'author': 'GIA', 'tags': {'zh_CN': ['战斗'], 'en_US': ['Combat']}, 'local_edit_mission': '采集蒙德明冠峡1个遗迹守卫', 'description': '', 'note': ''}

class MissionMain(MissionCombat):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",is_circle_search_enemy=True,)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

