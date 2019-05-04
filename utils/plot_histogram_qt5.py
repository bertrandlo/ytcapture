# coding=utf-8
from itertools import cycle
from collections import deque

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget

import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class PlotWin(QWidget):
    """ 3D BarChart https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html#bar-plots """
    def __init__(self,  data_lines_max_number=10, x_range=(0, 255), z_range=(0, 5)):
        """
        :param data_lines_max_number: max lines shown in chart
        :param x_range: x-axis range
        :param z_range: y-axis range
        PlotWin.insert_new_line(line): 1-D Series as Bar Dataset
        PlotWin.color(): generator of bar's color cyclely
        PlotWin.set_xticks(list): custom x-ticks and label
        """
        super().__init__()
        self.setObjectName("Matplotlib Widget")
        self.setWindowTitle("Gray Scale Statics")
        self.x_range = x_range

        self.fig = FigureCanvas(Figure())
        subplot_args = {'projection': '3d'}
        self.fig.axes = self.fig.figure.subplots(subplot_kw=subplot_args)

        self.data_lines_max_number = data_lines_max_number  # 預設顯示的資料列數
        self.y_ticks = list(range(0, data_lines_max_number, 1))
        self.lines = deque()  # 實際數據
        self.lines_draw = deque()  # 繪製的數據線

        self.fig.axes.view_init(elev=45, azim=30)
        self.fig.axes.yaxis.set_major_locator(plt.NullLocator())
        self.fig.axes.yaxis.set_major_formatter(plt.NullFormatter())
        self.fig.axes.set_xlabel("Gray Scale")
        self.fig.axes.set_zlabel("%")
        self.fig.axes.set_zlim3d(z_range)
        self.fig.axes.set_xlim3d(x_range)
        self.fig.axes.set_ylim3d((0, data_lines_max_number - 1))
        self.fig.axes.set_zticks(list(range(z_range[0], z_range[1], 1)))
        self.fig.axes.set_facecolor('#444444')
        self.fig.figure.tight_layout()

        plt.yticks(self.y_ticks[0::2])
        plt.xticks([0, 50, 100, 150, 200, 256])

        self.graphicsView = QtWidgets.QGraphicsView()
        self.vlayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.vlayout)
        self.vlayout.setStretch(1, 1)

        self.vlayout.addWidget(NavigationToolbar(self.fig, self))
        self.vlayout.addWidget(self.graphicsView)
        self.scene = QtWidgets.QGraphicsScene()

        self.graphics_proxy_widget = self.scene.addWidget(self.fig)  # type: QtWidgets.QGraphicsProxyWidget

        self.graphicsView.setScene(self.scene)
        self.graphicsView.fitInView(self.scene.sceneRect(), QtCore.Qt.KeepAspectRatio)
        self.resize(1024, 768)
        self.colors = self.color()

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphics_proxy_widget.setSizePolicy(sizePolicy)

    def set_xticks(self, ticks):
        self.fig.axes.set_xticks(ticks)
        self.fig.axes.set_xticklabels([str(i) for i in ticks])

    def fit_matplotlib_win(self):
        try:
            self.graphics_proxy_widget.resize(self.graphicsView.width(), self.graphicsView.height())  # 讓 matplotlib child widget fit graphicsview
            self.scene.setSceneRect(self.scene.itemsBoundingRect())  # 讓 graphicsscene 儘量放大並包括整個 matplotlib child widget
            self.graphicsView.fitInView(self.scene.sceneRect(), QtCore.Qt.KeepAspectRatio)  # graphicsview 盡量放大顯示整個 graphicsscene
            self.graphicsView.update()
        except AttributeError:
            pass

    def changeEvent(self, event):
        self.fit_matplotlib_win()

    def resizeEvent(self, event):
        self.fit_matplotlib_win()

    def insert_new_line(self, line):
        self.lines.append(line)

        for idx in range(len(self.lines_draw)):
            line = self.lines_draw.pop()
            line.remove()

        if len(self.lines) > self.data_lines_max_number:
            self.lines.popleft()

        for line, c, k in zip(self.lines, next(self.colors), self.y_ticks):
            self.lines_draw.append(self.fig.axes.bar(np.arange(self.x_range[1]+1), line, zs=k, zdir='y', color=c, alpha=0.8))

        self.fig.draw()
        self.scene.update()
        self.graphicsView.update()

    def color(self):
        _colors = cycle(['#7e1e9c', '#15b01a', '#0343df', '#ff81c0', '#e83a3a',
                         '#6e750e', '#029386', '#f97306', '#c20078', '#ad8150'])
        colors = deque()
        idx = 0
        while True:
            if idx >= self.data_lines_max_number:
                colors.popleft()
            else:
                idx = idx + 1

            colors.append(next(_colors))
            yield colors
