from source.mission.template.mission_just_collect import MissionJustCollect

tlp2m_default_value = {'start_position': [1840.81, -5598.66], 'end_position': [1791.43, -5681.05], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [1840.81, -5598.66], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [1818.65, -5587.81], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [1785.64, -5609.23], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [1771.97, -5630.56], 'special_key': None}, {'id': 5, 'motion': 'ANY', 'position': [1771.16, -5665.99], 'special_key': None}, {'id': 6, 'motion': 'ANY', 'position': [1791.43, -5681.05], 'special_key': None}], 'break_position': [[1840.81, -5598.66], [1818.65, -5587.81], [1785.64, -5609.23], [1771.97, -5630.56], [1771.16, -5665.99], [1791.43, -5681.05]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[1771.59, -5637.14]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '小灯草采集'}, 'author': 'GIA', 'tags': {'zh_CN': ['采集'], 'en_US': ['Collect']}, 'local_edit_mission': '小灯草采集', 'description': '', 'note': ''}

class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

