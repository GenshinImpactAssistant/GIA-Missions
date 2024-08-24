from source.mission.template.mission_just_collect import MissionJustCollect

tlp2m_default_value = {'start_position': [-10801.81, -2829.65], 'end_position': [-11030.61, -2837.34], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-10801.81, -2829.65], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-10847.23, -2903.71], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [-10877.61, -2855.34], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [-10928.23, -2855.34], 'special_key': None}, {'id': 5, 'motion': 'ANY', 'position': [-10955.61, -2848.21], 'special_key': None}, {'id': 6, 'motion': 'ANY', 'position': [-11005.48, -2827.59], 'special_key': None}, {'id': 7, 'motion': 'ANY', 'position': [-11030.61, -2837.34], 'special_key': None}], 'break_position': [[-10801.81, -2829.65], [-10847.23, -2903.71], [-10877.61, -2855.34], [-10928.23, -2855.34], [-10955.61, -2848.21], [-11005.48, -2827.59], [-11030.61, -2837.34]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[-10847.62, -2900.62], [-10878.0, -2852.25], [-10928.62, -2852.25], [-10959.66, -2849.15], [-11006.56, -2830.04], [-11037.07, -2845.64]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '悼灵花采集'}, 'author': 'GIA', 'tags': {'zh_CN': ['采集'], 'en_US': ['Collect']}, 'local_edit_mission': '悼灵花采集', 'description': '', 'note': ''}

class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

