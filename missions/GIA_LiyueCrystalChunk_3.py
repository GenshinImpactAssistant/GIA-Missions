from source.mission.template.mission_miner import MissionMiner

tlp2m_default_value = {'start_position': [-879.36, -1721.84], 'end_position': [-1063.21, -1795.8], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-879.36, -1721.84], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-976.42, -1755.77], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [-1063.21, -1795.8], 'special_key': None}], 'break_position': [[-879.36, -1721.84], [-976.42, -1755.77], [-1063.21, -1795.8]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[-1063.6, -1792.71]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '水晶矿-璃月渌华池1个'}, 'author': 'GIA', 'tags': {'zh_CN': ['矿物'], 'en_US': ['Mineral']}, 'local_edit_mission': '水晶矿-璃月渌华池1个', 'description': '', 'note': ''}

class MissionMain(MissionMiner):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

