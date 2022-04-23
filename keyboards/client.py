from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_visitor = KeyboardButton('Visitors')
button_add_visitor = KeyboardButton('Add visitor')
button_search_visitor = KeyboardButton('Search visitor')
button_select_visitors = KeyboardButton('Show visitors')
button_book = KeyboardButton('Books')
button_add_book = KeyboardButton('Add book')
button_search_book = KeyboardButton('Search book')
button_select_books = KeyboardButton('Show books')
button_library = KeyboardButton('Library')
button_add_book_for_visitor = KeyboardButton('Add book for visitor')
button_search_library = KeyboardButton('Search library')
button_select_library = KeyboardButton('Show library')
button_cancel = KeyboardButton('Cancel')
button_menu = KeyboardButton('Menu')

kb_general = ReplyKeyboardMarkup(resize_keyboard=True)
kb_general = kb_general.add(button_visitor).add(button_book).add(button_library)

kb_visitor = ReplyKeyboardMarkup(resize_keyboard=True)
kb_visitor = kb_visitor.add(button_add_visitor).row(button_search_visitor, button_select_visitors).add(button_menu)

kb_book = ReplyKeyboardMarkup(resize_keyboard=True)
kb_book = kb_book.add(button_add_book).row(button_search_book, button_select_books).add(button_menu)

kb_library = ReplyKeyboardMarkup(resize_keyboard=True)
kb_library = kb_library.add(button_add_book_for_visitor).row(button_search_library, button_select_library).add(button_menu)

kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel.add(button_cancel)