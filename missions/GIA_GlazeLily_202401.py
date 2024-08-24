from source.mission.template.mission_just_collect import MissionJustCollect

tlp2m_default_value = {'start_position': [-805.11, -4815.34], 'end_position': [-391.11, -4946.34], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-805.11, -4815.34], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-826.89, -4839.04], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [-825.76, -4882.8], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [-821.56, -4954.05], 'special_key': None}, {'id': 5, 'motion': 'ANY', 'position': [-778.64, -4979.29], 'special_key': None}, {'id': 6, 'motion': 'ANY', 'position': [-718.05, -5018.56], 'special_key': None}, {'id': 7, 'motion': 'ANY', 'position': [-701.61, -5059.59], 'special_key': None}, {'id': 8, 'motion': 'ANY', 'position': [-622.86, -5038.59], 'special_key': None}, {'id': 9, 'motion': 'ANY', 'position': [-540.36, -5076.09], 'special_key': None}, {'id': 10, 'motion': 'ANY', 'position': [-451.11, -5085.09], 'special_key': None}, {'id': 11, 'motion': 'ANY', 'position': [-452.61, -5061.84], 'special_key': None}, {'id': 12, 'motion': 'ANY', 'position': [-407.61, -5061.84], 'special_key': None}, {'id': 13, 'motion': 'ANY', 'position': [-370.86, -5064.84], 'special_key': None}, {'id': 14, 'motion': 'ANY', 'position': [-356.61, -5012.99], 'special_key': None}, {'id': 15, 'motion': 'ANY', 'position': [-454.4, -5010.99], 'special_key': None}, {'id': 16, 'motion': 'ANY', 'position': [-486.36, -4939.59], 'special_key': None}, {'id': 17, 'motion': 'ANY', 'position': [-391.11, -4946.34], 'special_key': None}], 'break_position': [[-805.11, -4815.34], [-826.89, -4839.04], [-825.76, -4882.8], [-821.56, -4954.05], [-778.64, -4979.29], [-718.05, -5018.56], [-701.61, -5059.59], [-622.86, -5038.59], [-540.36, -5076.09], [-451.11, -5085.09], [-452.61, -5061.84], [-407.61, -5061.84], [-370.86, -5064.84], [-356.61, -5012.99], [-454.4, -5010.99], [-486.36, -4939.59], [-391.11, -4946.34]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[-699.99, -5061.16], [-618.58, -5044.71], [-537.59, -5079.52], [-446.95, -5089.46], [-453.0, -5058.75], [-408.14, -5070.8], [-371.25, -5061.75], [-353.06, -5012.45], [-456.73, -5015.15], [-485.03, -4946.39], [-394.27, -4950.16]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '琉璃百合采集'}, 'author': 'GIA', 'tags': {'zh_CN': ['采集'], 'en_US': ['Collect']}, 'local_edit_mission': '琉璃百合采集', 'description': '', 'note': ''}

class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

