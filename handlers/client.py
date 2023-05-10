from aiogram import types, Dispatcher
from keyboards import sis_ad, python, alg_log, vr_ar, cyber, menu, fields, podacha
from create import bot, dp


date = dict()
INFO = '''
Приглашаем вас на обучение в IT-куб😁Теперь выбрать направление, ознакомиться с ним и подать заявление в разы проще!
От вас требуется лишь принять правильное решение, выбрать направление, заполнить анкету через бота и приехать с этим документам к нам!😀/menu , чтобы узнать больше!'''


# @dp.callback_query_handler(lambda c: c.data and c.data.startswith('f_'))
async def fields2(c: types.CallbackQuery):
    field = c.data[-2:]
    if field == 'sa':
        info = open('documents/sis.txt', 'rb').read().decode("UTF-8")
        await bot.send_message(c.from_user.id, text=info, reply_markup=sis_ad)
    elif field == 'py':
        info = open('documents/pyth.txt', 'rb').read().decode("UTF-8")
        await bot.send_message(c.from_user.id, text=info, reply_markup=python)
    elif field == 'al':
        info = open('documents/alg.txt', 'rb').read().decode("UTF-8")
        await bot.send_message(c.from_user.id, text=info, reply_markup=alg_log)
    elif field == 'vr':
        info = open('documents/vr.txt', 'rb').read().decode("UTF-8")
        await bot.send_message(c.from_user.id, text=info, reply_markup=vr_ar)
    elif field == 'cb':
        info = open('documents/cybergig.txt', 'rb').read().decode("UTF-8")
        await bot.send_message(c.from_user.id, text=info, reply_markup=cyber)
    date[c.from_user.id] = dict()
    await bot.answer_callback_query(c.id)


# @dp.callback_query_handler(lambda c: c.data == 'zayava')
async def zayava(c: types.CallbackQuery):
    doc = open('../documents/byudzhet-kub.docx', 'rb')
    await bot.send_document(chat_id=c.from_user.id, document=doc)
    await bot.answer_callback_query(c.id)


# @dp.message_handler(commands='start')
async def start(m: types.Message):
    date = int(m.date.hour)
    hello = ''
    if date in range(5, 13):
        hello = 'Доброе утро!'
    elif date in range(13, 18):
        hello = 'Добрый день!'
    elif date in range(18, 23):
        hello = 'Добрый вечер!'
    else:
        hello = 'Доброй ночи!'
    photo = open('photos/itcube.jpg', 'rb')
    await bot.send_photo(m.chat.id, photo, hello + ' ' + INFO, reply_markup=menu)


# @dp.message_handler(lambda m: m.text == 'Выбрать направление🎓')
async def field(m: types.Message):
    await m.answer('Выбираем!', reply_markup=fields)


# @dp.message_handler(lambda m: m.text == 'Отмена❌')
async def close(m: types.Message):
    remove = types.ReplyKeyboardRemove()
    await m.answer('Отменено', reply_markup=remove)


# dp.message_handler(lambda m: m.text == 'Поступить в IT-куб!')
async def podacha_zayavki(m: types.Message):
    await m.answer('Вы всего в нескольких шагах от поступления!!!!', reply_markup=podacha)


def reg_client_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(fields2, lambda c: c.data and c.data.startswith('f_'))
    # dp.register_callback_query_handler(zayava, lambda c: c.data == 'zayava')
    dp.register_message_handler(start, commands='start')
    dp.register_message_handler(field, lambda m: m.text == 'Узнать о направлениях🎓')
    dp.register_message_handler(podacha_zayavki, lambda m: m.text == 'Поступить в IT-куб!')
    dp.register_message_handler(close, lambda m: m.text == 'Отмена❌')
