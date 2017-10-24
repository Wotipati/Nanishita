# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QHBoxLayout, QLabel
from PyQt5.QtGui import QPixmap, QFont, QIcon


class SubjectButton(QWidget):

    def __init__(self):
        super().__init__()

        self.labels_subject = ['Meeting', 'Implementation', 'Experiment',
                               'Research', 'Paper survey', 'Writing a paper',
                               'Making slides', 'Taking a class', 'Chores']

        self.label_now_subject = QLabel('<h1></h1>', self)
        self.icon_now_subject = QLabel('<h1></h1>', self)
        self.layout_now_subject = QHBoxLayout()
        self.layout_grid = QGridLayout()
        self.buttons_subject = []
        self.init_ui()

        self.path_icons = ['./icon/meeting.png',
                           './icon/implementation.png',
                           './icon/experiment.png',
                           './icon/research.png',
                           './icon/survey.png',
                           './icon/paper.png',
                           './icon/slide.png',
                           './icon/class.png',
                           './icon/chores.png']

    def init_ui(self):
        path_icons = ['./icon/meeting.png',
                      './icon/implementation.png',
                      './icon/experiment.png',
                      './icon/research.png',
                      './icon/survey.png',
                      './icon/paper.png',
                      './icon/slide.png',
                      './icon/class.png',
                      './icon/chores.png']

        positions_subject = [(i, j) for i in range(3) for j in range(3)]

        for position, subject in zip(positions_subject, self.labels_subject):
            button = QPushButton(subject)
            button.setIcon(QIcon(path_icons[position[0]*3+position[1]]))
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
        path_icons = ['./icon/meeting.png',
                      './icon/implementation.png',
                      './icon/experiment.png',
                      './icon/research.png',
                      './icon/survey.png',
                      './icon/paper.png',
                      './icon/slide.png',
                      './icon/class.png',
                      './icon/chores.png']

        pixmap = QPixmap(path_icons[index])
        print(path_icons[index])
        pixmap_resized = pixmap.scaled(50, 50)
        self.icon_now_subject.setPixmap(pixmap_resized)
        self.label_now_subject.setText('<h1>{0}</h1>'.format((self.buttons_subject[index].text())))
