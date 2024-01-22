import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QLCDNumber
from PyQt5.QtWidgets import QFileDialog, QMainWindow
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from sozdanie import Generachia
from sozdanie import Pomoch
import pygame
import random
import os


class StarveSurvival(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.lvl = ['1234567', 2, 2]
        self.generachia = Generachia(self.lvl)
        self.pomoch = Pomoch(self.lvl)
        self.setupUI()
        self.generachia.color_data.connect(self.zakritie)

    def setupUI(self):
        self.setGeometry(300, 150, 1280, 720)
        self.setWindowTitle('Starve survival')

        self.greetine = QLabel(self)
        self.greetine.move(540, 100)
        self.greetine.setText("Starve survival")

        self.calculate_button = QPushButton('Начать новую игру', self)
        self.calculate_button.move(490, 200)
        self.calculate_button.resize(300, 70)
        self.calculate_button.clicked.connect(self.start_new)

        self.calculate_button = QPushButton('Продолжить с сохранения', self)
        self.calculate_button.move(490, 290)
        self.calculate_button.resize(300, 70)
        self.calculate_button.clicked.connect(self.start_old)

        self.calculate_button = QPushButton('Помощь', self)
        self.calculate_button.move(490, 380)
        self.calculate_button.resize(145, 70)
        self.calculate_button.clicked.connect(self.pomoch_)

        self.calculate_button = QPushButton('Выход из игры', self)
        self.calculate_button.move(645, 380)
        self.calculate_button.resize(145, 70)
        self.calculate_button.clicked.connect(self.vihod)

    def vihod(self):
        sys.exit()

    def pomoch_(self):
        self.pomoch.show()

    def start_new(self):
        self.generachia.show()

    def zakritie(self):
        self.generachia.close()
        self.file_name = '/'.join(os.path.abspath(f"mir/{self.lvl[0]}.txt").split('\\'))
        print(self.file_name)
        self.start()

    def start_old(self):
        self.file_name = QFileDialog.getOpenFileName(self, 'Выбор сохранения', '')[0]
        print(self.file_name)
        self.start()

    def start(self):

        def load_image(name, color_key=None):
            fullname = os.path.join('data', name)
            try:
                image = pygame.image.load(fullname).convert()
            except pygame.error as massage:
                print('Cannot load image:', name)
                raise SystemExit(massage)

            if color_key is not None:
                if color_key == -1:
                    color_key = image.get_at((0, 0))
                image.set_colorkey(color_key)
            else:
                image = image.convert_alpha()
            return image

        def load_level(filename):
            filename = "mir/" + filename
            # читаем уровень, убирая символы перевода строки
            with open(filename, 'r') as mapFile:
                level_map = [line.strip() for line in mapFile]
            # и подсчитываем максимальную длину
            level2 = level_map
            level_map = []
            for lev in level2:
                level_map.append(lev.split('%'))
            max_width = max(map(len, level_map))
            print(level_map)

            # дополняем каждую строку пустыми клетками ('.')
            return level_map

        def terminate():
            pygame.quit()
            sys.exit()

        def start_screen():
            intro_text = ["ЗАСТАВКА", "",
                          "Правила игры",
                          "Если в правилах несколько строк,",
                          "приходится выводить их построчно"]

            fon = pygame.transform.scale(load_image('fon.jpg'), (WIDTH, HEIGHT))
            screen.blit(fon, (0, 0))
            font = pygame.font.Font(None, 30)
            text_coord = 50
            for line in intro_text:
                string_rendered = font.render(line, 1, pygame.Color('black'))
                intro_rect = string_rendered.get_rect()
                text_coord += 10
                intro_rect.top = text_coord
                intro_rect.x = 10
                text_coord += intro_rect.height
                screen.blit(string_rendered, intro_rect)

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        terminate()
                    elif event.type == pygame.KEYDOWN or \
                            event.type == pygame.MOUSEBUTTONDOWN:
                        return  # начинаем игру
                pygame.display.flip()
                clock.tick(FPS)

        def generate_level(level):
            new_player, x, y = None, None, None
            for y in range(len(level)):
                for x in range(len(level[y])):
                    if level[y][x] == '.':
                        Tile('empty', x, y)
                    if level[y][x] == '0':
                        Tile('empty', x, y)
                    elif level[y][x] == '#':
                        Tile('wall', x, y)
                    elif level[y][x] == '@':
                        Tile('empty', x, y)
                        new_player = Player(x, y)
                    elif level[y][x] == 'q':
                        Tile('tree', x, y)
                    elif level[y][x] == 'w':
                        Tile('kamen', x, y)
                    elif level[y][x] == 'e':
                        Tile('gold', x, y)
                    elif level[y][x] == 'r':
                        Tile('diamond', x, y)
                    elif level[y][x] == 't':
                        Tile('ametists', x, y)
                    elif 's_d' in level[y][x]:
                        Tile('stena_derevo', x, y)
                    elif 'wolf' in level[y][x]:
                        Tile('wolf', x, y)
                    elif 'lisa' in level[y][x]:
                        Tile('lisa', x, y)
                    elif 'zaiz' in level[y][x]:
                        Tile('zaiz', x, y)
                    elif 'kust 1' in level[y][x]:
                        Tile('kust_1', x, y)
                    elif 'kust 2' in level[y][x]:
                        Tile('kust_2', x, y)
                    elif 'kust 3' in level[y][x]:
                        Tile('kust_3', x, y)
                    elif 'kust 4' in level[y][x]:
                        Tile('kust_4', x, y)
                    elif 'kust 5' in level[y][x]:
                        Tile('kust_5', x, y)
                    elif 'kust 6' in level[y][x]:
                        Tile('kust_6', x, y)
                    elif 'kust' in level[y][x]:
                        Tile('kust', x, y)
                    elif level[y][x] == 'verstak':
                        Tile('verstak', x, y)
                    elif 'koster' in level[y][x]:
                        Tile('koster', x, y)
                    elif 'water' in level[y][x]:
                        Tile('voda', x, y)
                    elif 'stena_kamen' in level[y][x]:
                        Tile('stena_kamen', x, y)
                    elif 'block_gold' in level[y][x]:
                        Tile('block_gold', x, y)
                    elif 'block_diamond' in level[y][x]:
                        Tile('block_diamond', x, y)
                    elif 'block_ametist' in level[y][x]:
                        Tile('block_ametist', x, y)
            # вернем игрока, а также размер поля в клетках
            return new_player, x, y

        def generate_level2(level):
            new_player, x, y = None, None, None
            for y in range(len(level)):
                for x in range(len(level[y])):
                    if level[y][x] == '.':
                        Tile('empty', x, y)
                    if level[y][x] == '0':
                        Tile('empty', x, y)
                    elif level[y][x] == '#':
                        Tile('wall', x, y)
                    elif level[y][x] == 'q':
                        Tile('tree', x, y)
                    elif level[y][x] == 'w':
                        Tile('kamen', x, y)
                    elif level[y][x] == 'e':
                        Tile('gold', x, y)
                    elif level[y][x] == 'r':
                        Tile('diamond', x, y)
                    elif level[y][x] == 't':
                        Tile('ametists', x, y)
            # вернем игрока, а также размер поля в клетках
            return x, y

        def inventar_skachivanie(name):
            name = name.split('/')
            name[-2] = 'inventar'
            filename = '/'.join(name)
            with open(filename, 'r') as mapFile:
                level2 = mapFile
                inventar_spisok = []
                for lev in level2:
                    inventar_spisok.extend(lev.split('%'))
                invent = []
                for inv in inventar_spisok:
                    invent.append(inv.split())
            return invent

        def inventar_spawn():
            for i in inventar:
                if 'pusto' in i:
                    pn = pygame.image.load('data/pusto.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                elif 'drevesina' in i:
                    pn = pygame.image.load('data/drevesina.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)

                    font = pygame.font.Font(None, 30)
                    text = font.render(str(i[-1]), 1, (100, 100, 100))
                    screen.blit(text, (380 + int(i[0]) * 50, 700))
                elif 'kamen_inv' in i:
                    pn = pygame.image.load('data/kamen_inv.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)

                    font = pygame.font.Font(None, 30)
                    text = font.render(str(i[-1]), 1, (100, 100, 100))
                    screen.blit(text, (380 + int(i[0]) * 50, 700))
                elif 'kirka_derevo' in i:
                    pn = pygame.image.load('data/kirka_derevo.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)

                    font = pygame.font.Font(None, 30)
                    text = font.render(str(i[-1]), 1, (100, 100, 100))
                    screen.blit(text, (380 + int(i[0]) * 50, 700))
                elif 'mech_derevo' in i:
                    pn = pygame.image.load('data/mech_derevo.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)

                    font = pygame.font.Font(None, 30)
                    text = font.render(str(i[-1]), 1, (100, 100, 100))
                    screen.blit(text, (380 + int(i[0]) * 50, 700))
                elif 'stena_derevo' in i:
                    pn = pygame.image.load('data/stena_derevo_craft.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)

                    font = pygame.font.Font(None, 30)
                    text = font.render(str(i[-1]), 1, (100, 100, 100))
                    screen.blit(text, (380 + int(i[0]) * 50, 700))
                elif 'verstak' in i:
                    pn = pygame.image.load('data/verstak_craft.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)

                    font = pygame.font.Font(None, 30)
                    text = font.render(str(i[-1]), 1, (100, 100, 100))
                    screen.blit(text, (380 + int(i[0]) * 50, 700))
                elif 'koster' in i:
                    pn = pygame.image.load('data/koster_craft.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)

                    font = pygame.font.Font(None, 30)
                    text = font.render(str(i[-1]), 1, (100, 100, 100))
                    screen.blit(text, (380 + int(i[0]) * 50, 700))
                elif 'gold_inv' in i:
                    pn = pygame.image.load('data/gold_inv.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)

                    font = pygame.font.Font(None, 30)
                    text = font.render(str(i[-1]), 1, (100, 100, 100))
                    screen.blit(text, (380 + int(i[0]) * 50, 700))
                elif 'diamond_inv' in i:
                    pn = pygame.image.load('data/diamond_inv.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)

                    font = pygame.font.Font(None, 30)
                    text = font.render(str(i[-1]), 1, (100, 100, 100))
                    screen.blit(text, (380 + int(i[0]) * 50, 700))
                elif 'ametist_inv' in i:
                    pn = pygame.image.load('data/ametist_inv.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)

                    font = pygame.font.Font(None, 30)
                    text = font.render(str(i[-1]), 1, (100, 100, 100))
                    screen.blit(text, (380 + int(i[0]) * 50, 700))
                elif 'kirka_kamen' in i:
                    pn = pygame.image.load('data/kirka_kamen.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)

                    font = pygame.font.Font(None, 30)
                    text = font.render(str(i[-1]), 1, (100, 100, 100))
                    screen.blit(text, (380 + int(i[0]) * 50, 700))
                elif 'kirka_gold' in i:
                    pn = pygame.image.load('data/kirka_gold.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)

                    font = pygame.font.Font(None, 30)
                    text = font.render(str(i[-1]), 1, (100, 100, 100))
                    screen.blit(text, (380 + int(i[0]) * 50, 700))
                elif 'kirka_diamond' in i:
                    pn = pygame.image.load('data/kirka_diamond.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)

                    font = pygame.font.Font(None, 30)
                    text = font.render(str(i[-1]), 1, (100, 100, 100))
                    screen.blit(text, (380 + int(i[0]) * 50, 700))
                elif 'kirka_ametist' in i:
                    pn = pygame.image.load('data/kirka_ametist.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)

                    font = pygame.font.Font(None, 30)
                    text = font.render(str(i[-1]), 1, (100, 100, 100))
                    screen.blit(text, (380 + int(i[0]) * 50, 700))
                elif 'agoda' in i:
                    pn = pygame.image.load('data/agoda.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)

                    font = pygame.font.Font(None, 30)
                    text = font.render(str(i[-1]), 1, (100, 100, 100))
                    screen.blit(text, (380 + int(i[0]) * 50, 700))
                elif 'maso_siroe' in i:
                    pn = pygame.image.load('data/maso_siroe.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)

                    font = pygame.font.Font(None, 30)
                    text = font.render(str(i[-1]), 1, (100, 100, 100))
                    screen.blit(text, (380 + int(i[0]) * 50, 700))
                elif 'maso_jarenoe' in i:
                    pn = pygame.image.load('data/maso_jarenoe.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)

                    font = pygame.font.Font(None, 30)
                    text = font.render(str(i[-1]), 1, (100, 100, 100))
                    screen.blit(text, (380 + int(i[0]) * 50, 700))
                elif 'stena_kamen' in i:
                    pn = pygame.image.load('data/stena_kamen_craft.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)

                    font = pygame.font.Font(None, 30)
                    text = font.render(str(i[-1]), 1, (100, 100, 100))
                    screen.blit(text, (380 + int(i[0]) * 50, 700))
                elif 'block_gold' in i:
                    pn = pygame.image.load('data/block_gold_craft.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)

                    font = pygame.font.Font(None, 30)
                    text = font.render(str(i[-1]), 1, (100, 100, 100))
                    screen.blit(text, (380 + int(i[0]) * 50, 700))
                elif 'block_diamond' in i:
                    pn = pygame.image.load('data/block_diamond_craft.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)

                    font = pygame.font.Font(None, 30)
                    text = font.render(str(i[-1]), 1, (100, 100, 100))
                    screen.blit(text, (380 + int(i[0]) * 50, 700))
                elif 'block_ametist' in i:
                    pn = pygame.image.load('data/block_ametist_craft.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)

                    font = pygame.font.Font(None, 30)
                    text = font.render(str(i[-1]), 1, (100, 100, 100))
                    screen.blit(text, (380 + int(i[0]) * 50, 700))
                elif 'mech_kamen' in i:
                    pn = pygame.image.load('data/mech_kamen.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)

                    font = pygame.font.Font(None, 30)
                    text = font.render(str(i[-1]), 1, (100, 100, 100))
                    screen.blit(text, (380 + int(i[0]) * 50, 700))
                elif 'mech_gold' in i:
                    pn = pygame.image.load('data/mech_gold.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)

                    font = pygame.font.Font(None, 30)
                    text = font.render(str(i[-1]), 1, (100, 100, 100))
                    screen.blit(text, (380 + int(i[0]) * 50, 700))
                elif 'mech_diamond' in i:
                    pn = pygame.image.load('data/mech_diamond.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)

                    font = pygame.font.Font(None, 30)
                    text = font.render(str(i[-1]), 1, (100, 100, 100))
                    screen.blit(text, (380 + int(i[0]) * 50, 700))
                elif 'mech_ametist' in i:
                    pn = pygame.image.load('data/mech_ametist.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)

                    font = pygame.font.Font(None, 30)
                    text = font.render(str(i[-1]), 1, (100, 100, 100))
                    screen.blit(text, (380 + int(i[0]) * 50, 700))

                elif 'HP' in i:
                    hp = int(i[1]) / 100
                    if hp > 1:
                        hp = 1
                    pygame.draw.rect(screen, (0, 0, 0), (415, 645, 150, 25))
                    pygame.draw.rect(screen, (255, 0, 0), (418, 648, int(144 * hp), 19))
                elif 'food' in i:
                    hp = int(i[1]) / 100
                    if hp > 1:
                        hp = 1
                    pygame.draw.rect(screen, (0, 0, 0), (565, 645, 150, 25))
                    # 72,6,7 - цвет болгарская роза
                    pygame.draw.rect(screen, (72, 6, 7), (568, 648, int(144 * hp), 19))
                elif 'cold' in i:
                    hp = int(i[1]) / 100
                    if hp > 1:
                        hp = 1
                    pygame.draw.rect(screen, (0, 0, 0), (715, 645, 150, 25))
                    # а 93 118 203 - Индиго Крайола
                    pygame.draw.rect(screen, (93, 118, 203), (718, 648, int(144 * hp), 19))

        def craft_spawn():
            q1 = 0
            w1 = 0
            e1 = 0
            r1 = 0
            t1 = 0
            maso_siroe = 0
            craft_chislo_x = 0
            craft_chislo_y = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'drevesina' in i:
                    q1 += int(i[2])
                elif 'kamen_inv' in i:
                    w1 += int(i[2])
                elif 'gold_inv' in i:
                    e1 += int(i[2])
                elif 'diamond_inv' in i:
                    r1 += int(i[2])
                elif 'ametist_inv' in i:
                    t1 += int(i[2])
                elif 'maso_siroe' in i:
                    maso_siroe += int(i[2])
            # проверка какие крафты создавать и их расположение
            if q1 >= 30:
                pn = pygame.image.load('data/kirka_derevo.png')
                ris_invent = pn.get_rect().move(craft_chislo_x * 50, craft_chislo_y * 50)
                screen.blit(pn, ris_invent)
                spisok_koord_craft.append([craft_chislo_x, craft_chislo_y, 50, 'kirka'])
                craft_chislo_x += 1
                if craft_chislo_x >= 5:
                    craft_chislo_x = 0
                    craft_chislo_y += 1
            if q1 >= 50:
                pn = pygame.image.load('data/mech_derevo.png')
                ris_invent = pn.get_rect().move(craft_chislo_x * 50, craft_chislo_y * 50)
                screen.blit(pn, ris_invent)
                spisok_koord_craft.append([craft_chislo_x, craft_chislo_y, 50, 'mech'])
                craft_chislo_x += 1
                if craft_chislo_x >= 5:
                    craft_chislo_x = 0
                    craft_chislo_y += 1
            if q1 >= 150:
                pn = pygame.image.load('data/stena_derevo_craft.png')
                ris_invent = pn.get_rect().move(craft_chislo_x * 50, craft_chislo_y * 50)
                screen.blit(pn, ris_invent)
                spisok_koord_craft.append([craft_chislo_x, craft_chislo_y, 50, 'stena_derevo'])
                craft_chislo_x += 1
                if craft_chislo_x >= 5:
                    craft_chislo_x = 0
                    craft_chislo_y += 1
            if q1 >= 100 and w1 > 30:
                pn = pygame.image.load('data/verstak_craft.png')
                ris_invent = pn.get_rect().move(craft_chislo_x * 50, craft_chislo_y * 50)
                screen.blit(pn, ris_invent)
                spisok_koord_craft.append([craft_chislo_x, craft_chislo_y, 50, 'verstak'])
                craft_chislo_x += 1
                if craft_chislo_x >= 5:
                    craft_chislo_x = 0
                    craft_chislo_y += 1
            if q1 >= 50 and w1 > 15:
                pn = pygame.image.load('data/koster_craft.png')
                ris_invent = pn.get_rect().move(craft_chislo_x * 50, craft_chislo_y * 50)
                screen.blit(pn, ris_invent)
                spisok_koord_craft.append([craft_chislo_x, craft_chislo_y, 50, 'koster'])
                craft_chislo_x += 1
                if craft_chislo_x >= 5:
                    craft_chislo_x = 0
                    craft_chislo_y += 1
            if q1 >= 60 and w1 > 20 and verstak_nalichie:
                pn = pygame.image.load('data/kirka_kamen.png')
                ris_invent = pn.get_rect().move(craft_chislo_x * 50, craft_chislo_y * 50)
                screen.blit(pn, ris_invent)
                spisok_koord_craft.append([craft_chislo_x, craft_chislo_y, 50, 'kirka_kamen'])
                craft_chislo_x += 1
                if craft_chislo_x >= 5:
                    craft_chislo_x = 0
                    craft_chislo_y += 1
            if q1 >= 90 and w1 > 50 and e1 > 20 and verstak_nalichie:
                pn = pygame.image.load('data/kirka_gold.png')
                ris_invent = pn.get_rect().move(craft_chislo_x * 50, craft_chislo_y * 50)
                screen.blit(pn, ris_invent)
                spisok_koord_craft.append([craft_chislo_x, craft_chislo_y, 50, 'kirka_gold'])
                craft_chislo_x += 1
                if craft_chislo_x >= 5:
                    craft_chislo_x = 0
                    craft_chislo_y += 1
            if w1 >= 90 and e1 > 50 and r1 > 15 and verstak_nalichie:
                pn = pygame.image.load('data/kirka_diamond.png')
                ris_invent = pn.get_rect().move(craft_chislo_x * 50, craft_chislo_y * 50)
                screen.blit(pn, ris_invent)
                spisok_koord_craft.append([craft_chislo_x, craft_chislo_y, 50, 'kirka_diamond'])
                craft_chislo_x += 1
                if craft_chislo_x >= 5:
                    craft_chislo_x = 0
                    craft_chislo_y += 1
            if e1 >= 90 and r1 > 50 and t1 > 15 and verstak_nalichie:
                pn = pygame.image.load('data/kirka_ametist.png')
                ris_invent = pn.get_rect().move(craft_chislo_x * 50, craft_chislo_y * 50)
                screen.blit(pn, ris_invent)
                spisok_koord_craft.append([craft_chislo_x, craft_chislo_y, 50, 'kirka_ametist'])
                craft_chislo_x += 1
                if craft_chislo_x >= 5:
                    craft_chislo_x = 0
                    craft_chislo_y += 1
            if maso_siroe > 0 and koster_proverka(player):
                pn = pygame.image.load('data/maso_jarenoe.png')
                ris_invent = pn.get_rect().move(craft_chislo_x * 50, craft_chislo_y * 50)
                screen.blit(pn, ris_invent)
                spisok_koord_craft.append([craft_chislo_x, craft_chislo_y, 50, 'maso_jarenoe'])
                craft_chislo_x += 1
                if craft_chislo_x >= 5:
                    craft_chislo_x = 0
                    craft_chislo_y += 1
            if w1 >= 130 and verstak_nalichie:
                pn = pygame.image.load('data/stena_kamen_craft.png')
                ris_invent = pn.get_rect().move(craft_chislo_x * 50, craft_chislo_y * 50)
                screen.blit(pn, ris_invent)
                spisok_koord_craft.append([craft_chislo_x, craft_chislo_y, 50, 'stena_kamen'])
                craft_chislo_x += 1
                if craft_chislo_x >= 5:
                    craft_chislo_x = 0
                    craft_chislo_y += 1
            if e1 >= 110 and verstak_nalichie:
                pn = pygame.image.load('data/block_gold_craft.png')
                ris_invent = pn.get_rect().move(craft_chislo_x * 50, craft_chislo_y * 50)
                screen.blit(pn, ris_invent)
                spisok_koord_craft.append([craft_chislo_x, craft_chislo_y, 50, 'block_gold'])
                craft_chislo_x += 1
                if craft_chislo_x >= 5:
                    craft_chislo_x = 0
                    craft_chislo_y += 1
            if r1 >= 95 and verstak_nalichie:
                pn = pygame.image.load('data/block_diamond_craft.png')
                ris_invent = pn.get_rect().move(craft_chislo_x * 50, craft_chislo_y * 50)
                screen.blit(pn, ris_invent)
                spisok_koord_craft.append([craft_chislo_x, craft_chislo_y, 50, 'block_diamond'])
                craft_chislo_x += 1
                if craft_chislo_x >= 5:
                    craft_chislo_x = 0
                    craft_chislo_y += 1
            if t1 >= 75 and verstak_nalichie:
                pn = pygame.image.load('data/block_ametist_craft.png')
                ris_invent = pn.get_rect().move(craft_chislo_x * 50, craft_chislo_y * 50)
                screen.blit(pn, ris_invent)
                spisok_koord_craft.append([craft_chislo_x, craft_chislo_y, 50, 'block_ametist'])
                craft_chislo_x += 1
                if craft_chislo_x >= 5:
                    craft_chislo_x = 0
                    craft_chislo_y += 1
            if q1 >= 70 and w1 >= 30 and verstak_nalichie:
                pn = pygame.image.load('data/mech_kamen.png')
                ris_invent = pn.get_rect().move(craft_chislo_x * 50, craft_chislo_y * 50)
                screen.blit(pn, ris_invent)
                spisok_koord_craft.append([craft_chislo_x, craft_chislo_y, 50, 'mech_kamen'])
                craft_chislo_x += 1
                if craft_chislo_x >= 5:
                    craft_chislo_x = 0
                    craft_chislo_y += 1
            if q1 >= 100 and w1 >= 60 and e1 >= 30 and verstak_nalichie:
                pn = pygame.image.load('data/mech_gold.png')
                ris_invent = pn.get_rect().move(craft_chislo_x * 50, craft_chislo_y * 50)
                screen.blit(pn, ris_invent)
                spisok_koord_craft.append([craft_chislo_x, craft_chislo_y, 50, 'mech_gold'])
                craft_chislo_x += 1
                if craft_chislo_x >= 5:
                    craft_chislo_x = 0
                    craft_chislo_y += 1
            if w1 >= 90 and e1 >= 50 and r1 >= 25 and verstak_nalichie:
                pn = pygame.image.load('data/mech_diamond.png')
                ris_invent = pn.get_rect().move(craft_chislo_x * 50, craft_chislo_y * 50)
                screen.blit(pn, ris_invent)
                spisok_koord_craft.append([craft_chislo_x, craft_chislo_y, 50, 'mech_diamond'])
                craft_chislo_x += 1
                if craft_chislo_x >= 5:
                    craft_chislo_x = 0
                    craft_chislo_y += 1
            if e1 >= 90 and r1 >= 60 and t1 >= 25 and verstak_nalichie:
                pn = pygame.image.load('data/mech_ametist.png')
                ris_invent = pn.get_rect().move(craft_chislo_x * 50, craft_chislo_y * 50)
                screen.blit(pn, ris_invent)
                spisok_koord_craft.append([craft_chislo_x, craft_chislo_y, 50, 'mech_ametist'])
                craft_chislo_x += 1
                if craft_chislo_x >= 5:
                    craft_chislo_x = 0
                    craft_chislo_y += 1

        class Tile(pygame.sprite.Sprite):
            def __init__(self, tile_type, pos_x, pos_y):
                super().__init__(tiles_group, all_sprites)
                self.image = tile_images[tile_type]
                self.rect = self.image.get_rect().move(
                    tile_width * pos_x, tile_height * pos_y)

        class Player(pygame.sprite.Sprite):
            def __init__(self, pos_x, pos_y):
                super().__init__(player_group, all_sprites)
                self.image = pygame.image.load("data/mar.webp").convert_alpha()
                self.rect = self.image.get_rect().move(
                    tile_width * pos_x - 12, tile_height * pos_y + 10)
                self.pos_x = pos_x
                self.pos_y = pos_y
                self.pos = (self.pos_x, self.pos_y)

            # def move(self, x, y):
                # self.pos_x = x
                # self.pos_y = y
                # self.rect = self.image.get_rect().move(
                    # tile_height * self.pos_x + 15, tile_height * self.pos_y + 5)

        def move(hero, dir):
            x, y = hero.pos
            if dir == 'up':
                if y > 0 and level_map[y - 1][x] == '0':
                    level_map[y][x] = '0'
                    level_map[y - 1][x] = '@'
                    y -= 1
                    camera.update(player)
                    # обновляем положение всех спрайтов
                    for sprite in all_sprites:
                        if 'Player' not in str(sprite):
                            camera.apply2(sprite)
            elif dir == 'down':
                if y < len(level_map) and level_map[y + 1][x] == '.' or level_map[y + 1][x] == '@' \
                        or level_map[y + 1][x] == '0':
                    level_map[y][x] = '0'
                    level_map[y + 1][x] = '@'
                    y += 1
                    for sprite in all_sprites:
                        if 'Player' not in str(sprite):
                            camera.apply3(sprite)
            elif dir == 'left':
                if x > 0 and level_map[y][x - 1] == '.' or level_map[y][x - 1] == '@' or level_map[y][x - 1] == '0':
                    # hero.move(x, y)
                    level_map[y][x] = '0'
                    level_map[y][x - 1] = '@'
                    x -= 1
                    for sprite in all_sprites:
                        if 'Player' not in str(sprite):
                            camera.apply4(sprite)
            elif dir == 'right':
                if x < len(level_map) and level_map[y][x + 1] == '.' or level_map[y][x + 1] == '@'\
                        or level_map[y][x + 1] == '0':
                    # hero.move(x, y)
                    level_map[y][x] = '0'
                    level_map[y][x + 1] = '@'
                    x += 1
                    for sprite in all_sprites:
                        if 'Player' not in str(sprite):
                            camera.apply5(sprite)
            hero.pos = x, y

        def dobicha_dereva():
            dob = 0
            for inv in inventar:
                if 'drevesina' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + random.randint(15, 25)
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'drevesina'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + random.randint(15, 25)
                    dob = 1

        def dobicha_kamna():
            dob = 0
            for inv in inventar:
                if 'kamen_inv' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + random.randint(12, 20)
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'kamen_inv'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + random.randint(12, 20)
                    dob = 1

        def dobicha_gold():
            dob = 0
            for inv in inventar:
                if 'gold_inv' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + random.randint(12, 20)
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'gold_inv'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + random.randint(12, 20)
                    dob = 1

        def dobicha_diamond():
            dob = 0
            for inv in inventar:
                if 'diamond_inv' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + random.randint(7, 15)
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'diamond_inv'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + random.randint(7, 15)
                    dob = 1

        def dobicha_ametostov():
            dob = 0
            for inv in inventar:
                if 'ametist_inv' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + random.randint(4, 9)
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'ametist_inv'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + random.randint(4, 9)
                    dob = 1

        def dobicha_agod():
            dob = 0
            for inv in inventar:
                if 'agoda' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'agoda'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1

        def spawn_resursa(resurs):
            # спавнит рандомно ресурс
            x = random.randrange(11, int(mir + 10) - 1)
            y = random.randrange(11, int(mir + 10) - 1)
            while level_map[x][y] != '0':
                if int(mir) - 1 <= x:
                    y += 1
                    x = 11
                    if int(mir / 10) - 1 <= y:
                        y = 11
                x += 1
            level_map[x][y] = resurs

        def dobicha(hero):
            x, y = hero.pos
            dobicha_nachati = 7
            # проверка на ресурсы вокруг игрока
            if y > 0 and level_map[y - 1][x] != '0':
                if level_map[y - 1][x] == 'q' and lomanie == dobicha_nachati - sila:
                    level_map[y - 1][x] = '0'
                    dobicha_dereva()
                    spawn_resursa('q')
                elif level_map[y - 1][x] == 'w' and lomanie == dobicha_nachati + 2 - sila and sila > 0:
                    level_map[y - 1][x] = '0'
                    dobicha_kamna()
                    spawn_resursa('w')
                elif level_map[y - 1][x] == 'e' and lomanie == dobicha_nachati + 4 - sila and sila > 1:
                    level_map[y - 1][x] = '0'
                    dobicha_gold()
                    spawn_resursa('e')
                elif level_map[y - 1][x] == 'r' and lomanie == dobicha_nachati + 6 - sila and sila > 2:
                    level_map[y - 1][x] = '0'
                    dobicha_diamond()
                    spawn_resursa('r')
                elif level_map[y - 1][x] == 't' and lomanie == dobicha_nachati + 8 - sila and sila > 3:
                    level_map[y - 1][x] = '0'
                    dobicha_ametostov()
                    spawn_resursa('t')
                for agods in range(6):
                    if 'kust ' + str(agods + 1) in level_map[y - 1][x]:
                        level_map[y - 1][x] = 'kust ' + str(agods) + ' ' + level_map[y - 1][x].split()[-1]
                        dobicha_agod()
                        ff = 0
                        for chet in range(len(kusti)):
                            if y - 1 in kusti[chet] and x in kusti[chet]:
                                kust__ = kusti[chet][2].split()
                                kust__[1] = str(int(kust__[1]) - 1)
                                kusti[chet] = [kusti[chet][0], kusti[chet][1], ' '.join(kust__)]
                                ff = 1
                                break
                        if ff == 0:
                            kusti.append([y - 1, x, level_map[y - 1][x]])
            if y > 0 and level_map[y - 1][x + 1] != '0':
                if level_map[y - 1][x + 1] == 'q' and lomanie == dobicha_nachati - sila:
                    level_map[y - 1][x + 1] = '0'
                    dobicha_dereva()
                    spawn_resursa('q')
                elif level_map[y - 1][x + 1] == 'w' and lomanie == dobicha_nachati + 2 - sila and sila > 0:
                    level_map[y - 1][x + 1] = '0'
                    dobicha_kamna()
                    spawn_resursa('w')
                elif level_map[y - 1][x + 1] == 'e' and lomanie == dobicha_nachati + 4 - sila and sila > 1:
                    level_map[y - 1][x + 1] = '0'
                    dobicha_gold()
                    spawn_resursa('e')
                elif level_map[y - 1][x + 1] == 'r' and lomanie == dobicha_nachati + 6 - sila and sila > 2:
                    level_map[y - 1][x + 1] = '0'
                    dobicha_diamond()
                    spawn_resursa('r')
                elif level_map[y - 1][x + 1] == 't' and lomanie == dobicha_nachati + 8 - sila and sila > 3:
                    level_map[y - 1][x + 1] = '0'
                    dobicha_ametostov()
                    spawn_resursa('t')
                for agods in range(6):
                    if 'kust ' + str(agods + 1) in level_map[y - 1][x + 1]:
                        level_map[y - 1][x + 1] = 'kust ' + str(agods) + ' ' + level_map[y - 1][x + 1].split()[-1]
                        dobicha_agod()
                        ff = 0
                        for chet in range(len(kusti)):
                            if y - 1 in kusti[chet] and x + 1 in kusti[chet]:
                                kust__ = kusti[chet][2].split()
                                kust__[1] = str(int(kust__[1]) - 1)
                                kusti[chet] = [kusti[chet][0], kusti[chet][1], ' '.join(kust__)]
                                ff = 1
                                break
                        if ff == 0:
                            kusti.append([y - 1, x + 1, level_map[y - 1][x + 1]])
            if y > 0 and level_map[y][x - 1] != '0':
                if level_map[y][x - 1] == 'q' and lomanie == dobicha_nachati - sila:
                    level_map[y][x - 1] = '0'
                    dobicha_dereva()
                    spawn_resursa('q')
                elif level_map[y][x - 1] == 'w' and lomanie == dobicha_nachati + 2 - sila and sila > 0:
                    level_map[y][x - 1] = '0'
                    dobicha_kamna()
                    spawn_resursa('w')
                elif level_map[y][x - 1] == 'e' and lomanie == dobicha_nachati + 4 - sila and sila > 1:
                    level_map[y][x - 1] = '0'
                    dobicha_gold()
                    spawn_resursa('e')
                elif level_map[y][x - 1] == 'r' and lomanie == dobicha_nachati + 6 - sila and sila > 2:
                    level_map[y][x - 1] = '0'
                    dobicha_diamond()
                    spawn_resursa('r')
                elif level_map[y][x - 1] == 't' and lomanie == dobicha_nachati + 8 - sila and sila > 3:
                    level_map[y][x - 1] = '0'
                    dobicha_ametostov()
                    spawn_resursa('t')
                for agods in range(6):
                    if 'kust ' + str(agods + 1) in level_map[y][x - 1]:
                        level_map[y][x - 1] = 'kust ' + str(agods) + ' ' + level_map[y][x - 1].split()[-1]
                        dobicha_agod()
                        ff = 0
                        for chet in range(len(kusti)):
                            if y in kusti[chet] and x - 1 in kusti[chet]:
                                kust__ = kusti[chet][2].split()
                                kust__[1] = str(int(kust__[1]) - 1)
                                kusti[chet] = [kusti[chet][0], kusti[chet][1], ' '.join(kust__)]
                                ff = 1
                                break
                        if ff == 0:
                            kusti.append([y, x - 1, level_map[y][x - 1]])
            if y > 0 and level_map[y][x + 1] != '0':
                if level_map[y][x + 1] == 'q' and lomanie == dobicha_nachati - sila:
                    level_map[y][x + 1] = '0'
                    dobicha_dereva()
                    spawn_resursa('q')
                elif level_map[y][x + 1] == 'w' and lomanie == dobicha_nachati + 2 - sila and sila > 0:
                    level_map[y][x + 1] = '0'
                    dobicha_kamna()
                    spawn_resursa('w')
                elif level_map[y][x + 1] == 'e' and lomanie == dobicha_nachati + 4 - sila and sila > 1:
                    level_map[y][x + 1] = '0'
                    dobicha_gold()
                    spawn_resursa('e')
                elif level_map[y][x + 1] == 'r' and lomanie == dobicha_nachati + 6 - sila and sila > 2:
                    level_map[y][x + 1] = '0'
                    dobicha_diamond()
                    spawn_resursa('r')
                elif level_map[y][x + 1] == 't' and lomanie == dobicha_nachati + 8 - sila and sila > 3:
                    level_map[y][x + 1] = '0'
                    dobicha_ametostov()
                    spawn_resursa('t')
                for agods in range(6):
                    if 'kust ' + str(agods + 1) in level_map[y][x + 1]:
                        level_map[y][x + 1] = 'kust ' + str(agods) + ' ' + level_map[y][x + 1].split()[-1]
                        dobicha_agod()
                        ff = 0
                        for chet in range(len(kusti)):
                            if y in kusti[chet] and x + 1 in kusti[chet]:
                                kust__ = kusti[chet][2].split()
                                kust__[1] = str(int(kust__[1]) - 1)
                                kusti[chet] = [kusti[chet][0], kusti[chet][1], ' '.join(kust__)]
                                ff = 1
                                break
                        if ff == 0:
                            kusti.append([y, x + 1, level_map[y][x + 1]])
            if y > 0 and level_map[y + 1][x - 1] != '0':
                if level_map[y + 1][x - 1] == 'q' and lomanie == dobicha_nachati - sila:
                    level_map[y + 1][x - 1] = '0'
                    dobicha_dereva()
                    spawn_resursa('q')
                elif level_map[y + 1][x - 1] == 'w' and lomanie == dobicha_nachati + 2 - sila and sila > 0:
                    level_map[y + 1][x - 1] = '0'
                    dobicha_kamna()
                    spawn_resursa('w')
                elif level_map[y + 1][x - 1] == 'e' and lomanie == dobicha_nachati + 4 - sila and sila > 1:
                    level_map[y + 1][x - 1] = '0'
                    dobicha_gold()
                    spawn_resursa('e')
                elif level_map[y + 1][x - 1] == 'r' and lomanie == dobicha_nachati + 6 - sila and sila > 2:
                    level_map[y + 1][x - 1] = '0'
                    dobicha_diamond()
                    spawn_resursa('r')
                elif level_map[y + 1][x - 1] == 't' and lomanie == dobicha_nachati + 8 - sila and sila > 3:
                    level_map[y + 1][x - 1] = '0'
                    dobicha_ametostov()
                    spawn_resursa('t')
                for agods in range(6):
                    if 'kust ' + str(agods + 1) in level_map[y + 1][x - 1]:
                        level_map[y + 1][x - 1] = 'kust ' + str(agods) + ' ' + level_map[y + 1][x - 1].split()[-1]
                        dobicha_agod()
                        ff = 0
                        for chet in range(len(kusti)):
                            if y + 1 in kusti[chet] and x - 1 in kusti[chet]:
                                kust__ = kusti[chet][2].split()
                                kust__[1] = str(int(kust__[1]) - 1)
                                kusti[chet] = [kusti[chet][0], kusti[chet][1], ' '.join(kust__)]
                                ff = 1
                                break
                        if ff == 0:
                            kusti.append([y + 1, x - 1, level_map[y + 1][x - 1]])
            if y > 0 and level_map[y + 1][x] != '0':
                if level_map[y + 1][x] == 'q' and lomanie == dobicha_nachati - sila:
                    level_map[y + 1][x] = '0'
                    dobicha_dereva()
                    spawn_resursa('q')
                elif level_map[y + 1][x] == 'w' and lomanie == dobicha_nachati + 2 - sila and sila > 0:
                    level_map[y + 1][x] = '0'
                    dobicha_kamna()
                    spawn_resursa('w')
                elif level_map[y + 1][x] == 'e' and lomanie == dobicha_nachati + 4 - sila and sila > 1:
                    level_map[y + 1][x] = '0'
                    dobicha_gold()
                    spawn_resursa('e')
                elif level_map[y + 1][x] == 'r' and lomanie == dobicha_nachati + 6 - sila and sila > 2:
                    level_map[y + 1][x] = '0'
                    dobicha_diamond()
                    spawn_resursa('r')
                elif level_map[y + 1][x] == 't' and lomanie == dobicha_nachati + 8 - sila and sila > 3:
                    level_map[y + 1][x] = '0'
                    dobicha_ametostov()
                    spawn_resursa('t')
                for agods in range(6):
                    if 'kust ' + str(agods + 1) in level_map[y + 1][x]:
                        level_map[y + 1][x] = 'kust ' + str(agods) + ' ' + level_map[y + 1][x].split()[-1]
                        dobicha_agod()
                        ff = 0
                        for chet in range(len(kusti)):
                            if y + 1 in kusti[chet] and x in kusti[chet]:
                                kust__ = kusti[chet][2].split()
                                kust__[1] = str(int(kust__[1]) - 1)
                                kusti[chet] = [kusti[chet][0], kusti[chet][1], ' '.join(kust__)]
                                ff = 1
                                break
                        if ff == 0:
                            kusti.append([y + 1, x, level_map[y + 1][x]])
            if y > 0 and level_map[y + 1][x + 1] != '0':
                if level_map[y + 1][x + 1] == 'q' and lomanie == dobicha_nachati - sila:
                    level_map[y + 1][x + 1] = '0'
                    dobicha_dereva()
                    spawn_resursa('q')
                elif level_map[y + 1][x + 1] == 'w' and lomanie == dobicha_nachati + 2 - sila and sila > 0:
                    level_map[y + 1][x + 1] = '0'
                    dobicha_kamna()
                    spawn_resursa('w')
                elif level_map[y + 1][x + 1] == 'e' and lomanie == dobicha_nachati + 4 - sila and sila > 1:
                    level_map[y + 1][x + 1] = '0'
                    dobicha_gold()
                    spawn_resursa('e')
                elif level_map[y + 1][x + 1] == 'r' and lomanie == dobicha_nachati + 6 - sila and sila > 2:
                    level_map[y + 1][x + 1] = '0'
                    dobicha_diamond()
                    spawn_resursa('r')
                elif level_map[y + 1][x + 1] == 't' and lomanie == dobicha_nachati + 8 - sila and sila > 3:
                    level_map[y + 1][x + 1] = '0'
                    dobicha_ametostov()
                    spawn_resursa('t')
                for agods in range(6):
                    if 'kust ' + str(agods + 1) in level_map[y + 1][x + 1]:
                        level_map[y + 1][x + 1] = 'kust ' + str(agods) + ' ' + level_map[y + 1][x + 1].split()[-1]
                        dobicha_agod()
                        ff = 0
                        for chet in range(len(kusti)):
                            if y + 1 in kusti[chet] and x + 1 in kusti[chet]:
                                kust__ = kusti[chet][2].split()
                                kust__[1] = str(int(kust__[1]) - 1)
                                kusti[chet] = [kusti[chet][0], kusti[chet][1], ' '.join(kust__)]
                                ff = 1
                                break
                        if ff == 0:
                            kusti.append([y + 1, x + 1, level_map[y + 1][x + 1]])
            if y > 0 and level_map[y - 1][x - 1] != '0':
                if level_map[y - 1][x - 1] == 'q' and lomanie == dobicha_nachati - sila:
                    level_map[y - 1][x - 1] = '0'
                    dobicha_dereva()
                    spawn_resursa('q')
                elif level_map[y - 1][x - 1] == 'w' and lomanie == dobicha_nachati + 2 - sila and sila > 0:
                    level_map[y - 1][x - 1] = '0'
                    dobicha_kamna()
                    spawn_resursa('w')
                elif level_map[y - 1][x - 1] == 'e' and lomanie == dobicha_nachati + 4 - sila and sila > 1:
                    level_map[y - 1][x - 1] = '0'
                    dobicha_gold()
                    spawn_resursa('e')
                elif level_map[y - 1][x - 1] == 'r' and lomanie == dobicha_nachati + 6 - sila and sila > 2:
                    level_map[y - 1][x - 1] = '0'
                    dobicha_diamond()
                    spawn_resursa('r')
                elif level_map[y - 1][x - 1] == 't' and lomanie == dobicha_nachati + 8 - sila and sila > 3:
                    level_map[y - 1][x - 1] = '0'
                    dobicha_ametostov()
                    spawn_resursa('t')
                for agods in range(6):
                    if 'kust ' + str(agods + 1) in level_map[y - 1][x - 1]:
                        level_map[y - 1][x - 1] = 'kust ' + str(agods) + ' ' + level_map[y - 1][x - 1].split()[-1]
                        dobicha_agod()
                        ff = 0
                        for chet in range(len(kusti)):
                            if y - 1 in kusti[chet] and x - 1 in kusti[chet]:
                                kust__ = kusti[chet][2].split()
                                kust__[1] = str(int(kust__[1]) - 1)
                                kusti[chet] = [kusti[chet][0], kusti[chet][1], ' '.join(kust__)]
                                ff = 1
                                break
                        if ff == 0:
                            kusti.append([y - 1, x - 1, level_map[y - 1][x - 1]])
            # level_x, level_y = generate_level2(load_level(self.file_name.split('/')[-1]))

        class Camera:
            # зададим начальный сдвиг камеры
            def __init__(self):
                self.dx = 0
                self.dy = 0

            # сдвинуть объект obj на смещение камеры
            def apply(self, obj):
                obj.rect.x += self.dx
                obj.rect.y += self.dy

            def apply2(self, obj):
                obj.rect.y += 75

            def apply3(self, obj):
                obj.rect.y -= 75

            def apply4(self, obj):
                obj.rect.x += 75

            def apply5(self, obj):
                obj.rect.x -= 75

            # позиционировать камеру на объекте target
            def update(self, target):
                self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
                self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)

        def v_inventar(material, w1):
            for inv in inventar:
                if material in inv:
                    if 0 < w1 < 356:
                        inventar[int(inv[0]) - 1][2] = w1
                        w1 = 0
                    elif w1 >= 356:
                        inventar[int(inv[0]) - 1][2] = 355
                        w1 -= 355
                    else:
                        inventar[int(inv[0]) - 1] = [inv[0], 'pusto', '0']

        # дальше идут крафты
        def craft_cirki():
            dob = 0
            for inv in inventar:
                if 'kirka_derevo' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'kirka_derevo'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            q1 = 0
            w1 = 0
            e1 = 0
            r1 = 0
            t1 = 0
            craft_chislo_x = 0
            craft_chislo_y = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'drevesina' in i:
                    q1 += int(i[2])
            q1 -= 30
            v_inventar('drevesina', q1)

        def craft_mech():
            dob = 0
            for inv in inventar:
                if 'mech_derevo' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'mech_derevo'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            q1 = 0
            w1 = 0
            e1 = 0
            r1 = 0
            t1 = 0
            craft_chislo_x = 0
            craft_chislo_y = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'drevesina' in i:
                    q1 += int(i[2])
            q1 -= 50
            v_inventar('drevesina', q1)

        def craft_stena():
            dob = 0
            for inv in inventar:
                if 'stena_derevo' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'stena_derevo'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            q1 = 0
            w1 = 0
            e1 = 0
            r1 = 0
            t1 = 0
            craft_chislo_x = 0
            craft_chislo_y = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'drevesina' in i:
                    q1 += int(i[2])
                elif 'kamen_inv' in i:
                    w1 += int(i[2])
            q1 -= 150
            v_inventar('drevesina', q1)

        def craft_stena_kamen():
            dob = 0
            for inv in inventar:
                if 'stena_kamen' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'stena_kamen'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            q1 = 0
            w1 = 0
            e1 = 0
            r1 = 0
            t1 = 0
            craft_chislo_x = 0
            craft_chislo_y = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'kamen_inv' in i:
                    w1 += int(i[2])
            w1 -= 130
            v_inventar('kamen_inv', w1)

        def craft_block_gold():
            dob = 0
            for inv in inventar:
                if 'block_gold' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'block_gold'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            q1 = 0
            w1 = 0
            e1 = 0
            r1 = 0
            t1 = 0
            craft_chislo_x = 0
            craft_chislo_y = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'gold_inv' in i:
                    w1 += int(i[2])
            w1 -= 110
            v_inventar('gold_inv', w1)

        def craft_block_diamond():
            dob = 0
            for inv in inventar:
                if 'block_diamond' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'block_diamond'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            q1 = 0
            w1 = 0
            e1 = 0
            r1 = 0
            t1 = 0
            craft_chislo_x = 0
            craft_chislo_y = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'diamond_inv' in i:
                    w1 += int(i[2])
            w1 -= 95
            v_inventar('diamond_inv', w1)

        def craft_block_ametist():
            dob = 0
            for inv in inventar:
                if 'block_ametist' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'block_ametist'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            q1 = 0
            w1 = 0
            e1 = 0
            r1 = 0
            t1 = 0
            craft_chislo_x = 0
            craft_chislo_y = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'ametist_inv' in i:
                    w1 += int(i[2])
            w1 -= 95
            v_inventar('ametist_inv', w1)

        def craft_verstak():
            dob = 0
            for inv in inventar:
                if 'verstak' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'verstak'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            q1 = 0
            w1 = 0
            e1 = 0
            r1 = 0
            t1 = 0
            craft_chislo_x = 0
            craft_chislo_y = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'drevesina' in i:
                    q1 += int(i[2])
                elif 'kamen_inv' in i:
                    w1 += int(i[2])
            q1 -= 100
            w1 -= 30
            v_inventar('drevesina', q1)
            v_inventar('kamen_inv', w1)

        def craft_koster():
            dob = 0
            for inv in inventar:
                if 'koster' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'koster'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            q1 = 0
            w1 = 0
            e1 = 0
            r1 = 0
            t1 = 0
            craft_chislo_x = 0
            craft_chislo_y = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'drevesina' in i:
                    q1 += int(i[2])
                elif 'kamen_inv' in i:
                    w1 += int(i[2])
            q1 -= 50
            w1 -= 15
            v_inventar('drevesina', q1)
            v_inventar('kamen_inv', w1)

        def craft_kirki_kamen():
            dob = 0
            for inv in inventar:
                if 'kirka_kamen' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'kirka_kamen'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            q1 = 0
            w1 = 0
            e1 = 0
            r1 = 0
            t1 = 0
            craft_chislo_x = 0
            craft_chislo_y = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'drevesina' in i:
                    q1 += int(i[2])
                elif 'kamen_inv' in i:
                    w1 += int(i[2])
            q1 -= 60
            w1 -= 20
            v_inventar('drevesina', q1)
            v_inventar('kamen_inv', w1)

        def craft_kirki_gold():
            dob = 0
            for inv in inventar:
                if 'kirka_gold' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'kirka_gold'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            q1 = 0
            w1 = 0
            e1 = 0
            r1 = 0
            t1 = 0
            craft_chislo_x = 0
            craft_chislo_y = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'drevesina' in i:
                    q1 += int(i[2])
                elif 'kamen_inv' in i:
                    w1 += int(i[2])
                elif 'gold_inv' in i:
                    e1 += int(i[2])
            q1 -= 90
            w1 -= 50
            e1 -= 20
            v_inventar('drevesina', q1)
            v_inventar('kamen_inv', w1)
            v_inventar('gold_inv', e1)

        def craft_kirki_diamond():
            dob = 0
            for inv in inventar:
                if 'kirka_diamond' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'kirka_diamond'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            q1 = 0
            w1 = 0
            e1 = 0
            r1 = 0
            t1 = 0
            craft_chislo_x = 0
            craft_chislo_y = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'diamond_inv' in i:
                    r1 += int(i[2])
                elif 'kamen_inv' in i:
                    w1 += int(i[2])
                elif 'gold_inv' in i:
                    e1 += int(i[2])
            w1 -= 90
            e1 -= 50
            r1 -= 15
            v_inventar('kamen_inv', w1)
            v_inventar('gold_inv', e1)
            v_inventar('diamond_inv', r1)

        def craft_kirki_ametist():
            dob = 0
            for inv in inventar:
                if 'kirka_ametist' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'kirka_ametist'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            q1 = 0
            w1 = 0
            e1 = 0
            r1 = 0
            t1 = 0
            craft_chislo_x = 0
            craft_chislo_y = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'diamond_inv' in i:
                    r1 += int(i[2])
                elif 'ametist_inv' in i:
                    t1 += int(i[2])
                elif 'gold_inv' in i:
                    e1 += int(i[2])
            e1 -= 90
            r1 -= 50
            t1 -= 15
            v_inventar('gold_inv', e1)
            v_inventar('diamond_inv', r1)
            v_inventar('ametist_inv', t1)

        def craft_mech_kamen():
            dob = 0
            for inv in inventar:
                if 'mech_kamen' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'mech_kamen'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            q1 = 0
            w1 = 0
            e1 = 0
            r1 = 0
            t1 = 0
            craft_chislo_x = 0
            craft_chislo_y = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'drevesina' in i:
                    q1 += int(i[2])
                elif 'kamen_inv' in i:
                    w1 += int(i[2])
            q1 -= 70
            w1 -= 30
            v_inventar('drevesina', q1)
            v_inventar('kamen_inv', w1)

        def craft_mech_gold():
            dob = 0
            for inv in inventar:
                if 'mech_gold' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'mech_gold'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            q1 = 0
            w1 = 0
            e1 = 0
            r1 = 0
            t1 = 0
            craft_chislo_x = 0
            craft_chislo_y = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'drevesina' in i:
                    q1 += int(i[2])
                elif 'kamen_inv' in i:
                    w1 += int(i[2])
                elif 'gold_inv' in i:
                    e1 += int(i[2])
            q1 -= 100
            w1 -= 60
            e1 -= 30
            v_inventar('drevesina', q1)
            v_inventar('kamen_inv', w1)
            v_inventar('gold_inv', e1)

        def craft_mech_diamond():
            dob = 0
            for inv in inventar:
                if 'mech_diamond' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'mech_diamond'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            q1 = 0
            w1 = 0
            e1 = 0
            r1 = 0
            t1 = 0
            craft_chislo_x = 0
            craft_chislo_y = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'diamond_inv' in i:
                    r1 += int(i[2])
                elif 'kamen_inv' in i:
                    w1 += int(i[2])
                elif 'gold_inv' in i:
                    e1 += int(i[2])
            w1 -= 90
            e1 -= 50
            r1 -= 25
            v_inventar('kamen_inv', w1)
            v_inventar('gold_inv', e1)
            v_inventar('diamond_inv', r1)

        def craft_mech_ametist():
            dob = 0
            for inv in inventar:
                if 'mech_ametist' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'mech_ametist'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            q1 = 0
            w1 = 0
            e1 = 0
            r1 = 0
            t1 = 0
            craft_chislo_x = 0
            craft_chislo_y = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'diamond_inv' in i:
                    r1 += int(i[2])
                elif 'ametist_inv' in i:
                    t1 += int(i[2])
                elif 'gold_inv' in i:
                    e1 += int(i[2])
            e1 -= 90
            r1 -= 60
            t1 -= 25
            v_inventar('gold_inv', e1)
            v_inventar('diamond_inv', r1)
            v_inventar('ametist_inv', t1)

        def craft_masa_jarennogo():
            dob = 0
            for inv in inventar:
                if 'maso_jarenoe' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'maso_jarenoe'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            maso_siroe = 0
            craft_chislo_x = 0
            craft_chislo_y = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'maso_siroe' in i:
                    maso_siroe += int(i[2])
            maso_siroe -= 1
            for inv in inventar:
                if 'maso_siroe' in inv:
                    # and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355
                    if 0 < maso_siroe < 356:
                        inventar[int(inv[0]) - 1][2] = maso_siroe
                        maso_siroe = 0
                    elif maso_siroe >= 356:
                        inventar[int(inv[0]) - 1][2] = 355
                        maso_siroe -= 355
                    else:
                        inventar[int(inv[0]) - 1] = [inv[0], 'pusto', '0']

        def stavka_bloka_vkl():
            print('режим вкл')

        def stavka_bloca(hero):
            x, y = hero.pos
            block = ''
            # проверка какой блок ставится и его переделка для карты
            if 'stena_derevo' in stavka_predmeta:
                block = 's_d'
            elif 'verstak' in stavka_predmeta:
                block = 'verstak'
            elif 'koster' in stavka_predmeta:
                block = 'koster'
            elif 'stena_kamen' in stavka_predmeta:
                block = 'stena_kamen'
            elif 'block_gold' in stavka_predmeta:
                block = 'block_gold'
            elif 'block_diamond' in stavka_predmeta:
                block = 'block_diamond'
            elif 'block_ametist' in stavka_predmeta:
                block = 'block_ametist'
            if 526 < event.pos[0] < 828 and 225 < event.pos[1] < 451:
                if 526 < event.pos[0] < 602 and 254 < event.pos[1] < 331:
                    if level_map[y - 1][x - 1] == '0':
                        level_map[y - 1][x - 1] = block
                        return 0
                elif 601 < event.pos[0] < 677 and 254 < event.pos[1] < 331:
                    if level_map[y - 1][x] == '0':
                        level_map[y - 1][x] = block
                        return 0
                elif 676 < event.pos[0] < 752 and 254 < event.pos[1] < 331:
                    if level_map[y - 1][x + 1] == '0':
                        level_map[y - 1][x + 1] = block
                        return 0
                elif 526 < event.pos[0] < 602 and 330 < event.pos[1] < 406:
                    if level_map[y][x - 1] == '0':
                        level_map[y][x - 1] = block
                        return 0
                elif 676 < event.pos[0] < 752 and 330 < event.pos[1] < 406:
                    if level_map[y][x + 1] == '0':
                        level_map[y][x + 1] = block
                        return 0
                elif 526 < event.pos[0] < 602 and 405 < event.pos[1] < 481:
                    if level_map[y + 1][x - 1] == '0':
                        level_map[y + 1][x - 1] = block
                        return 0
                elif 601 < event.pos[0] < 677 and 405 < event.pos[1] < 481:
                    if level_map[y + 1][x] == '0':
                        level_map[y + 1][x] = block
                        return 0
                elif 676 < event.pos[0] < 752 and 405 < event.pos[1] < 481:
                    if level_map[y + 1][x + 1] == '0':
                        level_map[y + 1][x + 1] = block
                        return 0
            return 1

        def verstak_proverka(hero):
            x, y = hero.pos
            # проверка на наличие верстака вокруг игрока
            verstak_nalichie = False
            if level_map[y - 1][x - 1] == 'verstak':
                verstak_nalichie = True
            if level_map[y - 1][x] == 'verstak':
                verstak_nalichie = True
            if level_map[y - 1][x + 1] == 'verstak':
                verstak_nalichie = True
            if level_map[y][x - 1] == 'verstak':
                verstak_nalichie = True
            if level_map[y][x + 1] == 'verstak':
                verstak_nalichie = True
            if level_map[y + 1][x - 1] == 'verstak':
                verstak_nalichie = True
            if level_map[y + 1][x] == 'verstak':
                verstak_nalichie = True
            if level_map[y + 1][x + 1] == 'verstak':
                verstak_nalichie = True
            return verstak_nalichie

        def koster_proverka(hero):
            x, y = hero.pos
            # проверка на наличие костра вокруг игрока
            koster_nalichie = False
            if 'koster' in level_map[y - 1][x - 1]:
                koster_nalichie = True
            if 'koster' in level_map[y - 1][x]:
                koster_nalichie = True
            if 'koster' in level_map[y - 1][x + 1]:
                koster_nalichie = True
            if 'koster' in level_map[y][x - 1]:
                koster_nalichie = True
            if 'koster' in level_map[y][x + 1]:
                koster_nalichie = True
            if 'koster' in level_map[y + 1][x - 1]:
                koster_nalichie = True
            if 'koster' in level_map[y + 1][x]:
                koster_nalichie = True
            if 'koster' in level_map[y + 1][x + 1]:
                koster_nalichie = True
            return koster_nalichie

        def dvigenie_mobov(player):
            x_dvig = 19
            y_dvig = 11
            x, y = player.pos
            dvig_1 = []
            dvig_2 = []
            for x_d in range(x_dvig):
                for y_d in range(y_dvig):
                    if 'zaiz' in level_map[y + y_d - 5][x + x_d - 9]:
                        dvig = 0
                        if x - 4 < x + x_d - 9 <= x and level_map[y + y_d - 5][x + x_d - 10] == '0':
                            level_map[y + y_d - 5][x + x_d - 10] = level_map[y + y_d - 5][x + x_d - 9]
                            level_map[y + y_d - 5][x + x_d - 9] = '0'
                            dvig = 1
                        elif x + 4 > x + x_d - 9 >= x and level_map[y + y_d - 5][x + x_d - 8] == '0' and \
                                dvig_1 != x + x_d - 9 and dvig_2 != y + y_d - 5:
                            level_map[y + y_d - 5][x + x_d - 8] = level_map[y + y_d - 5][x + x_d - 9]
                            level_map[y + y_d - 5][x + x_d - 9] = '0'
                            dvig = 1
                            dvig_1 = x + x_d - 8
                            dvig_2 = y + y_d - 5
                        elif y + 4 > y + y_d - 5 >= y and level_map[y + y_d - 4][x + x_d - 9] == '0' and \
                                dvig_1 != x + x_d - 9 and dvig_2 != y + y_d - 5:
                            level_map[y + y_d - 4][x + x_d - 9] = level_map[y + y_d - 5][x + x_d - 9]
                            level_map[y + y_d - 5][x + x_d - 9] = '0'
                            dvig = 1
                            dvig_1 = x + x_d - 9
                            dvig_2 = y + y_d - 4
                        elif y - 4 < y + y_d - 5 <= y and level_map[y + y_d - 6][x + x_d - 9] == '0':
                            level_map[y + y_d - 6][x + x_d - 9] = level_map[y + y_d - 5][x + x_d - 9]
                            level_map[y + y_d - 5][x + x_d - 9] = '0'
                            dvig = 1
                        if dvig == 0:
                            povorot = random.randint(1, 5)
                            if povorot == 1 and level_map[y + y_d - 6][x + x_d - 9] == '0':
                                level_map[y + y_d - 6][x + x_d - 9] = level_map[y + y_d - 5][x + x_d - 9]
                                level_map[y + y_d - 5][x + x_d - 9] = '0'
                            if povorot == 2 and level_map[y + y_d - 5][x + x_d - 10] == '0':
                                level_map[y + y_d - 5][x + x_d - 10] = level_map[y + y_d - 5][x + x_d - 9]
                                level_map[y + y_d - 5][x + x_d - 9] = '0'
                            if povorot == 3 and level_map[y + y_d - 5][x + x_d - 9] == '0':
                                level_map[y + y_d - 6][x + x_d - 8] = level_map[y + y_d - 5][x + x_d - 9]
                                level_map[y + y_d - 5][x + x_d - 9] = '0'
                            if povorot == 4 and level_map[y + y_d - 5][x + x_d - 9] == '0':
                                level_map[y + y_d - 4][x + x_d - 9] = level_map[y + y_d - 5][x + x_d - 9]
                                level_map[y + y_d - 5][x + x_d - 9] = '0'
                    elif 'lisa' in level_map[y + y_d - 5][x + x_d - 9]:
                        dvig = 0
                        if x - 4 < x + x_d - 9 < x and level_map[y + y_d - 5][x + x_d - 8] == '0' and \
                                dvig_1 != x + x_d - 9 and dvig_2 != y + y_d - 5:
                            level_map[y + y_d - 5][x + x_d - 8] = level_map[y + y_d - 5][x + x_d - 9]
                            level_map[y + y_d - 5][x + x_d - 9] = '0'
                            dvig = 1
                            dvig_1 = x + x_d - 8
                            dvig_2 = y + y_d - 5
                        elif x + 4 > x + x_d - 9 > x and level_map[y + y_d - 5][x + x_d - 10] == '0' and \
                                dvig_1 != x + x_d - 9 and dvig_2 != y + y_d - 5:
                            level_map[y + y_d - 5][x + x_d - 10] = level_map[y + y_d - 5][x + x_d - 9]
                            level_map[y + y_d - 5][x + x_d - 9] = '0'
                            dvig = 1
                            dvig_1 = x + x_d - 10
                            dvig_2 = y + y_d - 5
                        elif y + 4 > y + y_d - 5 >= y and level_map[y + y_d - 6][x + x_d - 9] == '0' and \
                                dvig_1 != x + x_d - 9 and dvig_2 != y + y_d - 5:
                            level_map[y + y_d - 6][x + x_d - 9] = level_map[y + y_d - 5][x + x_d - 9]
                            level_map[y + y_d - 5][x + x_d - 9] = '0'
                            dvig = 1
                            dvig_1 = x + x_d - 9
                            dvig_2 = y + y_d - 6
                        elif y - 4 < y + y_d - 5 <= y and level_map[y + y_d - 4][x + x_d - 9] == '0' and \
                                dvig_1 != x + x_d - 9 and dvig_2 != y + y_d - 5:
                            level_map[y + y_d - 4][x + x_d - 9] = level_map[y + y_d - 5][x + x_d - 9]
                            level_map[y + y_d - 5][x + x_d - 9] = '0'
                            dvig = 1
                            dvig_1 = x + x_d - 9
                            dvig_2 = y + y_d - 4
                        if dvig == 0:
                            povorot = random.randint(1, 5)
                            if povorot == 1 and level_map[y + y_d - 6][x + x_d - 9] == '0':
                                level_map[y + y_d - 6][x + x_d - 9] = level_map[y + y_d - 5][x + x_d - 9]
                                level_map[y + y_d - 5][x + x_d - 9] = '0'
                            if povorot == 2 and level_map[y + y_d - 5][x + x_d - 10] == '0':
                                level_map[y + y_d - 5][x + x_d - 10] = level_map[y + y_d - 5][x + x_d - 9]
                                level_map[y + y_d - 5][x + x_d - 9] = '0'
                            if povorot == 3 and level_map[y + y_d - 5][x + x_d - 9] == '0':
                                level_map[y + y_d - 6][x + x_d - 8] = level_map[y + y_d - 5][x + x_d - 9]
                                level_map[y + y_d - 5][x + x_d - 9] = '0'
                            if povorot == 4 and level_map[y + y_d - 5][x + x_d - 9] == '0':
                                level_map[y + y_d - 4][x + x_d - 9] = level_map[y + y_d - 5][x + x_d - 9]
                                level_map[y + y_d - 5][x + x_d - 9] = '0'
                    elif 'wolf' in level_map[y + y_d - 5][x + x_d - 9]:
                        dvig = 0
                        if x - 4 < x + x_d - 9 < x and level_map[y + y_d - 5][x + x_d - 8] == '0' and \
                                dvig_1 != x + x_d - 9 and dvig_2 != y + y_d - 5:
                            level_map[y + y_d - 5][x + x_d - 8] = level_map[y + y_d - 5][x + x_d - 9]
                            level_map[y + y_d - 5][x + x_d - 9] = '0'
                            dvig = 1
                            dvig_1 = x + x_d - 8
                            dvig_2 = y + y_d - 5
                        elif x + 4 > x + x_d - 9 > x and level_map[y + y_d - 5][x + x_d - 10] == '0' and \
                                dvig_1 != x + x_d - 9 and dvig_2 != y + y_d - 5:
                            level_map[y + y_d - 5][x + x_d - 10] = level_map[y + y_d - 5][x + x_d - 9]
                            level_map[y + y_d - 5][x + x_d - 9] = '0'
                            dvig = 1
                            dvig_1 = x + x_d - 10
                            dvig_2 = y + y_d - 5
                        elif y + 4 > y + y_d - 5 >= y and level_map[y + y_d - 6][x + x_d - 9] == '0' and \
                                dvig_1 != x + x_d - 9 and dvig_2 != y + y_d - 5:
                            level_map[y + y_d - 6][x + x_d - 9] = level_map[y + y_d - 5][x + x_d - 9]
                            level_map[y + y_d - 5][x + x_d - 9] = '0'
                            dvig = 1
                            dvig_1 = x + x_d - 9
                            dvig_2 = y + y_d - 6
                        elif y - 4 < y + y_d - 5 <= y and level_map[y + y_d - 4][x + x_d - 9] == '0' and \
                                dvig_1 != x + x_d - 9 and dvig_2 != y + y_d - 5:
                            level_map[y + y_d - 4][x + x_d - 9] = level_map[y + y_d - 5][x + x_d - 9]
                            level_map[y + y_d - 5][x + x_d - 9] = '0'
                            dvig = 1
                            dvig_1 = x + x_d - 9
                            dvig_2 = y + y_d - 4
                        if dvig == 0:
                            povorot = random.randint(1, 5)
                            if povorot == 1 and level_map[y + y_d - 6][x + x_d - 9] == '0':
                                level_map[y + y_d - 6][x + x_d - 9] = level_map[y + y_d - 5][x + x_d - 9]
                                level_map[y + y_d - 5][x + x_d - 9] = '0'
                            if povorot == 2 and level_map[y + y_d - 5][x + x_d - 10] == '0':
                                level_map[y + y_d - 5][x + x_d - 10] = level_map[y + y_d - 5][x + x_d - 9]
                                level_map[y + y_d - 5][x + x_d - 9] = '0'
                            if povorot == 3 and level_map[y + y_d - 5][x + x_d - 9] == '0':
                                level_map[y + y_d - 6][x + x_d - 8] = level_map[y + y_d - 5][x + x_d - 9]
                                level_map[y + y_d - 5][x + x_d - 9] = '0'
                            if povorot == 4 and level_map[y + y_d - 5][x + x_d - 9] == '0':
                                level_map[y + y_d - 4][x + x_d - 9] = level_map[y + y_d - 5][x + x_d - 9]
                                level_map[y + y_d - 5][x + x_d - 9] = '0'

        def yron_mobov(player):
            x, y = player.pos
            # проверка на нахождение враждебных мобов вокруг игрока, и нанесение урона, если да
            if y > 0 and level_map[y - 1][x] != '0':
                if 'lisa' in level_map[y - 1][x]:
                    inventar[-3][1] = str(int(inventar[-3][1]) - 10)
                elif 'wolf' in level_map[y - 1][x]:
                    inventar[-3][1] = str(int(inventar[-3][1]) - 20)
            if y > 0 and level_map[y - 1][x + 1] != '0':
                if 'lisa' in level_map[y - 1][x + 1]:
                    inventar[-3][1] = str(int(inventar[-3][1]) - 10)
                elif 'wolf' in level_map[y - 1][x + 1]:
                    inventar[-3][1] = str(int(inventar[-3][1]) - 20)
            if y > 0 and level_map[y][x - 1] != '0':
                if 'lisa' in level_map[y][x - 1]:
                    inventar[-3][1] = str(int(inventar[-3][1]) - 10)
                elif 'wolf' in level_map[y][x - 1]:
                    inventar[-3][1] = str(int(inventar[-3][1]) - 20)
            if y > 0 and level_map[y][x + 1] != '0':
                if 'lisa' in level_map[y][x + 1]:
                    inventar[-3][1] = str(int(inventar[-3][1]) - 10)
                elif 'wolf' in level_map[y][x + 1]:
                    inventar[-3][1] = str(int(inventar[-3][1]) - 20)
            if y > 0 and level_map[y + 1][x - 1] != '0':
                if 'lisa' in level_map[y + 1][x - 1]:
                    inventar[-3][1] = str(int(inventar[-3][1]) - 10)
                elif 'wolf' in level_map[y + 1][x - 1]:
                    inventar[-3][1] = str(int(inventar[-3][1]) - 20)
            if y > 0 and level_map[y + 1][x] != '0':
                if 'lisa' in level_map[y + 1][x]:
                    inventar[-3][1] = str(int(inventar[-3][1]) - 10)
                elif 'wolf' in level_map[y + 1][x]:
                    inventar[-3][1] = str(int(inventar[-3][1]) - 20)
            if y > 0 and level_map[y + 1][x + 1] != '0':
                if 'lisa' in level_map[y + 1][x + 1]:
                    inventar[-3][1] = str(int(inventar[-3][1]) - 10)
                elif 'wolf' in level_map[y + 1][x + 1]:
                    inventar[-3][1] = str(int(inventar[-3][1]) - 20)
            if y > 0 and level_map[y - 1][x - 1] != '0':
                if 'lisa' in level_map[y - 1][x - 1]:
                    inventar[-3][1] = str(int(inventar[-3][1]) - 10)
                elif 'wolf' in level_map[y - 1][x - 1]:
                    inventar[-3][1] = str(int(inventar[-3][1]) - 20)

        def maso_zaiz():
            dob = 0
            for inv in inventar:
                if 'maso_siroe' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'maso_siroe'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1

        def maso_lisa():
            dob = 0
            for inv in inventar:
                if 'maso_siroe' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 2
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'maso_siroe'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 2
                    dob = 1

        def maso_wolf():
            dob = 0
            for inv in inventar:
                if 'maso_siroe' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 3
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'maso_siroe'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 3
                    dob = 1

        def yron_po(player):
            x, y = player.pos
            # 600 330
            x_ydar = event.pos[0] - 270
            y_ydar = event.pos[1]
            pervoe = 3
            vtoroe = 2
            if x_ydar > y_ydar < 360 and x_ydar + y_ydar < 720:
                for ne_i in range(vtoroe):
                    for ne_i2 in range(pervoe):
                        if 'lisa' in level_map[y - ne_i - 1][x - 1 + ne_i2]:
                            mob = level_map[y - ne_i - 1][x - 1 + ne_i2].split()
                            mob[1] = str(int(mob[1]) - yron)
                            level_map[y - ne_i - 1][x - 1 + ne_i2] = ' '.join(mob)
                            if int(level_map[y - ne_i - 1][x - 1 + ne_i2].split()[1]) < 0:
                                level_map[y - ne_i - 1][x - 1 + ne_i2] = '0'
                                maso_lisa()
                                spawn_resursa('lisa 75')
                        if 'wolf' in level_map[y - ne_i - 1][x - 1 + ne_i2]:
                            mob = level_map[y - ne_i - 1][x - 1 + ne_i2].split()
                            mob[1] = str(int(mob[1]) - yron)
                            level_map[y - ne_i - 1][x - 1 + ne_i2] = ' '.join(mob)
                            if int(level_map[y - ne_i - 1][x - 1 + ne_i2].split()[1]) < 0:
                                level_map[y - ne_i - 1][x - 1 + ne_i2] = '0'
                                maso_wolf()
                                spawn_resursa('wolf 150')
                        if 'zaiz' in level_map[y - ne_i - 1][x - 1 + ne_i2]:
                            mob = level_map[y - ne_i - 1][x - 1 + ne_i2].split()
                            mob[1] = str(int(mob[1]) - yron)
                            level_map[y - ne_i - 1][x - 1 + ne_i2] = ' '.join(mob)
                            if int(level_map[y - ne_i - 1][x - 1 + ne_i2].split()[1]) < 0:
                                level_map[y - ne_i - 1][x - 1 + ne_i2] = '0'
                                maso_zaiz()
                                spawn_resursa('zaiz 25')
            if y_ydar < x_ydar > 360 and x_ydar + y_ydar > 720:
                print(1234)
                for ne_i in range(vtoroe):
                    for ne_i2 in range(pervoe):
                        if 'lisa' in level_map[y + ne_i2 - 1][x + 1 + ne_i]:
                            mob = level_map[y + ne_i2 - 1][x + 1 + ne_i].split()
                            mob[1] = str(int(mob[1]) - yron)
                            level_map[y + ne_i2 - 1][x + 1 + ne_i] = ' '.join(mob)
                            if int(level_map[y + ne_i2 - 1][x + 1 + ne_i].split()[1]) < 0:
                                level_map[y + ne_i2 - 1][x + 1 + ne_i] = '0'
                                maso_lisa()
                                spawn_resursa('lisa 75')
                        if 'wolf' in level_map[y + ne_i2 - 1][x + 1 + ne_i]:
                            mob = level_map[y + ne_i2 - 1][x + 1 + ne_i].split()
                            mob[1] = str(int(mob[1]) - yron)
                            level_map[y + ne_i2 - 1][x + 1 + ne_i] = ' '.join(mob)
                            if int(level_map[y + ne_i2 - 1][x + 1 + ne_i].split()[1]) < 0:
                                level_map[y + ne_i2 - 1][x + 1 + ne_i] = '0'
                                maso_wolf()
                                spawn_resursa('wolf 150')
                        if 'zaiz' in level_map[y + ne_i2 - 1][x + 1 + ne_i]:
                            mob = level_map[y + ne_i2 - 1][x + 1 + ne_i].split()
                            mob[1] = str(int(mob[1]) - yron)
                            level_map[y + ne_i2 - 1][x + 1 + ne_i] = ' '.join(mob)
                            if int(level_map[y + ne_i2 - 1][x + 1 + ne_i].split()[1]) < 0:
                                level_map[y + ne_i2 - 1][x + 1 + ne_i] = '0'
                                maso_zaiz()
                                spawn_resursa('zaiz 25')
            if x_ydar < y_ydar > 360 and x_ydar + y_ydar > 720:
                for ne_i in range(vtoroe):
                    for ne_i2 in range(pervoe):
                        if 'lisa' in level_map[y + ne_i + 1][x - 1 + ne_i2]:
                            mob = level_map[y + ne_i + 1][x - 1 + ne_i2].split()
                            mob[1] = str(int(mob[1]) - yron)
                            level_map[y + ne_i + 1][x - 1 + ne_i2] = ' '.join(mob)
                            if int(level_map[y + ne_i + 1][x - 1 + ne_i2].split()[1]) < 0:
                                level_map[y + ne_i + 1][x - 1 + ne_i2] = '0'
                                maso_lisa()
                                spawn_resursa('lisa 75')
                        if 'wolf' in level_map[y + ne_i + 1][x - 1 + ne_i2]:
                            mob = level_map[y + ne_i + 1][x - 1 + ne_i2].split()
                            mob[1] = str(int(mob[1]) - yron)
                            level_map[y + ne_i + 1][x - 1 + ne_i2] = ' '.join(mob)
                            if int(level_map[y + ne_i + 1][x - 1 + ne_i2].split()[1]) < 0:
                                level_map[y + ne_i + 1][x - 1 + ne_i2] = '0'
                                maso_wolf()
                                spawn_resursa('wolf 150')
                        if 'zaiz' in level_map[y + ne_i + 1][x - 1 + ne_i2]:
                            mob = level_map[y + ne_i + 1][x - 1 + ne_i2].split()
                            mob[1] = str(int(mob[1]) - yron)
                            level_map[y + ne_i + 1][x - 1 + ne_i2] = ' '.join(mob)
                            if int(level_map[y + ne_i + 1][x - 1 + ne_i2].split()[1]) < 0:
                                level_map[y + ne_i + 1][x - 1 + ne_i2] = '0'
                                maso_zaiz()
                                spawn_resursa('zaiz 25')
            if y_ydar > x_ydar < 360 and x_ydar + y_ydar < 720:
                for ne_i in range(vtoroe):
                    for ne_i2 in range(pervoe):
                        if 'lisa' in level_map[y + ne_i2 - 1][x - 1 - ne_i]:
                            mob = level_map[y + ne_i2 - 1][x - 1 - ne_i].split()
                            mob[1] = str(int(mob[1]) - yron)
                            level_map[y + ne_i2 - 1][x - 1 - ne_i] = ' '.join(mob)
                            if int(level_map[y + ne_i2 - 1][x - 1 - ne_i].split()[1]) < 0:
                                level_map[y + ne_i2 - 1][x - 1 - ne_i] = '0'
                                maso_lisa()
                                spawn_resursa('lisa 75')
                        if 'wolf' in level_map[y + ne_i2 - 1][x - 1 - ne_i]:
                            mob = level_map[y + ne_i2 - 1][x - 1 - ne_i].split()
                            mob[1] = str(int(mob[1]) - yron)
                            level_map[y + ne_i2 - 1][x - 1 - ne_i] = ' '.join(mob)
                            if int(level_map[y + ne_i2 - 1][x - 1 - ne_i].split()[1]) < 0:
                                level_map[y + ne_i2 - 1][x - 1 - ne_i] = '0'
                                maso_wolf()
                                spawn_resursa('wolf 150')
                        if 'zaiz' in level_map[y + ne_i2 - 1][x - 1 - ne_i]:
                            mob = level_map[y + ne_i2 - 1][x - 1 - ne_i].split()
                            mob[1] = str(int(mob[1]) - yron)
                            level_map[y + ne_i2 - 1][x - 1 - ne_i] = ' '.join(mob)
                            if int(level_map[y + ne_i2 - 1][x - 1 - ne_i].split()[1]) < 0:
                                level_map[y + ne_i2 - 1][x - 1 - ne_i] = '0'
                                maso_zaiz()
                                spawn_resursa('zaiz 25')

        def rezim_vstavka_bloca_pokaz():
            pn = pygame.image.load('data/molotok.png').convert_alpha()
            ris_invent = pn.get_rect().move(585, 355)
            screen.blit(pn, ris_invent)

        def rezim_kirki(kirka):
            pn = pygame.image.load(f'data/{kirka}.png')
            pn.set_colorkey((00, 168, 243))
            ris_invent = pn.get_rect().move(575, 340)
            screen.blit(pn, ris_invent)

        # with open(self.file_name, 'r') as f:
        WIDTH, HEIGHT = 1280, 720

        tile_width = tile_height = 75
        pygame.init()

        inventar = inventar_skachivanie(self.file_name)

        screen_size = (450, 800)
        # screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
        screen = pygame.display.set_mode((1280, 720))
        tile_images = {
            'empty': load_image('grass.png'),
            'tree': load_image('tree.png'),
            'kamen': load_image('kamen.png'),
            'gold': load_image('gold.png'),
            'diamond': load_image('diamond.png'),
            'ametists': load_image('ametists.png'),
            'stena_derevo': load_image('stena_derevo.png'),
            'lisa': load_image('lisa.png'),
            'wolf': load_image('wolf.png'),
            'kust': load_image('kust.png'),
            'verstak': load_image('verstak.png'),
            'koster': load_image('koster.png'),
            'zaiz': load_image('zaiz.png'),
            'kust_1': load_image('kust_1.png'),
            'kust_2': load_image('kust_2.png'),
            'kust_3': load_image('kust_3.png'),
            'kust_4': load_image('kust_4.png'),
            'kust_5': load_image('kust_5.png'),
            'kust_6': load_image('kust_6.png'),
            'voda': load_image('voda.png'),
            'stena_kamen': load_image('stena_kamen.png'),
            'block_gold': load_image('block_gold.png'),
            'block_diamond': load_image('block_diamond.png'),
            'block_ametist': load_image('block_ametist.png')
        }
        player_image = {
            'mar': load_image('mar.webp'),
            'pusto': load_image('pusto.png'),
            'drevesina': load_image('drevesina.png'),
            'kamen_inv': load_image('kamen_inv.png')
        }
        # основной персонаж
        # группы спрайтов
        all_sprites = pygame.sprite.Group()
        tiles_group = pygame.sprite.Group()
        player_group = pygame.sprite.Group()
        camera = Camera()
        level_map = load_level(self.file_name.split('/')[-1])
        player, level_x, level_y = generate_level(load_level(self.file_name.split('/')[-1]))



        mir = 10
        if 100 > len(level_map) > 50:
            mir = 50
        elif 150 > len(level_map) > 100:
            mir = 100
        elif len(level_map) > 200:
            mir = 200




        clock = pygame.time.Clock()

        FPS = 60
        running = True
        start_screen()
        y = 0
        x = 0
        bb = 1
        obnovlenie = 0
        lomanie = 0
        spisok_koord_craft = []
        q1 = 0
        w1 = 0
        e1 = 0
        r1 = 0
        t1 = 0
        stavka_predmeta = []
        print(123)
        rezim_vstavka_bloca = 0
        sila = 0
        yron = 0
        obnovlenie_mobov = 0
        kusti = []
        konez = 0

        with open('nastroiki_mira/' + self.file_name.split('/')[-1], 'r') as nygno:
            lvl = nygno.read().split()
            lvl[1] = int(lvl[1])
            lvl[2] = int(lvl[2])

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and konez == 0:
                    if event.key == pygame.K_UP:
                        move(player, 'up')
                        # camera.update(player)
                        # обновляем положение всех спрайтов
                        # for sprite in all_sprites:
                        # if 'Player' not in str(sprite):
                        # camera.apply2(sprite)
                        lomanie = 0
                        bb = 1
                    if event.key == pygame.K_DOWN:
                        move(player, 'down')
                        bb = 1
                        lomanie = 0
                    if event.key == pygame.K_LEFT:
                        move(player, 'left')
                        bb = 1
                        lomanie = 0
                    if event.key == pygame.K_RIGHT:
                        move(player, 'right')
                        bb = 1
                        lomanie = 0
                    if event.key == pygame.K_w:
                        move(player, 'up')
                        # camera.update(player)
                        # обновляем положение всех спрайтов
                        # for sprite in all_sprites:
                        # if 'Player' not in str(sprite):
                        # camera.apply2(sprite)
                        lomanie = 0
                        bb = 1
                    if event.key == pygame.K_s:
                        move(player, 'down')
                        bb = 1
                        lomanie = 0
                    if event.key == pygame.K_a:
                        move(player, 'left')
                        bb = 1
                        lomanie = 0
                    if event.key == pygame.K_d:
                        move(player, 'right')
                        bb = 1
                        lomanie = 0
                if event.type == pygame.MOUSEBUTTONDOWN and konez == 0:
                    if event.button == 3:
                        f = 0
                        for i in range(9):
                            if 365 + (i + 1) * 50 < event.pos[0] < 366 + (
                                    i + 2) * 50 and 670 < event.pos[1] and f == 0:
                                inventar[i] = [str(i + 1), 'pusto', '0']
                    if rezim_vstavka_bloca == 0:
                        if event.button == 1:
                            lomanie += 1
                            dobicha(player)
                    if event.button == 1 and yron > 0:
                        yron_po(player)
                    if len(spisok_koord_craft) != 0:
                        f = 0
                        for spi_koord in spisok_koord_craft:
                            if event.pos[0] < (spi_koord[0] + 1) * spi_koord[2] + 1 and event.pos[1] < (spi_koord[
                                    1] + 1) * spi_koord[2] + 1 and f == 0:
                                f = 1
                                print(spi_koord)
                                if spi_koord[3] == 'kirka':
                                    craft_cirki()
                                elif spi_koord[3] == 'mech':
                                    craft_mech()
                                elif spi_koord[3] == 'stena_derevo':
                                    craft_stena()
                                elif spi_koord[3] == 'verstak':
                                    craft_verstak()
                                elif spi_koord[3] == 'koster':
                                    craft_koster()
                                elif spi_koord[3] == 'kirka_kamen':
                                    craft_kirki_kamen()
                                elif spi_koord[3] == 'kirka_gold':
                                    craft_kirki_gold()
                                elif spi_koord[3] == 'kirka_diamond':
                                    craft_kirki_diamond()
                                elif spi_koord[3] == 'kirka_ametist':
                                    craft_kirki_ametist()
                                elif spi_koord[3] == 'maso_jarenoe':
                                    craft_masa_jarennogo()
                                elif spi_koord[3] == 'stena_kamen':
                                    craft_stena_kamen()
                                elif spi_koord[3] == 'block_gold':
                                    craft_block_gold()
                                elif spi_koord[3] == 'block_diamond':
                                    craft_block_diamond()
                                elif spi_koord[3] == 'block_ametist':
                                    craft_block_ametist()
                                elif spi_koord[3] == 'mech_kamen':
                                    craft_mech_kamen()
                                elif spi_koord[3] == 'mech_gold':
                                    craft_mech_gold()
                                elif spi_koord[3] == 'mech_diamond':
                                    craft_mech_diamond()
                                elif spi_koord[3] == 'mech_ametist':
                                    craft_mech_ametist()



                                    # 365 + (int(i[0]) * 50), 670
                    f = 0
                    for i in range(9):
                        if 365 + (i + 1) * 50 < event.pos[0] < 366 + (
                                    i + 2) * 50 and 670 < event.pos[1] and f == 0:
                            sila = 0
                            yron = 0
                            rezim_vstavka_bloca = 0
                            if 'stena_derevo' in inventar[i]:
                                stavka_predmeta = inventar[i]
                                stavka_bloka_vkl()
                                rezim_vstavka_bloca = 1
                            elif 'kirka_derevo' in inventar[i]:
                                sila = 1
                            elif 'verstak' in inventar[i]:
                                stavka_predmeta = inventar[i]
                                stavka_bloka_vkl()
                                rezim_vstavka_bloca = 1
                            elif 'koster' in inventar[i]:
                                stavka_predmeta = inventar[i]
                                stavka_bloka_vkl()
                                rezim_vstavka_bloca = 1
                            elif 'kirka_kamen' in inventar[i]:
                                sila = 2
                            elif 'kirka_gold' in inventar[i]:
                                sila = 3
                            elif 'kirka_diamond' in inventar[i]:
                                sila = 4
                            elif 'kirka_ametist' in inventar[i]:
                                sila = 5
                            elif 'mech_derevo' in inventar[i]:
                                yron = 15
                            elif 'agoda' in inventar[i]:
                                if int(inventar[-2][1]) < int(101):
                                    inventar[-2][1] = str(int(inventar[-2][1]) + 10)
                                inventar[i][2] = str(int(inventar[i][2]) - 1)
                                if inventar[i][2] == '0':
                                    inventar[i][1] = 'pusto'
                            elif 'maso_siroe' in inventar[i]:
                                if int(inventar[-2][1]) < int(101):
                                    inventar[-2][1] = str(int(inventar[-2][1]) + 10)
                                inventar[i][2] = str(int(inventar[i][2]) - 1)
                                if inventar[i][2] == '0':
                                    inventar[i][1] = 'pusto'
                            elif 'maso_jarenoe' in inventar[i]:
                                if int(inventar[-2][1]) < int(101):
                                    inventar[-2][1] = str(int(inventar[-2][1]) + 35)
                                inventar[i][2] = str(int(inventar[i][2]) - 1)
                                if inventar[i][2] == '0':
                                    inventar[i][1] = 'pusto'
                            elif 'stena_kamen' in inventar[i]:
                                stavka_predmeta = inventar[i]
                                stavka_bloka_vkl()
                                rezim_vstavka_bloca = 1
                            elif 'block_gold' in inventar[i]:
                                stavka_predmeta = inventar[i]
                                stavka_bloka_vkl()
                                rezim_vstavka_bloca = 1
                            elif 'block_diamond' in inventar[i]:
                                stavka_predmeta = inventar[i]
                                stavka_bloka_vkl()
                                rezim_vstavka_bloca = 1
                            elif 'block_ametist' in inventar[i]:
                                stavka_predmeta = inventar[i]
                                stavka_bloka_vkl()
                                rezim_vstavka_bloca = 1
                            elif 'mech_kamen' in inventar[i]:
                                yron = 25
                            elif 'mech_gold' in inventar[i]:
                                yron = 30
                            elif 'mech_diamond' in inventar[i]:
                                yron = 35
                            elif 'mech_ametist' in inventar[i]:
                                yron = 40
                            f = 1
                    if rezim_vstavka_bloca == 1:
                        blok_minus = stavka_bloca(player)
                        if blok_minus == 0:
                            stavka_predmeta[2] = str(int(stavka_predmeta[2]) - 1)
                            if int(stavka_predmeta[2]) > 0:
                                inventar[int(stavka_predmeta[0]) - 1] = stavka_predmeta
                                print(inventar)
                            else:
                                inventar[int(stavka_predmeta[0]) - 1] = [stavka_predmeta[0], 'pusto', '0']
                                rezim_vstavka_bloca = 0
                if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and konez == 1:
                    konez = 0
                    level2 = ['1 pusto 0%2 pusto 0%3 pusto 0%4 pusto 0%5 pusto 0%6 pusto 0%7 pusto 0%8 pusto 0%9 pusto 0%HP 100%food 100%cold 100']
                    inventar_spisok = []
                    for lev in level2:
                        inventar_spisok.extend(lev.split('%'))
                    inventar = []
                    for inv in inventar_spisok:
                        inventar.append(inv.split())
                    print(2)
                    print(inventar)
                    # if pygame.mouse.get_pressed()[0]:
                        # print(123)
            # all_sprites = pygame.sprite.Group()
            # tiles_group = pygame.sprite.Group()

            # level_x, level_y = generate_level2(level_map)

            screen.fill(pygame.Color('black'))
            obnovlenie += 1
            if obnovlenie == 270:
                obnovlenie = 0
                if int(inventar[-1][1]) > 0:
                    inventar[-1][1] = str(int(inventar[-1][1]) - 1)
                else:
                    inventar[-3][1] = str(int(inventar[-3][1]) - 9)
                if koster_proverka(player) and int(inventar[-1][1]) < 100:
                    inventar[-1][1] = str(int(inventar[-1][1]) + 10)
                if int(inventar[-2][1]) > 75 and int(inventar[-1][1]) > 75:
                    inventar[-3][1] = str(int(inventar[-3][1]) + 10)
                if int(inventar[-2][1]) > 0:
                    inventar[-2][1] = str(int(inventar[-2][1]) - 3)
                else:
                    inventar[-3][1] = str(int(inventar[-3][1]) - 9)
            if len(kusti) != 0:
                for chet in range(len(kusti))[::-1]:
                    kust = kusti[chet][2].split()
                    kust[2] = str(int(kust[2]) - 1)
                    if kust[2] == '0':
                        kust[1] = str(int(kust[1]) + 1)
                        kust[2] = '400'
                        level_map[kusti[chet][0]][kusti[chet][1]] = ' '.join(kust)
                    kusti[chet][2] = ' '.join(kust)
                    if kust[1] == '6':
                        del kusti[chet]
            verstak_nalichie = verstak_proverka(player)
            all_sprites = pygame.sprite.Group()
            tiles_group = pygame.sprite.Group()
            player_group = pygame.sprite.Group()
            player, level_x, level_y = generate_level(level_map)
            if bb == 1:
                camera.update(player)
                # обновляем положение всех спрайтов
                for sprite in all_sprites:
                    camera.apply(sprite)
            tiles_group.draw(screen)
            player_group.draw(screen)
            if rezim_vstavka_bloca == 1:
                rezim_vstavka_bloca_pokaz()
            # показывает, что держит персонаж
            if sila == 1:
                rezim_kirki('kirka_derevo')
            elif sila == 2:
                rezim_kirki('kirka_kamen')
            elif sila == 3:
                rezim_kirki('kirka_gold')
            elif sila == 4:
                rezim_kirki('kirka_diamond')
            elif sila == 5:
                rezim_kirki('kirka_ametist')
            elif yron == 15:
                rezim_kirki('mech_derevo')
            elif yron == 25:
                rezim_kirki('mech_kamen')
            elif yron == 30:
                rezim_kirki('mech_gold')
            elif yron == 35:
                rezim_kirki('mech_diamond')
            elif yron == 40:
                rezim_kirki('mech_ametist')
            inventar_spawn()
            craft_spawn()
            obnovlenie_mobov += 1
            if obnovlenie_mobov == 90:
                yron_mobov(player)
                dvigenie_mobov(player)
                obnovlenie_mobov = 0
            if int(inventar[-3][1]) <= 0:
                font = pygame.font.Font(None, 80)
                text = font.render(str('Вы погибли'), 1, (0, 0, 0))
                screen.blit(text, (380, 200))

                font = pygame.font.Font(None, 60)
                text = font.render(str('нажмите на любую клавишу, чтобы возрадится'), 1, (0, 0, 0))
                screen.blit(text, (280, 300))
                inventar[-3][1] = '-10000'
                konez = 1
            pygame.display.flip()
            clock.tick(50)

            maaaaap = ''
            for i in level_map:
                maaaaap += '\n' + '%'.join(i)
            with open('mir/' + lvl[0] + '.txt', 'w') as f:
                f.write(''.join(maaaaap))

            inven = ''
            for i in inventar:
                for i2 in i:
                    inven += str(i2) + ' '
                inven = inven[:-1] + '%'
            with open('inventar/' + lvl[0] + '.txt', 'w') as f:
                print(inven[:-1])
                f.write(''.join(inven)[:-1])
        pygame.quit()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    palette = QPalette()
    palette.setBrush(QPalette.Background, QBrush(QPixmap("data/fon_qt.png")))

    example = StarveSurvival()
    example.setPalette(palette)
    example.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
