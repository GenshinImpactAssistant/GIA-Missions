from source.mission.template.mission_just_collect import MissionJustCollect

META={'name': {'zh_CN': 'GIA_KalpalataLotus_3'}, 'author': 'GIA', 'tags': {'zh_CN': ['采集'], 'en_US': ['Collect']}, 'local_edit_mission': 'GIA_KalpalataLotus_3', 'description': '', 'note': '\n 必须需要纳西妲 Nahida must be needed'}

class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__(kyt2m_default_value, "kyt2m_default_name")

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

kyt2m_default_value = {'start_position': [-6489.25, 1623.0], 'end_position': [-6441.66, 1443.33], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [-6489.25, 1623.0], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [-6589.93, 1477.1], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [-6563.26, 1444.39], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [-6524.15, 1430.53], 'special_key': None}, {'id': 5, 'motion': 'ANY', 'position': [-6492.86, 1432.3], 'special_key': None}, {'id': 6, 'motion': 'ANY', 'position': [-6464.42, 1425.9], 'special_key': None}, {'id': 7, 'motion': 'ANY', 'position': [-6441.66, 1443.33], 'special_key': None}], 'break_position': [[-6489.25, 1623.0], [-6589.93, 1477.1], [-6563.26, 1444.39], [-6524.15, 1430.53], [-6492.86, 1432.3], [-6464.42, 1425.9], [-6441.66, 1448.33]], 'time': '', 'additional_info': {'kyt2m_version': '1.0', 'pickup_points': [1, 2, 3, 4, 5, 6], 'is_cliff_collection': True, 'is_active_pickup_in_bp': True, 'is_nahida_needed': True}, 'adsorptive_position': [[-6589.93, 1477.1], [-6563.26, 1444.39], [-6524.15, 1430.53], [-6492.86, 1432.3], [-6464.42, 1425.9], [-6441.66, 1448.33]]}
