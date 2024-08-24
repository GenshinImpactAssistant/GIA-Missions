from source.mission.template.mission_just_collect import MissionJustCollect

tlp2m_default_value = {'start_position': [9682.89, 7336.41], 'end_position': [9724.03, 7369.3], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [9682.89, 7336.41], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [9677.34, 7347.5], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [9632.7, 7361.33], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [9724.03, 7369.3], 'special_key': None}], 'break_position': [[9682.89, 7336.41], [9677.34, 7347.5], [9632.7, 7361.33], [9724.03, 7369.3]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[9669.24, 7339.53], [9632.31, 7364.42], [9723.63, 7372.38]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '天云草实采集'}, 'author': 'GIA', 'tags': {'zh_CN': ['采集'], 'en_US': ['Collect']}, 'local_edit_mission': '天云草实采集', 'description': '', 'note': ''}

class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

