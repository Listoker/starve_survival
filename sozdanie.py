import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import pyqtSignal
import random


class Generachia(QWidget):
    color_data = pyqtSignal(list)

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

        self.o1 = QLabel('Название', self)
        self.o1.move(int(self.x / 6.5) - int(self.x / 128), int(self.y / 220))
        self.o1.resize(int(self.x / 9.6), int(self.y / 10.8))
        self.o1.setStyleSheet('QLabel {background-color: ' + self.cvet[0] + '; color: #C0C0C0;}')

        self.o2 = QLabel('Сложность', self)
        self.o2.move(int(self.x / 6.5) - int(self.x / 96), int(self.y / 5.2))
        self.o2.resize(int(self.x / 9.6), int(self.y / 10.8))
        self.o2.setStyleSheet('QLabel {background-color: ' + self.cvet[0] + '; color: #C0C0C0;}')

        self.o3 = QLabel('Размер мира', self)
        self.o3.move(int(self.x / 6.5) - int(self.x / 96), int(self.y / 2.65))
        self.o3.resize(int(self.x / 9.6), int(self.y / 10.8))
        self.o3.setStyleSheet('QLabel {background-color: ' + self.cvet[0] + '; color: #C0C0C0;}')



        self.okno1 = QPushButton('Начать игру', self)
        self.okno1.move(int(self.x / 192), int(self.y / 1.54))
        self.okno1.resize(int(self.x / 19.2) * 3, int(self.y / 10.8))
        self.okno1.clicked.connect(self.start)
        self.okno1.setStyleSheet('QPushButton {background-color: #A3C1DA}')



        self.okno11 = QPushButton('простая', self)
        self.okno11.move(int(self.x / 192), int(self.y / 3.48))
        self.okno11.resize(int(self.x / 19.2), int(self.y / 10.8))
        self.okno11.clicked.connect(self.hardkor)
        self.okno11.setStyleSheet('QPushButton {background-color: #A3C1DA}')

        self.okno12 = QPushButton('нормальная', self)
        self.okno12.move(int(self.x / 16.69), int(self.y / 3.48))
        self.okno12.resize(int(self.x / 19.2), int(self.y / 10.8))
        self.okno12.clicked.connect(self.hardkor)
        self.okno12.setStyleSheet('QPushButton {background-color: #A3C1DA}')

        self.okno13 = QPushButton('сложная', self)
        self.okno13.move(int(self.x / 8.72), int(self.y / 3.48))
        self.okno13.resize(int(self.x / 19.2), int(self.y / 10.8))
        self.okno13.clicked.connect(self.hardkor)
        self.okno13.setStyleSheet('QPushButton {background-color: #A3C1DA}')



        self.first_value = QLineEdit(self)
        self.first_value.move(10, int(self.y / 10.8))
        self.first_value.resize(1200, int(self.y / 10.8))
        self.first_value.setText('9999')
        self.first_value.setStyleSheet('QLineEdit {background-color: #A3C1DA}')



        self.okno211 = QPushButton('маленький', self)
        self.okno211.move(int(self.x / 192), int(self.y / 2.16))
        self.okno211.resize(int(self.x / 19.2), int(self.y / 10.8))
        self.okno211.clicked.connect(self.mir)
        self.okno211.setStyleSheet('QPushButton {background-color: #A3C1DA}')

        self.okno212 = QPushButton('обычный', self)
        self.okno212.move(int(self.x / 16.69), int(self.y / 2.16))
        self.okno212.resize(int(self.x / 19.2), int(self.y / 10.8))
        self.okno212.clicked.connect(self.mir)
        self.okno212.setStyleSheet('QPushButton {background-color: #A3C1DA}')

        self.okno213 = QPushButton('большой', self)
        self.okno213.move(int(self.x / 8.72), int(self.y / 2.16))
        self.okno213.resize(int(self.x / 19.2), int(self.y / 10.8))
        self.okno213.clicked.connect(self.mir)
        self.okno213.setStyleSheet('QPushButton {background-color: #A3C1DA}')

    def mir(self):
        pass

    def hardkor(self):
        pass

    def start(self):
        q = 700
        w = 100
        e = 30
        r = 10
        t = 2
        mir = 100
        spawn = 1

        wolk = 20
        lisa = 15
        zaiz = 20
        kust = 30
        if self.lvl[2] == 1:
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
        map = []
        for i in range(int(mir / 10)):
            map2 = []
            for i in range(int(mir / 10)):
                map2.append('0')
            map.append(map2)
        for i in range(int(q)):
            x = random.randrange(0, int(mir / 10) - 1)
            y = random.randrange(0, int(mir / 10) - 1)
            while map[x][y] != '0':
                if int(mir / 10) <= x:
                    y += 1
                    x = 0
                    if int(mir / 10) <= y:
                        y = 1
                x += 1
            map[x][y] = 'q'
        for i in range(int(w)):
            x = random.randrange(0, int(mir / 10) - 1)
            y = random.randrange(0, int(mir / 10) - 1)
            while map[x][y] != '0':
                if int(mir / 10) <= x:
                    y += 1
                    x = 0
                    if int(mir / 10) <= y:
                        y = 1
                x += 1
            map[x][y] = 'w'
        for i in range(int(e)):
            x = random.randrange(0, int(mir / 10) - 1)
            y = random.randrange(0, int(mir / 10) - 1)
            while map[x][y] != '0':
                if int(mir / 10) <= x:
                    y += 1
                    x = 0
                    if int(mir / 10) <= y:
                        y = 1
                x += 1
            map[x][y] = 'e'
        for i in range(int(r)):
            x = random.randrange(0, int(mir / 10) - 1)
            y = random.randrange(0, int(mir / 10) - 1)
            while map[x][y] != '0':
                if int(mir / 10) <= x:
                    y += 1
                    x = 0
                    if int(mir / 10) <= y:
                        y = 1
                x += 1
            map[x][y] = 'r'
        for i in range(int(t)):
            x = random.randrange(0, int(mir / 10) - 1)
            y = random.randrange(0, int(mir / 10) - 1)
            while map[x][y] != '0':
                if int(mir / 10) <= x:
                    y += 1
                    x = 0
                    if int(mir / 10) <= y:
                        y = 1
                x += 1
            map[x][y] = 't'
        x = random.randrange(0, int(mir / 10) - 1)
        y = random.randrange(0, int(mir / 10) - 1)
        while map[x][y] != '0':
            if int(mir / 10) <= x:
                y += 1
                x = 0
                if int(mir / 10) <= y:
                    y = 1
            x += 1
        map[x][y] = '@'
        print(33)
        for i in range(int(wolk)):
            x = random.randrange(0, int(mir / 10) - 1)
            y = random.randrange(0, int(mir / 10) - 1)
            while map[x][y] != '0':
                if int(mir / 10) <= x:
                    y += 1
                    x = 0
                    if int(mir / 10) <= y:
                        y = 1
                x += 1
            map[x][y] = 'wolf 150'
        for i in range(int(lisa)):
            x = random.randrange(0, int(mir / 10) - 1)
            y = random.randrange(0, int(mir / 10) - 1)
            while map[x][y] != '0':
                if int(mir / 10) <= x:
                    y += 1
                    x = 0
                    if int(mir / 10) <= y:
                        y = 1
                x += 1
            map[x][y] = 'lisa 75'
        for i in range(int(zaiz)):
            x = random.randrange(0, int(mir / 10) - 1)
            y = random.randrange(0, int(mir / 10) - 1)
            while map[x][y] != '0':
                if int(mir / 10) <= x:
                    y += 1
                    x = 0
                    if int(mir / 10) <= y:
                        y = 1
                x += 1
            map[x][y] = 'zaiz 25'
        for i in range(int(kust)):
            x = random.randrange(0, int(mir / 10) - 1)
            y = random.randrange(0, int(mir / 10) - 1)
            while map[x][y] != '0':
                if int(mir / 10) <= x:
                    y += 1
                    x = 0
                    if int(mir / 10) <= y:
                        y = 1
                x += 1
            map[x][y] = 'kust 6 900'
        print(999)
        for i in range(10):
            map2 = []
            for q in range(int(mir / 10)):
                map2.append('water')
            map.insert(0, map2)
        for i in range(10):
            map2 = []
            for q in range(int(mir / 10)):
                map2.append('water')
            map.append(map2)
        map2 = []
        for i in range(10):
            map2.append('water')
        maaaaap = ''
        for i in map:
            maaaaap += '\n' + '$'.join(map2) + '$' + '$'.join(i) + '$' + '$'.join(map2)
        with open('mir/' + self.lvl[0] + '.txt', 'w') as f:
            f.write(''.join(maaaaap))
        with open('inventar/' + self.lvl[0] + '.txt', 'w') as f:
            f.write('1 pusto 0$2 pusto 0$3 pusto 0$4 pusto 0$5 pusto 0$6 pusto 0$7 pusto 0$8 pusto 0$9 pusto 0$HP 100$food 100$cold 100')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Generachia()
    example.show()
    sys.exit(app.exec())