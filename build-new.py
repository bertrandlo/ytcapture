# For CX_Freeze  Using "python build-new.py build"
import sys, os
from cx_Freeze import setup, Executable
# from PyQt5 import QtWebEngine
# Dependencies are automatically detected, but it might need fine tuning.
os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python36\tcl\tk8.6'

includes = ["numpy", "youtube_dl\\youtube_dl"]
base = "C:\\\\Users\\brt\\PycharmProjects\\ytcapture\\venv\\"
build_exe_options = {"packages": ["PyQt5", "os", "numpy", "encodings", "asyncio"],
                    #'build_exe': "b:\\",
                    'includes': includes,
                    'include_files': ["settings.json", "icon.qrc", "icon_qrc.py", "ffmpeg.exe", "resources\\", "youtube_dl\\"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None

setup(name="ytcapture",
      version="0.1",
      description="youtube video image capture",
      options={"build_exe": build_exe_options},
      executables=[Executable("ytcapture.py", base=base, icon=".\\resources\\box-multi-size.ico")])
