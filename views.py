from pytube import YouTube
import os
from flask import Blueprint, request, render_template, send_file

views = Blueprint(__name__, "views")

@views.route("/", methods=["GET", "POST"])
def index():
    video_url = ''
    resolutions = []
    if request.method == "POST":
        video_url = request.form["video_url"]
        yt = YouTube(video_url)
        resolutions = [stream.resolution for stream in yt.streams.filter(progressive=True)]

    # if request.method == "POST" and 'download_resolution' in request.form:
    #     yt = YouTube(video_url)
    #     ys = yt.streams.filter(res=f"{resolution}").first()
    #     if ys:
    #         title = yt.title
    #         file_path = f"{title}.mp4"
    #         ys.download(filename=title)
    #         return send_file(file_path, as_attachment=True)
        
    return render_template("index.html", resolutions=resolutions, video_url=video_url)
