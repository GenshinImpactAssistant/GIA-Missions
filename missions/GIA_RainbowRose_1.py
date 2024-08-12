from source.mission.template.mission_just_collect import MissionJustCollect

tlp2m_default_value = {'start_position': [-8704.86, -6503.84], 'end_position': [-8968.08, -6407.79], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-8704.86, -6503.84], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-8753.65, -6454.08], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [-8844.54, -6399.49], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [-8921.95, -6453.56], 'special_key': None}, {'id': 5, 'motion': 'ANY', 'position': [-8968.08, -6407.79], 'special_key': None}], 'break_position': [[-8704.86, -6503.84], [-8753.65, -6454.08], [-8844.54, -6399.49], [-8921.95, -6453.56], [-8968.08, -6407.79]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[-8846.56, -6400.07], [-8920.41, -6455.97], [-8975.28, -6409.66]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '采集苍晶区3个虹彩蔷薇'}, 'author': 'GIA', 'tags': {'zh_CN': ['采集'], 'en_US': ['Collect']}, 'local_edit_mission': '采集苍晶区3个虹彩蔷薇', 'description': '', 'note': ''}

class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

