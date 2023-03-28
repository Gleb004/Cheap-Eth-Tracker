from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import json
from imaplib import IMAP4, IMAP4_SSL
from aiogram.utils.callback_data import CallbackData
import email
import requests
from bs4 import BeautifulSoup
import lxml
import time

bot = Bot(token="")
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.message):
    while True:
        req = requests.get('https://crypto.com/defi/dashboard/gas-fees')
        soup = BeautifulSoup(req.text, 'lxml')
        x = soup.find("span", {"class": "GasPriceText__GasValueText-sc-1erxzig-0 bHfMrr"})
        x = str(x)
        x = x.replace('<span class="GasPriceText__GasValueText-sc-1erxzig-0 bHfMrr">', '')
        x = x.replace('</span>', '')
        print(x)
        try:
            if int(x) <= 18: #lower than
                await message.answer('The gas is low enough')
                break
        except: pass
        time.sleep(2)

if __name__ == "__main__":
    executor.start_polling(dp)



