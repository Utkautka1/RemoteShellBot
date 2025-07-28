from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_main_menu_keyboard() -> InlineKeyboardMarkup:
    """Создает клавиатуру главного меню"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🖥️ Управление ПК", callback_data="pc_control")],
            [InlineKeyboardButton(text="👨‍💻 Разработчики", callback_data="developers")],
            [InlineKeyboardButton(text="👤 Профиль", callback_data="profile")]
        ]
    )
    
    return keyboard 