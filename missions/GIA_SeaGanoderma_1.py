from source.mission.template.mission_just_collect import MissionJustCollect

META={'name': {'zh_CN': 'GIA_SeaGanoderma_1'}, 'author': 'GIA', 'tags': {'zh_CN': ['采集'], 'en_US': ['Collect']}, 'local_edit_mission': 'GIA_SeaGanoderma_1', 'description': '使用`酒馆路径转任务`的自定义任务', 'note': '\n 必须需要纳西妲 Nahida must be needed'}

class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__(kyt2m_default_value, "kyt2m_default_name")

if __name__ == '__main__':
    mission = MissionMain()
    mission.start()

kyt2m_default_value = {'start_position': [7591.25, 5885.25], 'end_position': [7466.6, 5657.0], 'position_list': [{'id': 1, 'motion': 'ANY', 'position': [7591.25, 5885.25], 'special_key': None}, {'id': 2, 'motion': 'ANY', 'position': [7583.94, 5758.42], 'special_key': None}, {'id': 3, 'motion': 'ANY', 'position': [7546.23, 5686.34], 'special_key': None}, {'id': 4, 'motion': 'ANY', 'position': [7466.6, 5657.0], 'special_key': None}], 'break_position': [[7591.25, 5885.25], [7583.94, 5758.42], [7546.23, 5686.34], [7466.6, 5657.0]], 'time': '', 'additional_info': {'kyt2m_version': '1.0', 'pickup_points': [2, 3], 'is_active_pickup_in_bp': True}, 'adsorptive_position': [[7583.94, 5758.42], [7546.23, 5686.34], [7466.6, 5657.0]]}
