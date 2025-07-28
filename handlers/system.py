from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.pc_control import get_system_keyboard, get_pc_control_keyboard
from texts.messages import (
    SYSTEM_MENU, TEMP_CLEARED, RECYCLE_CLEARED, API_ERROR
)
from utils.api_client import api_client

router = Router()

@router.callback_query(F.data == "system")
async def system_menu_handler(callback: CallbackQuery):
    """Обработчик меню системных функций"""
    await callback.message.edit_text(
        SYSTEM_MENU,
        reply_markup=get_system_keyboard()
    )

@router.callback_query(F.data == "os_version")
async def os_version_handler(callback: CallbackQuery):
    """Обработчик версии ОС"""
    version = api_client.get_os_version()
    if version:
        await callback.answer(f"ℹ️ Версия ОС: {version}")
        await callback.message.edit_text(
            f"ℹ️ Версия ОС: {version}",
            reply_markup=get_system_keyboard()
        )
    else:
        await callback.answer(API_ERROR)

@router.callback_query(F.data == "arch")
async def arch_handler(callback: CallbackQuery):
    """Обработчик архитектуры"""
    arch = api_client.get_arch()
    if arch:
        await callback.answer(f"🏗️ Архитектура: {arch}")
        await callback.message.edit_text(
            f"🏗️ Архитектура: {arch}",
            reply_markup=get_system_keyboard()
        )
    else:
        await callback.answer(API_ERROR)

@router.callback_query(F.data == "clear_temp")
async def clear_temp_handler(callback: CallbackQuery):
    """Обработчик очистки временных файлов"""
    success = api_client.clear_temp()
    if success:
        await callback.answer(TEMP_CLEARED)
        await callback.message.edit_text(
            TEMP_CLEARED,
            reply_markup=get_system_keyboard()
        )
    else:
        await callback.answer(API_ERROR)

@router.callback_query(F.data == "clear_recycle")
async def clear_recycle_handler(callback: CallbackQuery):
    """Обработчик очистки корзины"""
    success = api_client.clear_recycle_bin()
    if success:
        await callback.answer(RECYCLE_CLEARED)
        await callback.message.edit_text(
            RECYCLE_CLEARED,
            reply_markup=get_system_keyboard()
        )
    else:
        await callback.answer(API_ERROR) 