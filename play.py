#-*- coding: UTF-8 -*-
from flask import Flask , url_for, render_template ,request
import os, sys


app = Flask(__name__)

legal_suffix = ( 'WEBM', 'MP4', 'OGG' )

@app.route('/')
def index():
    files = os.listdir('static/video')
    return render_template('index.html', files=files,dir="")


@app.route('/<video_file>')
def play(video_file):
    user_agent = request.headers.get('User-Agent')
    #得到用户浏览器的类型
    video_file=video_file.replace('&','/')
    print(video_file)
    #在get 传文件路路径时，使用“&”作为分隔符，在程序内部使用“/”作为分隔符，在这里进行转换

    if os.path.isdir('static/video/' + video_file): #判断路径是否为文件夹，是则返回文件列表模板
        files = os.listdir('static/video/'+ video_file)
        return render_template('index.html', files=files,dir=video_file+"/")

    elif os.path.exists('static/video/' + video_file):
        files = os.listdir(os.path.split('static/video/' + video_file)[0])
        videolist = []
        for file in files:
            for suffix in legal_suffix:
                if suffix in file.split('.')[-1].upper():  # Check file in list have a suffix of webm, mp4 or ogg.
                    videolist.append(file)
        print(os.path.split(video_file)[0])
        return render_template('player.html', user_agent=user_agent, video_file=video_file,videolist=videolist,path=os.path.split(video_file)[0])
    return render_template('404.html', error="Video file %s doesn't exist!" % video_file), 404

if __name__ == '__main__':
    #app.run(port=8000)
    app.run(debug=True, host='0.0.0.0',port=8000 )

