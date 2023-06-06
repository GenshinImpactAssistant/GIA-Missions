# GIA-Missions
存放GIA自定义任务的仓库. 你可以通过GIA下载使用,或者通过PR提交你的自定义任务.

## 自定义任务添加方法
- 先[编写一个自定义任务](https://genshinimpactassistant.github.io/GIA-Document/#/zh_CN/dev/mission)
- 进入仓库主页面 (https://github.com/GenshinImpactAssistant/GIA-Missions/tree/main)
- 点击fork一份你的仓库(fork仓库可以参考[牛牛也能看懂的 GitHub Pull Request 使用指南 (*´▽｀)ノノ](https://maa.plus/docs/2.4-%E7%BA%AF%E7%BD%91%E9%A1%B5%E7%AB%AFPR%E6%95%99%E7%A8%8B.html))
- 进入missions文件夹 (https://github.com/GenshinImpactAssistant/GIA-Missions/tree/main/missions)
- 点击Upload Files,点击Commit Changes并开启一份PR
- 等待校验通过即可

> 如果你完全没看懂,也可以直接把文件扔到群里让大佬们帮你加进仓库(雾)

## 自定义任务META格式
自定义任务文件内必须要有META.

```python
META = {
        "name": "你的mission任务名", # 必填
        "author": "你的github用户名或其他名称", # 必填
        "tags": ["tag1", "tag2"], # 选填 # tags可以填写: `采集` `圣遗物` `战斗` `日常`
        "description": "任务描述", # 选填
        "note": "任务注释" # 选填
    }
```

github workflow会校验你的META是否符合规范.
