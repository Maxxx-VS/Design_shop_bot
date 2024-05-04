from bot_token import BOT_TOKEN
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, executor


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def cmd_start(message: types.Message):
    file = open('img/first_img.jpg', 'rb')
    text = "Привет!\nВы посетил магазин дизайнерских вещей для дома"
    await message.answer(text.upper())
    await message.answer_photo(file)











# executor.start_polling(dp)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())