# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import QTimer, QSize, Qt
from PyQt5.QtGui import QPixmap, QFont, QColor, QPainter, QIcon


class Stopwatch(QWidget):

    def __init__(self):
        super().__init__()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.time_count)
        self.sec = 0
        self.min = 0
        self.hour = 0
        self.sec_total = 0
        self.min_total = 0
        self.hour_total = 0

        self.icon_timer = QPushButton()
        self.label_time = QLabel(self)
        self.label_time_total = QLabel(self)
        self.is_started = False
        self.layout_main = QHBoxLayout()
        self.layout_timer = QVBoxLayout()
        self.layout_time_label = QVBoxLayout()
        self.button_switch = QPushButton("START", self)

        self.init_ui()

    def init_ui(self):
        font_time = QFont("ariel", 70)
        font_time.setBold(True)
        self.label_time.setFont(font_time)
        self.label_time.setAlignment(Qt.AlignCenter)
        self.label_time.setStyleSheet(
            "background-color:#3C3C46; color:#F2EBBF; border-radius:8px; border-width:0px; border-color:#D9D9D9;"
            "border-style: solid;")

        font_time_total = QFont("ariel", 20)
        font_time_total.setBold(True)
        self.label_time_total.setFont(font_time_total)
        self.label_time_total.setFixedHeight(40)
        self.label_time_total.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_time_total.setStyleSheet(
            "background-color:#3C3C46; color:#F2EBBF; border-radius:8px; border-width:0px; border-color:#D9D9D9;"
            "border-style: solid;")

        self.icon_timer.setIconSize(QSize(100, 100))
        self.icon_timer.setIcon(QIcon('./icon/stopwatch_stop.png'))
        self.icon_timer.setStyleSheet(
            "background-color:#3C3C46; color:#F2EBBF; border-radius:8px; border-width:0px; border-color:#D9D9D9;"
            "border-style:solid;")
        self.icon_timer.clicked.connect(lambda: self.timer_start(self.is_started))
        self.button_switch.setFixedWidth(100)
        self.button_switch.setFixedWidth(100)

        time = "{0:02d}:{1:02d}:{2:02d}".format(self.hour, self.min, self.sec)
        self.label_time.setText(time)

        total = "Today's total time: {0:02d}:{1:02d}:{2:02d}  ".format(self.hour_total, self.min_total, self.sec_total)
        self.label_time_total.setText(total)

        font_button = QFont("monospace", 20)
        font_button.setBold(True)

        self.button_switch.setStyleSheet("background-color:#3C3C46; color:#D9D9D9; border-radius:8px; border-width:0px;"
                                         "border-color:#D9D9D9; border-style:solid;")
        self.button_switch.setFont(font_button)
        self.button_switch.setFixedHeight(40)
        self.button_switch.setFixedWidth(110)
        self.button_switch.clicked.connect(lambda: self.timer_start(self.is_started))

        self.layout_time_label.addWidget(self.label_time)
        self.layout_time_label.addWidget(self.label_time_total)

        self.layout_timer.addWidget(self.icon_timer)
        self.layout_timer.addWidget(self.button_switch)

        self.layout_main.addLayout(self.layout_timer)
        self.layout_main.addLayout(self.layout_time_label)

    def timer_start(self, is_started):
        if is_started:
            self.timer.stop()
            self.button_switch.setText("START")

            self.icon_timer.setIconSize(QSize(100, 100))
            self.icon_timer.setIcon(QIcon('./icon/stopwatch_stop.png'))
            self.icon_timer.clicked.connect(lambda: self.timer_start(self.is_started))

            self.is_started = False

        else:
            self.timer.start(1000)
            self.button_switch.setText("STOP")

            self.icon_timer.setIconSize(QSize(100, 100))
            self.icon_timer.setIcon(QIcon('./icon/stopwatch_start.png'))
            self.icon_timer.clicked.connect(lambda: self.timer_start(self.is_started))

            self.is_started = True

    def timer_reset(self):
        self.timer.stop()
        self.sec  = 0
        self.min  = 0
        self.hour = 0

        time = "{0:02d}:{1:02d}:{2:02d}".format(self.hour, self.min, self.sec)
        self.label_time.setText(time)

        self.button_switch.setText("START")
        self.is_started = False

    def time_count(self):
        if self.sec < 59:
            self.sec += 1

        else:
            if self.min < 59:
                self.sec = 0
                self.min += 1

            elif self.min == 59:
                self.hour += 1
                self.min = 0
                self.sec = 0

        if self.sec_total < 59:
            self.sec_total += 1

        else:
            if self.min_total < 59:
                self.sec_total = 0
                self.min_total += 1

            elif self.min_total == 59:
                self.hour_total += 1
                self.min_total = 0
                self.sec_total = 0

        time = "{0:02d}:{1:02d}:{2:02d}".format(self.hour, self.min, self.sec)
        self.label_time.setText(time)

        total = "Today's total time: {0:02d}:{1:02d}:{2:02d}  ".format(self.hour_total, self.min_total, self.sec_total)
        self.label_time_total.setText(total)
