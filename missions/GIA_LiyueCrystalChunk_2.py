from source.mission.template.mission_miner import MissionMiner

tlp2m_default_value = {'start_position': [-879.36, -1721.84], 'end_position': [-549.36, -1806.09], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-879.36, -1721.84], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-814.03, -1828.46], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [-746.82, -1857.74], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [-631.37, -1751.77], 'special_key': None}, {'id': 5, 'motion': 'ANY', 'position': [-582.36, -1800.84], 'special_key': None}, {'id': 6, 'motion': 'ANY', 'position': [-562.86, -1824.09], 'special_key': None}, {'id': 7, 'motion': 'ANY', 'position': [-549.36, -1806.09], 'special_key': None}], 'break_position': [[-879.36, -1721.84], [-814.03, -1828.46], [-746.82, -1857.74], [-631.37, -1751.77], [-582.36, -1800.84], [-562.86, -1824.09], [-549.36, -1806.09]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[-582.75, -1797.75], [-563.25, -1821.0], [-549.75, -1803.0]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '水晶矿-璃月渌华池东北3个'}, 'author': 'GIA', 'tags': {'zh_CN': ['矿物'], 'en_US': ['Mineral']}, 'local_edit_mission': '水晶矿-璃月渌华池东北3个', 'description': '', 'note': ''}

class MissionMain(MissionMiner):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

