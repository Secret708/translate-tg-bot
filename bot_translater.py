from googletrans import Translator
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.types import Message

TOKEN = "123456:SAGTWH&^$78654263sgdjd" # вставляете свой токен бота. Его надо взять у @BotFather

bot = Bot(token=TOKEN)
dp = Dispatcher()
text = ''
translator = Translator()
list_users = []  # список словарей вместо бд (просто лень было сделать с бд :D)
language_user = 'en'
lang = 'en'
response = 'Список пользователей:\n\n'
id_new_admin = None
ID_ADMINS = [123456789, 987654321]  # вставляете свои айди администраторов
languages = [
    'af',  # африкаанс
    'sq',  # албанский
    'am',  # амхарский
    'ar',  # арабский
    'hy',  # армянский
    'az',  # азербайджанский
    'eu',  # баскский
    'be',  # белорусский
    'bn',  # бенгальский
    'bs',  # боснийский
    'bg',  # болгарский
    'ca',  # каталанский
    'ceb',  # себуано (филиппинский)
    'ny',  # чичева (нъянджа)
    'zh-cn',  # китайский (упрощённый)
    'zh-tw',  # китайский (традиционный)
    'co',  # корсиканский
    'hr',  # хорватский
    'cs',  # чешский
    'da',  # датский
    'nl',  # голландский
    'en',  # английский
    'eo',  # эсперанто
    'et',  # эстонский
    'tl',  # филиппинский (тагальский)
    'fi',  # финский
    'fr',  # французский
    'fy',  # фризский
    'gl',  # галисийский
    'ka',  # грузинский
    'de',  # немецкий
    'el',  # греческий
    'gu',  # гуджарати
    'ht',  # гаитянский креольский
    'ha',  # хауса
    'haw',  # гавайский
    'he',  # иврит (ранее 'iw')
    'hi',  # хинди
    'hmn',  # хмонг
    'hu',  # венгерский
    'is',  # исландский
    'ig',  # игбо
    'id',  # индонезийский
    'ga',  # ирландский
    'it',  # итальянский
    'ja',  # японский
    'jw',  # яванский
    'kn',  # каннада
    'kk',  # казахский
    'km',  # кхмерский
    'rw',  # киньяруанда
    'ko',  # корейский
    'ku',  # курдский
    'ky',  # киргизский
    'lo',  # лаосский
    'la',  # латынь
    'lv',  # латышский
    'lt',  # литовский
    'lb',  # люксембургский
    'mk',  # македонский
    'mg',  # малагасийский
    'ms',  # малайский
    'ml',  # малаялам
    'mt',  # мальтийский
    'mi',  # маори
    'mr',  # маратхи
    'mn',  # монгольский
    'my',  # бирманский
    'ne',  # непальский
    'no',  # норвежский
    'or',  # ория
    'ps',  # пушту
    'fa',  # персидский
    'pl',  # польский
    'pt',  # португальский
    'pa',  # панджаби
    'ro',  # румынский
    'ru',  # русский
    'sm',  # самоанский
    'gd',  # шотландский (гэльский)
    'sr',  # сербский
    'st',  # сесото
    'sn',  # шона
    'sd',  # синдхи
    'si',  # сингальский
    'sk',  # словацкий
    'sl',  # словенский
    'so',  # сомалийский
    'es',  # испанский
    'su',  # сунданский
    'sw',  # суахили
    'sv',  # шведский
    'tg',  # таджикский
    'ta',  # тамильский
    'tt',  # татарский
    'te',  # телугу
    'th',  # тайский
    'tr',  # турецкий
    'tk',  # туркменский
    'uk',  # украинский
    'ur',  # урду
    'ug',  # уйгурский
    'uz',  # узбекский
    'vi',  # вьетнамский
    'cy',  # валлийский
    'xh',  # коса
    'yi',  # идиш
    'yo',  # йоруба
    'zu',  # зулу
]

