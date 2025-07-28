from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.pc_control import get_logs_keyboard, get_pc_control_keyboard
from texts.messages import LOGS_MENU, API_ERROR
from utils.api_client import api_client

router = Router()

@router.callback_query(F.data == "logs")
async def logs_menu_handler(callback: CallbackQuery):
    """Обработчик меню логов"""
    await callback.message.edit_text(
        LOGS_MENU,
        reply_markup=get_logs_keyboard()
    )

@router.callback_query(F.data == "system_log")
async def system_log_handler(callback: CallbackQuery):
    """Обработчик системного лога"""
    logs = api_client.get_system_log()
    if logs:
        log_text = "📋 Системный лог (последние 10 записей):\n\n"
        for i, log in enumerate(logs[:10]):
            source = log.get('Source', 'Unknown')
            message = log.get('Message', 'No message')
            time = log.get('TimeGenerated', 'Unknown')
            
            log_text += f"{i+1}. {source}\n"
            log_text += f"   Время: {time}\n"
            log_text += f"   Сообщение: {message[:100]}...\n\n"
        
        if len(logs) > 10:
            log_text += f"... и еще {len(logs) - 10} записей"
        
        await callback.message.edit_text(
            log_text,
            reply_markup=get_logs_keyboard()
        )
    else:
        await callback.message.edit_text(
            API_ERROR,
            reply_markup=get_logs_keyboard()
        )

@router.callback_query(F.data == "network_log")
async def network_log_handler(callback: CallbackQuery):
    """Обработчик сетевого лога"""
    logs = api_client.get_network_log()
    if logs:
        log_text = "🌐 Сетевой лог (последние 10 записей):\n\n"
        for i, log in enumerate(logs[:10]):
            source = log.get('Source', 'Unknown')
            message = log.get('Message', 'No message')
            time = log.get('TimeGenerated', 'Unknown')
            
            log_text += f"{i+1}. {source}\n"
            log_text += f"   Время: {time}\n"
            log_text += f"   Сообщение: {message[:100]}...\n\n"
        
        if len(logs) > 10:
            log_text += f"... и еще {len(logs) - 10} записей"
        
        await callback.message.edit_text(
            log_text,
            reply_markup=get_logs_keyboard()
        )
    else:
        await callback.message.edit_text(
            API_ERROR,
            reply_markup=get_logs_keyboard()
        )

@router.callback_query(F.data == "event_log")
async def event_log_handler(callback: CallbackQuery):
    """Обработчик лога событий"""
    logs = api_client.get_event_log()
    if logs:
        log_text = "📝 Лог событий (последние 10 записей):\n\n"
        for i, log in enumerate(logs[:10]):
            source = log.get('Source', 'Unknown')
            message = log.get('Message', 'No message')
            time = log.get('TimeGenerated', 'Unknown')
            
            log_text += f"{i+1}. {source}\n"
            log_text += f"   Время: {time}\n"
            log_text += f"   Сообщение: {message[:100]}...\n\n"
        
        if len(logs) > 10:
            log_text += f"... и еще {len(logs) - 10} записей"
        
        await callback.message.edit_text(
            log_text,
            reply_markup=get_logs_keyboard()
        )
    else:
        await callback.message.edit_text(
            API_ERROR,
            reply_markup=get_logs_keyboard()
        )

@router.callback_query(F.data == "error_log")
async def error_log_handler(callback: CallbackQuery):
    """Обработчик лога ошибок"""
    logs = api_client.get_error_log()
    if logs:
        log_text = "❌ Лог ошибок (последние 10 записей):\n\n"
        for i, log in enumerate(logs[:10]):
            source = log.get('Source', 'Unknown')
            message = log.get('Message', 'No message')
            time = log.get('TimeGenerated', 'Unknown')
            
            log_text += f"{i+1}. {source}\n"
            log_text += f"   Время: {time}\n"
            log_text += f"   Сообщение: {message[:100]}...\n\n"
        
        if len(logs) > 10:
            log_text += f"... и еще {len(logs) - 10} записей"
        
        await callback.message.edit_text(
            log_text,
            reply_markup=get_logs_keyboard()
        )
    else:
        await callback.message.edit_text(
            API_ERROR,
            reply_markup=get_logs_keyboard()
        )

@router.callback_query(F.data == "login_log")
async def login_log_handler(callback: CallbackQuery):
    """Обработчик лога входов"""
    logs = api_client.get_login_log()
    if logs:
        log_text = "🔐 Лог входов (последние 10 записей):\n\n"
        for i, log in enumerate(logs[:10]):
            source = log.get('Source', 'Unknown')
            message = log.get('Message', 'No message')
            time = log.get('TimeGenerated', 'Unknown')
            
            log_text += f"{i+1}. {source}\n"
            log_text += f"   Время: {time}\n"
            log_text += f"   Сообщение: {message[:100]}...\n\n"
        
        if len(logs) > 10:
            log_text += f"... и еще {len(logs) - 10} записей"
        
        await callback.message.edit_text(
            log_text,
            reply_markup=get_logs_keyboard()
        )
    else:
        await callback.message.edit_text(
            API_ERROR,
            reply_markup=get_logs_keyboard()
        )

@router.callback_query(F.data == "file_open_log")
async def file_open_log_handler(callback: CallbackQuery):
    """Обработчик лога открытия файлов"""
    logs = api_client.get_file_open_log()
    if logs:
        log_text = "📁 Лог открытия файлов (последние 10 записей):\n\n"
        for i, log in enumerate(logs[:10]):
            source = log.get('Source', 'Unknown')
            message = log.get('Message', 'No message')
            time = log.get('TimeGenerated', 'Unknown')
            
            log_text += f"{i+1}. {source}\n"
            log_text += f"   Время: {time}\n"
            log_text += f"   Сообщение: {message[:100]}...\n\n"
        
        if len(logs) > 10:
            log_text += f"... и еще {len(logs) - 10} записей"
        
        await callback.message.edit_text(
            log_text,
            reply_markup=get_logs_keyboard()
        )
    else:
        await callback.message.edit_text(
            API_ERROR,
            reply_markup=get_logs_keyboard()
        ) 