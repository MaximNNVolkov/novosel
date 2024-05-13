import app_logger as loger
from aiogram.utils import markdown as fmt
from defs.classes import User
from fsm import StateUser
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from keyboards import inline
import asyncio
from database.novosel_base import save_res, get_photo


log = loger.get_logger(__name__)


async def opros_start(msg: Message, state: FSMContext):
    u = User(msg.from_user)
    u.add_user()
    log.info(u.info_user())
    await state.set_state(StateUser.vopros_1)
    await msg.answer(
        text=fmt.text(
            fmt.text(u.get_url(), ',', sep=''),
            fmt.text('Часто ли Вы задумываетесь о сохранности своего имущества'),
            fmt.text('(квартира, дом, дача)?'),
            sep=' '),
        reply_markup=inline.UsersVopros_1().create_kb())


async def write_answer_1(cb: CallbackQuery, state: FSMContext):
    u = User(cb.from_user)
    log.info(' '.join([await state.get_state(), cb.data, u.info_user()]))
    if cb.data == 'vopros_1:yes':
        await state.set_data([{cb.data.split(':')[0]: cb.data.split(':')[1]}])
    elif cb.data == 'vopros_1:no':
        await state.set_data([{cb.data.split(':')[0]: cb.data.split(':')[1]}])
    await cb.message.answer(
        text=fmt.text(
            fmt.text(u.get_url(), ',', sep=''),
            fmt.text('Находясь вне дома, беспокоитесь ли о том, что может'),
            fmt.text('произойти с домом/квартирой в Ваше отсутствие'),
            fmt.text('(например, зальют соседи сверху)?'),
            sep=' '),
        reply_markup=inline.UsersVopros_2().create_kb())
    await state.set_state(StateUser.vopros_2)


async def write_answer_2(cb: CallbackQuery, state: FSMContext):
    u = User(cb.from_user)
    log.info(' '.join([await state.get_state(), cb.data, u.info_user()]))
    d = await state.get_data()
    if cb.data == 'vopros_2:yes':
        d.extend([{cb.data.split(':')[0]: cb.data.split(':')[1]}])
        await state.set_data(data=d)
    elif cb.data == 'vopros_2:no':
        d.extend([{cb.data.split(':')[0]: cb.data.split(':')[1]}])
        await state.set_data(data=d)
    await cb.message.answer(
        text=fmt.text(
            fmt.text(u.get_url(), ',', sep=''),
            fmt.text('Выходя из дома, вы проверяете - выключили ли бытовые'),
            fmt.text('приборы (например, утюг) и/или коммунальные системы'),
            fmt.text('(например, воду, газ)?'),
            sep=' '),
        reply_markup=inline.UsersVopros_3().create_kb())
    await state.set_state(StateUser.vopros_3)


async def write_answer_3(cb: CallbackQuery, state: FSMContext):
    u = User(cb.from_user)
    log.info(' '.join([await state.get_state(), cb.data, u.info_user()]))
    d = await state.get_data()
    if cb.data == 'vopros_3:yes':
        d.extend([{cb.data.split(':')[0]: cb.data.split(':')[1]}])
        await state.set_data(data=d)
    elif cb.data == 'vopros_3:no':
        d.extend([{cb.data.split(':')[0]: cb.data.split(':')[1]}])
        await state.set_data(data=d)
    await cb.message.answer(
        text=fmt.text(
            fmt.text(u.get_url(), ',', sep=''),
            fmt.text('Используете ли вы дополнительное декоративное освещение'),
            fmt.text('(например, гирлянды, цветовые лампы) при украшении квартиры/дома'),
            fmt.text('к какому-либо празднику/событию (например, приход гостей, дни рождения и пр.)?'),
            sep=' '),
        reply_markup=inline.UsersVopros_4().create_kb())
    await state.set_state(StateUser.vopros_4)


async def write_answer_4(cb: CallbackQuery, state: FSMContext):
    u = User(cb.from_user)
    log.info(' '.join([await state.get_state(), cb.data, u.info_user()]))
    d = await state.get_data()
    if cb.data == 'vopros_4:yes':
        d.extend([{cb.data.split(':')[0]: cb.data.split(':')[1]}])
        await state.set_data(data=d)
    elif cb.data == 'vopros_4:no':
        d.extend([{cb.data.split(':')[0]: cb.data.split(':')[1]}])
        await state.set_data(data=d)
    await cb.message.answer(
        text=fmt.text(
            fmt.text(u.get_url(), ',', sep=''),
            fmt.text('Актуальна ли для Вас система "Умный дом", позволяющая контролировать'),
            fmt.text('работу коммунального обеспечения (например, свет, вода) и работу бытовой техники?'),
            sep=' '),
        reply_markup=inline.UsersVopros_5().create_kb())
    await state.set_state(StateUser.vopros_5)


async def write_answer_5(cb: CallbackQuery, state: FSMContext):
    u = User(cb.from_user)
    log.info(' '.join([await state.get_state(), cb.data, u.info_user()]))
    d = await state.get_data()
    if cb.data == 'vopros_5:yes':
        d.extend([{cb.data.split(':')[0]: cb.data.split(':')[1]}])
        await state.set_data(data=d)
    elif cb.data == 'vopros_5:no':
        d.extend([{cb.data.split(':')[0]: cb.data.split(':')[1]}])
        await state.set_data(data=d)
    await cb.message.answer(
        text=fmt.text(
            fmt.text(u.get_url(), ',', sep=''),
            fmt.text('Спасибо за ответы.'),
            fmt.text('Мы подобрали для Вас следующий вариант:'),
            sep=' '))
    await state.set_state(StateUser.result)
    await send_result(u, cb, state=state)


