from source.mission.template.mission_just_collect import MissionJustCollect

tlp2m_default_value = {'start_position': [-7123.11, -6990.84], 'end_position': [-7218.99, -6784.94], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-7123.11, -6990.84], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-7181.51, -6807.63], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [-7199.24, -6792.85], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [-7218.99, -6784.94], 'special_key': None}], 'break_position': [[-7123.11, -6990.84], [-7181.51, -6807.63], [-7199.24, -6792.85], [-7218.99, -6784.94]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[-7181.9, -6804.54], [-7194.58, -6786.67]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '柔灯铃采集'}, 'author': 'GIA', 'tags': {'zh_CN': ['采集'], 'en_US': ['Collect']}, 'local_edit_mission': '柔灯铃采集', 'description': '', 'note': ''}

class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

