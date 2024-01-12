# Импортируем библиотеку pygame
import pygame
import os
import sys
# Импортируем библиотеку random для случайного выбора карт и перемешивания колоды
from random import shuffle, choice
# Импортируем библиотеку time Для создания пауз во время игры
import time
# Импортируем tkinter для всплывающих сообщениях о завершении игры
from tkinter import Tk
from tkinter import messagebox
# Импортируем для записи результата игры в базу данных
import sqlite3
# Импортируем datetime для получения текущей даты при записи результата
import datetime
# Импортируем модули необходимые нам для создания стартового приложения с необходимыми настройками
from PyQt5.QtWidgets import QApplication, QWidget
import io
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QImage


# Пользовательский интерфейс для приложения с предварительными настройками
settings_app_template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>587</width>
    <height>531</height>
   </rect>
  </property>
  <property name="font">
   <font>
    <family>Times New Roman</family>
   </font>
  </property>
  <property name="windowTitle">
   <string>Настройки игры</string>
  </property>
  <widget class="QPushButton" name="start_button">
   <property name="geometry">
    <rect>
     <x>370</x>
     <y>470</y>
     <width>181</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Times New Roman</family>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Начать игру</string>
   </property>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>10</y>
     <width>191</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Times New Roman</family>
     <pointsize>18</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Количество карт:</string>
   </property>
  </widget>
  <widget class="QWidget" name="horizontalLayoutWidget">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>40</y>
     <width>371</width>
     <height>31</height>
    </rect>
   </property>
   <layout class="QHBoxLayout" name="horizontalLayout">
    <item>
     <widget class="QRadioButton" name="cards24">
      <property name="font">
       <font>
        <family>Times New Roman</family>
        <pointsize>14</pointsize>
       </font>
      </property>
      <property name="text">
       <string>24</string>
      </property>
      <attribute name="buttonGroup">
       <string notr="true">count_group</string>
      </attribute>
     </widget>
    </item>
    <item>
     <widget class="QRadioButton" name="cards36">
      <property name="font">
       <font>
        <family>Times New Roman</family>
        <pointsize>14</pointsize>
       </font>
      </property>
      <property name="text">
       <string>36</string>
      </property>
      <property name="checked">
       <bool>true</bool>
      </property>
      <attribute name="buttonGroup">
       <string notr="true">count_group</string>
      </attribute>
     </widget>
    </item>
    <item>
     <widget class="QRadioButton" name="cards52">
      <property name="font">
       <font>
        <family>Times New Roman</family>
        <pointsize>14</pointsize>
       </font>
      </property>
      <property name="text">
       <string>52</string>
      </property>
      <attribute name="buttonGroup">
       <string notr="true">count_group</string>
      </attribute>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QLabel" name="label_2">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>80</y>
     <width>241</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Times New Roman</family>
     <pointsize>18</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Тема карт:</string>
   </property>
  </widget>
  <widget class="QWidget" name="gridLayoutWidget">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>110</y>
     <width>211</width>
     <height>181</height>
    </rect>
   </property>
   <layout class="QGridLayout" name="gridLayout">
    <item row="1" column="0">
     <widget class="QRadioButton" name="theme1">
      <property name="font">
       <font>
        <family>Times New Roman</family>
        <pointsize>14</pointsize>
       </font>
      </property>
      <property name="text">
       <string>Тема 1</string>
      </property>
      <attribute name="buttonGroup">
       <string notr="true">themes_group</string>
      </attribute>
     </widget>
    </item>
    <item row="0" column="0">
     <widget class="QLabel" name="theme_1">
      <property name="text">
       <string/>
      </property>
     </widget>
    </item>
    <item row="1" column="1">
     <widget class="QRadioButton" name="theme2">
      <property name="font">
       <font>
        <family>Times New Roman</family>
        <pointsize>14</pointsize>
       </font>
      </property>
      <property name="text">
       <string>Тема 2</string>
      </property>
      <property name="checked">
       <bool>true</bool>
      </property>
      <attribute name="buttonGroup">
       <string notr="true">themes_group</string>
      </attribute>
     </widget>
    </item>
    <item row="0" column="1">
     <widget class="QLabel" name="theme_2">
      <property name="text">
       <string/>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QWidget" name="gridLayoutWidget_2">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>340</y>
     <width>211</width>
     <height>181</height>
    </rect>
   </property>
   <layout class="QGridLayout" name="gridLayout_2">
    <item row="0" column="0">
     <widget class="QLabel" name="shirt_1">
      <property name="text">
       <string/>
      </property>
     </widget>
    </item>
    <item row="0" column="1">
     <widget class="QLabel" name="shirt_2">
      <property name="text">
       <string/>
      </property>
     </widget>
    </item>
    <item row="1" column="0">
     <widget class="QRadioButton" name="shirt1">
      <property name="font">
       <font>
        <family>Times New Roman</family>
        <pointsize>14</pointsize>
       </font>
      </property>
      <property name="text">
       <string>Рубашка 1</string>
      </property>
      <attribute name="buttonGroup">
       <string notr="true">shirt_group</string>
      </attribute>
     </widget>
    </item>
    <item row="1" column="1">
     <widget class="QRadioButton" name="shirt2">
      <property name="font">
       <font>
        <family>Times New Roman</family>
        <pointsize>14</pointsize>
       </font>
      </property>
      <property name="text">
       <string>Рубашка 2</string>
      </property>
      <property name="checked">
       <bool>true</bool>
      </property>
      <attribute name="buttonGroup">
       <string notr="true">shirt_group</string>
      </attribute>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QLabel" name="label_7">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>300</y>
     <width>181</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Times New Roman</family>
     <pointsize>18</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Тема рубашек</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
 <buttongroups>
  <buttongroup name="count_group"/>
  <buttongroup name="shirt_group"/>
  <buttongroup name="themes_group"/>
 </buttongroups>
