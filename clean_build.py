import os, stat
from shutil import rmtree


def del_rw(action, name, exc):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)

build_exe_options = {
                    'build_exe':  "C:\\Users\\brt\\PycharmProjects\\ytcapture\\build\\exe.win-amd64-3.6\\"
}

excludes_files = [r'tcl',
                  r'tk',
                  r'platforms',
                  r'mediaservice',
                  r'imageformats',
                  r'lib\numpy\core\python36.dll',
                  r'lib\numpy\fft\python36.dll',
                  r'lib\numpy\linalg\python36.dll',
                  r'lib\numpy\random\python36.dll',
                  r'lib\PIL\python36.dll',
                  r'lib\PyQt5\python36.dll',
                  r'lib\numpy\fft\python36.dll',
                  r'lib\PyQt5\Qt5WebEngineCore.dll',
                  r'lib\PyQt5\Qt\bin\Qt5WebEngineCore.dll',
                  r'lib\PyQt5\Qt\bin\Qt5WebEngine.dll',
                  r'lib\PyQt5\Qt\bin\Qt5Network.dll',
                  r'lib\PyQt5\Qt\bin\Qt5QuickTemplates2.dll',
                  r'lib\PyQt5\Qt\bin\Qt5QuickParticles.dll',
                  r'lib\PyQt5\Qt\bin\Qt5Quick.dll',
                  r'lib\PyQt5\Qt\bin\Qt5Qml.dll',
                  r'lib\PyQt5\Qt\bin\Qt5Bluetooth.dll',
                  r'lib\PyQt5\Qt\bin\Qt5PrintSupport.dll',
                  r'lib\PyQt5\Qt\bin\Qt5Designer.dll',
                  r'lib\PyQt5\Qt\bin\Qt5DesignerComponents.dll',
                  r'lib\PyQt5\Qt\bin\designer.exe',
                  r'lib\PyQt5\Qt5Network.dll',
                  r'lib\PyQt5\Qt5Designer.dll',
                  r'lib\PyQt5\Qt5Quick.dll',
                  r'lib\PyQt5\QtQuick.pyd',
                  r'lib\PyQt5\Qt5Qml.dll',
                  r'lib\PyQt5\QtQml.pyd',
                  r'lib\PyQt5\Qt\resources\qtwebengine_resources.pak',
                  r'lib\PyQt5\Qt\resources\qtwebengine_resources_100p.pak',
                  r'lib\PyQt5\Qt\resources\qtwebengine_resources_200p.pak',
                  r'lib\PyQt5\Qt\resources\qtwebengine_devtools_resources.pak',
                  r'youtube_dl\.git']

for item in excludes_files:
    target = build_exe_options['build_exe'] + item
    print(target, os.path.isdir(target), os.path.isfile(target))
    if os.path.isdir(target):
        rmtree(target, onerror=del_rw)

    if os.path.isfile(target):
        os.remove(target)
