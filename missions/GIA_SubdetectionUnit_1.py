from source.mission.template.mission_just_collect import MissionJustCollect

tlp2m_default_value = {'start_position': [-7826.23, -10753.21], 'end_position': [-7739.48, -10694.34], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-7826.23, -10753.21], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-7752.27, -10777.06], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [-7729.23, -10788.97], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [-7708.86, -10737.21], 'special_key': None}, {'id': 5, 'motion': 'ANY', 'position': [-7732.11, -10693.22], 'special_key': None}, {'id': 6, 'motion': 'ANY', 'position': [-7739.48, -10694.34], 'special_key': None}], 'break_position': [[-7826.23, -10753.21], [-7752.27, -10777.06], [-7729.23, -10788.97], [-7708.86, -10737.21], [-7732.11, -10693.22], [-7739.48, -10694.34]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[-7758.12, -10782.95], [-7734.29, -10791.51], [-7712.97, -10740.29], [-7738.15, -10698.23]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '子探测单元采集'}, 'author': 'GIA', 'tags': {'zh_CN': ['采集'], 'en_US': ['Collect']}, 'local_edit_mission': '子探测单元采集', 'description': '', 'note': ''}

class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

