from source.mission.template.mission_combat import MissionCombat

tlp2m_default_value = {'start_position': [-1294.86, -3132.09], 'end_position': [-1417.1, -3018.6], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-1294.86, -3132.09], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-1417.1, -3018.6], 'special_key': None}], 'break_position': [[-1294.86, -3132.09], [-1417.1, -3018.6]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[-1417.49, -3015.51]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '采集璃月珉林西南1个遗迹守卫'}, 'author': 'GIA', 'tags': {'zh_CN': ['战斗'], 'en_US': ['Combat']}, 'local_edit_mission': '采集璃月珉林西南1个遗迹守卫', 'description': '', 'note': ''}

class MissionMain(MissionCombat):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",is_circle_search_enemy=True,)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()
