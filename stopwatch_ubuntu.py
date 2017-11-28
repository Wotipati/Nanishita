# -*- coding: utf-8 -*-

import time
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import QTimer, QSize, Qt
from PyQt5.QtGui import QFont, QIcon


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
        self.start_time = 0
        self.elapsed_time = 0
        self.elapsed_time_total = 0

        self.button_icon_timer = QPushButton()
        self.label_time = QLabel()
        self.label_time_total = QLabel()
        self.is_started = False
        self.button_label_timer = QPushButton("Start", self)
        self.layout_main = QHBoxLayout()

        self.init_ui()

    def init_ui(self):
        font_time = QFont("ariel", 50)
        font_time.setBold(True)
        self.label_time.setFont(font_time)
        self.label_time.setAlignment(Qt.AlignCenter)
        self.label_time.setStyleSheet("background-color:#3C3C46; color:#F2EBBF; border-radius:12px; border-style:solid;")

        font_time_total = QFont("ariel", 14)
        font_time_total.setBold(True)
        self.label_time_total.setFont(font_time_total)
        self.label_time_total.setFixedHeight(40)
        self.label_time_total.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label_time_total.setStyleSheet("background-color:#3C3C46; color:#F2EBBF; border-radius:12px;"
                                            "border-style:solid;")

        self.button_icon_timer.setIconSize(QSize(100, 100))
        self.button_icon_timer.setIcon(QIcon('./icon/stopwatch_stop.png'))
        self.button_icon_timer.setStyleSheet("background-color:#3C3C46; color:#F2EBBF; border-radius:50px;"
                                             "border-style:solid;")
        self.button_icon_timer.clicked.connect(lambda: self.timer_start(self.is_started))
        self.button_label_timer.setFixedWidth(100)
        self.button_label_timer.setFixedWidth(100)

        time = "{0:02d}:{1:02d}:{2:02d}".format(self.hour, self.min, self.sec)
        self.label_time.setText(time)

        total = "Today's total time: {0:02d}:{1:02d}:{2:02d}  ".format(self.hour_total, self.min_total, self.sec_total)
        self.label_time_total.setText(total)

        font_button = QFont("monospace", 15)
        font_button.setBold(True)

        self.button_label_timer.setStyleSheet("background-color:#3C3C46; color:#D9D9D9; border-radius:16px;"
                                              "border-style:solid;")
        self.button_label_timer.setFont(font_button)
        self.button_label_timer.setFixedHeight(40)
        self.button_label_timer.setFixedWidth(110)
        self.button_label_timer.clicked.connect(lambda: self.timer_start(self.is_started))

        layout_time_label = QVBoxLayout()
        layout_time_label.setSpacing(3)
        layout_time_label.addWidget(self.label_time)
        layout_time_label.addWidget(self.label_time_total)

        layout_timer = QVBoxLayout()
        layout_timer.setSpacing(3)
        layout_timer.addWidget(self.button_icon_timer)
        layout_timer.addWidget(self.button_label_timer)

        self.layout_main.addLayout(layout_timer)
        self.layout_main.addLayout(layout_time_label)

    def timer_start(self, is_started):
        if is_started:
            self.timer.stop()
            self.button_label_timer.setText("Start")

            self.button_icon_timer.setIconSize(QSize(100, 100))
            self.button_icon_timer.setIcon(QIcon('./icon/stopwatch_stop.png'))

            self.elapsed_time += time.time() - self.start_time
            self.elapsed_time_total += time.time() - self.start_time

            self.is_started = False

        else:
            self.start_time = time.time()
            self.timer.start(1000)
            self.button_label_timer.setText("Stop")

            self.button_icon_timer.setIconSize(QSize(100, 100))
            self.button_icon_timer.setIcon(QIcon('./icon/stopwatch_start.png'))

            self.is_started = True

    def timer_reset(self):
        self.timer.stop()
        self.sec = 0
        self.min = 0
        self.hour = 0

        time = "{0:02d}:{1:02d}:{2:02d}".format(self.hour, self.min, self.sec)
        self.label_time.setText(time)

        self.button_label_timer.setText("Start")
        self.button_icon_timer.setIconSize(QSize(100, 100))
        self.button_icon_timer.setIcon(QIcon('./icon/stopwatch_stop.png'))

        self.elapsed_time = 0

        self.is_started = False

    def time_count(self):
        s = self.elapsed_time + time.time() - self.start_time
        s_total = self.elapsed_time_total + time.time() - self.start_time

        self.sec = int(s) % 60
        m = int(s / 60)
        self.min = m % 60
        self.hour = int(m / 60)

        self.sec_total = int(s_total) % 60
        m_total = int(s_total / 60)
        self.min_total = m_total % 60
        self.hour_total = int(m_total / 60)

        elapsed_time = "{0:02d}:{1:02d}:{2:02d}".format(self.hour, self.min, self.sec)
        self.label_time.setText(elapsed_time)

        total = "Today's total time: {0:02d}:{1:02d}:{2:02d}  ".format(self.hour_total, self.min_total, self.sec_total)
        self.label_time_total.setText(total)
