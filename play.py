#-*- coding: UTF-8 -*-
from flask import Flask , url_for,send_from_directory, render_template ,request
import os, sys
app = Flask(__name__)
video_format = ( 'WEBM', 'MP4', 'OGG','FLV','AAC','MOV','MKV' )
photo_format = ( 'JPEG', 'PNG', 'GIF','JPG' )

@app.route('/')
def index():
    files = os.listdir('static/file')
    return render_template('index.html', files=files,dir="")


@app.route('/<video_file>')
def play(video_file):
    user_agent = request.headers.get('User-Agent')
    #得到用户浏览器的类型
    video_file=video_file.replace('&','/')
    print(video_file)
    #在get 传文件路路径时，使用“&”作为分隔符，在程序内部使用“/”作为分隔符，在这里进行转换

    if os.path.isdir('static/file/' + video_file) : #判断路径是否为文件夹，是则返回文件列表模板
        files = os.listdir('static/file/'+ video_file)
        return render_template('index.html', files=files,dir=video_file+"/")

    elif os.path.exists('static/file/' + video_file) and video_file.split('.')[-1].upper()in photo_format:#判断路径是否为图片，返回图片展示模板
        files = os.listdir(os.path.split('static/file/' + video_file)[0])  # 得到当前文件所在的目录
        photolist = []
        for file in files:
            if file.split('.')[-1].upper() in photo_format:  # 找到当前目录的所有图片文件，展示在一个页面上
                photolist.append(file)
        path = os.path.split(video_file)[0] + "/"
        print(path)
        return render_template('photo.html' ,path=path,photolist=photolist)

    elif os.path.exists('static/file/' + video_file) and video_file.split('.')[-1].upper()in video_format:#判断路径是否为视频，返回视频播放模板
        files = os.listdir(os.path.split('static/file/' + video_file)[0]) #得到当前文件所在的目录
        videolist = []
        for file in files:
            if file.split('.')[-1].upper() in video_format:  # 找到当前目录的所有视频文件，作为播放页面的播放列表
                videolist.append(file)
        path=os.path.split(video_file)[0]
        if path!="":
            path=path+"/"
        print(path)
        print("video_file："+video_file)
        return render_template('player.html', user_agent=user_agent, video_file=video_file,videolist=videolist,path=path)
    else:#不支持的文件类型返回404
        return render_template('404.html', error=" %s 不支持显示此文件!" % video_file), 404

if __name__ == '__main__':
    #app.run(port=8000)
    app.run(debug=True, host='0.0.0.0',port=8000 )

