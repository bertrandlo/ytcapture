# coding=utf-8

from subprocess import TimeoutExpired
from io import BytesIO
import ffmpeg
import youtube_dl
import json
import time

_settings = []
with open('settings.json', mode='r', encoding='utf8') as f:
    _settings = json.load(f)


def yt_streaming(channel_name):
    url = ""
    options = {'format': 'bestvideo/best', }
    channel_url = _settings["channels"][channel_name]["url"]

    with youtube_dl.YoutubeDL(options) as ydl:
        result = ydl.extract_info(channel_url, download=False)

    for node in result["formats"]:
        if node["height"] == 1080:
            url = node["url"]
            print(node["url"])

    proc = ffmpeg.input(url)\
        .filter("select", r"eq(pict_type,I)")\
        .filter("fps", "{}".format(1/int(_settings["interval"])))\
        .output("pipe:", format='rawvideo',  pix_fmt='rgb24')\
        .run_async(pipe_stdout=True)

    return proc


def yt_capture(channel_name):

    proc = yt_streaming(channel_name)

    while True:
        try:
            bytes_object = BytesIO()
            bytes_object.write(proc.stdout.read(1920*1080*3))
            checkvalue = yield bytes_object

        except (TypeError, AttributeError):
            yield None

        if checkvalue == StopIteration:
            proc.terminate()
            new_channel_name = yield None
            proc1 = yt_streaming(new_channel_name)
            print("Change To Channel --- {}".format(new_channel_name))
            proc = proc1
            checkvalue = None
