from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.pc_control import get_monitor_keyboard, get_pc_control_keyboard
from texts.messages import (
    MONITOR_MENU, CPU_USAGE, RAM_USAGE, DISK_USAGE, API_ERROR
)
from utils.api_client import api_client

router = Router()

@router.callback_query(F.data == "monitor")
async def monitor_menu_handler(callback: CallbackQuery):
    """Обработчик меню мониторинга"""
    await callback.message.edit_text(
        MONITOR_MENU,
        reply_markup=get_monitor_keyboard()
    )

@router.callback_query(F.data == "cpu_usage")
async def cpu_usage_handler(callback: CallbackQuery):
    """Обработчик загрузки CPU"""
    cpu_usage = api_client.get_cpu_usage()
    if cpu_usage is not None and isinstance(cpu_usage, (int, float)):
        usage_percent = cpu_usage * 100
        await callback.answer(f"🖥️ CPU: {usage_percent:.1f}%")
        await callback.message.edit_text(
            CPU_USAGE.format(usage=f"{usage_percent:.1f}"),
            reply_markup=get_monitor_keyboard()
        )
    else:
        await callback.answer(API_ERROR)

@router.callback_query(F.data == "ram_usage")
async def ram_usage_handler(callback: CallbackQuery):
    """Обработчик загрузки RAM"""
    ram_usage = api_client.get_ram_usage()
    if ram_usage is not None and isinstance(ram_usage, (int, float)):
        usage_percent = ram_usage * 100
        await callback.answer(f"💾 RAM: {usage_percent:.1f}%")
        await callback.message.edit_text(
            RAM_USAGE.format(usage=f"{usage_percent:.1f}"),
            reply_markup=get_monitor_keyboard()
        )
    else:
        await callback.answer(API_ERROR)

@router.callback_query(F.data == "disk_usage")
async def disk_usage_handler(callback: CallbackQuery):
    """Обработчик использования диска"""
    disk_usage = api_client.get_disk_usage()
    if disk_usage and isinstance(disk_usage, dict):
        used = disk_usage.get('Used', disk_usage.get('used', 0))
        free = disk_usage.get('Free', disk_usage.get('free', 0))
        capacity = disk_usage.get('Capacity', disk_usage.get('capacity', 0))
        
        # Проверяем, что все значения не None и capacity > 0
        if used is not None and free is not None and capacity is not None and capacity > 0:
            usage_percent = (used / capacity) * 100
            used_gb = used / (1024**3)
            free_gb = free / (1024**3)
            capacity_gb = capacity / (1024**3)
            
            disk_info = f"💿 Использование диска:\n\n"
            disk_info += f"📊 Использовано: {usage_percent:.1f}%\n"
            disk_info += f"💾 Занято: {used_gb:.1f} GB\n"
            disk_info += f"🆓 Свободно: {free_gb:.1f} GB\n"
            disk_info += f"📦 Общий объем: {capacity_gb:.1f} GB"
            
            await callback.answer(f"💿 Диск: {usage_percent:.1f}%")
            await callback.message.edit_text(
                disk_info,
                reply_markup=get_monitor_keyboard()
            )
        else:
            await callback.answer("❌ Нет данных о диске")
    else:
        await callback.answer(API_ERROR) 