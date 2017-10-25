# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout,\
                            QAction, QLabel, QScrollArea
from PyQt5.QtCore import QCoreApplication, QSize, Qt
from PyQt5.QtGui import QIcon
from stopwatch import Stopwatch
from subject_button import SubjectButton


class Timenote(QMainWindow):

    def __init__(self):
        super().__init__()

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.buttons_subject = SubjectButton()

        self.layout_main = QHBoxLayout()
        self.layout_user = QVBoxLayout()
        self.layout_subject_history = QVBoxLayout()

        self.init_ui()

    def init_ui(self):
        self.main_widget.setStyleSheet("background-color:#32393D;")

        stopwatch = Stopwatch()

        for button in self.buttons_subject.buttons_subject:
            button.clicked.connect(stopwatch.timer_reset)

        self.layout_user.addLayout(self.buttons_subject.layout_now_subject)
        self.layout_user.addLayout(stopwatch.layout_main)
        self.layout_user.addLayout(self.buttons_subject.layout_grid)
        self.layout_user.addLayout(self.buttons_subject.layout_editing_name)

        scroll_area_subjects = QScrollArea()
        scroll_area_subjects.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_area_subjects.setWidgetResizable(True)
        scroll_area_subjects.setEnabled(True)
        scroll_contents = QWidget(scroll_area_subjects)
        scroll_contents.setLayout(self.layout_subject_history)
        scroll_area_subjects.setWidget(scroll_contents)

        button_history = QPushButton("Finished this work")
        button_history.clicked.connect(self.add_history)

        layout_history = QVBoxLayout()
        layout_history.addWidget(button_history)
        layout_history.addWidget(scroll_area_subjects)

        self.layout_main.addLayout(self.layout_user)
        self.layout_main.addLayout(layout_history)

        self.main_widget.setLayout(self.layout_main)

        exit_action = QAction(QIcon('./icon/exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit Application')
        exit_action.triggered.connect(QCoreApplication.instance().quit)

        toolbar = self.addToolBar('&Toolbar')
        toolbar.addAction(exit_action)

        self.setGeometry(500, 500, 640, 360)
        self.setWindowTitle('stop watch')
        self.show()

    def add_history(self):
        text_finished_subject = self.buttons_subject.label_now_subject.text()
        label_history = QLabel()
        label_history.setText(text_finished_subject)

        icon_history = QPushButton()
        index = self.buttons_subject.index_now_subject
        icon_history.setIcon(QIcon(self.buttons_subject.path_icons[index]))
        icon_history.setIconSize(QSize(50, 50))
        icon_history.clicked.connect(lambda: self.buttons_subject.change_subject_name(text_finished_subject))

        layout_history = QHBoxLayout()
        layout_history.addWidget(icon_history)
        layout_history.addWidget(label_history)

        widget_history = QWidget()
        widget_history.setLayout(layout_history)

        self.layout_subject_history.addWidget(widget_history)


def main():
    app = QApplication(sys.argv)
    window = Timenote()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
