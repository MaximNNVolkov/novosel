from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


class UsersHelp:

    def create_kb(self):
        kb = InlineKeyboardMarkup()
        kb.row_width = 2
        btns = []
        btns.append(InlineKeyboardButton(text='OK', callback_data='UserOk'))
        btns.append(InlineKeyboardButton(text='Отмена', callback_data='UserCancel'))
        kb.row(btns[0], btns[1])
        return kb


class UsersVopros_1:

    def __init__(self):
        self.cb = CallbackData('vopros_1', 'name')

    def create_kb(self):
        kb = InlineKeyboardMarkup()
        kb.row_width = 2
        kb.row(InlineKeyboardButton(text='Да, всегда',
                                         callback_data=self.cb.new(name='yes')))
        kb.row(InlineKeyboardButton(text='Нет / редко',
                                         callback_data=self.cb.new(name='no')))
        return kb


class UsersVopros_2:

    def __init__(self):
        self.cb = CallbackData('vopros_2', 'name')

    def create_kb(self):
        kb = InlineKeyboardMarkup()
        kb.row_width = 2
        kb.row(InlineKeyboardButton(text='Да, всегда',
                                         callback_data=self.cb.new(name='yes')))
        kb.row(InlineKeyboardButton(text='Нет / редко',
                                         callback_data=self.cb.new(name='no')))
        return kb


class UsersVopros_3:

    def __init__(self):
        self.cb = CallbackData('vopros_3', 'name')

    def create_kb(self):
        kb = InlineKeyboardMarkup()
        kb.row_width = 2
        kb.row(InlineKeyboardButton(text='Да, всегда',
                                         callback_data=self.cb.new(name='yes')))
        kb.row(InlineKeyboardButton(text='Нет / редко',
                                         callback_data=self.cb.new(name='no')))
        return kb


class UsersVopros_4:

    def __init__(self):
        self.cb = CallbackData('vopros_4', 'name')

    def create_kb(self):
        kb = InlineKeyboardMarkup()
        kb.row_width = 2
        kb.row(InlineKeyboardButton(text='Да, всегда',
                                         callback_data=self.cb.new(name='yes')))
        kb.row(InlineKeyboardButton(text='Нет / редко',
                                         callback_data=self.cb.new(name='no')))
        return kb


class UsersVopros_5:

    def __init__(self):
        self.cb = CallbackData('vopros_5', 'name')

    def create_kb(self):
        kb = InlineKeyboardMarkup()
        kb.row_width = 2
        kb.row(InlineKeyboardButton(text='Да, всегда',
                                         callback_data=self.cb.new(name='yes')))
        kb.row(InlineKeyboardButton(text='Нет / редко',
                                         callback_data=self.cb.new(name='no')))
        return kb