</ui>
"""


# Класс каждой карты
class Card:
    # Инициализация класса
    def __init__(self, suit, value, image, is_active=True):
        # Значение карты
        self.value = value
        # Масть карты
        self.suit = suit
        # Фото для карты
        self.image_path = image
        self.is_active = is_active
        # Статус движения карты
        self.is_moving = False

    # Метод установления статуса карты активной или неактивной
    def set_active(self, active):
        self.is_active = active

    # Метод установления статуса движения карты
    def set_move(self, move_status):
        self.is_moving = move_status

    # Сравнения больше
    def __gt__(self, other, trump):
        # Если карта козырная она отбивает некозырную
        if self.suit == trump.suit and self.suit != other.suit:
            return True
        else:
            # Если масть карт совпадает
            if self.suit == other.suit:
                return VALUES.index(self.value) > VALUES.index(other.value)
            # Иначе картой нельзя отбить другую
            else:
                return False

    # Сравнение меньше
    def __lt__(self, other):
        if self.suit == other.suit:
            return VALUES.index(self.value) < VALUES.index(other.value)
        else:
            return False
        
    def __repr__(self):
        return f"{self.value}{self.suit}"
    

# Класс игрового поле
class Table(pygame.sprite.Sprite):
    # Инициализация класса
    def __init__(self, cell_size: tuple, size: tuple):
        # Наследуем спрайты
        pygame.sprite.Sprite.__init__(self)
        # Размеры ячейки
        self.cell_width, self.cell_height = cell_size
        # Размеры стола
        self.width, self.height = size
        # Количество ячеек
        self.cell_count = 6
        # Словарь карт где ключ - карта атакающая а значение - защищающая
        self.cards = {}
        # Создаем список стола в который будем добавлять путсые ячейки
        self.table = []
        # В цикле создаем 6 ячеек для карт
        for card in range(self.cell_count):
            # Координаты ячейки для карты
            x = 17 * vw + card * (7 * vw + 4 * vw)
            # Верхний отступ
            y = 20 * vw
            # Ширина и высота ячеек
            width = self.cell_width
            height = self.cell_height
            # Создаем обьект класса ячейки
            cell = Cell(card, x, y, width, height, CELL)
            # Добавляем ячейку в список ячеек
            self.table.append(cell)
            # Добавляем ячеку в группу спрайтов
            sprites.add(cell)

    # Метод очистки стола от карт
    def clear_table(self):
        cds = self.cards.copy()
        # Если у бота есть сообщение
        if bot.msg:
            # Удаляем из спрайтов это сообщение
            sprites.remove(bot.msg)
            bot.msg = False
        # Очищаем словарь значений карт поля
        self.cards.clear()
        # Удаляем из спрайтов объекты ячеек карт
        sprites.remove(self.table)
        # Очищаем список карт на столе
        self.table.clear()
        # В цикле проходимся до 6 и отрисовываем 6 новых пустых ячеек
        for card in range(self.cell_count):
            # Координаты ячейки для карты
            # Левый отступ + номер ячейки * (ширину ячейки + отступ)
            x = 17 * vw + card * (7 * vw + 4 * vw)
            # Верхний отступ
            y = 20 * vw
            # Ширина и высота ячеек
            width = self.cell_width
            height = self.cell_height
            # Создаем обьект класса ячейки
            cell = Cell(card, x, y, width, height, CELL)
            # Добавляем ячейку в список ячеек
            self.table.append(cell)
            # Добавляем ячеку в группу спрайтов
            sprites.add(cell)
        DECK.update()
        if bot.action_information:
            info = bot.action_information
            bot.action_information = False
        else:
            info = '-'
        steps.append([GAME_NUMBER, cds, bot.inventory.copy(), player.inventory.copy(), info])

    # Метод устаноки карты защищающегося на поле
    def set_deffend_card(self, bot_card: Card, table_card: Card):
        # Определяем ячейку карты которую будем перерисовывать и добавлять поверх карту
        attack_cardcell = [card for card in self.table if card.card == table_card][0]
        # Получаем номер ячейки карты
        card = attack_cardcell.index
        # Координата отбивающей карты
        x = attack_cardcell.x + 40
        y = attack_cardcell.y + 40
        # Размеры отбивающей карты
        width = self.cell_width
        height = self.cell_height
        # Создаем обьект класса ячейки
        cell = Cell(card, x, y, width, height, CELL)
        # Устанавливаем статус ячейки как защищающая
        cell.is_deffender = True
        # Устанавливаем карту для новой ячейки
        cell.set_card(bot_card)
        # Добавляем ячейку в список ячеек
        self.table.append(cell)
        # Добавляем ячеку в группу спрайтов
        sprites.add(cell)
        
    # Метод устаноки карты атакающего на поле
    def set_attack_card(self, bot_card: Card):
        # Добавляем в словарь по ключу положенной в ячейку карты пустое значение чтобы потом отбить эту карту
        self.cards[bot_card] = False
        # Проходимся в цикле по картам стола
        for card in self.table:
            # Если у ячейки стола нет карты отбивающей устанавливаем ее
            if not card.card:
                card.set_card(bot_card)
                # Прерываем цикл чтобы не установить одну и ту же карту на несколько других
                break

    # Метод проверки стола на завершение хода
    def check_table(self):
        # возвращаем у всех ли карт есть пара
        return all([True for card in self.cards if self.cards[card]])
    
    # Метод проверки стола на возможность положить карту
    def can_put_card(self, card: Card):
        # Если атакует пользователь
        if not bot.attack_status:
            # Если карт на столе еще нет возвращаем True
            if not self.cards:
                return True
            # Если на столе карт больше чем может взять ии запрещаем взять в руки карту
            if not bot.otbitie:
                if len([card for card in self.cards if not self.cards[card]]) == len(bot.inventory):
                    return False
            for cell in [card for card in self.table if card.card]:
                if cell.card.value == card.value:
                    return True
            return False
        # Если пользователь защищается
        else:
            # Проходим в цикле по картам стола
            for table_card in [card for card in list(table.cards.keys()) if not table.cards[card]]:
                # Если карта может отбить по правилам игры
                if card.__gt__(table_card, DECK.trump):
                    return True
            return False

     
# Класс ячейки на столе
class Cell(pygame.sprite.Sprite):
    def __init__(self, index, x, y, width, height, cell_color: tuple):
        # Наследуем спрайты
        pygame.sprite.Sprite.__init__(self)
        # Номер ячейки на столе
        self.index = index
        # Координаты ячейки по x и по y 
        self.x = x
        self.y = y
        # Цвет ячейки
        self.cell_color = cell_color
        # Ширина и высота ячейки
        self.width = width
        self.height = height
        # Наличие карты в ячейке
        self.card = False
        # Рисуем ячейку
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        # Устанавливаем положение ячейки
        self.rect.topleft = (self.x, self.y)
        # Статус защищающей карты
        self.is_deffender = False
    
    def update(self):
        # Если у ячейки есть карта то загружаем ее в ячейку
        if self.card:
            # ! Осуществить заполнение ячейки картинкой карты
            image = pygame.image.load(CARDS_PATH + self.card.image_path)
            image = pygame.transform.scale(image, (7 * vw, 10.5 * vw))
            self.image.blit(image, (0, 0))
        # Если нет карты
        else:
            self.image.fill(self.cell_color)
    
    # Метод установки карты
    def set_card(self, card):
        self.card = card


# Класс ячейки карты
class CardCell(pygame.sprite.Sprite):
    def __init__(self, size: tuple, coord: tuple, image_path: str, card: Card, step: int = False):
        # Наследуем спрайты
        pygame.sprite.Sprite.__init__(self)
        # Карта принадлежащая данной ячейке
        self.parent_card = card
        # Картинка этой карты
        self.image_path = image_path
        # Размеры ячейки
        self.width, self.height = size
        self.x, self.y = coord
        # шаг расположения карт
        self.step = step
        # Статус карты
        self.active = False
        # Загружаем изображение карты и изменяем его размер
        self.card = pygame.image.load(self.image_path)
        self.card = pygame.transform.scale(self.card, (self.width, self.height))
        # Если шаг меньше ширины карты
        if self.step < self.width:
            # Если карта в инвентаре не последняя то ее обрезаем и если
            if self.parent_card in player.inventory:
                if player.inventory.index(self.parent_card) != len(player.inventory) - 1:
                    # Создаем базу для отрисовывания нашего элемента
                    self.image = pygame.Surface((self.step, self.height))
                    # Помещаем картинку карты в ячейку
                    self.image.blit(self.card, (0, 0), (0, 0, self.step, self.height))
                # Иначе помещаем полностью
                else:
                    # Создаем базу для отрисовывания нашего элемента
                    self.image = pygame.Surface((self.width, self.height))
                    # Помещаем картинку карты в ячейку
                    self.image.blit(self.card, (0, 0))
            else:
                if bot.inventory.index(self.parent_card) != len(bot.inventory) - 1:
                    # Создаем базу для отрисовывания нашего элемента
                    self.image = pygame.Surface((self.step, self.height))
                    # Помещаем картинку карты в ячейку
                    self.image.blit(self.card, (0, 0), (0, 0, self.step, self.height))
                # Иначе помещаем полностью
                else:
                    # Создаем базу для отрисовывания нашего элемента
                    self.image = pygame.Surface((self.width, self.height))
                    # Помещаем картинку карты в ячейку
                    self.image.blit(self.card, (0, 0))
            # Создаем прямоугольник нашей карты
            self.rect = self.image.get_rect()
            # Перемещаем элемент на координату
            self.rect.topleft = (self.x, self.y)
        # Если шаг больше ширины карты
        else:
            # Создаем базу для отрисовывания нашего элемента
            self.image = pygame.Surface((self.width, self.height))
            # Создаем прямоугольник нашей карты
            self.rect = self.image.get_rect()
            # Перемещаем элемент на координату
            self.rect.topleft = (self.x, self.y)
            # Перемещаем элемент на координату
            self.rect.topleft = (self.x, self.y)
            # Помещаем картинку карты в ячейку
            self.image.blit(self.card, (0, 0))
        sprites.add(self)
    
    # Метод обновления спрайтов
    def update(self):
        pass
    
    # Метод делающий статус карты перемещаемой
    def set_active(self, active: bool):
        self.active = active
    
    # Метод получения активности карты
    def get_active(self):
        return self.active


# Класс перемещаемой карты
class Prewiew(pygame.sprite.Sprite):
    def __init__(self, cardcell: CardCell):
        # Наследуем спрайты
        pygame.sprite.Sprite.__init__(self)
        # Родительская ячейка карты в инвентаре
        self.cardcell = cardcell
        # Уст анавливаем статус ячейки как активной
        self.cardcell.set_active(True)
        # Размеры движущейся ячейки
        self.width, self.height = self.cardcell.width, self.cardcell.height
        # Поверхность для картинки карты
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        # Помещаем картинку карты в ячейку
        self.image.blit(self.cardcell.card, (0, 0))
        # Добавляем в спрайты движущуюся ячейкуч
        sprites.add(self)
    
    def update(self):
        # Если движущаяся ячейка активная
        if self.cardcell.active:
            # Если мы не перемещаем фигуру то удаляем представление карты из спрайтов
            if not self.cardcell.get_active():
                sprites.remove(self)
            # Иначе устанавливаем позицию на экране
            self.x, self.y = pygame.mouse.get_pos()
            self.rect.topleft = (self.x, self.y)


# Класс игровой колоды
class CardsDeck(pygame.sprite.Sprite):
    # Инициализация класса игровой колоды
    def __init__(self, CARDS, size):
        # Наследуем спрайты
        pygame.sprite.Sprite.__init__(self)
        # Размер отрисованного изображения колоды
        self.width, self.height = size
        # Список карт
        self.cards = CARDS
        # Козырь колоды
        self.trump = False
        # Создаем колоду карт (перемешанную)
        self.createDeck()
        # Создаем image и rect для sprit'ов
        self.image = pygame.Surface((self.height, self.height))
        self.rect = self.image.get_rect()
        # Загружаем карту козыря
        self.tramp = pygame.image.load(CARDS_PATH + self.trump.image_path)
        # Изменяем размеры карты козыря
        self.tramp = pygame.transform.scale(self.tramp, (self.width, self.height))
        # Загружаем изображение рубашки
        self.shirt = pygame.image.load('images' + os.sep + GORIZONTAL_SHIRT)
        self.shirt = pygame.transform.scale(self.shirt, (self.height, self.width))
        # Загружаем изображение заплатки
        self.zaplatka = pygame.image.load('images/table.png')
        # Размеры заплатки
        z_size = ((self.height - self.width) / 2, self.height - self.width)
        self.zaplatka = pygame.transform.scale(self.zaplatka, z_size)
        # Координаты колоды
        self.new_x = 2.5 * vw
        self.new_y = 20 * vw
        # Располагаем колоду
        self.rect.topleft = (self.new_x, self.new_y)
        # Получаем количество карт в колоде
        self.count_cards = str(self.count_deck())
        # Созздаем стиль щрифта
        self.number_font = pygame.font.SysFont(None, int(4 * vw))
        # Добавляем колоду в спрайты
        sprites.add(self)

    # Метод обновления спрайтов колоды
    def update(self):
        # Проверяем на количество карт в колоде и исходя из количества карт меняем вид колоды
        if self.count_deck() > 2:
            # Если в колоде есть и нижнняя козырная карта и верхние мы отображаем и верхние и нижнюю карты
            # Координаты козыря
            tramp_coords = (self.tramp.get_rect()[0] + ((self.height - self.width) / 2), self.tramp.get_rect()[1])
            # Координаты рубашки
            shirt_coords = (self.shirt.get_rect()[0], self.shirt.get_rect()[1] + ((self.height - self.width)))
            # координаты заплатки 2
            zapl2_coords = (self.width + ((self.height - self.width) / 2), 0)
            # Отрисовываем колоду поэтапно
            self.image.blit(self.tramp, tramp_coords)
            self.image.blit(self.shirt, shirt_coords)
            self.image.blit(self.zaplatka, (0, 0))
            self.image.blit(self.zaplatka, zapl2_coords)
            # Создаем надпись количества карт
            self.count_cards = str(self.count_deck())
            self.number_image = self.number_font.render(self.count_cards, True, (0, 0, 0))
            self.image.blit(self.number_image, (3.5 * vw, 5.5 * vw))
        elif self.count_deck() == 1:
            # Если в колоде только козырная карта то мы отображаем только ее
            self.image = pygame.Surface((self.width, self.height))
            self.rect = self.image.get_rect()
            self.rect.topleft = (self.new_x + (self.height - self.width) / 2, self.new_y)
            # Вставляем изображение в прямоугольник
            self.image.blit(self.tramp, (0, 0))
        elif self.count_deck() == 0:
            # Если в колоде не осталось карт удаляем колоду из спрайтов
            sprites.remove(self)

    # Функция создания перемешанной игровой колоды
    def createDeck(self):
        new_deck = []
        for c in self.cards:
            suit = c.split(".")[0][-1]
            value = c.split(".")[0][0:-1]
            # print(suit, value)
            image = c
            card = Card(suit, value, image)
            new_deck.append(card)
        self.cards = new_deck
        # Перемешиваем колоду
        shuffle(self.cards)
        # Последнюю карту в колоде делаем козырной и задаем масть козырей
        self.trump = self.cards[-1]

    # Функция получения списка карт колоды
    def get_deck(self):
        return [i for i in self.cards if i.is_active]

    # Функция удаления карты из активной колоды
    def del_cards(self, cards):
        # Устанавливаем для карт статус неактивных в колоде
        for card in self.cards:
            if card in cards:
                card.set_active(False)

    # Метод количества карт в колоде
    def count_deck(self):
        # Возвращаем карты колоды (которые активные)
        return len([i for i in self.cards if i.is_active])


# Класс биты
class Basket(pygame.sprite.Sprite):
    # Инициализация класса
    def __init__(self, size: tuple):
        # Наследуем спрайты
        pygame.sprite.Sprite.__init__(self)
        # Размеры биты
        self.width, self.height = size
        # Создаем список карт корзины
        self.basket = []
        # Создаем поле для нашей биты
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        # Перемещаем положение нашей биты
        new_x = 85 * vw
        new_y = 20 * vw
        # Координаты биты
        self.rect.topleft = (new_x, new_y)
        # Загружаем задний фон биты
        self.bita = pygame.image.load('images' + os.sep + VERTICAL_SHIRT)
        # Изменяем размеры биты
        self.bita = pygame.transform.scale(self.bita, (self.width, self.height))
        # Флаг рисования биты
        self.is_show = False
        # Надпись количества карт в бите
        self.count_cards = str(self.count_basket())
        self.number_font = pygame.font.SysFont(None, int(4 * vw))
        # Добавляем биту в группу спрайтов
        sprites.add(self)
    
    # Метод добавления карты в биту
    def add_card(self, card: Card):
        self.basket.append(card)

    # Метод количества карт в бите
    def count_basket(self):
        return len(self.basket)
    
    # Метод обновления спрайтов биты
    def update(self):
        # Если в бите есть карты то отображаем биту
        if self.count_basket() > 0:
            # Если биты не была показана раньше то добавляем ее в спрайты
            if not self.is_show:
                sprites.add(self)
                # Устанавливаем статус отображения на положительный
                not self.is_show
            # Показываем биту если в ней есть карты
            self.image.blit(self.bita, (0, 0))
            # Показываем надпись количества карт в бите
            self.count_cards = str(self.count_basket())
            self.number_image = self.number_font.render(self.count_cards, True, (0, 0, 0))
            self.image.blit(self.number_image, (3 * vw, 4 * vw))
        else:
            # Удаляем колоду из группы спрайтов
            sprites.remove(self)


# Класс бота
class Bot(pygame.sprite.Sprite):
    # Инициализация класса
    def __init__(self, deck: CardsDeck):
        # Наследуем спрайты
        pygame.sprite.Sprite.__init__(self)
        # Колода карт
        self.deck = deck
        # Инвентарь бота
        self.inventory = deck.get_deck()[:6]
        # Удаляем карты из колоды
        deck.del_cards(self.inventory)
        # Размеры карты
        self.width, self.height = (7 * vw, 10.5 * vw)
        # Список карт на руках
        self.hands = []
        # Наличие сообщения
        self.msg = False
        # Статус атакующего
        self.attack_status = False
        # Статус отбития карт на столе
        self.otbitie = True
        # Дополнительная информация о действии бота
        self.action_information = False
        # В цикле пробегаемся по количеству карт из инвенторя и располагаем их на экране
        for i in range(len(self.inventory)):
            # Получаем изображение карты инвентаря
            img_path = 'images' + os.sep + VERTICAL_SHIRT
            # Создаем обьект класса ячейки с картой
            try:
                step = (60 * vw - 7 * vw) / (len(self.inventory) - 1)
                size = (self.width, self.height)
                coords = (20 * vw + i * step, 2 * vw)
                inv_cell = CardCell(size, coords, img_path, self.inventory[i], step)
            except ZeroDivisionError:
                step = 1000
                size = (self.width, self.height)
                coords = (44.5 * vw, 2 * vw)
                inv_cell = CardCell(size, coords, img_path, self.inventory[i], step)
            self.hands.append(inv_cell)
        self.update()
    
    # Метод обновления положения всех карт инвентаря
    def update(self):
        # Удаляем из спрайтов ячейки карт ии
        sprites.remove(self.hands)
        # Очищаем список ячееккарт ии на руках
        self.hands.clear()
        # В цикле отрисовываем рубашки карт ии
        for i in range(len(self.inventory)):
            # Получаем изображение карты инвентаря
            img_path = 'images' + os.sep + VERTICAL_SHIRT
            # Создаем обьект класса ячейки с картой
            try:
                step = (60 * vw - 7 * vw) / (len(self.inventory) - 1)
                size = (self.width, self.height)
                coords = (20 * vw + i * step, 2 * vw)
                inv_cell = CardCell(size, coords, img_path, self.inventory[i], step)
            except ZeroDivisionError:
                step = 1000
                size = (self.width, self.height)
                coords = (44.5 * vw, 2 * vw)
                inv_cell = CardCell(size, coords, img_path, self.inventory[i], step)
            self.hands.append(inv_cell)

    # Метод устанавления статуса нападающего
    def set_attack_status(self, value: bool):
        self.attack_status = value
    
    # Метод возвращения статуса нападающего
    def get_attack_status(self):
        return self.attack_status
    
    # Метод защиты ии
    def deffend(self, table: Table, deck: CardsDeck):
        # Если ии до этого отбивал карты стола
        if self.otbitie:
            # В цикле проходимся по каждой карте которая лежит на столе и не отбита
            for table_card in [card for card in list(table.cards.keys()) if not table.cards[card]]:
                # Пробегаемся по каждой карте в инвентаре бота и проверяем можем ли мы отбить карту 
                # если нет то забираем все карты в инвентарь бота
                for bot_card in self.inventory:
                    # Благодаря заранее прописанным методам в классе карты проверяем может ли карта отбить атаку
                    if bot_card.__gt__(table_card, deck.trump):
                        card = bot_card
                        # Если в инвентаре ии есть карты кроме козырной способные отбить карту стола
                        if bot_card.suit == deck.trump.suit and table_card.suit != deck.trump.suit and \
                           [(card.suit != deck.trump.suit and \
                                 table_card.suit == card.suit and \
                                 card.__gt__(table_card, deck.trump)) for card in self.inventory \
                                    if (card.suit != deck.trump.suit and \
                                        table_card.suit == card.suit and \
                                        card.__gt__(table_card, deck.trump))]:
                            cards = []
                            check = []
                            for card in self.inventory:
                                if table_card.suit == card.suit and card.__gt__(table_card, deck.trump):
                                    check.append(card)
                            for test_card in check:
                                if test_card.__gt__(table_card, deck.trump):
                                    cards.append(test_card)
                            if cards:
                                card = min(cards, key=lambda x: VALUES.index(x.value))
                                self.action_information = "Замена козыря альтернативой"
                        # Добавляем в стол по ключу атакующей карты значение карты защищающей
                        table.cards[table_card] = card
                        # Удаляем из инвентаря карту положенную на стол
                        self.inventory.remove(card)
                        # Отрисовываем на столе положенную карту
                        table.set_deffend_card(card, table_card)
                        break
                # Если бот не может отбить карту
                else:
                    if self.action_information:
                        self.action_information += "Взятие карт ботом"
                    else:
                        self.action_information = "Взятие карт ботом"
                    self.msg = Message("Беру")
                    self.otbitie = False
    
    # Метод атаки бота
    def attack(self, table: Table, deck: CardsDeck):
        # Список карт для атаки
        cards = []
        # Получаем карты подходящие для подкидывания
        if not table.cards:
            if self.inventory:
                # Получаем случайную карту
                card = [choice(self.inventory)][0]
                # Если карта козырная
                if card.suit == DECK.trump.suit:
                    # Если в инвентаре ии не только козыри
                    if [card.suit != DECK.trump.suit for card in self.inventory if card.suit != DECK.trump.suit]:
                        while card.suit == DECK.trump.suit:
                            card = [choice(self.inventory)][0]
                    self.action_information = "Случайная карта стала козырем"
                cards.append(card)
            else:
                pass
        else:
            # В цикле пробегаемся по картам бота
            for bot_card in self.inventory:
                # пробегаемся по картам на столе
                for table_card in [card for card in list(table.cards.keys())]:
                    # Если значение карты инвентаря совпало со значением карты на столе добавляем в карты хода
                    if bot_card.value == table_card.value and len(cards) < 5:
                        cards.append(bot_card)
        # Обрабатываем карты подкидываемые ботом
        if cards:
            # Если карт подкидываемых карт больше чем у пользователя
            if len(cards) > len(player.inventory):
                cards = cards[:len(player.inventory)]
            # Проходим в цикле по подкидываемым картам
            for card in cards:
                # Удаляем карту из инвентаря
                self.inventory.remove(card)
                # Устанавливаем на стол карту атаки
                table.set_attack_card(card)
        # Если боту нечего подкинуть и все карты на столе отбиты
        else:
            # Если все карты на столе отбиты
            if False not in list(table.cards.values()):
                # Статус бота меняется на защищающегося
                self.attack_status = False
                # Добавляем карты в биту
                for para in list(table.cards.items()):
                    for card in para:
                        bita.add_card(card)
                # Обновляем инвентарь пользователя
                player.update_inventori(DECK)
                player.update()
                # Обновляем инвентарь ии
                self.update_inventori(DECK)
                # Очищаем стол
                table.clear_table()
        # Обновляем карты ии 
        self.update()

    # Метод обновления инвертаря
    def update_inventori(self, deck: CardsDeck):
        # Количество необходимых карт
        count_cards = 6 - len(self.inventory)
        # Если карт в инвентаре меньше 6
        if count_cards > 0:
            # Если в колоде больше карт чем нужно
            if len(deck.cards) > count_cards:
                cards = deck.get_deck()[:count_cards]
            # Если в колоде карт меньше чм нужно
            else:
                cards = deck.get_deck()
            # Удаляем карты их колоды
            deck.del_cards(cards)
            # Добаляем карты игроку если есть что добавлять
            if cards:
                for c in cards:
                    self.inventory.append(c)
            # Обновляем инвентарь ии и колоду
            self.update()
            deck.update()


# Класс сообщения
class Message(pygame.sprite.Sprite):
    # Инициализация класса
    def __init__(self, message: str):
        # Наследование спрайтов
        pygame.sprite.Sprite.__init__(self)
        # Создаем поверхность
        self.image = pygame.Surface((vw * 14, vw * 6))
        self.rect = self.image.get_rect()
        # Распологаем сообщение
        self.rect.topleft = (5 * vw, 4 * vw)
        # Наносим текст
        self.font = pygame.font.SysFont(None, int(6 * vw))
        self.label = self.font.render(message, True, (255, 255, 255))
        self.image.blit(self.label, (vw * 2, vw))
        # Добавляем кнопку в спрайты
        sprites.add(self)


# Класс игрока
class Player(pygame.sprite.Sprite):
    # Инициализация класса
    def __init__(self, deck: CardsDeck):
        pygame.sprite.Sprite.__init__(self)
        # Обьявляем основную колоду карт
        self.deck = deck
        # Создаем инвентарь из первых 6 карт колоды
        self.inventory = deck.get_deck()[:6]
        # Удаляем карты инвенторя из колоды
        deck.del_cards(self.inventory)
        # Размеры карты
        self.width, self.height = (7 * vw, 10.5 * vw)
        # Список карт на руках
        self.hands = []
        # Статус атакующего
        self.attack_status = None
        # В цикле пробегаемся по количеству карт из инвенторя и располагаем их на экране
        for i in range(len(self.inventory)):
            # Получаем изображение карты инвентаря
            img_path = self.inventory[i].image_path
            # Создаем обьект класса ячейки с картой
            try:
                step = (vw * 60 - vw * 7) / (len(self.inventory) - 1)
                coords = (20 * vw + i * step, vw * 37.5)
                size = (self.width, self.height)
                inv_cell = CardCell(size, coords, CARDS_PATH + img_path, self.inventory[i], step)
            except ZeroDivisionError:
                step = 1000
                coords = (44.5 * vw, 37.5 * vw)
                size = (self.width, self.height) 
                inv_cell = CardCell(size, coords, CARDS_PATH + img_path, self.inventory[i], step)
            self.hands.append(inv_cell)
        # Обновляем инвентарь игрока
        self.update()

    # Метод обновления положения всех карт инвентаря
    def update(self):
        # Удаляем из спрайтов все ячейка карт игрока
        sprites.remove(self.hands)
        # Очищаем список ячеек карт игрока
        self.hands.clear()
        # В цикле пробегаемся по картам инвентаря и отрисовываем их
        for i in range(len(self.inventory)):
            # Получаем изображение карты инвентаря
            img_path = self.inventory[i].image_path
            # Создаем обьект класса ячейки с картой
            try:
                step = (vw * 60 - vw * 7) / (len(self.inventory) - 1)
                coords = (20 * vw + i * step, vw * 37.5)
                size = (self.width, self.height)
                inv_cell = CardCell(size, coords, CARDS_PATH + img_path, self.inventory[i], step)
            except ZeroDivisionError:
                step = 1000
                coords = (44.5 * vw, 37.5 * vw)
                size = (self.width, self.height) 
                inv_cell = CardCell(size, coords, CARDS_PATH + img_path, self.inventory[i], step)
            # Добавляем в список ячеек карт ячейку
            self.hands.append(inv_cell)

    # Метод обновления инвертаря
    def update_inventori(self, deck: CardsDeck):
        # Количество необходимых карт
        count_cards = 6 - len(self.inventory)
        # Если карт в инвентаре меньше 6
        if count_cards > 0:
            if len(deck.cards) > count_cards:
                cards = deck.get_deck()[:count_cards]
            else:
                cards = deck.get_deck()
            # Удаляем карты их колоды
            deck.del_cards(cards)
            # Добаляем карты игроку
            for c in cards:
                player.inventory.append(c)
            # Обновляем инвентарь игрока и колоду карт
            self.update()
            deck.update()

    # Метод устанавления статуса нападающего
    def set_attack_status(self, value: bool):
        self.attack_status = value
    
    # Метод возвращения статуса нападающего
    def get_attack_status(self):
        return self.attack_status
    

# Класс кнопки паса / беру
class Button(pygame.sprite.Sprite):
    # Инициализация класса
    def __init__(self):
        # Наследуем спрайты
        pygame.sprite.Sprite.__init__(self)
        # Создаем поверхность для кнопки
        self.image = pygame.Surface((int(vw * 10), int(vw * 3)))
        self.rect = self.image.get_rect()
        # Располагаем кнопку на экране
        self.rect.topleft = (vw * 85, vw * 41)
        # Заполняем цветом кнопку
        self.image.fill(CELL, self.image.get_rect())
        # Созздаем надпись на кнопке
        self.font = pygame.font.SysFont(None, int(2 * vw))
        self.label = self.font.render("Пас / Беру", True, (0, 0, 0))
        self.image.blit(self.label, (2 * vw, vw))
        # Добавляем кнопку в спрайты
        sprites.add(self)


# Функция записи результата игры в бд
def write_result(winner, count_cards, steps):
    # Получаем настоящее время
    date = str(datetime.datetime.now())
    # Создаем соединение с базой данных
    con = sqlite3.connect('data/db.sqlite3')
    # Создаем курсор бд
    cur = con.cursor()
    # Формируем запрос
    qyery = f"""
    INSERT into Results (date, winner, cards) VALUES ('{date}', '{winner}', {count_cards})
    """
    # Делаем запрос в бд и вносим результат
    cur.execute(qyery)
    for i, step in enumerate(steps):
        query = f"""
        INSERT into Steps (game_id, table_cards, bot, player, info, step_id) Values
        ({step[0]},'{step[1]}', '{step[2]}', '{step[3]}', '{step[4]}', {i})
        """
        cur.execute(query)
        con.commit()
    # Подтверждаем изменение бд
    con.commit()
    # Закрываем соединение с бд
    con.close()


# Функция проверки победы
def check_win(player: Player, bot: Bot, deck: CardsDeck):
    # Если в колоде есть карты
    if deck.count_deck() != 0:
        return False
    # Если в колоде нет карт
    else:
        if not player.inventory and not bot.inventory:
            return "Ничья"
        # Если в инвентаре игрока нет карт
        elif not len(player.inventory):
            return "Игрок"
        # Если в инвентаре бота нет карт
        elif not len(bot.inventory):
            return "Бот"


# Функция отображения результата
def show_result(winner, count_cards, steps):
    # Исходя из переданного аргументы победителя выбираем действия
    match winner:
        case "Бот":
            # Записываем результат в бд
            write_result("Бот", count_cards, steps)
            time.sleep(1)
            # Включаем музыку проигрыша и окно о проигрыше игрока
            pygame.mixer.music.load('audio/loss.mp3')
            pygame.mixer.music.play(-1)
            messagebox.showinfo("(:", "Вы проиграли")
        case "Игрок":
            # Записываем результат в бд
            write_result("Игрок", count_cards, steps)
            time.sleep(1)
            # Включаем музыку победы и окно о победе игрока
            pygame.mixer.music.load('audio/win.mp3')
            pygame.mixer.music.play(-1)
            messagebox.showinfo("Поздравляем!!!", "Вы выиграли")
        case "Ничья":
            # Записываем результат в бд
            write_result("Ничья", count_cards, steps)
            time.sleep(1)
            # Включаем музыку победы и окно о победе игрока
            pygame.mixer.music.load('audio/win.mp3')
            pygame.mixer.music.play(-1)
            messagebox.showinfo(".............", "НИЧЬЯ!")


# Функция получения настроек из файла
def settings():
    # Читаем файл с настройками
    with open('settings.txt', 'r', encoding="utf-8") as file:
        data = file.readlines()
        data = [i.replace('\n', '') for i in data]
        # Количество карт
        count_cards = int(data[0])
        # Директория папки с картами
        cards_path = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + \
            data[1].split("/")[0] + os.path.sep + data[1].split("/")[1] + os.path.sep

    # Список карт
    cards = [i for i in list(os.listdir(cards_path))]
    # Список значений карт
    match count_cards:
        case 24:
            values = ['9', '10', 'V', 'D', 'K', 'T']
        case 36:
            values = ['6', '7', '8', '9', '10', 'V', 'D', 'K', 'T']
        case 52:
            values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'V', 'D', 'K', 'T']

    # Переделываем список карт
    new_cards = []
    for card in cards:
        if card.split(".")[0][:-1] in values:
            new_cards.append(card)
    cards = new_cards

    # Список мастей
    suits = ['C', 'V', 'K', 'B']
    # Цвет пустой ячейки карты
    cell = (160, 160, 160)
    # Название фото рубашки горизонтальной
    goriz_shirt = data[2]
    # Название фото рубашки вертикальной
    vertic_shirt = data[3]
    # Номер игры
    gane_number = len(sqlite3.connect('data/db.sqlite3').cursor().execute("SELECT * from Results").fetchall()) + 1
    return cards, suits, cell, goriz_shirt, vertic_shirt, values, cards_path, count_cards, gane_number


# Основная фуекция игры
def main():
    # Дедаем глобальными элементы дабы избежать ошибок с использованием обьектов класса вне функции
    global vw, sprites, player, DECK, bita, bot, table, CARDS, SUITS, CELL, GORIZONTAL_SHIRT, VERTICAL_SHIRT, \
           VALUES, CARDS_PATH, GAME_NUMBER, steps, running, COUNT_CARDS
    # Получаем настройки из файла
    CARDS, SUITS, CELL, GORIZONTAL_SHIRT, VERTICAL_SHIRT, VALUES, CARDS_PATH, COUNT_CARDS, GAME_NUMBER = settings()
    # Инициализируем pygame 
    pygame.init()
    # Убираем главное окно tkinter'а
    Tk().wm_withdraw()
    # Задаем название нашему окну игры
    pygame.display.set_caption("Durak")
    # Создаем экран
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    
    # Добавим музыки в нашу игру
    pygame.mixer.music.load('audio/agent_lis.mp3')
    pygame.mixer.music.play(-1)

    # Создаем заставку для игры
    preloader = pygame.image.load('images/preloader.jpg')
    preloader = pygame.transform.scale(preloader, screen.get_size())
    screen.blit(preloader, (0, 0))
    pygame.display.flip()
    time.sleep(2)

    # Создаем группу спрайтов
    sprites = pygame.sprite.Group()

    # Создаем условные единицы размера для адаптации размеров к любому компьютеру
    vw, vh = [i / 100 for i in screen.get_size()]
    # Примерные размеры для моего устройства
    # vw = 19.2px
    # vh = 10.8px

    # Загружаем задний фон
    bg = pygame.image.load('images/table.png')
    # Изменяем размеры заднего фона исходя из размеров окна
    bg = pygame.transform.scale(bg, screen.get_size())

    # Создаем стол для игры
    table = Table((7 * vw, 10.5 * vw), (59 * vw, 13.5 * vw))
    for cell in table.table:
        pygame.draw.rect(screen, CELL, (cell.x, cell.y, cell.width, cell.height))

    # Создаем новую перемешанную колоду карт
    DECK = CardsDeck(CARDS, (vw * 7, 10.5 * vw))

    # Создаем биту и передаем в нее ее размеры
    bita = Basket((vw * 7, 10.5 * vw))

    # Создаем игрока
    player = Player(DECK)

    # Создаем бота
    bot = Bot(DECK)

    # Кнопка паса
    button = Button()

    # Запуск игры
    running = True
    # Взятие карты в руки
    put_card = False

    # Список ходов
    steps = []

    while running:
        # Если игры завершена
        if check_win(player, bot, DECK):
            # Показываем результат с помощью функции
            show_result(check_win(player, bot, DECK), COUNT_CARDS, steps)
            pygame.quit()
        # В цикле прогаеся по ивентам окна
        for event in pygame.event.get():
            # Если пользователь нажал Esc
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            # Обработка события закрытия окна
            if event.type == pygame.QUIT:
                running = False
            # Обработка нажатия кнопки мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                # В цикле проходим по всем спрайтам карт инвенторя игрока
                for cardcell in player.hands:
                    # Если клик кнопки мыши был по карте и если карта не активная
                    # а также если по правилам игры можно положить карту
                    if cardcell.rect.collidepoint(event.pos) and not cardcell.get_active() and \
                       table.can_put_card(cardcell.parent_card):
                        # Если мы еще не взяли карту
                        if not put_card:
                            # Устанавливаем флаг
                            put_card = True
                            # Устанавливаем всем картам кроме тронутой статус не двигающихся
                            cardcell.set_active(True)
                            # В цикле пробегаемся по невзятым картам игрока и устанавливаем им статус неактивных
                            for other_ceil in player.hands:
                                if not (other_ceil is cardcell):
                                    other_ceil.set_active(False)
                            # Удаляемая карта
                            delete_cardcell = cardcell
                            prewiew = Prewiew(cardcell)
                            try:
                                # Обработка ошибки отсутствия карты в инвентаре
                                player.inventory.remove(cardcell.parent_card)
                            except ValueError:
                                continue
                            # Убираем из спрайтов обновляемую ячейку карты инвентаря
                            sprites.remove(cardcell)

                # В цикле пробегаемся по элементам стола
                for place in table.table:
                    # Если клик мыши был по ячейке стола
                    if place.rect.collidepoint(event.pos):    
                        # Получаем активную карту
                        card = [i for i in player.hands if i.get_active()]
                        # Если она есть и карты стола позволяют положить ее на стол по правилам игры
                        if card:
                            # Если бот защищается
                            if place.card not in table.cards and not bot.attack_status and not place.card:
                                # Удаляем из спрайтов отображение перемещаемой карты
                                sprites.remove(prewiew)
                                # Флаг того что карта установлена на стол
                                put_card = False 
                                table.cards[card[0].parent_card] = False
                                # Устанавливаем значение карты для позиции стола
                                place.set_card(card[0].parent_card)
                                # Устанавливаем в позицию стола картинку карты
                                place.update()
                                # Осуществление защиты бота
                                bot.deffend(table, DECK)
                                bot.update()
                                # Удаляем карту из списка спрайтов карт игрока
                                player.hands.remove(delete_cardcell)
                                # Перерисовываем карты игрока
                                player.update()
                            # Если бот атакует
                            elif place.card in table.cards and not table.cards[place.card]:
                                # Удаляем из спрайтов отображение перемещаемой карты
                                sprites.remove(prewiew) 
                                # Флаг того что карта установлена на стол
                                put_card = False
                                # Устанавливаем карту которой отбили в словарь по ключу отбиваемой
                                table.cards[place.card] = card[0].parent_card
                                table.set_deffend_card(card[0].parent_card, place.card)
                                # Атака бота
                                bot.attack(table, DECK)
                                bot.update()
                                try:
                                    # Удаляем карту из списка спрайтов карт игрока
                                    player.hands.remove(delete_cardcell)
                                except ValueError:
                                    continue
                                # Перерисовываем карты игрока
                                player.update()

                # Если нажатие было по кнопке пас/беру и в руках не взята карта
                if button.rect.collidepoint(event.pos) and not put_card:
                    # Если на столе есть карты то можно нажать на кнопку
                    if table.cards:
                        # Если отбивался бот
                        if not bot.attack_status:
                            # Если бот не отбился
                            if not bot.otbitie:
                                bot.otbitie = True
                                # Добавляем в инвентарь ии карты которые он не смог отбить
                                for para in list(table.cards.items()):
                                    for card in para:
                                        if card:
                                            bot.inventory.append(card)
                                # Обновляем инвентарь ии
                                bot.update()
                                # Обновляем инвентарь игрока
                                player.update_inventori(DECK)
                                # Очищаем стол
                                table.clear_table()
                            # Если бот отбился
                            else:
                                # Добавляем карты в биту
                                for para in list(table.cards.items()):
                                    for card in para:
                                        bita.add_card(card)
                                # Меняем статус атакующего
                                bot.attack_status = not bot.attack_status
                                # Обновляем инвентарь игрока
                                player.update_inventori(DECK)
                                player.update()
                                # Обновляем инвентарь ии
                                bot.update_inventori(DECK)
                                bot.update()
                                # Очищаем стол
                                if table.check_table():
                                    table.clear_table()
                                # Атака бота
                                bot.attack(table, DECK)
                        # Если отбивался игрок (функция беру)
                        elif bot.attack_status:
                            bot.attack_status = True
                            # Забираем карты со стола в инвентарь
                            for para in list(table.cards.items()):
                                for card in para:
                                    if card:
                                        player.inventory.append(card)
                            # Обновляем инвентарь игрока
                            player.update()
                            # Обновляем инвентарь ии
                            bot.update_inventori(DECK)
                            bot.update()
                            # Очищаем стол
                            table.clear_table()
                            # Атака бота
                            bot.attack(table, DECK)
                            
        # Обновляем экран и все его составляющие
        bita.update()
        sprites.update()
        screen.blit(bg, (0, 0))
        sprites.draw(screen)
        pygame.display.flip()
    
    # Выход из окна pygame 
    pygame.quit()


# Класс приложения с предварительными настройками
class SetSettings(QWidget):
    # Инициализация класса
    def __init__(self):
        # Наследуем QWidget
        super().__init__()
        # # Преобразуем ui 
        f = io.StringIO(settings_app_template)
        # Загружаем интерфейс
        uic.loadUi(f, self)
        self.InitUI()
        # Показываем окно
        self.show()
    
    # Метод ui 
    def InitUI(self):
        self.start_game = False
        # Подключаем функцию начала игры к кнопке
        self.start_button.clicked.connect(self.startgame)
        # Установим изображения в нашу форму
        self.theme_1_img = QImage("cards/theme1/KK.jpg")
        self.pixmap1 = QPixmap.fromImage(self.theme_1_img)
        self.pixmap1 = self.pixmap1.scaledToWidth(101)
        self.pixmap1 = self.pixmap1.scaledToHeight(148)
        self.theme_1.setPixmap(self.pixmap1)

        self.theme_2_img = QImage("cards/theme2/KK.png")
        self.pixmap2 = QPixmap.fromImage(self.theme_2_img)
        self.pixmap2 = self.pixmap2.scaledToWidth(101)
        self.pixmap2 = self.pixmap2.scaledToHeight(148)
        self.theme_2.setPixmap(self.pixmap2)

        self.shirt_1_img = QImage("images/vertical_shirt1.png")
        self.pixmap3 = QPixmap.fromImage(self.shirt_1_img)
        self.pixmap3 = self.pixmap3.scaledToWidth(101)
        self.pixmap3 = self.pixmap3.scaledToHeight(148)
        self.shirt_1.setPixmap(self.pixmap3)

        self.shirt_2_img = QImage("images/vertical_shirt2.png")
        self.pixmap4 = QPixmap.fromImage(self.shirt_2_img)
        self.pixmap4 = self.pixmap4.scaledToWidth(101)
        self.pixmap4 = self.pixmap4.scaledToHeight(148)
        self.shirt_2.setPixmap(self.pixmap4)
    
    # Метод запуска игры
    def startgame(self):
        # На случай многократного нажатия на кнопку пресекаем его
        if not self.start_game:
            not self.start_game
            # Записываем настройки в файл
            self.set_settings()
            # Закрываем окно настроек
            self.close()
            # Объявляем основную игровую функцию
            main()
    
    # Метод получающий значение
    def set_settings(self):
        # Получаем количество карт
        COUNT_CARDS = self.count_group.checkedButton().text()
        # Получаем тему карт
        THEME_DIR = "cards/theme1" if self.theme1.isChecked() else "cards/theme2"
        # Получаем путь рубашки
        GORIZONTAL_SHIRT = 'gorizontal_shirt1.png' if self.shirt1.isChecked() else 'gorizontal_shirt2.png'
        VERTIVAL_SHIRT = 'vertical_shirt1.png' if self.shirt1.isChecked() else 'vertical_shirt2.png'
        DATA = [COUNT_CARDS, THEME_DIR, GORIZONTAL_SHIRT, VERTIVAL_SHIRT]
        # Запись настроек в файл
        with open('settings.txt', 'w') as file:
            for d in DATA:
                file.writelines(d + "\n")
                

# Запуск нашего приложения
if __name__ == "__main__":
    # Запускаем окно установки настроек
    app = QApplication(sys.argv)
    settengs_app = SetSettings()
    sys.exit(app.exec())