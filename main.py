import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QMainWindow, QRadioButton, \
    QLineEdit, QLabel, QCheckBox, QListWidget
from PyQt5.QtCore import Qt


class AddAndEditMacroWindow(QWidget):

    def __init__(self, title_str):
        super().__init__()
        self.initWindow(title_str)


    def initWindow(self, title_str):
        self.setWindowTitle(title_str)
        self.resize(450, 400)

        self.h_box_layout_1 = QHBoxLayout()

        label1 = QLabel('F12키를 통해 현재 마우스 위치를 Macro 항목에 추가합니다. \n저장된 순서에 따라 Macro가 순차적으로 실행됩니다.', self)

        label1.setAlignment(Qt.AlignLeft)

        self.h_box_layout_1.addWidget(label1)

        # font1 = label1.font()
        # font1.setPointSize(12)
        # label1.setFont(font1)

        start_button = QPushButton('시작/중지 설정')
        mouse_button = QPushButton('마우스 추가')
        keyboard_button = QPushButton('키보드 추가')
        delay_button = QPushButton('지연 추가')

        self.h_box_layout_2 = QHBoxLayout()
        self.v_box_1_inside_layout_2 = QVBoxLayout()

        self.command_list = QListWidget()
        self.command_list.setWordWrap(True)

        self.command_list.setStyleSheet("QListWidget"
                                        "{"
                                        "border : 4px solid black;"
                                        "background : white;"
                                        "}")
        self.command_list.setGeometry(0, 0, 1000, 1000)
        self.command_list.insertItem(0, "매크로 1")

        self.v_box_1_inside_layout_2.addWidget(self.command_list)

        self.v_box_2_inside_layout_2 = QVBoxLayout()

        self.v_box_2_inside_layout_2.setSpacing(0)
        self.v_box_2_inside_layout_2.addWidget(start_button)
        self.v_box_2_inside_layout_2.addWidget(mouse_button)
        self.v_box_2_inside_layout_2.addWidget(keyboard_button)
        self.v_box_2_inside_layout_2.addWidget(delay_button)

        self.v_box_2_inside_layout_2.addStretch(0)
        self.v_box_2_inside_layout_2.setSpacing(10)
        self.v_box_2_inside_layout_2.setContentsMargins(0, 0, 0, 0)

        self.h_box_layout_2.addLayout(self.v_box_1_inside_layout_2, 3)
        self.h_box_layout_2.addLayout(self.v_box_2_inside_layout_2, 1)

        self.wrapper = QVBoxLayout()

        # 주석

        self.wrapper.addLayout(self.h_box_layout_1)
        self.wrapper.addLayout(self.h_box_layout_2, 5)

        self.setLayout(self.wrapper)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Armko Macro")
        self.resize(450, 350)

        # geo = self.geometry()

        add_button = QPushButton('Macro 추가')
        edit_button = QPushButton('Macro 편집')
        copy_button = QPushButton('Macro 복제')
        delect_button = QPushButton('Macro 삭제')

        add_button.clicked.connect(self.add_macro)

        edit_button.clicked.connect(self.edit_macro)

        self.macro_start_radio = QRadioButton("매크로 시작")
        self.macro_start_radio.setObjectName("macro_start_radio")

        self.macro_stop_radio = QRadioButton("매크로 중지")
        self.macro_stop_radio.setObjectName("macro_stop_radio")


        self.h_box_layout_1 = QHBoxLayout()
        self.h_box_layout_1.addWidget(self.macro_start_radio)
        self.h_box_layout_1.addWidget(self.macro_stop_radio)
        self.h_box_layout_1.addStretch(2)

        #박건우 멍청이

        self.h_box_layout_2 = QHBoxLayout()

        self.v_box_1_inside_layout_2 = QVBoxLayout()
        self.macro_list = QListWidget()
        #self.macro_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.macro_list.setWordWrap(True)

        self.macro_list.setStyleSheet("QListWidget"
                                      "{"
                                      "border : 4px solid black;"
                                      "background : white;"
                                      "}")

        self.macro_list.setGeometry(0, 0, 1000, 1000)

        self.macro_list.insertItem(0, "매크로 1")

        self.v_box_1_inside_layout_2.addWidget(self.macro_list)
        # asdf
        self.v_box_2_inside_layout_2 = QVBoxLayout()
        self.v_box_2_inside_layout_2.setSpacing(0)
        self.v_box_2_inside_layout_2.addWidget(add_button)
        self.v_box_2_inside_layout_2.addWidget(edit_button)
        self.v_box_2_inside_layout_2.addWidget(copy_button)
        self.v_box_2_inside_layout_2.addWidget(delect_button)

        self.v_box_2_inside_layout_2.addStretch(0)
        self.v_box_2_inside_layout_2.setSpacing(10)
        self.v_box_2_inside_layout_2.setContentsMargins(0, 0, 0, 0)

        self.h_box_layout_2.addLayout(self.v_box_1_inside_layout_2, 3)
        self.h_box_layout_2.addLayout(self.v_box_2_inside_layout_2, 1)

        self.h_box_layout_3 = QHBoxLayout()

        self.float_top = QCheckBox("최상단에 띄우기")
        self.float_top.setObjectName("float_top")

        self.h_box_layout_3.addWidget(self.float_top)

        self.wrapper = QVBoxLayout()
        self.wrapper.setAlignment(Qt.AlignTop)

        self.wrapper.addLayout(self.h_box_layout_1)

        self.temp_widget = QWidget()

        self.temp_widget.setLayout(self.h_box_layout_2)

        self.wrapper.addWidget(self.temp_widget, 10)
        #
        self.wrapper.addLayout(self.h_box_layout_3)

        self.macro_stop_radio.toggle()

        self.setLayout(self.wrapper)

        self.show()

    def add_macro(self):
        self.add_macro_window = AddAndEditMacroWindow("Add Macro")

        self.add_macro_window.show()

    def edit_macro(self):
        self.edit_macro_window = AddAndEditMacroWindow("Edit Macro")

        self.edit_macro_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())