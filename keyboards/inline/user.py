from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import configparser


config = configparser.ConfigParser()
config.read("config.ini")


class UsersHelp():

    def create_kb():
        kb = InlineKeyboardMarkup()
        kb.row_width = 2
        btns = []
        btns.append(InlineKeyboardButton(text='OK', callback_data='UserOk'))
        btns.append(InlineKeyboardButton(text='Отмена', callback_data='UserCancel'))
        kb.row(btns[0], btns[1])
        return kb


class UsersCheckSales():

    def create_kb():
        kb = InlineKeyboardMarkup()
        kb.row_width = 2
        btns = []
        btns.append(InlineKeyboardButton(text='Верно', callback_data='CheckOk'))
        btns.append(InlineKeyboardButton(text='Исправить', callback_data='CheckChange'))
        kb.row(btns[0], btns[1])
        return kb


class UserProducts():
    kbs = config['atrs']
    config.read_dict()

    def create_kb(self):
        btns = []
        kb = InlineKeyboardMarkup()
        kb.row_width = 5
        for k in self.kbs:
            btns.append(InlineKeyboardButton(text=k, callback_data='Change'+k))
        kb.add(*btns)
        return kb
