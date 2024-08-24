from source.mission.template.mission_just_collect import MissionJustCollect

tlp2m_default_value = {'start_position': [-11540.98, -1233.2], 'end_position': [-11594.31, -1290.69], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-11540.98, -1233.2], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-11527.5, -1149.14], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [-11628.36, -1151.34], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [-11641.9, -1073.15], 'special_key': None}, {'id': 5, 'motion': 'ANY', 'position': [-11735.02, -1049.77], 'special_key': None}, {'id': 6, 'motion': 'ANY', 'position': [-11746.71, -1181.71], 'special_key': None}, {'id': 7, 'motion': 'ANY', 'position': [-11558.23, -1256.71], 'special_key': None}, {'id': 8, 'motion': 'ANY', 'position': [-11560.86, -1271.34], 'special_key': None}, {'id': 9, 'motion': 'ANY', 'position': [-11560.86, -1271.34], 'special_key': None}, {'id': 10, 'motion': 'ANY', 'position': [-11594.31, -1290.69], 'special_key': None}], 'break_position': [[-11540.98, -1233.2], [-11527.5, -1149.14], [-11628.36, -1151.34], [-11641.9, -1073.15], [-11735.02, -1049.77], [-11746.71, -1181.71], [-11558.23, -1256.71], [-11560.86, -1271.34], [-11560.86, -1271.34], [-11594.31, -1290.69]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[-11628.75, -1148.25], [-11558.62, -1253.62], [-11561.25, -1268.25]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '万相石采集'}, 'author': 'GIA', 'tags': {'zh_CN': ['采集'], 'en_US': ['Collect']}, 'local_edit_mission': '万相石采集', 'description': '', 'note': ''}

class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

