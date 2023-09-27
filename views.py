from flask import Blueprint, request, render_template, send_file, redirect
import os
import yt_dlp

views = Blueprint(__name__, "views")

def get_video_info(video_url):
    with yt_dlp.YoutubeDL() as ydl:
        info = ydl.extract_info(video_url, download=False)
        return info

def filter_resolutions(resolutions, video_ext):
    filtered_resolutions = []
    for resolution in resolutions:
        if resolution["video_ext"] == video_ext:
            filtered_resolutions.append(resolution)
    return filtered_resolutions

@views.route("/", methods=["GET", "POST"])
def index():
    video_url = ""
    resolutions = []
    filtered_resolutions = []
    if request.method == "POST" and 'select_video' in request.form:
        video_url = request.form["video_url"]
        ydl = yt_dlp.YoutubeDL()
        info = ydl.extract_info(video_url, download=False)
        resolutions = info["formats"]
        filtered_resolutions = filter_resolutions(resolutions, "mp4")
        print(filtered_resolutions)

    if request.method == "POST" and 'download_resolution' in request.form:
        download_file = request.form.get("download_resolution")
        return redirect(f"{download_file}")

    return render_template("index.html", resolutions=filtered_resolutions, video_url=video_url)
