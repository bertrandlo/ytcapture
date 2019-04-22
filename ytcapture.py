# coding=utf-8
import sys
import time
import gc
import json

from os.path import expanduser
from datetime import datetime
from PIL import Image
from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsScene, QGraphicsPixmapItem, QGraphicsTextItem
from PyQt5.QtCore import Qt, pyqtSlot, pyqtSignal, QThread
from PyQt5.QtGui import QIcon, QPixmap, QImage, QResizeEvent, QMouseEvent, QFont, QColor

import ytcapture_ui
from css_theme import cssStyle
from pipe_reader_async import yt_capture
from util import bytes_to_image, image_refine
import icon_qrc

# tesserocr windows build whl download
# https://github.com/simonflueckiger/tesserocr-windows_build/releases

settings = []
with open('settings.json', mode='r', encoding='utf8') as f:
    settings = json.load(f)


class PipeWorker(QThread):

    signal_update = pyqtSignal(object)

    def __init__(self, signal_terminate):
        super().__init__()
        self.flag_terminate = False

        self.signal_terminate = signal_terminate
        self.url = ""
        self.proc_ffmpeg = yt_capture(list(settings["channels"].keys())[0])
        self.channel_name = list(settings["channels"].keys())[0]

    @pyqtSlot()
    def terminate(self,):
        pass

    def run(self):

        next(self.proc_ffmpeg)

        while True:
            frame = next(self.proc_ffmpeg)
            img = bytes_to_image(frame)

            if type(img) is Image.Image and not self.flag_terminate:
                self.signal_update.emit(img)

            if self.flag_terminate:
                self.proc_ffmpeg.send(StopIteration)
                self.proc_ffmpeg.send(self.channel_name)
                self.flag_terminate = False


class ScreenCapture(QWidget, ytcapture_ui.Ui_TessReader):

    signal_terminate = pyqtSignal()
    signal_graphicview_update = pyqtSignal()

    def __init__(self, parent=None):
        super(ScreenCapture, self).__init__(parent)
        self.setupUi(self)

        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.image = Image.open('resources/Loading.png', mode='r')  # type: Image.Image
        self.pixmap_item = self.scene.addPixmap(QPixmap('resources/Loading.png'))

        self.pipe_worker = PipeWorker(self.signal_terminate)
        self.pipe_worker.start()
        self.pipe_worker.signal_update.connect(lambda img: self.update(img), Qt.QueuedConnection)

        self.content = ""
        for channel in settings["channels"]:
            self.comboBox.addItem("{} - {} [{}]".format(channel, settings["channels"][channel]["url"], settings["channels"][channel]["quality"]), channel)

        self.comboBox.currentIndexChanged.connect(self.reloading)

    def reloading(self):
        self.show_loading_cover()
        self.pipe_worker.channel_name = self.comboBox.itemData(self.comboBox.currentIndex())
        self.pipe_worker.flag_terminate = True

    def show_loading_cover(self):
        self.image = Image.open('resources/Loading.png', mode='r')  # type: Image.Image
        self.pixmap_item = self.scene.addPixmap(QPixmap('resources/Loading.png'))
        self.scene.update()

    def autofit(self):
        #print("SIZE=", self.scene.itemsBoundingRect())
        self.scene.setSceneRect(self.scene.itemsBoundingRect())
        self.graphicsView.fitInView(self.scene.itemsBoundingRect(), Qt.KeepAspectRatio)
        self.scene.update()

    def closeEvent(self, event):
        self.signal_terminate.emit()

    @pyqtSlot(object)
    def update(self, img):
        del self.image
        self.image = img
        data = image_refine(img)  # 重新調整 Image 的 Channel 否則 Qt5 轉換成 QImage 會 Crash
        qim = QImage(data, img.size[0], img.size[1], QImage.Format_ARGB32)
        pix = QPixmap.fromImage(qim)

        self.scene.removeItem(self.pixmap_item)
        del self.pixmap_item
        gc.collect()

        self.pixmap_item = self.scene.addPixmap(pix)
        self.scene.setSceneRect(self.scene.itemsBoundingRect())
        self.graphicsView.update()
        self.graphicsView.fitInView(self.pixmap_item, Qt.KeepAspectRatio)

    def resizeEvent(self, event: QResizeEvent):
        if (self.graphicsView.scene() is not None) and (self.pixmap_item is not None):
            self.graphicsView.fitInView(self.pixmap_item, Qt.KeepAspectRatio)
            self.graphicsView.update()

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        self.image.save("{}/Desktop/{}.png".format(expanduser("~"), datetime.strftime(datetime.now(), "%Y%m%d-%H%M%S")))

    def showEvent(self, event):
        self.autofit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(':/resources/box-multi-size.ico'))

    win = ScreenCapture()
    win.setWindowTitle("YT Capture")
    win.setStyleSheet(cssStyle)
    win.show()
    sys.exit(app.exec_())
