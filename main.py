import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from sozdanie import Generachia
from sozdanie import Pomoch
from sozdanie import VseMiri
import pygame
import random
import os


class StarveSurvival(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.lvl = ['1234567', 2, 2]
        self.generachia = Generachia(self.lvl)
        self.pomoch = Pomoch(self.lvl)
        self.vse_miri = VseMiri(self.lvl)
        self.setupUI()
        self.generachia.color_data.connect(self.zakritie)
        self.vse_miri.signal__.connect(self.zakritie2)

    def setupUI(self):
        self.setGeometry(300, 150, 1280, 720)
        self.setWindowTitle('Starve survival')

        self.greetine = QLabel(self)
        self.greetine.move(570, 100)
        self.greetine.resize(400, 100)
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
        self.start()

    def zakritie2(self):
        self.vse_miri.close()
        self.file_name = '/'.join(os.path.abspath(f"mir/{self.lvl[0]}.txt").split('\\'))
        self.start()

    def start_old(self):
        # self.file_name = QFileDialog.getOpenFileName(self, 'Выбор сохранения', '')[0]
        self.vse_miri.show()
        # print(self.file_name)
        # self.start()

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
            # функция для получения карты из тестового документа
            with open(filename, 'r') as mapFile:
                level_map = [line.strip() for line in mapFile]
            level2 = level_map
            level_map = []
            # разбивает текст на список
            for lev in level2:
                level_map.append(lev.split('%'))
            return level_map

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
                    elif 'chest' in level[y][x]:
                        Tile('chest', x, y)
            # вернем игрока, а также размер поля в клетках
            return new_player, x, y

        def generate_level_kust(level):
            for y in range(len(level)):
                for x in range(len(level[y])):
                    if 'kust 1' in level[y][x]:
                        kusti.append([y, x, level_map[y][x]])
                    elif 'kust 2' in level[y][x]:
                        kusti.append([y, x, level_map[y][x]])
                    elif 'kust 3' in level[y][x]:
                        kusti.append([y, x, level_map[y][x]])
                    elif 'kust 4' in level[y][x]:
                        kusti.append([y, x, level_map[y][x]])
                    elif 'kust 5' in level[y][x]:
                        kusti.append([y, x, level_map[y][x]])
                    elif 'kust 6' in level[y][x]:
                        pass
                    elif 'kust' in level[y][x]:
                        kusti.append([y, x, level_map[y][x]])

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

        def text_napisanie_chisla(i):
            font = pygame.font.Font(None, 30)
            text = font.render(str(i[-1]), 1, (100, 100, 100))
            screen.blit(text, (380 + int(i[0]) * 50, 700))

        def inventar_spawn():
            for i in inventar:
                # проверка какие предметы в инвентаре и их спавн в окне игры
                if 'pusto' in i:
                    pn = pygame.image.load('data/pusto.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                elif 'drevesina' in i:
                    pn = pygame.image.load('data/drevesina.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                    text_napisanie_chisla(i)
                elif 'kamen_inv' in i:
                    pn = pygame.image.load('data/kamen_inv.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                    text_napisanie_chisla(i)
                elif 'kirka_derevo' in i:
                    pn = pygame.image.load('data/kirka_derevo.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                    text_napisanie_chisla(i)
                elif 'mech_derevo' in i:
                    pn = pygame.image.load('data/mech_derevo.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                    text_napisanie_chisla(i)
                elif 'stena_derevo' in i:
                    pn = pygame.image.load('data/stena_derevo_craft.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                    text_napisanie_chisla(i)
                elif 'verstak' in i:
                    pn = pygame.image.load('data/verstak_craft.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                    text_napisanie_chisla(i)
                elif 'koster' in i:
                    pn = pygame.image.load('data/koster_craft.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                    text_napisanie_chisla(i)
                elif 'gold_inv' in i:
                    pn = pygame.image.load('data/gold_inv.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                    text_napisanie_chisla(i)
                elif 'diamond_inv' in i:
                    pn = pygame.image.load('data/diamond_inv.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                    text_napisanie_chisla(i)
                elif 'ametist_inv' in i:
                    pn = pygame.image.load('data/ametist_inv.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                    text_napisanie_chisla(i)
                elif 'kirka_kamen' in i:
                    pn = pygame.image.load('data/kirka_kamen.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                    text_napisanie_chisla(i)
                elif 'kirka_gold' in i:
                    pn = pygame.image.load('data/kirka_gold.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                    text_napisanie_chisla(i)
                elif 'kirka_diamond' in i:
                    pn = pygame.image.load('data/kirka_diamond.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                    text_napisanie_chisla(i)
                elif 'kirka_ametist' in i:
                    pn = pygame.image.load('data/kirka_ametist.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                    text_napisanie_chisla(i)
                elif 'agoda' in i:
                    pn = pygame.image.load('data/agoda.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                    text_napisanie_chisla(i)
                elif 'maso_siroe' in i:
                    pn = pygame.image.load('data/maso_siroe.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                    text_napisanie_chisla(i)
                elif 'maso_jarenoe' in i:
                    pn = pygame.image.load('data/maso_jarenoe.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                    text_napisanie_chisla(i)
                elif 'stena_kamen' in i:
                    pn = pygame.image.load('data/stena_kamen_craft.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                    text_napisanie_chisla(i)
                elif 'block_gold' in i:
                    pn = pygame.image.load('data/block_gold_craft.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                    text_napisanie_chisla(i)
                elif 'block_diamond' in i:
                    pn = pygame.image.load('data/block_diamond_craft.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                    text_napisanie_chisla(i)
                elif 'block_ametist' in i:
                    pn = pygame.image.load('data/block_ametist_craft.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                    text_napisanie_chisla(i)
                elif 'mech_kamen' in i:
                    pn = pygame.image.load('data/mech_kamen.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                    text_napisanie_chisla(i)
                elif 'mech_gold' in i:
                    pn = pygame.image.load('data/mech_gold.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                    text_napisanie_chisla(i)
                elif 'mech_diamond' in i:
                    pn = pygame.image.load('data/mech_diamond.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                    text_napisanie_chisla(i)
                elif 'mech_ametist' in i:
                    pn = pygame.image.load('data/mech_ametist.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                    text_napisanie_chisla(i)
                elif 'chest' in i:
                    pn = pygame.image.load('data/chest_craft.png')
                    ris_invent = pn.get_rect().move(365 + (int(i[0]) * 50), 670)
                    screen.blit(pn, ris_invent)
                    text_napisanie_chisla(i)


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
                    # 72,6,7 - цвет болгарская роза, не знаю зачем, но я даже нашел интересные цвета
                    pygame.draw.rect(screen, (72, 6, 7), (568, 648, int(144 * hp), 19))
                elif 'cold' in i:
                    hp = int(i[1]) / 100
                    if hp > 1:
                        hp = 1
                    pygame.draw.rect(screen, (0, 0, 0), (715, 645, 150, 25))
                    # а 93 118 203 - Индиго Крайола
                    pygame.draw.rect(screen, (93, 118, 203), (718, 648, int(144 * hp), 19))

        def text_napisanie_chisla_chest(i, nomer_sunduka):
            font = pygame.font.Font(None, 30)
            text = font.render(str(i[-1]), 1, (100, 100, 100))
            screen.blit(text, (1100 + int(i[0]) * 50, 30 + 50 * nomer_sunduka))

        def chest_spawn(nomer, nomer_sunduka):
            i = nomer.split()
            # проверка какие предметы в сундуке и их спавн в окне игры
            if 'pusto' in i:
                pn = pygame.image.load('data/pusto.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
            elif 'drevesina' in i:
                pn = pygame.image.load('data/drevesina.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
                text_napisanie_chisla_chest(i, nomer_sunduka)
            elif 'kamen_inv' in i:
                pn = pygame.image.load('data/kamen_inv.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
                text_napisanie_chisla_chest(i, nomer_sunduka)
            elif 'kirka_derevo' in i:
                pn = pygame.image.load('data/kirka_derevo.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
                text_napisanie_chisla_chest(i, nomer_sunduka)
            elif 'mech_derevo' in i:
                pn = pygame.image.load('data/mech_derevo.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
                text_napisanie_chisla_chest(i, nomer_sunduka)
            elif 'stena_derevo' in i:
                pn = pygame.image.load('data/stena_derevo_craft.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
                text_napisanie_chisla_chest(i, nomer_sunduka)
            elif 'verstak' in i:
                pn = pygame.image.load('data/verstak_craft.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
                text_napisanie_chisla_chest(i, nomer_sunduka)
            elif 'koster' in i:
                pn = pygame.image.load('data/koster_craft.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
                text_napisanie_chisla_chest(i, nomer_sunduka)
            elif 'gold_inv' in i:
                pn = pygame.image.load('data/gold_inv.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
                text_napisanie_chisla_chest(i, nomer_sunduka)
            elif 'diamond_inv' in i:
                pn = pygame.image.load('data/diamond_inv.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
                text_napisanie_chisla_chest(i, nomer_sunduka)
            elif 'ametist_inv' in i:
                pn = pygame.image.load('data/ametist_inv.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
                text_napisanie_chisla_chest(i, nomer_sunduka)
            elif 'kirka_kamen' in i:
                pn = pygame.image.load('data/kirka_kamen.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
                text_napisanie_chisla_chest(i, nomer_sunduka)
            elif 'kirka_gold' in i:
                pn = pygame.image.load('data/kirka_gold.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
                text_napisanie_chisla_chest(i, nomer_sunduka)
            elif 'kirka_diamond' in i:
                pn = pygame.image.load('data/kirka_diamond.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
                text_napisanie_chisla_chest(i, nomer_sunduka)
            elif 'kirka_ametist' in i:
                pn = pygame.image.load('data/kirka_ametist.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
                text_napisanie_chisla_chest(i, nomer_sunduka)
            elif 'agoda' in i:
                pn = pygame.image.load('data/agoda.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
                text_napisanie_chisla_chest(i, nomer_sunduka)
            elif 'maso_siroe' in i:
                pn = pygame.image.load('data/maso_siroe.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
                text_napisanie_chisla_chest(i, nomer_sunduka)
            elif 'maso_jarenoe' in i:
                pn = pygame.image.load('data/maso_jarenoe.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
                text_napisanie_chisla_chest(i, nomer_sunduka)
            elif 'stena_kamen' in i:
                pn = pygame.image.load('data/stena_kamen_craft.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
                text_napisanie_chisla_chest(i, nomer_sunduka)
            elif 'block_gold' in i:
                pn = pygame.image.load('data/block_gold_craft.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
                text_napisanie_chisla_chest(i, nomer_sunduka)
            elif 'block_diamond' in i:
                pn = pygame.image.load('data/block_diamond_craft.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
                text_napisanie_chisla_chest(i, nomer_sunduka)
            elif 'block_ametist' in i:
                pn = pygame.image.load('data/block_ametist_craft.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
                text_napisanie_chisla_chest(i, nomer_sunduka)
            elif 'mech_kamen' in i:
                pn = pygame.image.load('data/mech_kamen.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
                text_napisanie_chisla_chest(i, nomer_sunduka)
            elif 'mech_gold' in i:
                pn = pygame.image.load('data/mech_gold.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
                text_napisanie_chisla_chest(i, nomer_sunduka)
            elif 'mech_diamond' in i:
                pn = pygame.image.load('data/mech_diamond.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
                text_napisanie_chisla_chest(i, nomer_sunduka)
            elif 'mech_ametist' in i:
                pn = pygame.image.load('data/mech_ametist.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
                text_napisanie_chisla_chest(i, nomer_sunduka)
            elif 'chest' in i:
                pn = pygame.image.load('data/chest_craft.png')
                ris_invent = pn.get_rect().move(1080 + (int(i[0]) * 50), 50 * nomer_sunduka)
                screen.blit(pn, ris_invent)
                text_napisanie_chisla_chest(i, nomer_sunduka)
            spisok_koord_chest.append([1080 + (int(i[0]) * 50) + 50, 50, nomer_sunduka, int(i[0]), i[1], int(i[2])])

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
            if q1 >= 70 and w1 > 20:
                pn = pygame.image.load('data/chest_craft.png')
                ris_invent = pn.get_rect().move(craft_chislo_x * 50, craft_chislo_y * 50)
                screen.blit(pn, ris_invent)
                spisok_koord_craft.append([craft_chislo_x, craft_chislo_y, 50, 'chest'])
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

        def move(hero, dir):
            # перемещение героя
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

        def dobicha_vsego(material, minimum, maksimum):
            dob = 0
            for inv in inventar:
                if material in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + random.randint(minimum, maksimum)
                    dob = 1
                    break
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = material
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + random.randint(minimum, maksimum)
                    break

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
                    if int(mir) - 1 <= y:
                        y = 11
                x += 1
            level_map[x][y] = resurs

        def dobicha(hero):
            x, y = hero.pos
            dobicha_nachati = 7
            # проверка на ресурсы вокруг игрока
            pervoe = 3
            vtoroe = 3
            for ne_i in range(vtoroe):
                for ne_i2 in range(pervoe):
                    if level_map[y - ne_i + 1][x - 1 + ne_i2] == 'q' and lomanie == dobicha_nachati - sila:
                        level_map[y - ne_i + 1][x - 1 + ne_i2] = '0'
                        dobicha_vsego('drevesina', 15, 25)
                        spawn_resursa('q')
                    elif level_map[y - ne_i + 1][x - 1 + ne_i2] == 'w' and lomanie == dobicha_nachati + 2 - \
                            sila and sila > 0:
                        level_map[y - ne_i + 1][x - 1 + ne_i2] = '0'
                        dobicha_vsego('kamen_inv', 12, 20)
                        spawn_resursa('w')
                    elif level_map[y - ne_i + 1][x - 1 + ne_i2] == 'e' and lomanie == dobicha_nachati + 4 - \
                            sila and sila > 1:
                        level_map[y - ne_i + 1][x - 1 + ne_i2] = '0'
                        dobicha_vsego('gold_inv', 10, 18)
                        spawn_resursa('e')
                    elif level_map[y - ne_i + 1][x - 1 + ne_i2] == 'r' and lomanie == dobicha_nachati + 6 - \
                            sila and sila > 2:
                        level_map[y - ne_i + 1][x - 1 + ne_i2] = '0'
                        dobicha_vsego('diamond_inv', 7, 15)
                        spawn_resursa('r')
                    elif level_map[y - ne_i + 1][x - 1 + ne_i2] == 't' and lomanie == dobicha_nachati + 8 - \
                            sila and sila > 3:
                        level_map[y - ne_i + 1][x - 1 + ne_i2] = '0'
                        dobicha_vsego('ametist_inv', 4, 9)
                        spawn_resursa('t')
                    for agods in range(6):
                        if 'kust ' + str(agods + 1) in level_map[y - ne_i + 1][x - 1 + ne_i2]:
                            level_map[y - ne_i + 1][x - 1 + ne_i2] = 'kust ' + str(agods) + ' ' + level_map[y - ne_i + 1][x - 1 + ne_i2].split()[-1]
                            dobicha_agod()
                            ff = 0
                            for chet in range(len(kusti)):
                                if y - ne_i + 1 in kusti[chet] and x - 1 + ne_i2 in kusti[chet]:
                                    kust__ = kusti[chet][2].split()
                                    kust__[1] = str(int(kust__[1]) - 1)
                                    kusti[chet] = [kusti[chet][0], kusti[chet][1], ' '.join(kust__)]
                                    ff = 1
                                    break
                            if ff == 0:
                                kusti.append([y - ne_i + 1, x - 1 + ne_i2, level_map[y - ne_i + 1][x - 1 + ne_i2]])
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

        def dobavlenie_predmeta_v(predmet):
            # добавляет предмет в инвентарь
            dob = 0
            for inv in inventar:
                if predmet in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
                    break
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = predmet
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    break

        def dobavlenie_predmeta_v_most_inv(predmet, w1, hero, nomer, nomer_v):
            # добавляет предмет в инвентарь
            dob = 0
            for inv in inventar:
                if predmet in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + w1
                    dob = 1
                    break
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = predmet
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + w1
                    break
            x, y = hero.pos
            # проверка на наличие сундуков вокруг игрока
            pervoe = 3
            vtoroe = 3
            nomer_chest = -1
            dob = 0
            for ne_i in range(vtoroe):
                for ne_i2 in range(pervoe):
                    if 'chest' in level_map[y - ne_i + 1][x - 1 + ne_i2] and dob == 0:
                        nomer_chest += 1
                        if nomer_chest == nomer // 3:
                            invent_chest = level_map[y - ne_i + 1][x - 1 + ne_i2].split('&')
                            invent_chest[nomer_v] = f"{nomer_v} pusto 0"
                            level_map[y - ne_i + 1][x - 1 + ne_i2] = '&'.join(invent_chest)
                            dob = 1

        def dobavlenie_predmeta_v_most_chest(predmet, w1, hero):
            x, y = hero.pos
            # проверка на наличие сундуков вокруг игрока
            pervoe = 3
            vtoroe = 3
            dob = 0
            for ne_i in range(vtoroe):
                for ne_i2 in range(pervoe):
                    if 'chest' in level_map[y - ne_i + 1][x - 1 + ne_i2]:
                        invent_chest = level_map[y - ne_i + 1][x - 1 + ne_i2].split('&')
            # добавляет предмет в инвентарь
                        for invv in invent_chest:
                            inv = invv.split()
                            if predmet in inv and dob != 1 and int(inv[2]) < 355:
                                inv[2] = str(int(inv[2]) + w1)
                                inv = ' '.join(inv)
                                invent_chest[invent_chest.index(invv)] = inv
                                level_map[y - ne_i + 1][x - 1 + ne_i2] = '&'.join(invent_chest)
                                dob = 1
                                break
                        for invv in invent_chest:
                            inv = invv.split()
                            if 'pusto' in inv and dob != 1:
                                inv[2] = str(w1)
                                inv[1] = predmet
                                inv = ' '.join(inv)
                                invent_chest[invent_chest.index(invv)] = inv
                                level_map[y - ne_i + 1][x - 1 + ne_i2] = '&'.join(invent_chest)
                                dob = 1
                                break

        # дальше идут крафты
        def craft_cirki():
            dobavlenie_predmeta_v('kirka_derevo')
            q1 = 0
            # для удобства добавления крафтов, так как qwerty клавиатура почти у всех, то то ее можно как уровни считать
            # q - первый уровень и тд
            # w1 = 0
            # e1 = 0
            # r1 = 0
            # t1 = 0
            # craft_chislo_x = 0
            # craft_chislo_y = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'drevesina' in i:
                    q1 += int(i[2])
            q1 -= 30
            v_inventar('drevesina', q1)

        # в угоду оптимизации, так как не придется считать все ресурсы, а только те, которые нужны

        def craft_mech():
            dobavlenie_predmeta_v('mech_derevo')
            q1 = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'drevesina' in i:
                    q1 += int(i[2])
            q1 -= 50
            v_inventar('drevesina', q1)

        def craft_stena():
            dobavlenie_predmeta_v('stena_derevo')
            q1 = 0
            w1 = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'drevesina' in i:
                    q1 += int(i[2])
                elif 'kamen_inv' in i:
                    w1 += int(i[2])
            q1 -= 150
            v_inventar('drevesina', q1)

        def craft_stena_kamen():
            dobavlenie_predmeta_v('stena_kamen')
            w1 = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'kamen_inv' in i:
                    w1 += int(i[2])
            w1 -= 130
            v_inventar('kamen_inv', w1)

        def craft_block_gold():
            dobavlenie_predmeta_v('block_gold')
            w1 = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'gold_inv' in i:
                    w1 += int(i[2])
            w1 -= 110
            v_inventar('gold_inv', w1)

        def craft_block_diamond():
            dobavlenie_predmeta_v('block_diamond')
            w1 = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'diamond_inv' in i:
                    w1 += int(i[2])
            w1 -= 95
            v_inventar('diamond_inv', w1)

        def craft_block_ametist():
            dobavlenie_predmeta_v('block_ametist')
            w1 = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'ametist_inv' in i:
                    w1 += int(i[2])
            w1 -= 95
            v_inventar('ametist_inv', w1)

        def craft_verstak():
            dobavlenie_predmeta_v('verstak')
            q1 = 0
            w1 = 0
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

        def craft_chest():
            dobavlenie_predmeta_v('chest')
            q1 = 0
            w1 = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'drevesina' in i:
                    q1 += int(i[2])
                elif 'kamen_inv' in i:
                    w1 += int(i[2])
            q1 -= 70
            w1 -= 20
            v_inventar('drevesina', q1)
            v_inventar('kamen_inv', w1)

        def craft_koster():
            dobavlenie_predmeta_v('koster')
            q1 = 0
            w1 = 0
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
            dobavlenie_predmeta_v('kirka_kamen')
            q1 = 0
            w1 = 0
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
            dobavlenie_predmeta_v('kirka_gold')
            q1 = 0
            w1 = 0
            e1 = 0
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
            dobavlenie_predmeta_v('kirka_diamond')
            w1 = 0
            e1 = 0
            r1 = 0
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
            dobavlenie_predmeta_v('kirka_ametist')
            e1 = 0
            r1 = 0
            t1 = 0
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
            dobavlenie_predmeta_v('mech_kamen')
            q1 = 0
            w1 = 0
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
            dobavlenie_predmeta_v('mech_gold')
            q1 = 0
            w1 = 0
            e1 = 0
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
            dobavlenie_predmeta_v('mech_diamond')
            w1 = 0
            e1 = 0
            r1 = 0
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
            dobavlenie_predmeta_v('mech_ametist')
            e1 = 0
            r1 = 0
            t1 = 0
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
            dobavlenie_predmeta_v('maso_jarenoe')
            maso_siroe = 0
            spisok_koord_craft.clear()
            for i in inventar:
                if 'maso_siroe' in i:
                    maso_siroe += int(i[2])
            maso_siroe -= 1
            for inv in inventar:
                if 'maso_siroe' in inv:
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
            elif 'chest' in stavka_predmeta:
                block = 'chest&1 pusto 0&2 pusto 0&3 pusto 0'
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
            pervoe = 3
            vtoroe = 3
            for ne_i in range(vtoroe):
                for ne_i2 in range(pervoe):
                    if level_map[y - ne_i + 1][x - 1 + ne_i2] == 'verstak':
                        verstak_nalichie = True
            return verstak_nalichie

        def chest_proverka(hero):
            x, y = hero.pos
            # проверка на наличие сундуков вокруг игрока
            pervoe = 3
            vtoroe = 3
            nomer_sunduka = -1
            for ne_i in range(vtoroe):
                for ne_i2 in range(pervoe):
                    if 'chest' in level_map[y - ne_i + 1][x - 1 + ne_i2]:
                        nomer_sunduka += 1
                        invent_chest = level_map[y - ne_i + 1][x - 1 + ne_i2].split('&')
                        for nomer in invent_chest[1:]:
                            chest_spawn(nomer, nomer_sunduka)


        def koster_proverka(hero):
            x, y = hero.pos
            # проверка на наличие костра вокруг игрока
            koster_nalichie = False
            pervoe = 3
            vtoroe = 3
            for ne_i in range(vtoroe):
                for ne_i2 in range(pervoe):
                    if level_map[y - ne_i + 1][x - 1 + ne_i2] == 'koster':
                        koster_nalichie = True
            return koster_nalichie

        def randomnoe_dvigenie(x_d, y_d, x, y):
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

        def dvigenie_mobov(player):
            # враждебные мобы способны отбегать от игрока, но они всегда возвращаются
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
                            randomnoe_dvigenie(x_d, y_d, x, y)
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
                        if level_map[y + y_d - 5][x + x_d - 9] == '#':
                            dvig = 1
                        if dvig == 0:
                            randomnoe_dvigenie(x_d, y_d, x, y)
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
                        # if level_map[y + y_d - 5][x + x_d - 8] == '#':
                            # dvig = 1
                        # elif level_map[y + y_d - 5][x + x_d - 10] == '#':
                            # dvig = 1
                        # elif level_map[y + y_d - 6][x + x_d - 9] == '#':
                            # dvig = 1
                        # elif level_map[y + y_d - 4][x + x_d - 9] == '#':
                            # dvig = 1
                        if level_map[y + y_d - 5][x + x_d - 9] == '#':
                            dvig = 1
                        if dvig == 0:
                            randomnoe_dvigenie(x_d, y_d, x, y)

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

        def maso_v(scolco):
            # добавляет мясо в инвентарь
            dob = 0
            for inv in inventar:
                if 'maso_siroe' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + scolco
                    dob = 1
                    break
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'maso_siroe'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + scolco
                    break

        def yron_po(player):
            x, y = player.pos
            # 600 330
            x_ydar = event.pos[0] - 270
            y_ydar = event.pos[1]
            pervoe = 3
            vtoroe = 2
            # проверка ударили ли вы кого нибудь
            if x_ydar > y_ydar < 360 and x_ydar + y_ydar < 720:
                for ne_i in range(vtoroe):
                    for ne_i2 in range(pervoe):
                        if 'lisa' in level_map[y - ne_i - 1][x - 1 + ne_i2]:
                            mob = level_map[y - ne_i - 1][x - 1 + ne_i2].split()
                            mob[1] = str(int(mob[1]) - yron)
                            level_map[y - ne_i - 1][x - 1 + ne_i2] = ' '.join(mob)
                            if int(level_map[y - ne_i - 1][x - 1 + ne_i2].split()[1]) < 0:
                                level_map[y - ne_i - 1][x - 1 + ne_i2] = '0'
                                maso_v(2)
                                spawn_resursa('lisa 75')
                        if 'wolf' in level_map[y - ne_i - 1][x - 1 + ne_i2]:
                            mob = level_map[y - ne_i - 1][x - 1 + ne_i2].split()
                            mob[1] = str(int(mob[1]) - yron)
                            level_map[y - ne_i - 1][x - 1 + ne_i2] = ' '.join(mob)
                            if int(level_map[y - ne_i - 1][x - 1 + ne_i2].split()[1]) < 0:
                                level_map[y - ne_i - 1][x - 1 + ne_i2] = '0'
                                maso_v(3)
                                spawn_resursa('wolf 150')
                        if 'zaiz' in level_map[y - ne_i - 1][x - 1 + ne_i2]:
                            mob = level_map[y - ne_i - 1][x - 1 + ne_i2].split()
                            mob[1] = str(int(mob[1]) - yron)
                            level_map[y - ne_i - 1][x - 1 + ne_i2] = ' '.join(mob)
                            if int(level_map[y - ne_i - 1][x - 1 + ne_i2].split()[1]) < 0:
                                level_map[y - ne_i - 1][x - 1 + ne_i2] = '0'
                                maso_v(1)
                                spawn_resursa('zaiz 25')
            if y_ydar < x_ydar > 360 and x_ydar + y_ydar > 720:
                for ne_i in range(vtoroe):
                    for ne_i2 in range(pervoe):
                        if 'lisa' in level_map[y + ne_i2 - 1][x + 1 + ne_i]:
                            mob = level_map[y + ne_i2 - 1][x + 1 + ne_i].split()
                            mob[1] = str(int(mob[1]) - yron)
                            level_map[y + ne_i2 - 1][x + 1 + ne_i] = ' '.join(mob)
                            if int(level_map[y + ne_i2 - 1][x + 1 + ne_i].split()[1]) < 0:
                                level_map[y + ne_i2 - 1][x + 1 + ne_i] = '0'
                                maso_v(2)
                                spawn_resursa('lisa 75')
                        if 'wolf' in level_map[y + ne_i2 - 1][x + 1 + ne_i]:
                            mob = level_map[y + ne_i2 - 1][x + 1 + ne_i].split()
                            mob[1] = str(int(mob[1]) - yron)
                            level_map[y + ne_i2 - 1][x + 1 + ne_i] = ' '.join(mob)
                            if int(level_map[y + ne_i2 - 1][x + 1 + ne_i].split()[1]) < 0:
                                level_map[y + ne_i2 - 1][x + 1 + ne_i] = '0'
                                maso_v(3)
                                spawn_resursa('wolf 150')
                        if 'zaiz' in level_map[y + ne_i2 - 1][x + 1 + ne_i]:
                            mob = level_map[y + ne_i2 - 1][x + 1 + ne_i].split()
                            mob[1] = str(int(mob[1]) - yron)
                            level_map[y + ne_i2 - 1][x + 1 + ne_i] = ' '.join(mob)
                            if int(level_map[y + ne_i2 - 1][x + 1 + ne_i].split()[1]) < 0:
                                level_map[y + ne_i2 - 1][x + 1 + ne_i] = '0'
                                maso_v(1)
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
                                maso_v(2)
                                spawn_resursa('lisa 75')
                        if 'wolf' in level_map[y + ne_i + 1][x - 1 + ne_i2]:
                            mob = level_map[y + ne_i + 1][x - 1 + ne_i2].split()
                            mob[1] = str(int(mob[1]) - yron)
                            level_map[y + ne_i + 1][x - 1 + ne_i2] = ' '.join(mob)
                            if int(level_map[y + ne_i + 1][x - 1 + ne_i2].split()[1]) < 0:
                                level_map[y + ne_i + 1][x - 1 + ne_i2] = '0'
                                maso_v(3)
                                spawn_resursa('wolf 150')
                        if 'zaiz' in level_map[y + ne_i + 1][x - 1 + ne_i2]:
                            mob = level_map[y + ne_i + 1][x - 1 + ne_i2].split()
                            mob[1] = str(int(mob[1]) - yron)
                            level_map[y + ne_i + 1][x - 1 + ne_i2] = ' '.join(mob)
                            if int(level_map[y + ne_i + 1][x - 1 + ne_i2].split()[1]) < 0:
                                level_map[y + ne_i + 1][x - 1 + ne_i2] = '0'
                                maso_v(1)
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
                                maso_v(2)
                                spawn_resursa('lisa 75')
                        if 'wolf' in level_map[y + ne_i2 - 1][x - 1 - ne_i]:
                            mob = level_map[y + ne_i2 - 1][x - 1 - ne_i].split()
                            mob[1] = str(int(mob[1]) - yron)
                            level_map[y + ne_i2 - 1][x - 1 - ne_i] = ' '.join(mob)
                            if int(level_map[y + ne_i2 - 1][x - 1 - ne_i].split()[1]) < 0:
                                level_map[y + ne_i2 - 1][x - 1 - ne_i] = '0'
                                maso_v(3)
                                spawn_resursa('wolf 150')
                        if 'zaiz' in level_map[y + ne_i2 - 1][x - 1 - ne_i]:
                            mob = level_map[y + ne_i2 - 1][x - 1 - ne_i].split()
                            mob[1] = str(int(mob[1]) - yron)
                            level_map[y + ne_i2 - 1][x - 1 - ne_i] = ' '.join(mob)
                            if int(level_map[y + ne_i2 - 1][x - 1 - ne_i].split()[1]) < 0:
                                level_map[y + ne_i2 - 1][x - 1 - ne_i] = '0'
                                maso_v(1)
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

        WIDTH, HEIGHT = 1280, 720

        tile_width = tile_height = 75
        pygame.init()

        inventar = inventar_skachivanie(self.file_name)

        screen = pygame.display.set_mode((1280, 720))
        # получение обьектов из памяти
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
            'block_ametist': load_image('block_ametist.png'),
            'chest': load_image('chest.png')
        }
        player_image = {
            'mar': load_image('mar.webp'),
            'pusto': load_image('pusto.png'),
            'drevesina': load_image('drevesina.png'),
            'kamen_inv': load_image('kamen_inv.png')
        }
        # основной персонаж
        # группы спрайтов
        kusti = []
        all_sprites = pygame.sprite.Group()
        tiles_group = pygame.sprite.Group()
        player_group = pygame.sprite.Group()
        camera = Camera()
        level_map = load_level(self.file_name.split('/')[-1])
        player, level_x, level_y = generate_level(load_level(self.file_name.split('/')[-1]))

        generate_level_kust(level_map)

        mir = 10
        # размеры мира
        if 100 > len(level_map) > 50:
            mir = 50
        elif 150 > len(level_map) > 100:
            mir = 100
        elif len(level_map) > 200:
            mir = 200

        clock = pygame.time.Clock()

        # FPS = 60
        running = True
        # start_screen()
        # y = 0
        # x = 0
        bb = 1
        obnovlenie = 0
        lomanie = 0
        spisok_koord_craft = []
        spisok_koord_chest = []
        # q1 = 0
        # w1 = 0
        # e1 = 0
        # r1 = 0
        # t1 = 0
        stavka_predmeta = []
        rezim_vstavka_bloca = 0
        sila = 0
        yron = 0
        obnovlenie_mobov = 0
        konez = 0

        kakoi_ikran = 0

        with open('nastroiki_mira/' + self.file_name.split('/')[-1], 'r') as nygno:
            lvl = nygno.read().split('%_%')

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                if event.type == pygame.KEYDOWN and konez == 0:
                    # кнопки на которые ходит персонаж
                    if event.key == pygame.K_UP:
                        move(player, 'up')
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
                    if event.key == pygame.K_F11:
                        if kakoi_ikran == 0:
                            screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
                            kakoi_ikran = 1
                        else:
                            screen = pygame.display.set_mode((1280, 720))
                            kakoi_ikran = 0
                if event.type == pygame.MOUSEBUTTONDOWN and konez == 0:
                    if event.button == 3:
                        f = 0
                        for i in range(9):
                            if 365 + (i + 1) * 50 < event.pos[0] < 366 + (
                                    i + 2) * 50 and 670 < event.pos[1] and f == 0:
                                if len(spisok_koord_chest) != 0:
                                    dobavlenie_predmeta_v_most_chest(inventar[i][1],
                                                                     int(inventar[i][2]), player)
                                inventar[i] = [str(i + 1), 'pusto', '0']

                    if rezim_vstavka_bloca == 0:
                        if event.button == 1:
                            lomanie += 1
                            dobicha(player)
                    if event.button == 1 and yron > 0:
                        yron_po(player)
                    if len(spisok_koord_chest) != 0:
                        f = 0
                        nomer = -1
                        for spi_koord in spisok_koord_chest:
                            nomer += 1
                            if 1130 < event.pos[0] < (spi_koord[0] + 1) + 1 and event.pos[1] < (spi_koord[
                                    1] + 1 + 50 * spi_koord[2]) + 1 and f == 0:
                                f = 1
                                dobavlenie_predmeta_v_most_inv(spisok_koord_chest[nomer][-2], spisok_koord_chest[nomer][-1], player, nomer, spisok_koord_chest[nomer][-3])
                    if len(spisok_koord_craft) != 0:
                        f = 0
                        for spi_koord in spisok_koord_craft:
                            if event.pos[0] < (spi_koord[0] + 1) * spi_koord[2] + 1 and event.pos[1] < (spi_koord[
                                    1] + 1) * spi_koord[2] + 1 and f == 0:
                                f = 1
                                # проверка какой предмет крафтится
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
                                elif spi_koord[3] == 'chest':
                                    craft_chest()
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
                    f = 0
                    for i in range(9):
                        if 365 + (i + 1) * 50 < event.pos[0] < 366 + (
                                    i + 2) * 50 and 670 < event.pos[1] and f == 0:
                            sila = 0
                            yron = 0
                            rezim_vstavka_bloca = 0
                            # проверка, на какой предмет нажали и включение соответствующего режима
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
                            elif 'chest' in inventar[i]:
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
                            else:
                                inventar[int(stavka_predmeta[0]) - 1] = [stavka_predmeta[0], 'pusto', '0']
                                rezim_vstavka_bloca = 0
                if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and konez == 1:
                    konez = 0
                    # перезапись, на пустой инвентарь
                    level2 = ['1 pusto 0%2 pusto 0%3 pusto 0%4 pusto 0%5 pusto 0%6 pusto 0%7 pusto 0%8 pusto 0%9 pusto 0%HP 100%food 100%cold 100']
                    inventar_spisok = []
                    for lev in level2:
                        inventar_spisok.extend(lev.split('%'))
                    inventar = []
                    for inv in inventar_spisok:
                        inventar.append(inv.split())
                    # if pygame.mouse.get_pressed()[0]:
                        # print(123)
            # all_sprites = pygame.sprite.Group()
            # tiles_group = pygame.sprite.Group()

            # level_x, level_y = generate_level2(level_map)

            screen.fill(pygame.Color('black'))
            obnovlenie += 1
            if obnovlenie == 270:
                # обновляет статы
                obnovlenie = 0
                if int(inventar[-1][1]) > 0:
                    inventar[-1][1] = str(int(inventar[-1][1]) - 1 * int(lvl[1]))
                else:
                    inventar[-3][1] = str(int(inventar[-3][1]) - 9 * int(lvl[1]))
                if koster_proverka(player) and int(inventar[-1][1]) < 100:
                    inventar[-1][1] = str(int(inventar[-1][1]) + 10)
                if int(inventar[-2][1]) > 75 and int(inventar[-1][1]) > 75:
                    inventar[-3][1] = str(int(inventar[-3][1]) + 10)
                if int(inventar[-2][1]) > 0:
                    inventar[-2][1] = str(int(inventar[-2][1]) - 3 * int(lvl[1]))
                else:
                    inventar[-3][1] = str(int(inventar[-3][1]) - 9 * int(lvl[1]))
            if len(kusti) != 0:
                # проверяет кусты, и выращивает на них ягоды
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
            spisok_koord_chest.clear()
            chest_proverka(player)
            craft_spawn()
            obnovlenie_mobov += 1
            if obnovlenie_mobov == 45:
                # двигает мобов
                yron_mobov(player)
                dvigenie_mobov(player)
                obnovlenie_mobov = 0
            if int(inventar[-3][1]) <= 0:
                # проверяет здоровье, и если оно ниже, то персонажем нельзя управлять и вещи теряются
                font = pygame.font.Font(None, 80)
                text = font.render(str('Вы погибли'), 1, (0, 0, 0))
                screen.blit(text, (380, 200))

                font = pygame.font.Font(None, 60)
                text = font.render(str('нажмите на любую клавишу, чтобы возрадится'), 1, (0, 0, 0))
                screen.blit(text, (280, 300))
                inventar[-3][1] = '-10000'
                konez = 1
                sila = 0
                yron = 0
                rezim_vstavka_bloca = 0
            pygame.display.flip()
            clock.tick(50)

            # сохранение мира
            maaaaap = ''
            for i in level_map:
                maaaaap += '\n' + '%'.join(i)
            maaaaap = maaaaap.split('\n')
            while len(maaaaap[0]) == 0:
                del maaaaap[0]
            maaaaap = '\n'.join(maaaaap)
            with open('mir/' + lvl[0] + '.txt', 'w') as f:
                f.write(''.join(maaaaap))

            inven = ''
            for i in inventar:
                for i2 in i:
                    inven += str(i2) + ' '
                inven = inven[:-1] + '%'
            with open('inventar/' + lvl[0] + '.txt', 'w') as f:
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