# async def send_result(u, cb, state: FSMContext):
#     log.info(u.info_user())
#     log.info(' '.join([await state.get_state(), u.info_user()]))
#     d = await state.get_data()
#     print(d[1].values(), str(d[1].values()) == "dict_values(['yes'])")
#     c = 0
#     save_res(u.id, d)
#     if d[1].get('vopros_2') == 'yes':
#         await cb.bot.send_message(chat_id=u.id,
#             text=fmt.hide_link(
#                 url='https://megamarket.ru/catalog/details/komplekt-umnyh-datchikov-i-haba-sber-100058880808_40440/'))
#         c += 1
#         await asyncio.sleep(delay=1)
#     if d[2].get('vopros_3') == 'yes':
#         await cb.bot.send_message(chat_id=u.id,
#             text=fmt.hide_link(
#                 url='https://megamarket.ru/catalog/details/rozetka-umnaya-sber-sbdv-00123-100058872843_40440/'))
#         c += 1
#         await asyncio.sleep(delay=1)
#     if d[3].get('vopros_4') == 'yes':
#         await cb.bot.send_message(chat_id=u.id,
#             text=fmt.hide_link(
#                 url='https://megamarket.ru/catalog/details/umnaya-svetodiodnaya-lenta-sber-sbdv-00033-600005039388/'))
#         c += 1
#         await asyncio.sleep(delay=1)
#     if d[4].get('vopros_5') == 'yes':
#         await cb.bot.send_message(chat_id=u.id,
#             text=fmt.hide_link(
#                 url='https://megamarket.ru/catalog/details/umnaya-kolonka-sber-sberboom-galakticheskiy-siniy-100065009469/'))
#         c += 1
#     if c == 0:
#         await cb.bot.send_message(chat_id=u.id,
#             text=fmt.hide_link(
#                 url='https://megamarket.ru/catalog/details/umnaya-kolonka-sber-sberboom-galakticheskiy-siniy-100065009469/'))
#     await state.finish()


async def send_result(u, cb, state: FSMContext):
    log.info(u.info_user())
    log.info(' '.join([await state.get_state(), u.info_user()]))
    d = await state.get_data()
    c = 0
    save_res(u.id, d)
    if (str(d[0].values()) == "dict_values(['yes'])") & (str(d[1].values()) == "dict_values(['yes'])") & \
            (str(d[2].values()) == "dict_values(['yes'])") & (str(d[3].values()) == "dict_values(['yes'])") & \
            (str(d[4].values()) == "dict_values(['yes'])"):
        photo_file_id = get_photo('3in1')
        await cb.bot.send_photo(chat_id=u.id, photo=photo_file_id)
        await cb.bot.send_message(chat_id=u.id, text=fmt.text('Создайте свой умный дом по цене от 26610 руб.'))
    elif (str(d[0].values()) == "dict_values(['yes'])") & (str(d[1].values()) == "dict_values(['yes'])") & \
            (str(d[2].values()) == "dict_values(['yes'])") & (str(d[3].values()) == "dict_values(['no'])") & \
            (str(d[4].values()) == "dict_values(['no'])"):
        photo_file_id = get_photo('security')
        await cb.bot.send_photo(chat_id=u.id, photo=photo_file_id)
        await cb.bot.send_message(chat_id=u.id, text=fmt.text('Добавь безопасности и комфорта по цене от 10500 руб.'))
    elif (str(d[0].values()) == "dict_values(['no'])") & (str(d[1].values()) == "dict_values(['no'])") & \
            (str(d[2].values()) == "dict_values(['no'])") & (str(d[3].values()) == "dict_values(['yes'])") & \
            (str(d[4].values()) == "dict_values(['no'])"):
        photo_file_id = get_photo('light')
        await cb.bot.send_photo(chat_id=u.id, photo=photo_file_id)
        await cb.bot.send_message(chat_id=u.id, text=fmt.text('Добавь уюта в свой дом по цене от 6070 руб.'))
    elif (str(d[0].values()) == "dict_values(['no'])") & (str(d[1].values()) == "dict_values(['no'])") & \
            (str(d[2].values()) == "dict_values(['no'])") & (str(d[3].values()) == "dict_values(['no'])") & \
            (str(d[4].values()) == "dict_values(['no'])"):
        photo_file_id = get_photo('light')
        await cb.bot.send_photo(chat_id=u.id, photo=photo_file_id)
        await cb.bot.send_message(chat_id=u.id, text=fmt.text('Попробуйте с малого, сделайте вашу квартиру уютнее с \
        нашими лампочками и лентой по цене от 1480 руб.'))
    else:
        photo_file_id = get_photo('for_all')
        await cb.bot.send_photo(chat_id=u.id, photo=photo_file_id)
        await cb.bot.send_message(chat_id=u.id, text=fmt.text('Создайте дом, который заботится о Вас: сделает всё по \
        щелчку, уменьшит счёт за коммуналку, подсветит путь, развеет страхи и просто обновит обстановку'))
    await state.finish()
