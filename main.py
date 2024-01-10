import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QLCDNumber
from PyQt5.QtWidgets import QFileDialog
from sozdanie import Generachia
import pygame
import random
import os


class StarveSurvival(QWidget):
    def __init__(self):
        super().__init__()
        self.lvl = ['1234567', 2, 2]
        self.generachia = Generachia(self.lvl)
        self.setupUI()

    def setupUI(self):
        self.setGeometry(300, 150, 1280, 720)
        self.setWindowTitle('Starve survival')

        self.greetine = QLabel(self)
        self.greetine.move(0, 0)
        self.greetine.setText("Starve survival")

        self.calculate_button = QPushButton('Начать новую игру', self)
        self.calculate_button.move(150, 60)
        self.calculate_button.resize(290, 140)
        self.calculate_button.clicked.connect(self.start_new)

        self.calculate_button = QPushButton('Продолжить с сохранения', self)
        self.calculate_button.move(150, 260)
        self.calculate_button.resize(290, 40)
        self.calculate_button.clicked.connect(self.start_old)

        self.calculate_button = QPushButton('Выход из игры', self)
        self.calculate_button.move(150, 460)
        self.calculate_button.resize(290, 40)
        self.calculate_button.clicked.connect(self.vihod)

    def vihod(self):
        sys.exit()

    def start_new(self):
        self.generachia.show()

    def start_old(self):
        self.file_name = QFileDialog.getOpenFileName(self, 'Выбор сохранения', '')[0]

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
            filename = "data/" + filename
            # читаем уровень, убирая символы перевода строки
            with open(filename, 'r') as mapFile:
                level_map = [line.strip() for line in mapFile]
            # и подсчитываем максимальную длину
            level2 = level_map
            level_map = []
            for lev in level2:
                level_map.append(lev.split('$'))
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
                    elif level[y][x] == 's_d':
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
                    inventar_spisok.extend(lev.split('$'))
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

                elif 'HP' in i:
                    hp = int(i[1]) / 100
                    pygame.draw.rect(screen, (0, 0, 0), (415, 645, 150, 25))
                    pygame.draw.rect(screen, (255, 0, 0), (418, 648, int(144 * hp), 19))
                elif 'food' in i:
                    hp = int(i[1]) / 100
                    pygame.draw.rect(screen, (0, 0, 0), (565, 645, 150, 25))
                    # 72,6,7 - цвет болгарская роза
                    pygame.draw.rect(screen, (72, 6, 7), (568, 648, int(144 * hp), 19))
                elif 'cold' in i:
                    hp = int(i[1]) / 100
                    pygame.draw.rect(screen, (0, 0, 0), (715, 645, 150, 25))
                    # а 93 118 203 - Индиго Крайола
                    pygame.draw.rect(screen, (93, 118, 203), (718, 648, int(144 * hp), 19))

        def craft_spawn():
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
                elif 'diamond_inv' in i:
                    r1 += int(i[2])
                elif 'ametist_inv' in i:
                    t1 += int(i[2])
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
                    tile_width * pos_x + 15, tile_height * pos_y + 5)
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

        def dobicha(hero):
            x, y = hero.pos
            dobicha_nachati = 7
            if y > 0 and level_map[y - 1][x] != '0':
                if level_map[y - 1][x] == 'q' and lomanie == dobicha_nachati - sila:
                    level_map[y - 1][x] = '0'
                    dobicha_dereva()
                elif level_map[y - 1][x] == 'w' and lomanie == dobicha_nachati + 2 - sila and sila > 0:
                    level_map[y - 1][x] = '0'
                    dobicha_kamna()
                elif level_map[y - 1][x] == 'e' and lomanie == dobicha_nachati + 4 - sila and sila > 1:
                    level_map[y - 1][x] = '0'
                    dobicha_gold()
                elif level_map[y - 1][x] == 'r' and lomanie == dobicha_nachati + 6 - sila and sila > 2:
                    level_map[y - 1][x] = '0'
                    dobicha_diamond()
                elif level_map[y - 1][x] == 't' and lomanie == dobicha_nachati + 8 - sila and sila > 3:
                    level_map[y - 1][x] = '0'
                    dobicha_ametostov()
                for agods in range(6):
                    if 'kust ' + str(agods + 1) in level_map[y - 1][x]:
                        level_map[y - 1][x] = 'kust ' + str(agods) + ' ' + level_map[y - 1][x].split()[-1]
                        dobicha_agod()
            if y > 0 and level_map[y - 1][x + 1] != '0':
                if level_map[y - 1][x + 1] == 'q' and lomanie == dobicha_nachati - sila:
                    level_map[y - 1][x + 1] = '0'
                    dobicha_dereva()
                elif level_map[y - 1][x + 1] == 'w' and lomanie == dobicha_nachati + 2 - sila and sila > 0:
                    level_map[y - 1][x + 1] = '0'
                    dobicha_kamna()
                elif level_map[y - 1][x + 1] == 'e' and lomanie == dobicha_nachati + 4 - sila and sila > 1:
                    level_map[y - 1][x + 1] = '0'
                    dobicha_gold()
                elif level_map[y - 1][x + 1] == 'r' and lomanie == dobicha_nachati + 6 - sila and sila > 2:
                    level_map[y - 1][x + 1] = '0'
                    dobicha_diamond()
                elif level_map[y - 1][x + 1] == 't' and lomanie == dobicha_nachati + 8 - sila and sila > 3:
                    level_map[y - 1][x + 1] = '0'
                    dobicha_ametostov()
                for agods in range(6):
                    if 'kust ' + str(agods + 1) in level_map[y - 1][x + 1]:
                        level_map[y - 1][x + 1] = 'kust ' + str(agods) + ' ' + level_map[y - 1][x + 1].split()[-1]
                        dobicha_agod()
            if y > 0 and level_map[y][x - 1] != '0':
                if level_map[y][x - 1] == 'q' and lomanie == dobicha_nachati - sila:
                    level_map[y][x - 1] = '0'
                    dobicha_dereva()
                elif level_map[y][x - 1] == 'w' and lomanie == dobicha_nachati + 2 - sila and sila > 0:
                    level_map[y][x - 1] = '0'
                    dobicha_kamna()
                elif level_map[y][x - 1] == 'e' and lomanie == dobicha_nachati + 4 - sila and sila > 1:
                    level_map[y][x - 1] = '0'
                    dobicha_gold()
                elif level_map[y][x - 1] == 'r' and lomanie == dobicha_nachati + 6 - sila and sila > 2:
                    level_map[y][x - 1] = '0'
                    dobicha_diamond()
                elif level_map[y][x - 1] == 't' and lomanie == dobicha_nachati + 8 - sila and sila > 3:
                    level_map[y][x - 1] = '0'
                    dobicha_ametostov()
                for agods in range(6):
                    if 'kust ' + str(agods + 1) in level_map[y][x - 1]:
                        level_map[y][x - 1] = 'kust ' + str(agods) + ' ' + level_map[y][x - 1].split()[-1]
                        dobicha_agod()
            if y > 0 and level_map[y][x + 1] != '0':
                if level_map[y][x + 1] == 'q' and lomanie == dobicha_nachati - sila:
                    level_map[y][x + 1] = '0'
                    dobicha_dereva()
                elif level_map[y][x + 1] == 'w' and lomanie == dobicha_nachati + 2 - sila and sila > 0:
                    level_map[y][x + 1] = '0'
                    dobicha_kamna()
                elif level_map[y][x + 1] == 'e' and lomanie == dobicha_nachati + 4 - sila and sila > 1:
                    level_map[y][x + 1] = '0'
                    dobicha_gold()
                elif level_map[y][x + 1] == 'r' and lomanie == dobicha_nachati + 6 - sila and sila > 2:
                    level_map[y][x + 1] = '0'
                    dobicha_diamond()
                elif level_map[y][x + 1] == 't' and lomanie == dobicha_nachati + 8 - sila and sila > 3:
                    level_map[y][x + 1] = '0'
                    dobicha_ametostov()
                for agods in range(6):
                    if 'kust ' + str(agods + 1) in level_map[y][x + 1]:
                        level_map[y][x + 1] = 'kust ' + str(agods) + ' ' + level_map[y][x + 1].split()[-1]
                        dobicha_agod()
            if y > 0 and level_map[y + 1][x - 1] != '0':
                if level_map[y + 1][x - 1] == 'q' and lomanie == dobicha_nachati - sila:
                    level_map[y + 1][x - 1] = '0'
                    dobicha_dereva()
                elif level_map[y + 1][x - 1] == 'w' and lomanie == dobicha_nachati + 2 - sila and sila > 0:
                    level_map[y + 1][x - 1] = '0'
                    dobicha_kamna()
                elif level_map[y + 1][x - 1] == 'e' and lomanie == dobicha_nachati + 4 - sila and sila > 1:
                    level_map[y + 1][x - 1] = '0'
                    dobicha_gold()
                elif level_map[y + 1][x - 1] == 'r' and lomanie == dobicha_nachati + 6 - sila and sila > 2:
                    level_map[y + 1][x - 1] = '0'
                    dobicha_diamond()
                elif level_map[y + 1][x - 1] == 't' and lomanie == dobicha_nachati + 8 - sila and sila > 3:
                    level_map[y + 1][x - 1] = '0'
                    dobicha_ametostov()
                for agods in range(6):
                    if 'kust ' + str(agods + 1) in level_map[y + 1][x - 1]:
                        level_map[y + 1][x - 1] = 'kust ' + str(agods) + ' ' + level_map[y + 1][x - 1].split()[-1]
                        dobicha_agod()
            if y > 0 and level_map[y + 1][x] != '0':
                if level_map[y + 1][x] == 'q' and lomanie == dobicha_nachati - sila:
                    level_map[y + 1][x] = '0'
                    dobicha_dereva()
                elif level_map[y + 1][x] == 'w' and lomanie == dobicha_nachati + 2 - sila and sila > 0:
                    level_map[y + 1][x] = '0'
                    dobicha_kamna()
                elif level_map[y + 1][x] == 'e' and lomanie == dobicha_nachati + 4 - sila and sila > 1:
                    level_map[y + 1][x] = '0'
                    dobicha_gold()
                elif level_map[y + 1][x] == 'r' and lomanie == dobicha_nachati + 6 - sila and sila > 2:
                    level_map[y + 1][x] = '0'
                    dobicha_diamond()
                elif level_map[y + 1][x] == 't' and lomanie == dobicha_nachati + 8 - sila and sila > 3:
                    level_map[y + 1][x] = '0'
                    dobicha_ametostov()
                for agods in range(6):
                    if 'kust ' + str(agods + 1) in level_map[y + 1][x]:
                        level_map[y + 1][x] = 'kust ' + str(agods) + ' ' + level_map[y + 1][x].split()[-1]
                        dobicha_agod()
            if y > 0 and level_map[y + 1][x + 1] != '0':
                if level_map[y + 1][x + 1] == 'q' and lomanie == dobicha_nachati - sila:
                    level_map[y + 1][x + 1] = '0'
                    dobicha_dereva()
                elif level_map[y + 1][x + 1] == 'w' and lomanie == dobicha_nachati + 2 - sila and sila > 0:
                    level_map[y + 1][x + 1] = '0'
                    dobicha_kamna()
                elif level_map[y + 1][x + 1] == 'e' and lomanie == dobicha_nachati + 4 - sila and sila > 1:
                    level_map[y + 1][x + 1] = '0'
                    dobicha_gold()
                elif level_map[y + 1][x + 1] == 'r' and lomanie == dobicha_nachati + 6 - sila and sila > 2:
                    level_map[y + 1][x + 1] = '0'
                    dobicha_diamond()
                elif level_map[y + 1][x + 1] == 't' and lomanie == dobicha_nachati + 8 - sila and sila > 3:
                    level_map[y + 1][x + 1] = '0'
                    dobicha_ametostov()
                for agods in range(6):
                    if 'kust ' + str(agods + 1) in level_map[y + 1][x + 1]:
                        level_map[y + 1][x + 1] = 'kust ' + str(agods) + ' ' + level_map[y + 1][x + 1].split()[-1]
                        dobicha_agod()
            if y > 0 and level_map[y - 1][x - 1] != '0':
                if level_map[y - 1][x - 1] == 'q' and lomanie == dobicha_nachati - sila:
                    level_map[y - 1][x - 1] = '0'
                    dobicha_dereva()
                elif level_map[y - 1][x - 1] == 'w' and lomanie == dobicha_nachati + 2 - sila and sila > 0:
                    level_map[y - 1][x - 1] = '0'
                    dobicha_kamna()
                elif level_map[y - 1][x - 1] == 'e' and lomanie == dobicha_nachati + 4 - sila and sila > 1:
                    level_map[y - 1][x - 1] = '0'
                    dobicha_gold()
                elif level_map[y - 1][x - 1] == 'r' and lomanie == dobicha_nachati + 6 - sila and sila > 2:
                    level_map[y - 1][x - 1] = '0'
                    dobicha_diamond()
                elif level_map[y - 1][x - 1] == 't' and lomanie == dobicha_nachati + 8 - sila and sila > 3:
                    level_map[y - 1][x - 1] = '0'
                    dobicha_ametostov()
                for agods in range(6):
                    if 'kust ' + str(agods + 1) in level_map[y - 1][x - 1]:
                        level_map[y - 1][x - 1] = 'kust ' + str(agods) + ' ' + level_map[y - 1][x - 1].split()[-1]
                        dobicha_agod()
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
                self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2 - 27)
                self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)

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
                elif 'kamen_inv' in i:
                    w1 += int(i[2])
            q1 -= 30
            for inv in inventar:
                if 'drevesina' in inv:
                    # and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355
                    if 0 < q1 < 356:
                        inventar[int(inv[0]) - 1][2] = q1
                        q1 = 0
                    elif q1 >= 356:
                        inventar[int(inv[0]) - 1][2] = 355
                        q1 -= 355
                    else:
                        inventar[int(inv[0]) - 1] = [inv[0], 'pusto', '0']

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
                elif 'kamen_inv' in i:
                    w1 += int(i[2])
            q1 -= 50
            for inv in inventar:
                if 'drevesina' in inv:
                    # and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355
                    if 0 < q1 < 356:
                        inventar[int(inv[0]) - 1][2] = q1
                        q1 = 0
                    elif q1 >= 356:
                        inventar[int(inv[0]) - 1][2] = 355
                        q1 -= 355
                    else:
                        inventar[int(inv[0]) - 1] = [inv[0], 'pusto', '0']

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
            for inv in inventar:
                if 'drevesina' in inv:
                    # and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355
                    if 0 < q1 < 356:
                        inventar[int(inv[0]) - 1][2] = q1
                        q1 = 0
                    elif q1 >= 356:
                        inventar[int(inv[0]) - 1][2] = 355
                        q1 -= 355
                    else:
                        inventar[int(inv[0]) - 1] = [inv[0], 'pusto', '0']

        def craft_verstak():
            dob = 0
            for inv in inventar:
                if 'verstak' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'verstak'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 2
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
            for inv in inventar:
                if 'drevesina' in inv:
                    # and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355
                    if 0 < q1 < 356:
                        inventar[int(inv[0]) - 1][2] = q1
                        q1 = 0
                    elif q1 >= 356:
                        inventar[int(inv[0]) - 1][2] = 355
                        q1 -= 355
                    else:
                        inventar[int(inv[0]) - 1] = [inv[0], 'pusto', '0']
                if 'kamen' in inv:
                    # and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355
                    if 0 < w1 < 356:
                        inventar[int(inv[0]) - 1][2] = w1
                        w1 = 0
                    elif w1 >= 356:
                        inventar[int(inv[0]) - 1][2] = 355
                        w1 -= 355
                    else:
                        inventar[int(inv[0]) - 1] = [inv[0], 'pusto', '0']

        def craft_koster():
            dob = 0
            for inv in inventar:
                if 'koster' in inv and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355:
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 1
                    dob = 1
            for inv in inventar:
                if 'pusto' in inv and dob != 1:
                    inventar[int(inv[0]) - 1][1] = 'koster'
                    inventar[int(inv[0]) - 1][2] = int(inv[2]) + 2
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
            for inv in inventar:
                if 'drevesina' in inv:
                    # and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355
                    if 0 < q1 < 356:
                        inventar[int(inv[0]) - 1][2] = q1
                        q1 = 0
                    elif q1 >= 356:
                        inventar[int(inv[0]) - 1][2] = 355
                        q1 -= 355
                    else:
                        inventar[int(inv[0]) - 1] = [inv[0], 'pusto', '0']
                if 'kamen' in inv:
                    # and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355
                    if 0 < w1 < 356:
                        inventar[int(inv[0]) - 1][2] = w1
                        w1 = 0
                    elif w1 >= 356:
                        inventar[int(inv[0]) - 1][2] = 355
                        w1 -= 355
                    else:
                        inventar[int(inv[0]) - 1] = [inv[0], 'pusto', '0']

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
            for inv in inventar:
                if 'drevesina' in inv:
                    # and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355
                    if 0 < q1 < 356:
                        inventar[int(inv[0]) - 1][2] = q1
                        q1 = 0
                    elif q1 >= 356:
                        inventar[int(inv[0]) - 1][2] = 355
                        q1 -= 355
                    else:
                        inventar[int(inv[0]) - 1] = [inv[0], 'pusto', '0']
                if 'kamen' in inv:
                    # and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355
                    if 0 < w1 < 356:
                        inventar[int(inv[0]) - 1][2] = w1
                        w1 = 0
                    elif w1 >= 356:
                        inventar[int(inv[0]) - 1][2] = 355
                        w1 -= 355
                    else:
                        inventar[int(inv[0]) - 1] = [inv[0], 'pusto', '0']

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
            for inv in inventar:
                if 'drevesina' in inv:
                    # and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355
                    if 0 < q1 < 356:
                        inventar[int(inv[0]) - 1][2] = q1
                        q1 = 0
                    elif q1 >= 356:
                        inventar[int(inv[0]) - 1][2] = 355
                        q1 -= 355
                    else:
                        inventar[int(inv[0]) - 1] = [inv[0], 'pusto', '0']
                if 'kamen' in inv:
                    # and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355
                    if 0 < w1 < 356:
                        inventar[int(inv[0]) - 1][2] = w1
                        w1 = 0
                    elif w1 >= 356:
                        inventar[int(inv[0]) - 1][2] = 355
                        w1 -= 355
                    else:
                        inventar[int(inv[0]) - 1] = [inv[0], 'pusto', '0']
                if 'gold_inv' in inv:
                    # and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355
                    if 0 < e1 < 356:
                        inventar[int(inv[0]) - 1][2] = e1
                        e1 = 0
                    elif e1 >= 356:
                        inventar[int(inv[0]) - 1][2] = 355
                        e1 -= 355
                    else:
                        inventar[int(inv[0]) - 1] = [inv[0], 'pusto', '0']

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
            for inv in inventar:
                if 'diamond_inv' in inv:
                    # and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355
                    if 0 < r1 < 356:
                        inventar[int(inv[0]) - 1][2] = r1
                        r1 = 0
                    elif r1 >= 356:
                        inventar[int(inv[0]) - 1][2] = 355
                        r1 -= 355
                    else:
                        inventar[int(inv[0]) - 1] = [inv[0], 'pusto', '0']
                if 'kamen' in inv:
                    # and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355
                    if 0 < w1 < 356:
                        inventar[int(inv[0]) - 1][2] = w1
                        w1 = 0
                    elif w1 >= 356:
                        inventar[int(inv[0]) - 1][2] = 355
                        w1 -= 355
                    else:
                        inventar[int(inv[0]) - 1] = [inv[0], 'pusto', '0']
                if 'gold_inv' in inv:
                    # and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355
                    if 0 < e1 < 356:
                        inventar[int(inv[0]) - 1][2] = e1
                        e1 = 0
                    elif e1 >= 356:
                        inventar[int(inv[0]) - 1][2] = 355
                        e1 -= 355
                    else:
                        inventar[int(inv[0]) - 1] = [inv[0], 'pusto', '0']

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
            for inv in inventar:
                if 'diamond_inv' in inv:
                    # and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355
                    if 0 < r1 < 356:
                        inventar[int(inv[0]) - 1][2] = r1
                        r1 = 0
                    elif r1 >= 356:
                        inventar[int(inv[0]) - 1][2] = 355
                        r1 -= 355
                    else:
                        inventar[int(inv[0]) - 1] = [inv[0], 'pusto', '0']
                if 'ametist_inv' in inv:
                    # and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355
                    if 0 < t1 < 356:
                        inventar[int(inv[0]) - 1][2] = t1
                        t1 = 0
                    elif t1 >= 356:
                        inventar[int(inv[0]) - 1][2] = 355
                        t1 -= 355
                    else:
                        inventar[int(inv[0]) - 1] = [inv[0], 'pusto', '0']
                if 'gold_inv' in inv:
                    # and dob != 1 and int(inventar[int(inv[0]) - 1][2]) < 355
                    if 0 < e1 < 356:
                        inventar[int(inv[0]) - 1][2] = e1
                        e1 = 0
                    elif e1 >= 356:
                        inventar[int(inv[0]) - 1][2] = 355
                        e1 -= 355
                    else:
                        inventar[int(inv[0]) - 1] = [inv[0], 'pusto', '0']

        def stavka_bloka_vkl():
            print('режим вкл')

        def stavka_bloca(hero):
            x, y = hero.pos
            block = ''
            if 'stena_derevo' in stavka_predmeta:
                block = 's_d'
            elif 'verstak' in stavka_predmeta:
                block = 'verstak'
            elif 'koster' in stavka_predmeta:
                block = 'koster'
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
                        # доделать
                        dvig = 0
                        if x - 4 < x + x_d - 9 < x and level_map[y + y_d - 5][x + x_d - 8] == '0' and \
                                dvig_1 != x + x_d - 9 and dvig_2 != y + y_d - 5:
                            level_map[y + y_d - 5][x + x_d - 8] = level_map[y + y_d - 5][x + x_d - 9]
                            level_map[y + y_d - 5][x + x_d - 9] = '0'
                            dvig = 1
                            dvig_1 = x + x_d - 8
                            dvig_2 = y + y_d - 5
                            print(123)
                        elif x + 4 > x + x_d - 9 > x and level_map[y + y_d - 5][x + x_d - 10] == '0' and \
                                dvig_1 != x + x_d - 9 and dvig_2 != y + y_d - 5:
                            level_map[y + y_d - 5][x + x_d - 10] = level_map[y + y_d - 5][x + x_d - 9]
                            level_map[y + y_d - 5][x + x_d - 9] = '0'
                            dvig = 1
                            dvig_1 = x + x_d - 10
                            dvig_2 = y + y_d - 5
                            print(345)
                        elif y + 4 > y + y_d - 5 >= y and level_map[y + y_d - 6][x + x_d - 9] == '0' and \
                                dvig_1 != x + x_d - 9 and dvig_2 != y + y_d - 5:
                            level_map[y + y_d - 6][x + x_d - 9] = level_map[y + y_d - 5][x + x_d - 9]
                            level_map[y + y_d - 5][x + x_d - 9] = '0'
                            dvig = 1
                            dvig_1 = x + x_d - 9
                            dvig_2 = y + y_d - 6
                            print(789)
                        elif y - 4 < y + y_d - 5 <= y and level_map[y + y_d - 4][x + x_d - 9] == '0' and \
                                dvig_1 != x + x_d - 9 and dvig_2 != y + y_d - 5:
                            level_map[y + y_d - 4][x + x_d - 9] = level_map[y + y_d - 5][x + x_d - 9]
                            level_map[y + y_d - 5][x + x_d - 9] = '0'
                            dvig = 1
                            dvig_1 = x + x_d - 9
                            dvig_2 = y + y_d - 4
                            print(999)
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
                        # доделать
                        dvig = 0
                        if x - 4 < x + x_d - 9 < x and level_map[y + y_d - 5][x + x_d - 8] == '0' and \
                                dvig_1 != x + x_d - 9 and dvig_2 != y + y_d - 5:
                            level_map[y + y_d - 5][x + x_d - 8] = level_map[y + y_d - 5][x + x_d - 9]
                            level_map[y + y_d - 5][x + x_d - 9] = '0'
                            dvig = 1
                            dvig_1 = x + x_d - 8
                            dvig_2 = y + y_d - 5
                            print(123)
                        elif x + 4 > x + x_d - 9 > x and level_map[y + y_d - 5][x + x_d - 10] == '0' and \
                                dvig_1 != x + x_d - 9 and dvig_2 != y + y_d - 5:
                            level_map[y + y_d - 5][x + x_d - 10] = level_map[y + y_d - 5][x + x_d - 9]
                            level_map[y + y_d - 5][x + x_d - 9] = '0'
                            dvig = 1
                            dvig_1 = x + x_d - 10
                            dvig_2 = y + y_d - 5
                            print(345)
                        elif y + 4 > y + y_d - 5 >= y and level_map[y + y_d - 6][x + x_d - 9] == '0' and \
                                dvig_1 != x + x_d - 9 and dvig_2 != y + y_d - 5:
                            level_map[y + y_d - 6][x + x_d - 9] = level_map[y + y_d - 5][x + x_d - 9]
                            level_map[y + y_d - 5][x + x_d - 9] = '0'
                            dvig = 1
                            dvig_1 = x + x_d - 9
                            dvig_2 = y + y_d - 6
                            print(789)
                        elif y - 4 < y + y_d - 5 <= y and level_map[y + y_d - 4][x + x_d - 9] == '0' and \
                                dvig_1 != x + x_d - 9 and dvig_2 != y + y_d - 5:
                            level_map[y + y_d - 4][x + x_d - 9] = level_map[y + y_d - 5][x + x_d - 9]
                            level_map[y + y_d - 5][x + x_d - 9] = '0'
                            dvig = 1
                            dvig_1 = x + x_d - 9
                            dvig_2 = y + y_d - 4
                            print(999)
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


        def yron_po(player):
            x, y = player.pos
            print(123)


        with open(self.file_name, 'r') as f:
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
                'voda': load_image('voda.png')
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
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
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
                    if event.type == pygame.MOUSEBUTTONDOWN:
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


                                        # 365 + (int(i[0]) * 50), 670
                        f = 0
                        for i in range(9):
                            if 365 + (i + 1) * 50 < event.pos[0] < 366 + (
                                        i + 2) * 50 and 670 < event.pos[1] and f == 0:
                                sila = 0
                                yron = 0
                                if 'stena_derevo' in inventar[i]:
                                    stavka_predmeta = inventar[i]
                                    stavka_bloka_vkl()
                                    if rezim_vstavka_bloca == 1:
                                        rezim_vstavka_bloca = 0
                                    else:
                                        rezim_vstavka_bloca = 1
                                elif 'kirka_derevo' in inventar[i]:
                                    sila = 1
                                elif 'verstak' in inventar[i]:
                                    stavka_predmeta = inventar[i]
                                    stavka_bloka_vkl()
                                    if rezim_vstavka_bloca == 1:
                                        rezim_vstavka_bloca = 0
                                    else:
                                        rezim_vstavka_bloca = 1
                                elif 'koster' in inventar[i]:
                                    stavka_predmeta = inventar[i]
                                    stavka_bloka_vkl()
                                    if rezim_vstavka_bloca == 1:
                                        rezim_vstavka_bloca = 0
                                    else:
                                        rezim_vstavka_bloca = 1
                                elif 'kirka_kamen' in inventar[i]:
                                    sila = 2
                                elif 'kirka_gold' in inventar[i]:
                                    sila = 3
                                elif 'kirka_diamond' in inventar[i]:
                                    sila = 4
                                elif 'kirka_derevo' in inventar[i]:
                                    sila = 5
                                elif 'mech_derevo' in inventar[i]:
                                    yron = 1
                                elif 'agoda' in inventar[i]:
                                    if int(inventar[-2][1]) < int(101):
                                        inventar[-2][1] = str(int(inventar[-2][1]) + 10)
                                    inventar[i][2] = str(int(inventar[i][2]) - 1)
                                    if inventar[i][2] == '0':
                                        inventar[i][1] = 'pusto'
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
                        if int(inventar[-3][1]) <= 0:
                            print("проигрыш")
                    if koster_proverka(player) and int(inventar[-1][1]) < 100:
                        inventar[-1][1] = str(int(inventar[-1][1]) + 10)
                    if int(inventar[-2][1]) > 75 and int(inventar[-1][1]) > 75:
                        inventar[-3][1] = str(int(inventar[-3][1]) + 10)
                    if int(inventar[-2][1]) > 0:
                        inventar[-2][1] = str(int(inventar[-2][1]) - 3)
                    else:
                        inventar[-3][1] = str(int(inventar[-3][1]) - 9)
                        if int(inventar[-3][1]) <= 0:
                            print("проигрыш")
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
                inventar_spawn()
                craft_spawn()
                obnovlenie_mobov += 1
                if obnovlenie_mobov == 90:
                    yron_mobov(player)
                    dvigenie_mobov(player)
                    obnovlenie_mobov = 0
                pygame.display.flip()
                clock.tick(50)
            pygame.quit()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = StarveSurvival()
    example.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