languages_message = """    'af',     # африкаанс
    'sq',     # албанский
    'am',     # амхарский
    'ar',     # арабский
    'hy',     # армянский
    'az',     # азербайджанский
    'eu',     # баскский
    'be',     # белорусский
    'bn',     # бенгальский
    'bs',     # боснийский
    'bg',     # болгарский
    'ca',     # каталанский
    'ceb',    # себуано (филиппинский)
    'ny',     # чичева (нъянджа)
    'zh-cn',  # китайский (упрощённый)
    'zh-tw',  # китайский (традиционный)
    'co',     # корсиканский
    'hr',     # хорватский
    'cs',     # чешский
    'da',     # датский
    'nl',     # голландский
    'en',     # английский
    'eo',     # эсперанто
    'et',     # эстонский
    'tl',     # филиппинский (тагальский)
    'fi',     # финский
    'fr',     # французский
    'fy',     # фризский
    'gl',     # галисийский
    'ka',     # грузинский
    'de',     # немецкий
    'el',     # греческий
    'gu',     # гуджарати
    'ht',     # гаитянский креольский
    'ha',     # хауса
    'haw',    # гавайский
    'he',     # иврит (ранее 'iw')
    'hi',     # хинди
    'hmn',    # хмонг
    'hu',     # венгерский
    'is',     # исландский
    'ig',     # игбо
    'id',     # индонезийский
    'ga',     # ирландский
    'it',     # итальянский
    'ja',     # японский
    'jw',     # яванский
    'kn',     # каннада
    'kk',     # казахский
    'km',     # кхмерский
    'rw',     # киньяруанда
    'ko',     # корейский
    'ku',     # курдский
    'ky',     # киргизский
    'lo',     # лаосский
    'la',     # латынь
    'lv',     # латышский
    'lt',     # литовский
    'lb',     # люксембургский
    'mk',     # македонский
    'mg',     # малагасийский
    'ms',     # малайский
    'ml',     # малаялам
    'mt',     # мальтийский
    'mi',     # маори
    'mr',     # маратхи
    'mn',     # монгольский
    'my',     # бирманский
    'ne',     # непальский
    'no',     # норвежский
    'or',     # ория
    'ps',     # пушту
    'fa',     # персидский
    'pl',     # польский
    'pt',     # португальский
    'pa',     # панджаби
    'ro',     # румынский
    'ru',     # русский
    'sm',     # самоанский
    'gd',     # шотландский (гэльский)
    'sr',     # сербский
    'st',     # сесото
    'sn',     # шона
    'sd',     # синдхи
    'si',     # сингальский
    'sk',     # словацкий
    'sl',     # словенский
    'so',     # сомалийский
    'es',     # испанский
    'su',     # сунданский
    'sw',     # суахили
    'sv',     # шведский
    'tg',     # таджикский
    'ta',     # тамильский
    'tt',     # татарский
    'te',     # телугу
    'th',     # тайский
    'tr',     # турецкий
    'tk',     # туркменский
    'uk',     # украинский
    'ur',     # урду
    'ug',     # уйгурский
    'uz',     # узбекский
    'vi',     # вьетнамский
    'cy',     # валлийский
    'xh',     # коса
    'yi',     # идиш
    'yo',     # йоруба
    'zu',     # зулу"""


def lang_user(user_id):  # выводит язык пользователя
    for user in list_users:
        if user['id'] == user_id:
            return user['lang']

    return None


def user_in_dict(user_id):  # находит пользователя по его айди
    for user in list_users:
        if user['id'] == user_id:
            return user

    return None


def is_admin(user_id):  #
    return int(user_id) in ID_ADMINS


async def split_and_send_message(message: Message, text,
                                 max=3000):  # функция разделяет сообщение если оно больше 3000 символов
    if len(text) > 3000:
        for i in range(0, len(text), max):
            part = text[i:i + max]
            await message.answer(part)
    else:
        await message.answer(text)

@dp.message(lambda message: message.text == '/start')  # отправляет приветственное сообщение
async def start(message: Message):
    await message.answer(
        'Привет я бот переводчик напиши мне текст, а я переведу его. Чтобы настроить язык напиши /lang, а чтобы начать перевод текста напиши /translate <text>. Если вы хотите узнать все доступные языки, то напишите /languages')


@dp.message(lambda message: message.text.startswith('/translate'))  # переводит текст
async def language(message: Message):
    global text, language_user

    parts = message.text.split()

    if len(parts) > 1:
        try:
            text = " ".join(parts[1:])
        except Exception as e:
            print(f'Ошибка: {e}')

    user_id = message.from_user.id

    for lang in languages:
        if lang_user(user_id) == lang:
            language_user = lang

    text_translation = await translator.translate(text, dest=language_user)

    if text_translation.text:
        await split_and_send_message(message, text_translation.text)
    else:
        await message.answer('Вы не ввели текст или его не удалось перевести')

    text = ' '


@dp.message(lambda message: message.text == '/languages')  # выводит все доступные языки
async def language(message: Message):
    await message.answer(languages_message)


@dp.message(lambda message: message.text.startswith('/lang'))  # позволяет установить язык для перевода
async def set_language(message: Message):
    global lang

    parts = message.text.split()

    if len(parts) > 0:
        try:
            lang = " ".join(parts[1:])
        except Exception as e:
            print(f'Ошибка: {e}')

    user_id = message.from_user.id

    if user_in_dict(user_id):
        user_in_dict(user_id)['lang'] = lang
        await message.answer(f"Вы поменяли язык на {lang}")
    else:
        lang_user = {'id': user_id, 'lang': lang}
        list_users.append(lang_user)
        await message.answer(f"Вы установили язык {lang}")


@dp.message(lambda message: message.text == '/users')  # выводит историю всех пользователей, которые пользовались ботом
async def users(message: Message):
    global response

    user_id = message.from_user.id

    if user_id in ID_ADMINS:

        if list_users != []:
            for user in list_users:
                response += f"ID: {user['id']}, Язык пользователя: {user['lang']}, Admin: {is_admin(user['id'])}\n"

            await split_and_send_message(message, response)
        else:
            await message.answer('Пользователи не пользуются ботом')

    else:
        await message.answer('Вы не являетесь админом этого бота')


@dp.message(lambda message: message.text.startswith('/add_admin'))  # добавление новых админов
async def add_admin(message: Message):
    global id_new_admin
    user_id = message.from_user.id

    if user_id in ID_ADMINS:
        parts = message.text.split()

        if len(parts) > 0:
            try:
                id_new_admin = " ".join(parts[1:])
            except Exception as e:
                print(e)

        ID_ADMINS.append(int(id_new_admin))

        await message.answer('Новый админ бота')

        id_new_admin = None

    else:
        await message.answer('Вы не являетесь админом этого бота')


async def main():  # функция основного цикла программы
    while True:
        try:
            print('Запуск бота')
            await dp.start_polling(bot)
        except Exception as e:
            print(f'Ошибка: {e}')
            await asyncio.sleep(3)


if __name__ == "__main__":
    asyncio.run(main())