# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import QSize, Qt


class SubjectButton(QWidget):

    def __init__(self):
        super().__init__()

        self.labels_subject = ['Meeting', 'Implementation', 'Research',
                               'Experiment', 'Survey', 'Writing a paper',
                               'Making slides', 'Taking a class', 'Chores']

        self.path_icons = ['./icon/subject/meeting.png',
                           './icon/subject/implementation.png',
                           './icon/subject/research.png',
                           './icon/subject/experiment.png',
                           './icon/subject/survey.png',
                           './icon/subject/paper.png',
                           './icon/subject/slide.png',
                           './icon/subject/class.png',
                           './icon/subject/chores.png']

        self.label_now_subject = QLabel('<h1></h1>', self)
        self.icon_now_subject = QPushButton()
        self.layout_now_subject = QHBoxLayout()
        self.layout_grid = QGridLayout()
        self.buttons_subject = []
        self.init_ui()

    def init_ui(self):
        self.icon_now_subject.setFixedHeight(100)
        self.icon_now_subject.setFixedWidth(100)
        self.icon_now_subject.setStyleSheet(
            "background-color:#3C3C46; color:#D9D9D9; border-radius:8px; border-width:0px; border-color:#D9D9D9;"
            "border-style: solid;")
        self.label_now_subject.setStyleSheet(
            "color:#D9D9D9; border-radius:8px; border-width:0px; border-color:#D9D9D9; border-style:solid;")

        positions_subject = [(i, j) for i in range(3) for j in range(3)]

        for position, subject in zip(positions_subject, self.labels_subject):
            button = QPushButton(subject)
            font_button = QFont("monospace", 13)
            button.setFont(font_button)
            button.setFixedHeight(55)
            button.setFixedWidth(160)
            button.setIconSize(QSize(50, 50))
            button.setIcon(QIcon(self.path_icons[position[0]*3+position[1]]))
            button.setStyleSheet(
                "background-color:#3C3C46; color:#D9D9D9; border-radius:8px; border-width:0px; border-color:#D9D9D9;"
                "border-style:solid;")
            self.buttons_subject.append(button)
            self.layout_grid.addWidget(button, *position)

        self.buttons_subject[0].clicked.connect(lambda: self.display_now_subject(0))
        self.buttons_subject[1].clicked.connect(lambda: self.display_now_subject(1))
        self.buttons_subject[2].clicked.connect(lambda: self.display_now_subject(2))
        self.buttons_subject[3].clicked.connect(lambda: self.display_now_subject(3))
        self.buttons_subject[4].clicked.connect(lambda: self.display_now_subject(4))
        self.buttons_subject[5].clicked.connect(lambda: self.display_now_subject(5))
        self.buttons_subject[6].clicked.connect(lambda: self.display_now_subject(6))
        self.buttons_subject[7].clicked.connect(lambda: self.display_now_subject(7))
        self.buttons_subject[8].clicked.connect(lambda: self.display_now_subject(8))

        self.layout_now_subject.addWidget(self.icon_now_subject)
        self.layout_now_subject.addWidget(self.label_now_subject)

    def display_now_subject(self, index):
        self.icon_now_subject.setIconSize(QSize(80, 80))
        self.icon_now_subject.setIcon(QIcon(self.path_icons[index]))
        self.label_now_subject.setText('<font size="20" face="monospace"><b>{0}</b></font>'.format((self.buttons_subject[index].text())))
