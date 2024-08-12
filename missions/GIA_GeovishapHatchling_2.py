from source.mission.template.mission_combat import MissionCombat

tlp2m_default_value = {'start_position': [-1510.86, -1517.34], 'end_position': [-1459.09, -1491.38], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-1510.86, -1517.34], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-1459.09, -1491.38], 'special_key': None}], 'break_position': [[-1510.86, -1517.34], [-1459.09, -1491.38]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[-1470.25, -1485.25], [-1441.84, -1488.75]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '采集璃月天遒谷右边2个幼岩龙蜥'}, 'author': 'GIA', 'tags': {'zh_CN': ['战斗'], 'en_US': ['Combat']}, 'local_edit_mission': '采集璃月天遒谷右边2个幼岩龙蜥', 'description': '', 'note': ''}

class MissionMain(MissionCombat):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",is_circle_search_enemy=True,)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

