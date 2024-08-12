from source.mission.template.mission_combat import MissionCombat

tlp2m_default_value = {'start_position': [-4794.75, 1217.65], 'end_position': [-5109.67, 1458.83], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-4794.75, 1217.65], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-4856.35, 1276.04], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [-4958.97, 1323.17], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [-5108.41, 1397.46], 'special_key': None}, {'id': 5, 'motion': 'ANY', 'position': [-5109.67, 1458.83], 'special_key': None}], 'break_position': [[-4794.75, 1217.65], [-4856.35, 1276.04], [-4958.97, 1323.17], [-5108.41, 1397.46], [-5109.67, 1458.83]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[-5110.38, 1452.89]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '采集须弥阿陀河谷1个遗迹守卫'}, 'author': 'GIA', 'tags': {'zh_CN': ['战斗'], 'en_US': ['Combat']}, 'local_edit_mission': '采集须弥阿陀河谷1个遗迹守卫', 'description': '', 'note': ''}

class MissionMain(MissionCombat):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",is_circle_search_enemy=True,)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

