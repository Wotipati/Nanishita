# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QHBoxLayout, QLabel, QLineEdit
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

        self.button_label_now_subject = QPushButton("Good Morning!!!")
        self.button_icon_now_subject = QPushButton()
        self.index_now_subject = 0
        self.layout_now_subject = QHBoxLayout()
        self.layout_grid = QGridLayout()
        self.buttons_subject = []

        self.layout_editing_name = QHBoxLayout()
        self.textbox_editing_name = QLineEdit()
        self.button_editing_name = QPushButton("Rename", self)

        self.init_ui()

    def init_ui(self):
        self.button_icon_now_subject.setFixedHeight(90)
        self.button_icon_now_subject.setFixedWidth(90)
        self.button_icon_now_subject.setStyleSheet("background-color:#3C3C46; color:#D9D9D9; border-radius:45px;"
                                                   "border-width:3px; border-color:#586473; border-style:solid")

        self.button_icon_now_subject.setIconSize(QSize(66, 66))
        self.button_icon_now_subject.setIcon(QIcon("./icon/morning.png"))

        font_now_subject = QFont("monospace", 30)
        font_now_subject.setBold(True)
        self.button_label_now_subject.setFont(font_now_subject)
        self.button_label_now_subject.setStyleSheet("background-color:#32393D; color:#D9D9D9; border-radius:8px;"
                                                    "text-align:left; border-style:solid")

        positions_subject = [(i, j) for i in range(3) for j in range(3)]
        self.layout_grid.setSpacing(5)

        for position, subject in zip(positions_subject, self.labels_subject):
            button_label = QPushButton(subject)
            font_button = QFont("monospace", 14)
            button_label.setFont(font_button)
            button_label.setFixedHeight(60)
            button_label.setFixedWidth(108)
            button_label.setStyleSheet("background-color:#32393D; color:#D9D9D9; text-align:left; border-style:solid")

            button_icon = QPushButton()
            button_icon.setFixedHeight(60)
            button_icon.setFixedWidth(60)
            button_icon.setIconSize(QSize(38, 38))
            button_icon.setIcon(QIcon(self.path_icons[position[0]*3+position[1]]))
            button_icon.setStyleSheet("background-color:#3C3C46; color:#D9D9D9; border-radius: 30px;"
                                      "border-style:solid; border-width:2px; border-color:#586473;")

            self.buttons_subject.append(button_icon)
            self.buttons_subject.append(button_label)

            layout_buttons = QHBoxLayout()
            layout_buttons.setSpacing(2)
            layout_buttons.addWidget(button_icon)
            layout_buttons.addWidget(button_label)

            self.layout_grid.addLayout(layout_buttons, *position)

        self.buttons_subject[0].clicked.connect(lambda: self.display_now_subject(0))
        self.buttons_subject[1].clicked.connect(lambda: self.display_now_subject(0))
        self.buttons_subject[2].clicked.connect(lambda: self.display_now_subject(1))
        self.buttons_subject[3].clicked.connect(lambda: self.display_now_subject(1))
        self.buttons_subject[4].clicked.connect(lambda: self.display_now_subject(2))
        self.buttons_subject[5].clicked.connect(lambda: self.display_now_subject(2))
        self.buttons_subject[6].clicked.connect(lambda: self.display_now_subject(3))
        self.buttons_subject[7].clicked.connect(lambda: self.display_now_subject(3))
        self.buttons_subject[8].clicked.connect(lambda: self.display_now_subject(4))
        self.buttons_subject[9].clicked.connect(lambda: self.display_now_subject(4))
        self.buttons_subject[10].clicked.connect(lambda: self.display_now_subject(5))
        self.buttons_subject[11].clicked.connect(lambda: self.display_now_subject(5))
        self.buttons_subject[12].clicked.connect(lambda: self.display_now_subject(6))
        self.buttons_subject[13].clicked.connect(lambda: self.display_now_subject(6))
        self.buttons_subject[14].clicked.connect(lambda: self.display_now_subject(7))
        self.buttons_subject[15].clicked.connect(lambda: self.display_now_subject(7))
        self.buttons_subject[16].clicked.connect(lambda: self.display_now_subject(8))
        self.buttons_subject[17].clicked.connect(lambda: self.display_now_subject(8))

        self.button_editing_name.setStyleSheet("background-color:#3C3C46; color:#D9D9D9; border-radius:12px;"
                                               "border-width:0px; border-color:#3A6A9A; border-style:solid;")
        font_button = QFont("monospace", 17)
        font_button.setBold(True)
        self.button_editing_name.setFont(font_button)
        self.button_editing_name.setFixedHeight(30)
        self.button_editing_name.setFixedWidth(110)
        self.button_editing_name.clicked.connect(lambda: self.change_subject_name(self.textbox_editing_name.text()))

        self.textbox_editing_name.setFixedHeight(23)
        self.textbox_editing_name.setFont(font_button)
        self.textbox_editing_name.setStyleSheet("background-color:#3C3C46; color:#D9D9D9; border-radius:8px;"
                                                "border-width:0px; border-color:#D9D9D9; border-style:outset;")
        self.textbox_editing_name.returnPressed.connect(
            lambda: self.change_subject_name(self.textbox_editing_name.text()))

        self.layout_editing_name.addWidget(self.textbox_editing_name)
        self.layout_editing_name.addWidget(self.button_editing_name)

        self.layout_now_subject.addWidget(self.button_icon_now_subject)
        self.layout_now_subject.addWidget(self.button_label_now_subject)

    def display_now_subject(self, index):
        self.index_now_subject = index
        self.button_icon_now_subject.setIconSize(QSize(57, 57))
        self.button_icon_now_subject.setIcon(QIcon(self.path_icons[index]))
        self.button_label_now_subject.setText(self.labels_subject[index])

    def change_subject_name(self, new_subject_name):
        self.button_label_now_subject.setText(new_subject_name)
        self.textbox_editing_name.clear()
