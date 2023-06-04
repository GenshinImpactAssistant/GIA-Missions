from source.mission.template.mission_just_collect import MissionJustCollectGroup
META={
    'name':{
        'zh_CN':'采集琉璃百合',
        'en_US':'Collect Glaze Lily'
    },
    'author':"GIA",
    'tags':{
        'zh_CN':["采集"],
        'en_US':["Collect"]
    },
    'description': {
        'zh_CN':"采集约10个琉璃百合。",
        'en_US':"Collect about 10 Glaze Lily."
    },
    'note': ""
}
class MissionMain(MissionJustCollectGroup):
    def __init__(self):
        super().__init__(['GlazeLily20230513214207i0',
                          'GlazeLily20230513214422i0',
                          'GlazeLily20230513214617i0'
                          ],
                           name='MissionGlazeLily')

if __name__ == '__main__':
    import time
    MissionMain().start()
    while 1:time.sleep(1)