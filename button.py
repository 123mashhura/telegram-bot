Ahmedov_54🌗, [29.11.2024 16:57]
import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from config import BOT_TOKEN as token
from button import *
bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(Command('start'))
async def StartCommand(message: Message):
    await message.answer_photo(photo='https://www.restroapp.com/blog/wp-content/uploads/2020/03/online-food-ordering-statistics-RestroApp.jpg',caption='Online Food ga xush kelibsiz',reply_markup=menyu)


@dp.message(F.text =='Taomlar')
async def taomlar1(message: Message):
    await message.answer_photo(photo='https://www.restroapp.com/blog/wp-content/uploads/2020/03/online-food-ordering-statistics-RestroApp.jpg',caption='Taomlardan birini tanlang',reply_markup=taomlar2)

@dp.message(F.text == 'Aloqa')
async def aloqa(message: Message):
    await message.answer(text='https://t.me/Xudashukur',reply_markup=menyu)

@dp.message(F.text =='Osh')
async def taomlar1(message: Message):
    await message.answer_photo(photo='https://main-cdn.sbermegamarket.ru/upload/photo_2024_04_05_110642_660fb112f7f91.jpg',caption='Osh (/ɒʃ/, Kyrgyz: [ɔɕ], Russian: [oʂ]) is the second-largest city in Kyrgyzstan, located in the Fergana Valley in the south of the country. It is often referred to as the "capital of the south".[4] It is the oldest city in the country (estimated by UNESCO[5] to be more than 3,000 years old) and has served as the administrative center of Osh Region since 1939. The city has an ethnically mixed population of 322,164 in 2021,[3] comprising Kyrgyz, Uzbeks, Ukrainians, Koreans, and other smaller ethnic groups.',reply_markup=taomlar2)



@dp.message(F.text == 'Lavash')
async def taomlar1(x:Message):
    await x.answer_photo(photo='https://i.ytimg.com/vi/17Q4gdwsUM8/maxresdefault.jpg',caption='Lavash (Armenian: լավաշ; Persian: نان لواش) is a thin flatbread[9] usually leavened, traditionally baked in a tandoor (tonir or tanoor) or on a sajj, and common to the cuisines of South Caucasus, West Asia, and the areas surrounding the Caspian Sea.[10][11][12] Lavash is one of the most widespread types of bread in Armenia, Azerbaijan, Iran and Turkey.[13] The traditional recipe can be adapted to the modern kitchen by using a griddle or wok instead of the tonir.[14]',reply_markup=taomlar2)

@dp.message(F.text == 'KFC')
async def taomlar1(x:Message):
    await x.answer_photo(photo='https://i.ytimg.com/vi/17Q4gdwsUM8/maxresdefault.jpg',caption='Lavash (Armenian: լավաշ; Persian: نان لواش) is a thin flatbread[9] usually leavened, traditionally baked in a tandoor (tonir or tanoor) or on a sajj, and common to the cuisines of South Caucasus, West Asia, and the areas surrounding the Caspian Sea.[10][11][12] Lavash is one of the most widespread types of bread in Armenia, Azerbaijan, Iran and Turkey.[13] The traditional recipe can be adapted to the modern kitchen by using a griddle or wok instead of the tonir.[14]',reply_markup=taomlar2)

@dp.message(F.text == 'Shashlik')
async def taomlar1(x:Message):
    await x.answer_photo(photo='https://fs.tonkosti.ru/4j/9y/4j9yrc1l070gs0cgkgkw080gg.jpg',caption='''Kebab (UK: /kɪˈbæb/, US: /kɪˈbɑːb/; Persian: كباب,[1] kabāb, Arabic: كباب,[2] [kaˈbaːb]; Turkish: kebap, [kebɑp]), kabob (North American), kebap, kebob, or kabab (Kashmir) is a variety of roasted meat dishes that originated in the Middle East.

Kebabs consist of cut up ground meat, sometimes with vegetables and various other accompaniments according to the specific recipe. Although kebabs are typically cooked on a skewer over a fire, some kebab dishes are oven-baked in a pan, or prepared as a stew such as tas kebab.[3][4] The traditional meat for kebabs is most often lamb meat, but regional recipes may include beef, goat, chicken, fish, or even pork (depending on whether or not there are specific religious prohibitions).''',reply_markup=taomlar2)

Ahmedov_54🌗, [29.11.2024 16:57]


@dp.message(F.text =='Ortga')
async def taomlar1(message: Message):
    await message.answer(text='Assosiy menyu',reply_markup=menyu)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())