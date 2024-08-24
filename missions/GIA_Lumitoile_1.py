from source.mission.template.mission_just_collect import MissionJustCollect

tlp2m_default_value = {'start_position': [-9198.36, -10146.84], 'end_position': [-9206.36, -10360.59], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-9198.36, -10146.84], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-9136.11, -10208.66], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [-9188.61, -10272.84], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [-9208.11, -10313.18], 'special_key': None}, {'id': 5, 'motion': 'ANY', 'position': [-9206.36, -10360.59], 'special_key': None}], 'break_position': [[-9198.36, -10146.84], [-9136.11, -10208.66], [-9188.61, -10272.84], [-9208.11, -10313.18], [-9206.36, -10360.59]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[-9134.24, -10216.78], [-9189.01, -10281.23], [-9208.5, -10310.09], [-9204.41, -10359.53]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '幽光星星采集'}, 'author': 'GIA', 'tags': {'zh_CN': ['采集'], 'en_US': ['Collect']}, 'local_edit_mission': '幽光星星采集', 'description': '', 'note': ''}

class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

