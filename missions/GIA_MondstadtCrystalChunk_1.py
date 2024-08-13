from source.mission.template.mission_miner import MissionMiner

tlp2m_default_value = {'start_position': [3335.15, -6682.34], 'end_position': [3504.41, -6643.39], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [3335.15, -6682.34], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [3435.87, -6693.57], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [3481.92, -6638.88], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [3490.52, -6613.54], 'special_key': None}, {'id': 5, 'motion': 'ANY', 'position': [3504.41, -6643.39], 'special_key': None}], 'break_position': [[3335.15, -6682.34], [3435.87, -6693.57], [3481.92, -6638.88], [3490.52, -6613.54], [3504.41, -6643.39]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[3481.52, -6635.79], [3504.01, -6640.3]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '水晶块-蒙德望风山地东南2个'}, 'author': 'GIA', 'tags': {'zh_CN': ['矿物'], 'en_US': ['Mineral']}, 'local_edit_mission': '水晶块-蒙德望风山地东南2个', 'description': '挖挖挖挖挖挖挖挖挖挖挖挖挖挖挖', 'note': ''}

class MissionMain(MissionMiner):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

