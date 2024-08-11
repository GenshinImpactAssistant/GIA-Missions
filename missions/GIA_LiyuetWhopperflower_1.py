from source.mission.template.mission_combat import MissionCombat

tlp2m_default_value = {'start_position': [-657.36, -3358.84], 'end_position': [-631.86, -3214.34], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-657.36, -3358.84], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-628.18, -3378.9], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [-702.86, -3352.59], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [-685.09, -3321.17], 'special_key': None}, {'id': 5, 'motion': 'ANY', 'position': [-664.46, -3277.95], 'special_key': None}, {'id': 6, 'motion': 'ANY', 'position': [-631.86, -3214.34], 'special_key': None}], 'break_position': [[-657.36, -3358.84], [-628.18, -3378.9], [-702.86, -3352.59], [-685.09, -3321.17], [-664.46, -3277.95], [-631.86, -3214.34]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[-628.57, -3375.81], [-703.25, -3349.5], [-640.31, -3221.18]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '采集璃月珉林附近3个骗骗花'}, 'author': 'GIA', 'tags': {'zh_CN': ['战斗'], 'en_US': ['Combat']}, 'local_edit_mission': '采集璃月珉林附近3个骗骗花', 'description': '', 'note': ''}

class MissionMain(MissionCombat):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",is_circle_search_enemy=True,)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

