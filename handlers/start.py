from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from utils.database import user_db
from utils.config import ROLE_USER, ROLE_ADMIN
from keyboards.main_menu import get_main_menu_keyboard
from texts.messages import WELCOME_MESSAGE, ACCESS_DENIED

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    """Обработчик команды /start"""
    telegram_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    
    # Проверяем существование пользователя
    if not user_db.user_exists(telegram_id):
        # Регистрируем нового пользователя
        user_db.create_user(
            telegram_id=telegram_id,
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        await message.answer(
            f"{WELCOME_MESSAGE}\n\n✅ Вы успешно зарегистрированы!",
            reply_markup=get_main_menu_keyboard()
        )
    else:
        # Получаем информацию о пользователе
        user = user_db.get_user(telegram_id)
        role = user.get('role', ROLE_USER)
        
        if role == ROLE_ADMIN:
            await message.answer(
                f"{WELCOME_MESSAGE}\n\n🔐 Доступ разрешен!",
                reply_markup=get_main_menu_keyboard()
            )
        else:
            await message.answer(ACCESS_DENIED) 