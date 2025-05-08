import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QScrollArea, QFormLayout
from PyQt5.QtCore import pyqtSignal
import random
from PyQt5 import QtWidgets


class Generachia(QWidget):
    color_data = pyqtSignal()

    def __init__(self, lvl):
        super(Generachia, self).__init__()
        self.lvl = lvl
        self.cvet = ['black']
        self.qcvet = 'A3C1DA'
        self.x = 1920
        self.y = 1080
        self.cvet_nadpisi = '000000'
        self.x = 1280
        self.y = 720
        self.setupUI()

    def setupUI(self):
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowTitle('Создание мира')
        self.setStyleSheet(f"background-color: {self.cvet[0]};")

        # добавление кнопок и текста в интерфейс

        self.o1 = QLabel('Название', self)
        self.o1.move(600, int(self.y / 220))
        self.o1.resize(int(self.x / 9.6), int(self.y / 10.8))
        self.o1.setStyleSheet('QLabel {background-color: ' + self.cvet[0] + '; color: #C0C0C0;}')

        self.o2 = QLabel('Сложность', self)
        self.o2.move(595, int(self.y / 5.2))
        self.o2.resize(int(self.x / 9.6), int(self.y / 10.8))
        self.o2.setStyleSheet('QLabel {background-color: ' + self.cvet[0] + '; color: #C0C0C0;}')

        self.o3 = QLabel('Размер мира', self)
        self.o3.move(590, int(self.y / 2.65))
        self.o3.resize(int(self.x / 9.6), int(self.y / 10.8))
        self.o3.setStyleSheet('QLabel {background-color: ' + self.cvet[0] + '; color: #C0C0C0;}')

        self.okno1 = QPushButton('Начать игру', self)
        self.okno1.move(660, int(self.y / 1.54))
        self.okno1.resize(570, int(self.y / 10.8))
        self.okno1.clicked.connect(self.start)
        self.okno1.setStyleSheet('QPushButton {background-color: #A3C1DA}')

        self.okno1 = QPushButton('Отмена', self)
        self.okno1.move(50, int(self.y / 1.54))
        self.okno1.resize(570, int(self.y / 10.8))
        self.okno1.clicked.connect(self.otmena)
        self.okno1.setStyleSheet('QPushButton {background-color: #A3C1DA}')

        self.okno11 = QPushButton('простая', self)
        self.okno11.move(50, int(self.y / 3.48))
        self.okno11.resize(380, int(self.y / 10.8))
        self.okno11.clicked.connect(self.hardkor)
        self.okno11.setStyleSheet('QPushButton {background-color: #A3C1DA}')

        self.okno12 = QPushButton('нормальная', self)
        self.okno12.move(455, int(self.y / 3.48))
        self.okno12.resize(375, int(self.y / 10.8))
        self.okno12.clicked.connect(self.hardkor)
        self.okno12.setStyleSheet('QPushButton {background-color: #A3C1DA}')

        self.okno13 = QPushButton('сложная', self)
        self.okno13.move(855, int(self.y / 3.48))
        self.okno13.resize(375, int(self.y / 10.8))
        self.okno13.clicked.connect(self.hardkor)
        self.okno13.setStyleSheet('QPushButton {background-color: #A3C1DA}')

        self.first_value = QLineEdit(self)
        self.first_value.move(50, int(self.y / 10.8))
        self.first_value.resize(1180, int(self.y / 10.8))
        self.first_value.setText('Новый мир')
        self.first_value.setStyleSheet('QLineEdit {background-color: #A3C1DA}')

        self.okno211 = QPushButton('маленький', self)
        self.okno211.move(50, int(self.y / 2.16))
        self.okno211.resize(380, int(self.y / 10.8))
        self.okno211.clicked.connect(self.mir)
        self.okno211.setStyleSheet('QPushButton {background-color: #A3C1DA}')

        self.okno212 = QPushButton('обычный', self)
        self.okno212.move(455, int(self.y / 2.16))
        self.okno212.resize(375, int(self.y / 10.8))
        self.okno212.clicked.connect(self.mir)
        self.okno212.setStyleSheet('QPushButton {background-color: #A3C1DA}')

        self.okno213 = QPushButton('большой', self)
        self.okno213.move(855, int(self.y / 2.16))
        self.okno213.resize(375, int(self.y / 10.8))
        self.okno213.clicked.connect(self.mir)
        self.okno213.setStyleSheet('QPushButton {background-color: #A3C1DA}')

    def otmena(self):
        Generachia.close(self)

    def mir(self):
        button = QApplication.instance().sender()
        if button.text() == 'маленький':
            self.lvl[2] = 1
        if button.text() == 'обычный':
            self.lvl[2] = 2
        if button.text() == 'большой':
            self.lvl[2] = 3

    def hardkor(self):
        button = QApplication.instance().sender()
        # изменение сложности
        if button.text() == 'простая':
            self.lvl[1] = 1
        if button.text() == 'нормальная':
            self.lvl[1] = 2
        if button.text() == 'сложная':
            self.lvl[1] = 3

    def mir_sozdan(self, mir, q, spawn):
        for i in range(int(q)):
            x = random.randrange(0, int(mir / 10) - 1)
            y = random.randrange(0, int(mir / 10) - 1)

            while self.map_[x][y] != 'nothing@#plain@#grass@#pusto':
                if int(mir / 10) - 1 <= x:
                    y += 1
                    x = 0
                    if int(mir / 10) - 1 <= y:
                        y = 1
                x += 1
            self.map_[x][y] = spawn

    def start(self):
        # начало создания мира
        # стандартное количество обьектов
        q = 700
        w = 100
        e = 30
        r = 10
        t = 2
        mir = 1000

        wolk = 20
        lisa = 15
        zaiz = 20
        kust = 30
        if self.lvl[2] == 1:
            # изменение количества обьектов под размер мира
            mir = 500
            q *= 0.5
            w *= 0.5
            e *= 0.5
            r *= 0.5
            t *= 0.5
        elif self.lvl[2] == 2:
            mir = 1000
        elif self.lvl[2] == 3:
            mir = 2000
            q *= 6
            w *= 6
            e *= 6
            r *= 6
            t *= 6
        self.map_ = []
        for i in range(int(mir / 10)):
            map2 = []
            for i in range(int(mir / 10)):
                map2.append('nothing@#plain@#grass@#pusto')
            self.map_.append(map2)
        # добавление обьектов в мир
        self.mir_sozdan(mir, q, 'q_wood@#plain@#grass@#pusto')
        self.mir_sozdan(mir, w, 'w_stone@#plain@#grass@#pusto')
        self.mir_sozdan(mir, e, 'e_gold@#plain@#grass@#pusto')
        self.mir_sozdan(mir, r, 'r_diamond@#plain@#grass@#pusto')
        self.mir_sozdan(mir, t, 't_ametist@#plain@#grass@#pusto')
        x = random.randrange(0, int(mir / 10) - 1)
        y = random.randrange(0, int(mir / 10) - 1)
        while self.map_[x][y] != 'nothing@#plain@#grass@#pusto':
            if int(mir / 10) <= x:
                y += 1
                x = 0
                if int(mir / 10) <= y:
                    y = 1
            x += 1
        self.map_[x][y] = 'player@#plain@#grass@#pusto'
        # добавление животных в мир
        self.mir_sozdan(mir, wolk, 'wolf 150 @#plain@#grass@#pusto')
        self.mir_sozdan(mir, lisa, 'lisa 75 @#plain@#grass@#pusto')
        self.mir_sozdan(mir, zaiz, 'zaiz 25 @#plain@#grass@#pusto')
        self.mir_sozdan(mir, kust, 'kust 6 400 @#plain@#grass@#pusto')
        # добавление границ в мир
        for i in range(10):
            map2 = []
            for q in range(int(mir / 10)):
                map2.append('water@#ocean@#water@#pusto')
            self.map_.insert(0, map2)
        for i in range(10):
            map2 = []
            for q in range(int(mir / 10)):
                map2.append('water@#ocean@#water@#pusto')
            self.map_.append(map2)
        map2 = []
        for i in range(10):
            map2.append('water@#ocean@#water@#pusto')
        maaaaap = ''
        self.lvl[0] = self.first_value.text()
        # переделывание мира в текстовый формат
        for i in self.map_:
            maaaaap += '\n' + '%'.join(map2) + '%' + '%'.join(i) + '%' + '%'.join(map2)
        # создание файла мира
        with open('mir/' + self.lvl[0] + '.txt', 'w') as f:
            f.write(''.join(maaaaap))
        with open('inventar/' + self.lvl[0] + '.txt', 'w') as f:
            f.write('1 pusto 0%2 pusto 0%3 pusto 0%4 pusto 0%5 pusto 0%6 pusto 0%7 pusto 0%8 pusto 0%9 pusto 0%HP 100%food 100%cold 100')
        with open('nastroiki_mira/' + self.lvl[0] + '.txt', 'w') as f:
            self.lvl[1] = str(self.lvl[1])
            self.lvl[2] = str(self.lvl[2])
            self.lvl.append('0')
            self.lvl.append('0')
            self.lvl.append('0')
            f.write('%_%'.join(self.lvl))
        self.color_data.emit()


