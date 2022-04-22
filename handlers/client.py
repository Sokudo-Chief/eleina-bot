from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from datebase import visitors as v
from datebase import books as b
from keyboards import kb_general

class FSMClient(StatesGroup):
    number = State()
    vis_name = State()
    surname = State()
    adress = State()

class FSMClient2(StatesGroup):
    name_book = State()
    author = State()
    toms = State()


async def send_welcome(message: types.Message):
    await message.reply("Привет, меня создал @sokudo_chief!", reply_markup=kb_general)

#---------------------------------------------------------------------

async def upload(message: types.Message):
    await FSMClient.number.set()
    await message.reply("Введите номер посетителя")

async def insert_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Номер'] = message.text
    await FSMClient.next()
    await message.reply("Введите имя посетителя")

async def insert_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Имя'] = message.text
    await FSMClient.next()
    await message.reply("Введите фамилию посетителя")

async def insert_surname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Фамилия'] = message.text
    await FSMClient.next()
    await message.reply("Введите адрес посетителя")

async def insert_adress(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Адрес'] = message.text
        number =  int(data.get('Номер'))
        name =  data.get('Имя')
        surname =  data.get('Фамилия')
        adress =  data.get('Адрес')
        record = [(number, name, surname, adress)]
        print(record)
        v.insert(record)
        await message.answer(str(record), reply_markup=kb_general)
    await message.answer('Посетитель добавлен')
    await state.finish()

#---------------------------------------------------------------------

async def upload2(message: types.Message):
    await FSMClient2.name_book.set()
    await message.reply("Введите название книги")

async def insert_name_book(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Имя'] = message.text
    await FSMClient2.next()
    await message.reply("Введите автора книги")

async def insert_author(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Автор'] = message.text
    await FSMClient2.next()
    await message.reply("Введите количество томов")

async def insert_toms(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Томы'] = message.text
        name = data.get('Имя')
        author = data.get('Автор')
        toms = int(data.get('Томы'))
        record = (b.maxID()+1, name, author, toms)
        print(record)
        b.insert(record)
        await message.answer(str(record), reply_markup=kb_general)
    await message.answer('Книга добавлена')
    await state.finish()

#---------------------------------------------------------------------

async def send_visitors(message: types.Message):
    visitors = v.SelectTable()
    answer = ''
    for visitor in visitors:
        answer = answer + str(visitor[0]) + ' ' + visitor[1] + ' ' + visitor[2] + ' ' + visitor[3] + '\n'
    print(answer)
    await message.reply(answer[:-1])

async def send_books(message: types.Message):
    books = b.SelectTable()
    answer = ''
    for book in books:
        answer = answer + str(book[0]) + ': "' + book[1] + '", ' + book[2] + ', ' + str(book[3]) + '\n'
    print(answer)
    await message.reply(answer[:-1])

#---------------------------------------------------------------------

async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("Отменено", reply_markup=kb_general)


async def echo(message: types.Message):
    await message.answer(message.text)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cancel, commands=['cancel'], state='*')
    dp.register_message_handler(cancel, Text(equals='cancel', ignore_case=True), state='*')

    dp.register_message_handler(send_welcome, commands=['start'])
    dp.register_message_handler(send_visitors, commands=['visitors'])
    dp.register_message_handler(send_books, commands=['books'])

    dp.register_message_handler(upload, commands=['visitor'], state=None)
    dp.register_message_handler(insert_number, state=FSMClient.number)
    dp.register_message_handler(insert_name, state=FSMClient.vis_name)
    dp.register_message_handler(insert_surname, state=FSMClient.surname)
    dp.register_message_handler(insert_adress, state=FSMClient.adress)

    dp.register_message_handler(upload2, commands=['book'], state=None)
    dp.register_message_handler(insert_name_book, state=FSMClient2.name_book)
    dp.register_message_handler(insert_author, state=FSMClient2.author)
    dp.register_message_handler(insert_toms, state=FSMClient2.toms)

    dp.register_message_handler(echo)
    
