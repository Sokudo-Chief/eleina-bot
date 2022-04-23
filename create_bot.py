from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage    # позволяет хранить данные в ОЗУ

API_TOKEN = '5139167255:AAEv-LJGt5ZugibYyzH0Cf8eGBj28_aolCA'

storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
