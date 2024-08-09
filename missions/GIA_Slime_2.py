from source.mission.template.mission_combat import MissionCombat

tlp2m_default_value = {'start_position': [1942.89, -4949.84], 'end_position': [2061.39, -4692.09], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [1942.89, -4949.84], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [1835.74, -4902.34], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [1853.3, -4864.14], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [1865.64, -4834.3], 'special_key': None}, {'id': 5, 'motion': 'ANY', 'position': [1834.89, -4824.09], 'special_key': None}, {'id': 6, 'motion': 'ANY', 'position': [1833.57, -4763.74], 'special_key': None}, {'id': 7, 'motion': 'ANY', 'position': [1913.89, -4739.2], 'special_key': None}, {'id': 8, 'motion': 'ANY', 'position': [1937.31, -4715.78], 'special_key': None}, {'id': 9, 'motion': 'ANY', 'position': [1981.59, -4718.33], 'special_key': None}, {'id': 10, 'motion': 'ANY', 'position': [2026.34, -4730.44], 'special_key': None}, {'id': 11, 'motion': 'ANY', 'position': [2035.75, -4722.47], 'special_key': None}, {'id': 12, 'motion': 'ANY', 'position': [2052.48, -4723.31], 'special_key': None}, {'id': 13, 'motion': 'ANY', 'position': [2086.23, -4722.75], 'special_key': None}, {'id': 14, 'motion': 'ANY', 'position': [2084.83, -4700.72], 'special_key': None}, {'id': 15, 'motion': 'ANY', 'position': [2061.39, -4692.09], 'special_key': None}], 'break_position': [[1942.89, -4949.84], [1835.74, -4902.34], [1865.64, -4834.3], [1834.89, -4824.09], [1833.57, -4763.74], [1913.89, -4739.2], [1937.31, -4715.78], [1981.59, -4718.33], [2026.34, -4730.44], [2035.75, -4722.47], [2086.23, -4722.75], [2084.83, -4700.72], [2061.39, -4692.09]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[1837.18, -4835.69], [1981.2, -4715.25], [2025.95, -4727.35], [2061.0, -4689.0]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '采集酒庄右边一些史莱姆'}, 'author': 'GIA', 'tags': {'zh_CN': ['战斗'], 'en_US': ['Combat']}, 'local_edit_mission': '采集酒庄右边一些史莱姆', 'description': '', 'note': ''}

class MissionMain(MissionCombat):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name")

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

