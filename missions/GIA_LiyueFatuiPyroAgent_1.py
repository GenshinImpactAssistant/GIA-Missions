from source.mission.template.mission_combat import MissionCombat

tlp2m_default_value = {'start_position': [-181.11, -1686.34], 'end_position': [-235.11, -1648.59], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-181.11, -1686.34], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-235.11, -1648.59], 'special_key': None}], 'break_position': [[-181.11, -1686.34], [-235.11, -1648.59]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[-228.41, -1655.08]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '采集渌华池右边一个债务处理人'}, 'author': 'GIA', 'tags': {'zh_CN': ['战斗'], 'en_US': ['Combat']}, 'local_edit_mission': '采集渌华池右边一个债务处理人', 'description': '', 'note': ''}

class MissionMain(MissionCombat):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

