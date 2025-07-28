from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.pc_control import get_power_keyboard, get_pc_control_keyboard
from texts.messages import (
    POWER_MENU, SHUTDOWN_CONFIRM, REBOOT_CONFIRM, SLEEP_CONFIRM,
    LOCK_CONFIRM, LOGOUT_CONFIRM, SUCCESS_MESSAGE, API_ERROR
)
from utils.api_client import api_client

router = Router()

@router.callback_query(F.data == "power")
async def power_menu_handler(callback: CallbackQuery):
    """Обработчик меню управления питанием"""
    await callback.message.edit_text(
        POWER_MENU,
        reply_markup=get_power_keyboard()
    )

@router.callback_query(F.data == "reboot")
async def reboot_handler(callback: CallbackQuery):
    """Обработчик перезагрузки"""
    success = api_client.reboot_pc()
    if success:
        await callback.answer(REBOOT_CONFIRM)
        await callback.message.edit_text(
            REBOOT_CONFIRM,
            reply_markup=get_power_keyboard()
        )
    else:
        await callback.answer(API_ERROR)

@router.callback_query(F.data == "sleep")
async def sleep_handler(callback: CallbackQuery):
    """Обработчик перевода в сон"""
    success = api_client.sleep_pc()
    if success:
        await callback.answer(SLEEP_CONFIRM)
        await callback.message.edit_text(
            SLEEP_CONFIRM,
            reply_markup=get_power_keyboard()
        )
    else:
        await callback.answer(API_ERROR)

@router.callback_query(F.data == "lock")
async def lock_handler(callback: CallbackQuery):
    """Обработчик блокировки экрана"""
    success = api_client.lock_pc()
    if success:
        await callback.answer(LOCK_CONFIRM)
        await callback.message.edit_text(
            LOCK_CONFIRM,
            reply_markup=get_power_keyboard()
        )
    else:
        await callback.answer(API_ERROR)

@router.callback_query(F.data == "logout")
async def logout_handler(callback: CallbackQuery):
    """Обработчик завершения сеанса"""
    success = api_client.logout_pc()
    if success:
        await callback.answer(LOGOUT_CONFIRM)
        await callback.message.edit_text(
            LOGOUT_CONFIRM,
            reply_markup=get_power_keyboard()
        )
    else:
        await callback.answer(API_ERROR)

@router.callback_query(F.data == "current_user")
async def current_user_handler(callback: CallbackQuery):
    """Обработчик получения текущего пользователя"""
    user = api_client.get_current_user()
    if user:
        await callback.answer(f"👤 Текущий пользователь: {user}")
        await callback.message.edit_text(
            f"👤 Текущий пользователь: {user}",
            reply_markup=get_power_keyboard()
        )
    else:
        await callback.answer(API_ERROR)

@router.callback_query(F.data == "switch_user")
async def switch_user_handler(callback: CallbackQuery):
    """Обработчик смены пользователя"""
    success = api_client.switch_user()
    if success:
        await callback.answer("🔄 Пользователь сменен")
        await callback.message.edit_text(
            "🔄 Пользователь сменен",
            reply_markup=get_power_keyboard()
        )
    else:
        await callback.answer(API_ERROR) 