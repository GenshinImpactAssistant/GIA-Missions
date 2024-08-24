from source.mission.template.mission_just_collect import MissionJustCollect

tlp2m_default_value = {'start_position': [-1578.36, -2490.84], 'end_position': [-1786.11, -2675.24], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-1578.36, -2490.84], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-1652.77, -2525.77], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [-1721.5, -2539.8], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [-1765.82, -2529.14], 'special_key': None}, {'id': 5, 'motion': 'ANY', 'position': [-1804.11, -2516.33], 'special_key': None}, {'id': 6, 'motion': 'ANY', 'position': [-1844.07, -2542.6], 'special_key': None}, {'id': 7, 'motion': 'ANY', 'position': [-1871.0, -2593.09], 'special_key': None}, {'id': 8, 'motion': 'ANY', 'position': [-1883.62, -2660.97], 'special_key': None}, {'id': 9, 'motion': 'ANY', 'position': [-1786.11, -2675.24], 'special_key': None}], 'break_position': [[-1578.36, -2490.84], [-1652.77, -2525.77], [-1721.5, -2539.8], [-1765.82, -2529.14], [-1804.11, -2516.33], [-1844.07, -2542.6], [-1871.0, -2593.09], [-1883.62, -2660.97], [-1786.11, -2675.24]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[-1801.22, -2520.42], [-1795.57, -2681.09]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '绝云椒椒采集'}, 'author': 'GIA', 'tags': {'zh_CN': ['采集'], 'en_US': ['Collect']}, 'local_edit_mission': '绝云椒椒采集', 'description': '', 'note': ''}

class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

