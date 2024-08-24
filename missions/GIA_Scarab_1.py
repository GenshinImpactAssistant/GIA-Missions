from source.mission.template.mission_just_collect import MissionJustCollect

tlp2m_default_value = {'start_position': [-8592.86, 3464.92], 'end_position': [-8843.98, 3664.97], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-8592.86, 3464.92], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-8740.54, 3479.04], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [-8781.72, 3579.5], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [-8730.36, 3623.09], 'special_key': None}, {'id': 5, 'motion': 'ANY', 'position': [-8843.98, 3664.97], 'special_key': None}], 'break_position': [[-8592.86, 3464.92], [-8740.54, 3479.04], [-8781.72, 3579.5], [-8730.36, 3623.09], [-8843.98, 3664.97]], 'time': '', 'additional_info': {'path_recorder': '1.0', 'manually_modified': 'true'}, 'adsorptive_position': [[-8782.12, 3582.59], [-8730.75, 3626.18], [-8844.38, 3668.06]], 'generate_from': 'path recorder 1.0'}

META={'name': {'zh_CN': '圣金虫采集'}, 'author': 'GIA', 'tags': {'zh_CN': ['采集'], 'en_US': ['Collect']}, 'local_edit_mission': '圣金虫采集', 'description': '', 'note': ''}

class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__(tlp2m_default_value, "tlp2m_default_name",)

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

