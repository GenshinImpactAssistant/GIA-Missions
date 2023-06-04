from source.mission.template.mission_just_collect import MissionJustCollect
from source.util import t2t
META={
    'name':{
        'zh_CN':'采集琉璃袋1',
        'en_US':'Collect Violetgrass 1'
    },
    'author':"GIA",
    'tags':["采集"],
    'note':"not recommend"
}
class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__("LLDV2P120230507182352i0", "MissionVioletgrass1")