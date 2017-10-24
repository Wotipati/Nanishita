# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap, QFont


class Subject(QWidget):

    def __init__(self):
        super().__init__()

        self.label_now_subject = QLabel(self)
        self.layout_button = QVBoxLayout()
        self.init_ui()

    def init_ui(self):
        font_time = QFont()
        font_time.setPointSize(50)
        font_time.setBold(True)
        self.label_time.setFont(font_time)

        layout_timer = QHBoxLayout()
        icon_timer = QLabel()
        pixmap_timer = QPixmap('./icon/stopwatch.png')
        pixmap_timer_resized = pixmap_timer.scaled(150, 150)
        icon_timer.setPixmap(pixmap_timer_resized)
        layout_timer.addWidget(icon_timer)
        layout_timer.addWidget(self.label_time)

        time = "{0:02d}:{1:02d}:{2:02d}".format(self.hour, self.min, self.sec)
        self.label_time.setText(str(time))

        font_button = QFont()
        font_button.setPointSize(20)
        font_button.setBold(True)

        button_start = QPushButton("Start", self)
        button_start.setFont(font_button)
        button_start.clicked.connect(self.timer_start)

        button_stop = QPushButton("Stop", self)
        button_stop.setFont(font_button)
        button_stop.clicked.connect(lambda: self.timer.stop())

        button_reset = QPushButton("Reset", self)
        button_reset.setFont(font_button)
        button_reset.clicked.connect(self.timer_reset)

        layout_button = QHBoxLayout()
        layout_button.addWidget(button_start)
        layout_button.addWidget(button_stop)
        layout_button.addWidget(button_reset)

        self.layout_main.addLayout(layout_timer)
        self.layout_main.addLayout(layout_button)
