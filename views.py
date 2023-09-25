from pytube import YouTube
import os
from flask import Blueprint, request, render_template, send_file

views = Blueprint(__name__, "views")


@views.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video_url = request.form["video_url"]
        yt = YouTube(video_url)
        ys = yt.streams.get_highest_resolution()
        ys.download()

        return send_file(f"{yt.title}.mp4", as_attachment=True)

    return render_template("index.html")
