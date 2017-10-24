# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout,\
                            QLCDNumber, QAction, QLabel, QLineEdit, QTextEdit
from PyQt5.QtCore import QCoreApplication, QTimer
from PyQt5.QtGui import QIcon
from stopwatch import Stopwatch
from subject import Subject


class Timenote(QMainWindow):

    def __init__(self):
        super().__init__()

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.labels_subject = ['Meeting', 'Implementation', 'Experiment',
                               'Research', 'Paper survey', 'Writing a paper',
                               'Making slides', 'Taking a class', 'Chores']

        self.label_now_subject = QLabel()
        self.layout_main = QHBoxLayout()
        self.layout_user = QVBoxLayout()
        self.layout_grid = QGridLayout()
        self.buttons_subject = []
        self.init_ui()

    def init_ui(self):
        self.layout_user.addWidget(self.label_now_subject)

        stopwatch = Stopwatch()
        self.layout_user.addLayout(stopwatch.layout_main)
        self.main_widget.setLayout(self.layout_user)

        positions_subject = [(i, j) for i in range(3) for j in range(3)]

        for position, subject in zip(positions_subject, self.labels_subject):
            button = QPushButton(subject)
            #button.clicked.connect(lambda: self.display_now_subject(button))
            self.buttons_subject.append(button)

            self.layout_grid.addWidget(button, *position)

        for i in range(9):
            self.buttons_subject[i].clicked.connect(lambda: self.display_now_subject(self.buttons_subject[i]))

        self.layout_user.addLayout(self.layout_grid)

        exit_action = QAction(QIcon('./icon/exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit Application')
        exit_action.triggered.connect(QCoreApplication.instance().quit)

        toolbar = self.addToolBar('&Toolbar')
        toolbar.addAction(exit_action)

        self.setGeometry(500, 500, 300, 200)
        self.setWindowTitle('stop watch')
        self.show()

    def display_now_subject(self, button):
        index = self.labels_subject.index(button.text())
        print(button.text())
        i = int(index / 3)
        j = index % 3
        self.label_now_subject.setText(self.labels_subject[index])


def main():
    app = QApplication(sys.argv)
    window = Timenote()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()