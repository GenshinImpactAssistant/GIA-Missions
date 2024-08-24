from source.mission.template.mission_just_collect import MissionJustCollect

tlp2m_default_value = {'start_position': [-4039.6, -1939.09], 'end_position': [-3903.23, -1873.48], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-4039.6, -1939.09], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-3945.73, -1901.34], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [-3903.23, -1873.48], 'special_key': None}], 'break_position': [[-4039.6, -1939.09], [-3945.73, -1901.34], [-3903.23, -1873.48]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[-3949.83, -1906.09], [-3904.48, -1879.82]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '树王圣体菇采集'}, 'author': 'GIA', 'tags': {'zh_CN': ['采集'], 'en_US': ['Collect']}, 'local_edit_mission': '树王圣体菇采集', 'description': '', 'note': ''}

class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

