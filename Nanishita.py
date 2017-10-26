# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QScrollArea
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QFont
from stopwatch import Stopwatch
from subject_button import SubjectButton


class Timenote(QMainWindow):

    def __init__(self):
        super().__init__()

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.buttons_subject = SubjectButton()
        self.stopwatch = Stopwatch()

        self.layout_main = QHBoxLayout()
        self.layout_user = QVBoxLayout()
        self.layout_subject_history = QVBoxLayout()

        self.init_ui()

    def init_ui(self):
        self.main_widget.setStyleSheet("background-color:#32393D;")

        for button in self.buttons_subject.buttons_subject:
            button.clicked.connect(self.stopwatch.timer_reset)

        self.layout_user.addLayout(self.buttons_subject.layout_now_subject)
        self.layout_user.addLayout(self.stopwatch.layout_main)
        self.layout_user.addLayout(self.buttons_subject.layout_grid)
        self.layout_user.addLayout(self.buttons_subject.layout_editing_name)

        self.layout_subject_history.setAlignment(Qt.AlignTop)
        self.layout_subject_history.setSpacing(2)

        scroll_area_subjects = QScrollArea()
        scroll_area_subjects.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area_subjects.setWidgetResizable(True)
        scroll_area_subjects.setEnabled(True)
        scroll_area_subjects.setStyleSheet("background-color:#3C3C46; border-radius:18px; border-width:0px;"
                                           "border-color:#586473; border-style:solid")
        scroll_contents = QWidget(scroll_area_subjects)
        scroll_contents.setLayout(self.layout_subject_history)
        scroll_area_subjects.setWidget(scroll_contents)

        font_button = QFont("monospace", 20)
        font_button.setBold(True)

        button_history = QPushButton("Today's history")
        button_history.setFont(font_button)
        button_history.setFixedHeight(40)
        button_history.setStyleSheet("background-color:#3C3C46; color:#D9D9D9; border-radius:16px; border-width:0px;"
                                     "border-color:#3A6A9A; border-style:solid;")

        self.buttons_subject.button_icon_now_subject.clicked.connect(self.add_history)
        self.buttons_subject.button_label_now_subject.clicked.connect(self.add_history)

        layout_history = QVBoxLayout()
        layout_history.addWidget(button_history)
        layout_history.addWidget(scroll_area_subjects)

        self.layout_main.addLayout(self.layout_user)
        self.layout_main.addLayout(layout_history)

        self.main_widget.setLayout(self.layout_main)

        self.setGeometry(50, 50, 870, 360)
        self.setWindowTitle('stop watch')
        self.show()

    def add_history(self):
        b = self.stopwatch.hour + self.stopwatch.min + self.stopwatch.sec
        if b != 0 and self.stopwatch.is_started is False:
            text_finished_subject = self.buttons_subject.button_label_now_subject.text()
            font_button = QFont("monospace", 20)
            font_button.setBold(True)
            button_label = QPushButton(text_finished_subject)
            button_label.setFont(font_button)
            button_label.setFixedHeight(30)
            button_label.setStyleSheet("background-color:#3C3C46; color:#D9D9D9; text-align:left; border-style:solid")
            button_label.clicked.connect(lambda: self.buttons_subject.display_now_subject(index))
            button_label.clicked.connect(lambda: self.buttons_subject.change_subject_name(text_finished_subject))

            button_icon = QPushButton()
            button_icon.setFixedHeight(60)
            button_icon.setFixedWidth(60)
            button_icon.setIconSize(QSize(38, 38))
            index = self.buttons_subject.index_now_subject
            button_icon.setIcon(QIcon(self.buttons_subject.path_icons[index]))
            button_icon.setStyleSheet("background-color:#32393D; color:#D9D9D9; border-radius: 30px; border-style:solid;"
                                      "border-width:2px; border-color:#586473;")
            button_icon.clicked.connect(lambda: self.buttons_subject.display_now_subject(index))
            button_icon.clicked.connect(lambda: self.buttons_subject.change_subject_name(text_finished_subject))

            elapsed_time = "{0:02d}:{1:02d}:{2:02d}".format(self.stopwatch.hour, self.stopwatch.min, self.stopwatch.sec)
            button_time = QPushButton(elapsed_time)
            font_button.setBold(False)
            button_time.setFont(font_button)
            button_time.setFixedHeight(30)
            button_time.setFixedWidth(200)
            button_time.setStyleSheet("background-color:#3C3C46; color:#D9D9D9; text-align:right; border-style:solid")

            layout_label_and_time = QVBoxLayout()
            layout_label_and_time.setSpacing(2)
            layout_label_and_time.setAlignment(Qt.AlignRight)
            layout_label_and_time.addWidget(button_label)
            layout_label_and_time.addWidget(button_time)

            layout_history = QHBoxLayout()
            layout_history.setAlignment(Qt.AlignLeft)
            layout_history.setSpacing(4)
            layout_history.addWidget(button_icon)
            layout_history.addLayout(layout_label_and_time)

            widget_history = QWidget()
            widget_history.setLayout(layout_history)

            self.layout_subject_history.addWidget(widget_history)


def main():
    app = QApplication(sys.argv)
    window = Timenote()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
