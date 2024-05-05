from bot_token import BOT_TOKEN, API
import asyncio
import logging
import requests
import json
from aiogram import Bot, Dispatcher, types, executor


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def cmd_start(message: types.Message):
    # markup = types.InlineKeyboardMarkup()
    # btn1 = types.KeyboardButton("ДА!", callback_data='yes')
    # btn2 = types.KeyboardButton("НЕТ!", callback_data='no')
    # markup.add(btn1, btn2)
    file = open('img/first_img.jpg', 'rb')
    text_1 = (f"Привет 👋🏻, <b>{message.chat.first_name}!</b> \n"
            "Это магазин дизайнерских вещей для дома")
    text_2 = ("<b>Из какого ты города? 🇷🇺</b>")
    await message.answer(text_1.upper())
    await message.answer_photo(file)
    await message.answer(text_2.upper())

@dp.message_handler(content_types=['text'])
async def cmd_name(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Картины из смолы", callback_data='paintings'))
    markup.add(types.InlineKeyboardButton("Вазы из гипса", callback_data='vases'))
    markup.add(types.InlineKeyboardButton("Уникальные часы", callback_data='clocks'))
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')

    data = res.json()
    print(data)
    text_3 = (f"<b>{message.chat.first_name}!</b>\n"
               f"выбирай, что ты хочешь купить для своего\n"
               f"любимого ❤️ дома")
    text_4 = (f'Сейчас в городе: <b>{city.capitalize()}</b> температура <b>{round(data["main"]["temp"], 1)}</b> градусов!')
    await message.answer(text_4)
    await message.answer(text_3.upper(), reply_markup=markup)


@dp.callback_query_handler()
async def callback(call):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Больше - на нашем сайте", url='https://github.com/Maxxx-VS?tab=repositorie'))
    file_1 = open('img/paint.jpg', 'rb')
    file_2 = open('img/vase.jpeg', 'rb')
    file_3 = open('img/clock.jpg', 'rb')
    if call.data == 'paintings':
        await call.message.answer_photo(file_1, reply_markup=markup)
    if call.data == 'vases':
        await call.message.answer_photo(file_2, reply_markup=markup)
    if call.data == 'clocks':
        await call.message.answer_photo(file_3, reply_markup=markup)













# Запуск процесса поллинга новых апдейтов
# executor.start_polling(dp)
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())