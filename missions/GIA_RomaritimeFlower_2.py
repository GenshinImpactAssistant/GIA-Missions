from source.mission.template.mission_just_collect import MissionJustCollect

tlp2m_default_value = {'start_position': [-4953.86, -8256.25], 'end_position': [-4855.35, -8067.71], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-4953.86, -8256.25], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-5028.29, -8223.95], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [-5093.37, -8135.59], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [-5101.78, -8072.48], 'special_key': None}, {'id': 5, 'motion': 'ANY', 'position': [-5080.75, -8037.42], 'special_key': None}, {'id': 6, 'motion': 'ANY', 'position': [-5108.59, -8015.32], 'special_key': None}, {'id': 7, 'motion': 'ANY', 'position': [-5098.86, -7952.34], 'special_key': None}, {'id': 8, 'motion': 'ANY', 'position': [-5065.6, -7983.57], 'special_key': None}, {'id': 9, 'motion': 'ANY', 'position': [-5027.61, -7934.71], 'special_key': None}, {'id': 10, 'motion': 'ANY', 'position': [-4940.98, -7948.09], 'special_key': None}, {'id': 11, 'motion': 'ANY', 'position': [-4917.73, -7980.34], 'special_key': None}, {'id': 12, 'motion': 'ANY', 'position': [-4855.35, -8067.71], 'special_key': None}], 'break_position': [[-4953.86, -8256.25], [-5028.29, -8223.95], [-5093.37, -8135.59], [-5101.78, -8072.48], [-5080.75, -8037.42], [-5108.59, -8015.32], [-5098.86, -7952.34], [-5065.6, -7983.57], [-5027.61, -7934.71], [-4940.98, -7948.09], [-4917.73, -7980.34], [-4855.35, -8067.71]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[-5108.98, -8012.23], [-5099.25, -7949.25], [-5028.0, -7931.62], [-4941.37, -7945.0], [-4918.12, -7977.25], [-4855.75, -8064.63]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '海露花采集'}, 'author': 'GIA', 'tags': {'zh_CN': ['采集'], 'en_US': ['Collect']}, 'local_edit_mission': '海露花采集', 'description': '', 'note': ''}

class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

