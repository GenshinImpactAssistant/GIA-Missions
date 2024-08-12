from source.mission.template.mission_combat import MissionCombat

tlp2m_default_value = {'start_position': [-6010.98, 1101.15], 'end_position': [-5987.23, 1004.41], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-6010.98, 1101.15], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-5987.69, 1058.13], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [-5987.23, 1004.41], 'special_key': None}], 'break_position': [[-6010.98, 1101.15], [-5987.69, 1058.13], [-5987.23, 1004.41]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[-5989.73, 998.48]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '采集须弥善见地1个遗迹守卫'}, 'author': 'GIA', 'tags': {'zh_CN': ['战斗'], 'en_US': ['Combat']}, 'local_edit_mission': '采集须弥善见地1个遗迹守卫', 'description': '', 'note': ''}

class MissionMain(MissionCombat):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",is_circle_search_enemy=True,)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

