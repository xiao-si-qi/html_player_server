#-*- coding: UTF-8 -*-
from flask import Flask , url_for,send_from_directory, render_template ,request
import os, sys
app = Flask(__name__)
video_format = ( 'WEBM', 'MP4', 'OGG','FLV','AAC','MOV','MKV' )
photo_format = ( 'JPEG', 'PNG', 'GIF','JPG','BMP')

def get_file_list(file_path):#返回按日期排序的文件列表
    dir_list = os.listdir(file_path)
    if not dir_list:
        return
    else:
        # 注意，这里使用lambda表达式，将文件按照最后修改时间顺序升序排列
        # os.path.getmtime() 函数是获取文件最后修改时间
        # os.path.getctime() 函数是获取文件最后创建时间
        dir_list = sorted(dir_list,  key=lambda x: os.path.getmtime(os.path.join(file_path, x)))
        # print(dir_list)
        return dir_list

@app.route('/')
def index():
    files = get_file_list('static/file')
    file_type = []
    for file in files: #拿到目录下的所有的文件夹和文件名，判断文件类型
        if os.path.isdir('static/file/'+ file):
            file_type.append([file, "文件夹"])
        else:
            file_type.append([file, file.split(".")[-1]])
    return render_template('index.html', file_type=file_type, dir="")



@app.route('/<video_file>')
def play(video_file):
    user_agent = request.headers.get('User-Agent')
    #得到用户浏览器的类型
    video_file=video_file.replace('&','/')
    print(video_file)
    #在get 传文件路路径时，使用“&”作为分隔符，在程序内部使用“/”作为分隔符，在这里进行转换

    if os.path.isdir('static/file/' + video_file) : #判断路径是否为文件夹，是则返回文件列表模板
        files = get_file_list('static/file/'+ video_file)
        file_type=[]
        for file in files:#拿到该目录下的所有的文件夹和文件名，判断文件类型
            if os.path.isdir('static/file/' + video_file+"/"+file):#判断是否为文件夹
               file_type.append([file,"文件夹"])
            else:
               file_type.append([file,file.split(".")[-1]])#拿到文件的扩展名
        return render_template('index.html', file_type=file_type,dir=video_file+"/")

    elif os.path.exists('static/file/' + video_file) and video_file.split('.')[-1].upper()in photo_format:#判断路径是否为图片，返回图片展示模板
        files = get_file_list(os.path.split('static/file/' + video_file)[0])  # 得到当前文件所在的目录
        photolist = []
        for file in files:
            if file.split('.')[-1].upper() in photo_format:  # 找到当前目录的所有图片文件，展示在一个页面上
                photolist.append(file)
        path = os.path.split(video_file)[0] + "/"
        print(path)
        return render_template('photo.html' ,path=path,photolist=photolist)

    elif os.path.exists('static/file/' + video_file) and video_file.split('.')[-1].upper()in video_format:#判断路径是否为视频，返回视频播放模板
        files = get_file_list(os.path.split('static/file/' + video_file)[0]) #得到当前文件所在的目录
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

    elif os.path.exists('static/file/' + video_file):#不支持的文件类型返回下载界面
        return render_template("download.html",link=video_file)


    else:#返回错误页面
        return render_template('404.html', error_message="打开路径出错：/"+video_file,error="不能打开此路径，可能是文件已被删除" ), 404

@app.errorhandler(404)
def miss(e):
    return render_template('404.html',error="非法的路径"), 404

if __name__ == '__main__':
    #app.run(port=8000)
    app.run( host='0.0.0.0',port=8000 )#host='0.0.0.0'，允许任任意IP访问

