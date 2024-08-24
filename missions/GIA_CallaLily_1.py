from source.mission.template.mission_just_collect import MissionJustCollect

tlp2m_default_value = {'start_position': [2619.39, -4820.59], 'end_position': [2665.97, -4754.17], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [2619.39, -4820.59], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [2659.97, -4862.11], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [2702.51, -4877.11], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [2707.84, -4835.32], 'special_key': None}, {'id': 5, 'motion': 'ANY', 'position': [2698.3, -4782.31], 'special_key': None}, {'id': 6, 'motion': 'ANY', 'position': [2668.97, -4767.66], 'special_key': None}, {'id': 7, 'motion': 'ANY', 'position': [2665.97, -4754.17], 'special_key': None}], 'break_position': [[2619.39, -4820.59], [2659.97, -4862.11], [2702.51, -4877.11], [2707.84, -4835.32], [2698.3, -4782.31], [2668.97, -4767.66], [2665.97, -4754.17]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[2659.57, -4859.02], [2668.57, -4764.57], [2665.57, -4751.08]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '嘟嘟莲采集'}, 'author': 'GIA', 'tags': {'zh_CN': ['采集'], 'en_US': ['Collect']}, 'local_edit_mission': '嘟嘟莲采集', 'description': '', 'note': ''}

class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

