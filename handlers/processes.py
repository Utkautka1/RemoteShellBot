from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.pc_control import get_processes_keyboard, get_pc_control_keyboard
from texts.messages import (
    PROCESSES_MENU, PROCESS_LIST, PROCESS_KILLED, PROCESS_STARTED,
    ENTER_PROCESS_NAME, ENTER_PROCESS_PATH, API_ERROR
)
from utils.api_client import api_client

router = Router()

class ProcessStates(StatesGroup):
    waiting_for_process_name = State()
    waiting_for_process_path = State()

@router.callback_query(F.data == "processes")
async def processes_menu_handler(callback: CallbackQuery):
    """Обработчик меню управления процессами"""
    await callback.message.edit_text(
        PROCESSES_MENU,
        reply_markup=get_processes_keyboard()
    )

@router.callback_query(F.data == "list_processes")
async def list_processes_handler(callback: CallbackQuery):
    """Обработчик списка процессов"""
    await callback.answer(PROCESS_LIST)
    
    processes = api_client.list_processes()
    if processes:
        # Формируем список процессов (ограничиваем для читаемости)
        process_list = "📋 Список процессов:\n\n"
        for i, process in enumerate(processes[:20]):  # Показываем первые 20
            name = process.get('ProcessName', 'Unknown')
            pid = process.get('Id', 'N/A')
            cpu = process.get('CPU', 0)
            memory = process.get('WS', 0)
            
            # Безопасное форматирование с проверкой на None
            cpu_str = f"{cpu:.2f}%" if cpu is not None else "N/A"
            memory_str = f"{memory/1024/1024:.1f}MB" if memory is not None else "N/A"
            
            process_list += f"{i+1}. {name} (PID: {pid})\n"
            process_list += f"   CPU: {cpu_str}, Memory: {memory_str}\n\n"
        
        if len(processes) > 20:
            process_list += f"... и еще {len(processes) - 20} процессов"
        
        await callback.message.edit_text(
            process_list,
            reply_markup=get_processes_keyboard()
        )
    else:
        await callback.message.edit_text(
            API_ERROR,
            reply_markup=get_processes_keyboard()
        )

@router.callback_query(F.data == "find_pid")
async def find_pid_handler(callback: CallbackQuery, state: FSMContext):
    """Обработчик поиска PID процесса"""
    await callback.message.edit_text(
        ENTER_PROCESS_NAME,
        reply_markup=get_processes_keyboard()
    )
    await state.set_state(ProcessStates.waiting_for_process_name)

@router.message(ProcessStates.waiting_for_process_name)
async def process_name_handler(message: Message, state: FSMContext):
    """Обработка имени процесса для поиска PID"""
    process_name = message.text.strip()
    
    pid = api_client.get_process_pid(process_name)
    if pid:
        await message.answer(f"🔍 PID процесса '{process_name}': {pid}")
    else:
        await message.answer(f"❌ Процесс '{process_name}' не найден")
    
    await state.clear()

@router.callback_query(F.data == "start_process")
async def start_process_handler(callback: CallbackQuery, state: FSMContext):
    """Обработчик запуска процесса"""
    await callback.message.edit_text(
        ENTER_PROCESS_PATH,
        reply_markup=get_processes_keyboard()
    )
    await state.set_state(ProcessStates.waiting_for_process_path)

@router.message(ProcessStates.waiting_for_process_path)
async def process_path_handler(message: Message, state: FSMContext):
    """Обработка пути к процессу"""
    process_path = message.text.strip()
    
    success = api_client.start_process(process_path)
    if success:
        await message.answer(PROCESS_STARTED)
    else:
        await message.answer(API_ERROR)
    
    await state.clear() 