class Pomoch(QWidget):
    def __init__(self, lvl):
        super(Pomoch, self).__init__()
        self.lvl = lvl
        self.cvet = ['black']
        self.qcvet = 'A3C1DA'
        self.x = 1920
        self.y = 1080
        self.cvet_nadpisi = '000000'
        self.x = 1280
        self.y = 720
        self.setupUI()

    def setupUI(self):
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowTitle('Обучение')
        self.setStyleSheet(f"background-color: {self.cvet[0]};")

        self.o1 = QLabel('                                                                            Обучение\n'
                         '1 Управление: двигатся можно на клавиши wasd или стрелочки\n'
                         '2 чтобы добыть блок нужно нажимать на клавиши мыши, размещая курсор на игровом поле\n'
                         '3 чтобы взять в руки предмет, надо нажать на него в инвентаре\n'
                         '4 чтобы создать предмет, нужно нажать на него в левой верхней части экрана\n'
                         '5 чтобы постать блок, нужно нажать на него в инвентаре, а после нажать на клетку рядом с аватаром\n'
                         '6 чтобы ударить моба, нужно взять в руки мечь и нажать в направлении животного(надо находится поблизости)\n'
                         '7 чтобы выкинуть предмет, нужно нажать на правую клавишу мыши с наставленным курсором на предмет в инвентаре\n'
                         '8 чтобы пополнить индикатор холода, нужно находится рядом с костром\n'
                         '9 чтобы пополнить индикатор голода, нужно покушать\n'
                         '10 игру можно открыть на полный экран, нажав f11\n'
                         '11 если показатель хп упадет до 0, то вы погибните\n'
                         '12 если вы находитесь рядом с верстаком, то доступно больше крафтов\n'
                         '13 чтобы выйти из игры, нажмите esc\n', self)
        self.o1.move(10, 10)
        self.o1.resize(int(1200), int(400))
        self.o1.setStyleSheet('QLabel {background-color: ' + self.cvet[0] + '; color: #C0C0C0;}')


