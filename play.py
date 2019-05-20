#-*- coding: UTF-8 -*-
from flask import Flask , url_for, render_template ,request
import os, sys


app = Flask(__name__)

legal_suffix = ( 'WEBM', 'MP4', 'OGG' )

@app.route('/')
def index():
    files=os.listdir('static/video')
    video_exist = False
    for video_file in files:
        for suffix in legal_suffix :
            if suffix in video_file.split('.')[-1].upper(): # Check file in list have a suffix of webm, mp4 or ogg. 
                video_exist = True
                print(files)
                return render_template('index.html', files=files)
    return render_template('404.html', error="Video directory is empty!"), 404

@app.route('/<video_file>')
def play(video_file):
    user_agent=request.headers.get('User-Agent')
    files = os.listdir('static/video')
    if os.path.exists('static/video/' + video_file):
        for suffix in legal_suffix :
            if suffix in video_file.split('.')[-1].upper():
                return render_template('player.html', user_agent=user_agent, video_file=video_file,files=files)
    return render_template('404.html', error="Video file %s doesn't exist!" % video_file), 404

if __name__ == '__main__':
    #app.run(port=8000)
    app.run(debug=True, host='0.0.0.0',port=8000 )

