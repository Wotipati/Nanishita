# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout,\
                            QLCDNumber, QAction, QLabel, QLineEdit, QTextEdit
from PyQt5.QtCore import QCoreApplication, QTimer
from PyQt5.QtGui import QIcon
from stopwatch import Stopwatch
from subject_button import SubjectButton


class Timenote(QMainWindow):

    def __init__(self):
        super().__init__()

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.layout_main = QHBoxLayout()
        self.layout_user = QVBoxLayout()

        self.init_ui()

    def init_ui(self):
        buttons_subject = SubjectButton()
        self.layout_user.addLayout(buttons_subject.layout_now_subject)

        stopwatch = Stopwatch()
        self.layout_user.addLayout(stopwatch.layout_main)
        self.main_widget.setLayout(self.layout_user)

        self.layout_user.addLayout(buttons_subject.layout_grid)

        for button in buttons_subject.buttons_subject:
            button.clicked.connect(stopwatch.timer_reset)

        exit_action = QAction(QIcon('./icon/exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit Application')
        exit_action.triggered.connect(QCoreApplication.instance().quit)

        toolbar = self.addToolBar('&Toolbar')
        toolbar.addAction(exit_action)

        self.setGeometry(500, 500, 640, 360)
        self.setWindowTitle('stop watch')
        self.show()


def main():
    app = QApplication(sys.argv)
    window = Timenote()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()