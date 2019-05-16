# 基于Flask和Plyr的HTML5视频播放器 - Simple Player
搭建服务器让手机观看电脑上的视频

HTML5 播放器来自[Plyr](https://github.com/selz/plyr)，我的仓库里有 fork 的。

依赖：
- python3
- Flask
- Flvplayer.swf

将Flvplayer.swf 置于目录 static/ 下。该文件可以从[此处](http://www.xdowns.com/soft/1/95/2014/Soft_130297.html)获得。不考虑 Flash 兼容的可以不管(本来就是为了手机上看)。


将视频放到 static/video/ 里，然后运行服务器，用浏览器访问服务器就可以观看视频了。

```
python play.py
```

默认为127.0.0.1:8000，修改host和port需要参考[Flask](http://dormousehole.readthedocs.org/en/latest/)

移动端 AOSP 和 PC 端 chrome 观看视频运行良好。
