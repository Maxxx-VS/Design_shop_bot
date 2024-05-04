from bot_token import BOT_TOKEN
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, executor


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def cmd_start(message: types.Message):
    file = open('img/first_img.jpg', 'rb')
    text_1 = ("<b>Привет!👋🏻\n"
            "Это магазин дизайнерских вещей для дома</b>")
    text_2 = ("<b>Напиши своё имя</b>")
    await message.answer(text_1.upper())
    await message.answer_photo(file)
    await message.answer(text_2.upper())

@dp.message_handler(content_types='text')
async def cmd_name(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Картины из смолы", callback_data='paintings'))
    markup.add(types.InlineKeyboardButton("Вазы из гипса", callback_data='vases'))
    markup.add(types.InlineKeyboardButton("Уникальные часы", callback_data='clocks'))
    text_3 = (f"<b>Привет{1}!\n"
               f"выбирай, что ты хочешь купить для своего\n"
               f"любимого ❤️ дома</b>")
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











# executor.start_polling(dp)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())