from source.mission.template.mission_just_collect import MissionJustCollect

tlp2m_default_value = {'start_position': [6833.64, 6004.41], 'end_position': [6232.14, 5874.66], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [6833.64, 6004.41], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [6591.5, 6034.51], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [6521.64, 5979.66], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [6516.39, 5949.66], 'special_key': None}, {'id': 5, 'motion': 'ANY', 'position': [6429.15, 5888.18], 'special_key': None}, {'id': 6, 'motion': 'ANY', 'position': [6380.89, 5840.41], 'special_key': None}, {'id': 7, 'motion': 'ANY', 'position': [6373.39, 5844.91], 'special_key': None}, {'id': 8, 'motion': 'ANY', 'position': [6349.14, 5865.66], 'special_key': None}, {'id': 9, 'motion': 'ANY', 'position': [6302.4, 5825.91], 'special_key': None}, {'id': 10, 'motion': 'ANY', 'position': [6268.14, 5825.91], 'special_key': None}, {'id': 11, 'motion': 'ANY', 'position': [6232.14, 5874.66], 'special_key': None}], 'break_position': [[6833.64, 6004.41], [6591.5, 6034.51], [6521.64, 5979.66], [6516.39, 5949.66], [6429.15, 5888.18], [6380.89, 5840.41], [6373.39, 5844.91], [6349.14, 5865.66], [6302.4, 5825.91], [6268.14, 5825.91], [6232.14, 5874.66]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[6586.75, 6033.28], [6517.21, 5980.66], [6509.46, 5945.14], [6431.29, 5879.89], [6372.41, 5840.09], [6346.77, 5865.01], [6296.66, 5828.77], [6268.36, 5822.88], [6228.76, 5871.02]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '血斛采集'}, 'author': 'GIA', 'tags': {'zh_CN': ['采集'], 'en_US': ['Collect']}, 'local_edit_mission': '血斛采集', 'description': '', 'note': ''}

class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

