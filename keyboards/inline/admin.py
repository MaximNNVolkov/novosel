from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


class AdminDates:

    def __init__(self):
        self.cb = CallbackData('dates', 'name')

    def create_kb(self):
        kb = InlineKeyboardMarkup()
        kb.row_width = 2
        kb.row(InlineKeyboardButton(text='Сегодня',
                                         callback_data=self.cb.new(name='today')))
        kb.row(InlineKeyboardButton(text='Вчера',
                                         callback_data=self.cb.new(name='yesterday')))
        kb.row(InlineKeyboardButton(text='Неделя',
                                         callback_data=self.cb.new(name='week')))
        kb.row(InlineKeyboardButton(text='Месяц',
                                         callback_data=self.cb.new(name='month')))
        return kb
