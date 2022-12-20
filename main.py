import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QMainWindow, QRadioButton, \
    QLineEdit, QLabel, QCheckBox, QListWidget, QTextEdit, QTextBrowser, QComboBox, QMessageBox, QDialogButtonBox
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
import keyboard, pyautogui, time

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

        #layout_1 = start & Stop layout
        self.h_box_layout_1 = QHBoxLayout()
        self.h_box_layout_1.addWidget(self.macro_start_radio)
        self.h_box_layout_1.addWidget(self.macro_stop_radio)
        self.h_box_layout_1.addStretch(2)

        #layout2 = label과 push버튼을 포함한 layout
        self.h_box_layout_2 = QHBoxLayout()
        #layout2에 vbox1을 생성하여 label 생성
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

        #layout2에 vbox2를 생성하여 push버튼 삽입
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

        # layout3 = 체크박스를 포함한 layout
        self.h_box_layout_3 = QHBoxLayout()
        self.float_top = QCheckBox("최상단에 띄우기")
        self.float_top.setObjectName("float_top")
        self.h_box_layout_3.addWidget(self.float_top)

        #wrapper를 통해 모든 layout을 넣어 실행
        self.wrapper = QVBoxLayout()
        self.wrapper.setAlignment(Qt.AlignTop)
        self.wrapper.addLayout(self.h_box_layout_1)
        self.temp_widget = QWidget()
        self.temp_widget.setLayout(self.h_box_layout_2)
        self.wrapper.addWidget(self.temp_widget, 10)
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

    def closeEvent(self, event):
        reply = QMessageBox.information(self, 'Warning', '종료하겠습니까?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class AddAndEditMacroWindow(QWidget):
#Myapp(Qwidget)의 상속 class 시작
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

        self.h_box_layout_2 = QHBoxLayout()

        self.v_box_1_inside_layout_2 = QVBoxLayout()
        label1 = QLabel('매크로 이름:')
        label1.setAlignment(Qt.AlignLeft)
        self.v_box_1_inside_layout_2.addWidget(label1)
        self.h_box_layout_2.addLayout(self.v_box_1_inside_layout_2)
        # 예외 수정(2022.12.12)
        # 이전 코드
        # self.h_box_layout_2.addLayout(self.v_box_1_inside_layout_2)
        # addWidget 으로 layout 추가하려는 이상한 시도 수정

        self.v_box_2_inside_layout_2 = QVBoxLayout()
        name1 = QLineEdit()
        self.textedit1 = QLineEdit(self)
        self.textedit1.setText("이름을 입력하세요.")
        self.v_box_2_inside_layout_2.addWidget(self.textedit1)
        self.h_box_layout_2.addLayout(self.v_box_2_inside_layout_2)
        #2022.12.12
        #Textedit을 통한 Macro 이름 설정
        #참고 문헌 https://newbie-developer.tistory.com/149

        start_button = QPushButton('시작/중지 설정')
        mouse_button = QPushButton('마우스 추가')
        keyboard_button = QPushButton('키보드 추가')
        delay_button = QPushButton('지연 추가')
        delect_button = QPushButton('삭제')
        save_button = QPushButton('저장')


        self.h_box_layout_3 = QHBoxLayout()
        self.v_box_3_inside_layout_3 = QVBoxLayout()

        self.command_list = QListWidget()
        self.command_list.setWordWrap(True)

        self.command_list.setStyleSheet("QListWidget"
                                        "{"
                                        "border : 4px solid black;"
                                        "background : white;"
                                        "}")
        self.command_list.setGeometry(0, 0, 1000, 1000)
        self.command_list.insertItem(0, "매크로 1")

        self.v_box_3_inside_layout_3.addWidget(self.command_list)

        self.v_box_4_inside_layout_3 = QVBoxLayout()

        self.v_box_4_inside_layout_3.setSpacing(0)
        self.v_box_4_inside_layout_3.addWidget(start_button)
        self.v_box_4_inside_layout_3.addWidget(mouse_button)
        self.v_box_4_inside_layout_3.addWidget(keyboard_button)
        self.v_box_4_inside_layout_3.addWidget(delay_button)
        self.v_box_4_inside_layout_3.addWidget(delect_button)
        self.v_box_4_inside_layout_3.addWidget(save_button)

        self.v_box_4_inside_layout_3.addStretch(0)
        self.v_box_4_inside_layout_3.setSpacing(10)
        self.v_box_4_inside_layout_3.setContentsMargins(0, 0, 0, 0)

        self.h_box_layout_3.addLayout(self.v_box_3_inside_layout_3, 3)
        self.h_box_layout_3.addLayout(self.v_box_4_inside_layout_3, 1)

        self.wrapper = QVBoxLayout()


        self.wrapper.addLayout(self.h_box_layout_1)
        self.wrapper.addLayout(self.h_box_layout_2)
        self.wrapper.addLayout(self.h_box_layout_3, 5)

        self.setLayout(self.wrapper)

        start_button.clicked.connect(self.start_macro)
        mouse_button.clicked.connect(self.mouse_macro)


    def start_macro(self):
        self.start_macro_window = StartSetting("시작/중지 설정")

        self.start_macro_window.show()

    def mouse_macro(self):
        self.mouse_macro_window = MouseSetting("Mouse 좌표 설정")

        self.mouse_macro_window.show()


class StartSetting(QWidget):    ###시작/중지 설정###

    def __init__(self, title_str1):
        super().__init__()
        self.initWindow(title_str1)


    def initWindow(self, title_str1):
        self.setWindowTitle(title_str1)
        self.resize(350, 150)

        self.h_box_layout_1 = QHBoxLayout() #label Hbox 1
        label1 = QLabel('Macro 시작 버튼을 설정하세요. \n반복 횟수가 0일 경우 무한 루프.', self)
        label1.setAlignment(Qt.AlignLeft)
        self.h_box_layout_1.addWidget(label1)


        self.h_box_layout_2 = QHBoxLayout() #시작버튼 Hbox2
        self.v_box_1_inside_layout_2 = QVBoxLayout()
        self.v_box_1_inside_layout_2.setAlignment(Qt.AlignVCenter)
        label1 = QLabel('시작 버튼: ')
        label1.setAlignment(Qt.AlignLeft)

        self.v_box_1_inside_layout_2.addWidget(label1)
        # self.h_box_layout_2.addLayout(self.v_box_1_inside_layout_2)

        # 22.12.17 노영준: ******** 클래스 생성자 메서드를 실행하여 인스턴스 객체를 만드시는 겁니다. 클래스 이름을 띡하고 놓는 것이 아니라. ********
        # QVBoxLayout() 메서드가 사용 가능한 QVBoxLayout 객체를 반환합니다.
        # 그냥 QVBoxLayout 만 사용 하시면 안 됩니다.
        self.v_box_2_inside_layout_2 = QVBoxLayout()
        combo1 = QComboBox(self)
        combo1_list = ['F1', 'F2', 'F3', 'F4', 'F5']
        combo1.addItems(combo1_list)
        self.v_box_2_inside_layout_2.addWidget(combo1)


        self.h_box_layout_2.addLayout(self.v_box_1_inside_layout_2, 1)
        self.h_box_layout_2.addLayout(self.v_box_2_inside_layout_2, 1)
        self.h_box_layout_2.addStretch(3)

        self.h_box_layout_3 = QHBoxLayout() #종료버튼 Hbox3

        self.v_box_1_inside_layout_3 = QVBoxLayout()
        label1 = QLabel('종료 버튼: ')
        label1.setAlignment(Qt.AlignLeft)
        self.v_box_1_inside_layout_3.setAlignment(Qt.AlignVCenter)
        self.v_box_1_inside_layout_3.addWidget(label1)

        self.v_box_2_inside_layout_3 = QVBoxLayout()
        combo1 = QComboBox(self)
        combo1_list = ['F6', 'F7', 'F8', 'F9', 'F0']
        combo1.addItems(combo1_list)
        self.v_box_2_inside_layout_3.addWidget(combo1)

        self.h_box_layout_3.addLayout(self.v_box_1_inside_layout_3, 1)
        self.h_box_layout_3.addLayout(self.v_box_2_inside_layout_3, 1)
        self.h_box_layout_3.addStretch(3)

        self.h_box_layout_4 = QHBoxLayout()  # 반복횟수 Hbox4
        self.v_box_1_inside_layout_4 = QVBoxLayout()
        label1 = QLabel('반복 횟수:')
        label1.setAlignment(Qt.AlignLeft)
        self.v_box_1_inside_layout_4.setAlignment(Qt.AlignVCenter)
        self.v_box_1_inside_layout_4.addWidget(label1)

        self.h_box_layout_4.addLayout(self.v_box_1_inside_layout_4, 1)
        # 예외 수정(2022.12.12)
        # 이전 코드
        # self.h_box_layout_2.addLayout(self.v_box_1_inside_layout_2)
        # addWidget 으로 layout 추가하려는 이상한 시도 수정

        self.v_box_2_inside_layout_4 = QVBoxLayout()
        name1 = QLineEdit()
        self.textedit1 = QLineEdit(self)
        self.textedit1.setText("  ")
        self.textedit1.setFixedSize(40, 20)
        self.v_box_2_inside_layout_4.addWidget(self.textedit1)
        self.h_box_layout_4.addLayout(self.v_box_2_inside_layout_4, 1)
        self.h_box_layout_4.addStretch(3)

        self.h_box_layout_5 = QHBoxLayout()
        Save_button = QPushButton('Save')
        Cancel_button = QPushButton('Cancel')
        self.v_box_1_inside_layout_5 = QVBoxLayout()
        self.v_box_1_inside_layout_5.addWidget(Save_button)
        self.v_box_2_inside_layout_5 = QVBoxLayout()
        self.v_box_2_inside_layout_5.addWidget(Cancel_button)
        self.h_box_layout_5.addLayout(self.v_box_1_inside_layout_5, 1)
        self.h_box_layout_5.addLayout(self.v_box_2_inside_layout_5, 1)
        self.h_box_layout_5.addStretch(3)

        self.wrapper = QVBoxLayout()
        self.wrapper.addLayout(self.h_box_layout_1, 1)
        self.wrapper.setAlignment(Qt.AlignTop)
        self.wrapper.addLayout(self.h_box_layout_2, 1)
        self.wrapper.addLayout(self.h_box_layout_3, 2)
        self.wrapper.addLayout(self.h_box_layout_4, 1)
        self.wrapper.addLayout(self.h_box_layout_5, 1)
        self.setLayout(self.wrapper)


class MouseSetting(QWidget):    ###시작/중지 설정###

    def __init__(self, title_str2):
        super().__init__()
        self.initWindow(title_str2)

    def initWindow(self, title_str2):
        self.setWindowTitle(title_str2)
        self.resize(250, 150)

        self.h_box_layout_1 = QHBoxLayout() #label Hbox 1
        label1 = QLabel('Mouse 좌표를 설정하세요. \nF10을 통해 현재 좌표 저장.', self)
        label1.setAlignment(Qt.AlignLeft)
        self.h_box_layout_1.addWidget(label1)

        self.h_box_layout_2 = QHBoxLayout() #시작버튼 Hbox2
        self.v_box_1_inside_layout_2 = QVBoxLayout()
        self.v_box_1_inside_layout_2.setAlignment(Qt.AlignVCenter)
        label1 = QLabel('Mouse 좌표: ')
        label1.setAlignment(Qt.AlignLeft)
        self.v_box_1_inside_layout_2.addWidget(label1)
        self.h_box_layout_2.addLayout(self.v_box_1_inside_layout_2, 1)


        self.v_box_2_inside_layout_2 = QVBoxLayout()


        self.wrapper = QVBoxLayout()
        self.wrapper.addLayout(self.h_box_layout_1, 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())