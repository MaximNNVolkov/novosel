from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


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
