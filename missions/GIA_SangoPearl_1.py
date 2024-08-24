from source.mission.template.mission_just_collect import MissionJustCollect

tlp2m_default_value = {'start_position': [2327.15, 5886.66], 'end_position': [2350.39, 6196.91], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [2327.15, 5886.66], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [2377.77, 5998.54], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [2361.71, 6002.54], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [2356.52, 6005.47], 'special_key': None}, {'id': 5, 'motion': 'ANY', 'position': [2318.89, 6070.41], 'special_key': None}, {'id': 6, 'motion': 'ANY', 'position': [2327.14, 6072.16], 'special_key': None}, {'id': 7, 'motion': 'ANY', 'position': [2326.24, 6098.02], 'special_key': None}, {'id': 8, 'motion': 'ANY', 'position': [2363.14, 6144.91], 'special_key': None}, {'id': 9, 'motion': 'ANY', 'position': [2351.64, 6146.41], 'special_key': None}, {'id': 10, 'motion': 'ANY', 'position': [2338.89, 6146.16], 'special_key': None}, {'id': 11, 'motion': 'ANY', 'position': [2342.39, 6156.91], 'special_key': None}, {'id': 12, 'motion': 'ANY', 'position': [2352.89, 6158.16], 'special_key': None}, {'id': 13, 'motion': 'ANY', 'position': [2350.39, 6196.91], 'special_key': None}], 'break_position': [[2327.15, 5886.66], [2377.77, 5998.54], [2361.71, 6002.54], [2356.52, 6005.47], [2318.89, 6070.41], [2327.14, 6072.16], [2326.24, 6098.02], [2363.14, 6144.91], [2351.64, 6146.41], [2338.89, 6146.16], [2342.39, 6156.91], [2352.89, 6158.16], [2350.39, 6196.91]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[2377.38, 6001.62], [2349.85, 6002.94], [2326.1, 6067.13], [2331.32, 6093.98], [2339.45, 6157.46], [2362.75, 6148.0], [2349.98, 6190.42]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '珊瑚真珠采集'}, 'author': 'GIA', 'tags': {'zh_CN': ['采集'], 'en_US': ['Collect']}, 'local_edit_mission': '珊瑚真珠采集', 'description': '', 'note': ''}

class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

