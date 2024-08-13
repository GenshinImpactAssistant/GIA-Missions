from source.mission.template.mission_just_collect import MissionJustCollect

tlp2m_default_value = {'start_position': [-7502.27, -6451.1], 'end_position': [-7523.48, -6372.59], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-7502.27, -6451.1], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-7516.86, -6395.84], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [-7523.48, -6372.59], 'special_key': None}], 'break_position': [[-7502.27, -6451.1], [-7516.86, -6395.84], [-7523.48, -6372.59]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[-7517.25, -6392.75], [-7523.88, -6369.5]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '采集秋分山西侧2个柔灯铃'}, 'author': 'GIA', 'tags': {'zh_CN': ['采集'], 'en_US': ['Collect']}, 'local_edit_mission': '采集秋分山西侧2个柔灯铃', 'description': '', 'note': ''}

class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

