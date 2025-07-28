from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.main_menu import get_main_menu_keyboard
from keyboards.pc_control import get_pc_control_keyboard
from texts.messages import MAIN_MENU, PC_CONTROL_MENU, DEVELOPERS_INFO, PROFILE_MENU
from utils.database import user_db

router = Router()

@router.callback_query(F.data == "main_menu")
async def main_menu_handler(callback: CallbackQuery):
    """Обработчик главного меню"""
    await callback.message.edit_text(
        MAIN_MENU,
        reply_markup=get_main_menu_keyboard()
    )

@router.callback_query(F.data == "pc_control")
async def pc_control_handler(callback: CallbackQuery):
    """Обработчик управления ПК"""
    await callback.message.edit_text(
        PC_CONTROL_MENU,
        reply_markup=get_pc_control_keyboard()
    )

@router.callback_query(F.data == "developers")
async def developers_handler(callback: CallbackQuery):
    """Обработчик информации о разработчиках"""
    await callback.message.edit_text(
        DEVELOPERS_INFO,
        reply_markup=get_main_menu_keyboard()
    )

@router.callback_query(F.data == "profile")
async def profile_handler(callback: CallbackQuery):
    """Обработчик профиля пользователя"""
    user = user_db.get_user(callback.from_user.id)
    if user:
        profile_text = PROFILE_MENU.format(
            telegram_id=user.get('telegramId', 'Не указано'),
            first_name=user.get('username', 'Не указано'),
            username=user.get('username', 'Не указано'),
            role=user.get('role', 'user'),
            created_at='База данных PostgreSQL'
        )
    else:
        profile_text = "❌ Профиль не найден в базе данных"
    
    await callback.message.edit_text(
        profile_text,
        reply_markup=get_main_menu_keyboard()
    ) 