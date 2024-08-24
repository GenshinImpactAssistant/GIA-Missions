from source.mission.template.mission_just_collect import MissionJustCollect

tlp2m_default_value = {'start_position': [-8797.48, 3922.42], 'end_position': [-8686.85, 4061.42], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-8797.48, 3922.42], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-8696.85, 4036.42], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [-8688.66, 4037.97], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [-8686.85, 4061.42], 'special_key': None}], 'break_position': [[-8797.48, 3922.42], [-8696.85, 4036.42], [-8688.66, 4037.97], [-8686.85, 4061.42]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[-8698.56, 4036.37], [-8684.6, 4062.17]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '赤念果采集'}, 'author': 'GIA', 'tags': {'zh_CN': ['采集'], 'en_US': ['Collect']}, 'local_edit_mission': '赤念果采集', 'description': '', 'note': ''}

class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

