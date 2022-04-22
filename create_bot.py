from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage    # позволяет хранить данные в ОЗУ

API_TOKEN = '5139167255:AAH2Us5ha8MxcrW-UTaetjk-oxgVcqlVagw'

storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