class VseMiri(QWidget):
    signal__ = pyqtSignal()

    def __init__(self, lvl):
        super(VseMiri, self).__init__()
        self.lvl = lvl
        self.cvet = ['black']
        self.qcvet = 'A3C1DA'
        self.x = 1920
        self.y = 1080
        self.cvet_nadpisi = '000000'
        self.x = 1280
        self.y = 720
        self.setupUI()

    def setupUI(self):
        self.setGeometry(0, 0, 1280, 720)
        self.setWindowTitle('Обучение')
        self.setStyleSheet(f"background-color: {self.cvet[0]};")

        self.o1 = QLabel('Ваши миры', self)
        self.o1.move(100, int(self.y / 220))
        self.o1.resize(int(self.x / 9.6), int(self.y / 10.8))
        self.o1.setStyleSheet('QLabel {background-color: ' + self.cvet[0] + '; color: #C0C0C0;}')

        doroga = '/'.join(os.getcwd().split('\\'))

        spisok_mirov = os.listdir(f'{doroga}/mir')

        mygroupbox = QtWidgets.QGroupBox('')
        forma = QFormLayout()
        labellist = []
        forma.addRow(self.o1)
        vihod = QPushButton("Выйти")
        vihod.setStyleSheet('QPushButton {background-color: #FFFFFF}')
        vihod.clicked.connect(self.zakritie)
        forma.addRow(vihod)
        for i in range(len(spisok_mirov)):
            labellist.append(QPushButton(spisok_mirov[i], self))
            labellist[i].setStyleSheet('QPushButton {background-color: #A3C1DA}')
            labellist[i].clicked.connect(self.mir)
            forma.addRow(labellist[i])

        mygroupbox.setLayout(forma)
        scroll = QScrollArea()
        scroll.setWidget(mygroupbox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(700)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(scroll)

    def zakritie(self):
        VseMiri.close(self)

    def mir(self):
        button = QApplication.instance().sender()
        with open('nastroiki_mira/' + button.text()) as f:
            f = f.read().split('%_%')
            self.lvl[0] = f[0]
            self.lvl[1] = f[1]
            self.lvl[2] = f[2]
        self.signal__.emit()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
