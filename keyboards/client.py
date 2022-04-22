from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_add_visitor = KeyboardButton('/visitor')
button_select_visitors = KeyboardButton('/visitors')
button_add_book = KeyboardButton('/book')
button_select_books = KeyboardButton('/books')
button_cancel = KeyboardButton('/cancel')

kb_general = ReplyKeyboardMarkup()
kb_general.add(button_add_visitor).add(button_add_book).add(button_select_visitors).add(button_select_books).add(button_cancel)
