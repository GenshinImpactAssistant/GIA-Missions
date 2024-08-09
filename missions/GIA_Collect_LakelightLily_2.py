from source.mission.template.mission_just_collect import MissionJustCollect

tlp2m_default_value = {'start_position': [-5887.24, -9027.88], 'end_position': [-5695.98, -8791.84], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-5887.24, -9027.88], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-5816.97, -8952.14], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [-5782.91, -8945.01], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [-5751.13, -8925.22], 'special_key': None}, {'id': 5, 'motion': 'ANY', 'position': [-5728.75, -8925.55], 'special_key': None}, {'id': 6, 'motion': 'ANY', 'position': [-5713.11, -8935.09], 'special_key': None}, {'id': 7, 'motion': 'ANY', 'position': [-5710.58, -8920.36], 'special_key': None}, {'id': 8, 'motion': 'ANY', 'position': [-5726.36, -8863.34], 'special_key': None}, {'id': 9, 'motion': 'ANY', 'position': [-5728.36, -8860.34], 'special_key': None}, {'id': 10, 'motion': 'ANY', 'position': [-5737.35, -8805.84], 'special_key': None}, {'id': 11, 'motion': 'ANY', 'position': [-5735.86, -8789.84], 'special_key': None}, {'id': 12, 'motion': 'ANY', 'position': [-5741.48, -8786.96], 'special_key': None}, {'id': 13, 'motion': 'ANY', 'position': [-5722.58, -8779.92], 'special_key': None}, {'id': 14, 'motion': 'ANY', 'position': [-5697.35, -8785.09], 'special_key': None}, {'id': 15, 'motion': 'ANY', 'position': [-5694.11, -8785.84], 'special_key': None}, {'id': 16, 'motion': 'ANY', 'position': [-5695.98, -8791.84], 'special_key': None}], 'break_position': [[-5887.24, -9027.88], [-5816.97, -8952.14], [-5782.91, -8945.01], [-5751.13, -8925.22], [-5728.75, -8925.55], [-5713.11, -8935.09], [-5710.58, -8920.36], [-5726.36, -8863.34], [-5728.36, -8860.34], [-5737.35, -8805.84], [-5735.86, -8789.84], [-5741.48, -8786.96], [-5722.58, -8779.92], [-5697.35, -8785.09], [-5694.11, -8785.84], [-5695.98, -8791.84]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true', 'is_active_pickup_in_bp': True}, 'adsorptive_position': [[-5716.81, -8934.0], [-5728.66, -8868.8], [-5738.63, -8796.54], [-5692.09, -8790.22]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '采集湖中垂柳左边的湖光铃兰'}, 'author': 'GIA', 'tags': {'zh_CN': ['采集'], 'en_US': ['Collect']}, 'local_edit_mission': '采集湖中垂柳左边的湖光铃兰', 'description': '', 'note': ''}

class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name")

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

