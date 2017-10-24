# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QFont, QColor, QPainter


class Stopwatch(QWidget):

    def __init__(self):
        super().__init__()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.time_count)
        self.sec  = 0
        self.min  = 0
        self.hour = 0
        self.label_time = QLabel(self)

        self.layout_main = QVBoxLayout()

        self.init_ui()

    def init_ui(self):
        font_time = QFont("ariel", 70)
        font_time.setBold(True)
        self.label_time.setFont(font_time)
        self.label_time.setStyleSheet("color:#F2EBBF;")

        layout_timer = QHBoxLayout()
        icon_timer = QLabel()
        pixmap_timer = QPixmap('./icon/stopwatch.png')
        pixmap_timer_resized = pixmap_timer.scaled(150, 150)
        icon_timer.setPixmap(pixmap_timer_resized)
        layout_timer.addWidget(icon_timer)
        layout_timer.addWidget(self.label_time)

        time = "{0:02d}:{1:02d}:{2:02d}".format(self.hour, self.min, self.sec)
        self.label_time.setText(str(time))

        font_button = QFont("monospace", 20)
        font_button.setBold(True)

        button_start = QPushButton("Start", self)
        button_start.setStyleSheet("background-color:#3C3C46; color:#D9D9D9;")
        button_start.setFont(font_button)
        button_start.setFixedHeight(50)
        button_start.clicked.connect(self.timer_start)

        button_stop = QPushButton("Stop", self)
        button_stop.setStyleSheet("background-color:#3C3C46; color:#D9D9D9;")
        button_stop.setFont(font_button)
        button_stop.setFixedHeight(50)
        button_stop.clicked.connect(lambda: self.timer.stop())

        button_reset = QPushButton("Reset", self)
        button_reset.setStyleSheet("background-color:#3C3C46; color:#D9D9D9;")
        button_reset.setFont(font_button)
        button_reset.setFixedHeight(50)
        button_reset.clicked.connect(self.timer_reset)

        layout_button = QHBoxLayout()
        layout_button.addWidget(button_start)
        layout_button.addWidget(button_stop)
        layout_button.addWidget(button_reset)

        self.layout_main.addLayout(layout_timer)
        self.layout_main.addLayout(layout_button)

    def timer_start(self):
        self.timer.start(1000)

    def timer_reset(self):
        self.timer.stop()
        self.sec  = 00
        self.min  = 00
        self.hour = 00

        time = "{0:02d}:{1:02d}:{2:02d}".format(self.hour, self.min, self.sec)
        self.label_time.setText(time)

    def time_count(self):
        if self.sec < 59:
            self.sec += 1

        else:
            if self.min < 59:
                self.sec = 00
                self.min += 1

            elif self.min == 59:
                self.hour += 1
                self.min = 00
                self.sec = 00

        time = "{0:02d}:{1:02d}:{2:02d}".format(self.hour, self.min, self.sec)
        self.label_time.setText(time)
