from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.pc_control import get_browser_keyboard, get_pc_control_keyboard
from texts.messages import (
    BROWSER_MENU, BROWSER_HISTORY, CACHE_CLEARED, COOKIES_CLEARED,
    SITE_OPENED, PAGE_SAVED, TABS_LIST, TAB_CLOSED, FILE_DOWNLOADED,
    ENTER_URL, ENTER_SELECTOR, API_ERROR
)
from utils.api_client import api_client

router = Router()

class BrowserStates(StatesGroup):
    waiting_for_url = State()
    waiting_for_selector = State()

@router.callback_query(F.data == "browser")
async def browser_menu_handler(callback: CallbackQuery):
    """Обработчик меню браузера"""
    await callback.message.edit_text(
        BROWSER_MENU,
        reply_markup=get_browser_keyboard()
    )

@router.callback_query(F.data == "browser_history")
async def browser_history_handler(callback: CallbackQuery):
    """Обработчик истории браузера"""
    await callback.answer(BROWSER_HISTORY)
    
    history = api_client.get_browser_history()
    if history:
        history_text = "📚 История браузера (последние 10 записей):\n\n"
        for i, entry in enumerate(history[:10]):
            url = entry.get('url', 'Unknown')
            title = entry.get('title', 'No title')
            time = entry.get('last_visit_time', 'Unknown')
            
            history_text += f"{i+1}. {title}\n"
            history_text += f"   URL: {url}\n"
            history_text += f"   Время: {time}\n\n"
        
        if len(history) > 10:
            history_text += f"... и еще {len(history) - 10} записей"
        
        await callback.message.edit_text(
            history_text,
            reply_markup=get_browser_keyboard()
        )
    else:
        await callback.message.edit_text(
            API_ERROR,
            reply_markup=get_browser_keyboard()
        )

@router.callback_query(F.data == "clear_cache")
async def clear_cache_handler(callback: CallbackQuery):
    """Обработчик очистки кэша"""
    success = api_client.clear_browser_cache()
    if success:
        await callback.answer(CACHE_CLEARED)
        await callback.message.edit_text(
            CACHE_CLEARED,
            reply_markup=get_browser_keyboard()
        )
    else:
        await callback.answer(API_ERROR)

@router.callback_query(F.data == "clear_cookies")
async def clear_cookies_handler(callback: CallbackQuery):
    """Обработчик очистки куки"""
    success = api_client.clear_cookies()
    if success:
        await callback.answer(COOKIES_CLEARED)
        await callback.message.edit_text(
            COOKIES_CLEARED,
            reply_markup=get_browser_keyboard()
        )
    else:
        await callback.answer(API_ERROR)

@router.callback_query(F.data == "site_screenshot")
async def site_screenshot_handler(callback: CallbackQuery, state: FSMContext):
    """Обработчик скриншота сайта"""
    await callback.message.edit_text(
        "📸 Скриншот сайта\n\n" + ENTER_URL,
        reply_markup=get_browser_keyboard()
    )
    await state.set_state(BrowserStates.waiting_for_url)

@router.callback_query(F.data == "open_site")
async def open_site_handler(callback: CallbackQuery, state: FSMContext):
    """Обработчик открытия сайта"""
    await callback.message.edit_text(
        "🌐 Открыть сайт\n\n" + ENTER_URL,
        reply_markup=get_browser_keyboard()
    )
    await state.set_state(BrowserStates.waiting_for_url)

@router.callback_query(F.data == "save_page")
async def save_page_handler(callback: CallbackQuery, state: FSMContext):
    """Обработчик сохранения страницы"""
    await callback.message.edit_text(
        "💾 Сохранить страницу\n\n" + ENTER_URL,
        reply_markup=get_browser_keyboard()
    )
    await state.set_state(BrowserStates.waiting_for_url)

@router.callback_query(F.data == "open_tabs")
async def open_tabs_handler(callback: CallbackQuery):
    """Обработчик открытых вкладок"""
    await callback.answer(TABS_LIST)
    
    tabs = api_client.get_open_tabs()
    if tabs:
        tabs_text = "📑 Открытые вкладки:\n\n"
        for i, tab in enumerate(tabs[:10]):
            title = tab.get('MainWindowTitle', 'Unknown')
            pid = tab.get('Id', 'N/A')
            
            tabs_text += f"{i+1}. {title}\n"
            tabs_text += f"   PID: {pid}\n\n"
        
        if len(tabs) > 10:
            tabs_text += f"... и еще {len(tabs) - 10} вкладок"
        
        await callback.message.edit_text(
            tabs_text,
            reply_markup=get_browser_keyboard()
        )
    else:
        await callback.message.edit_text(
            API_ERROR,
            reply_markup=get_browser_keyboard()
        )

@router.callback_query(F.data == "download_file")
async def download_file_handler(callback: CallbackQuery, state: FSMContext):
    """Обработчик скачивания файла"""
    await callback.message.edit_text(
        "📥 Скачать файл\n\n" + ENTER_URL,
        reply_markup=get_browser_keyboard()
    )
    await state.set_state(BrowserStates.waiting_for_url)

@router.message(BrowserStates.waiting_for_url)
async def process_url(message: Message, state: FSMContext):
    """Обработка URL"""
    url = message.text.strip()
    
    # Определяем действие на основе состояния
    data = await state.get_data()
    action = data.get('action', 'open_site')
    
    if action == 'site_screenshot':
        file_path = api_client.save_site_screenshot(url)
        if file_path:
            await message.answer(f"📸 Скриншот сайта сохранен: {file_path}")
        else:
            await message.answer(API_ERROR)
    
    elif action == 'open_site':
        success = api_client.open_site(url)
        if success:
            await message.answer(SITE_OPENED)
        else:
            await message.answer(API_ERROR)
    
    elif action == 'save_page':
        file_path = api_client.save_page(url)
        if file_path:
            await message.answer(f"💾 Страница сохранена: {file_path}")
        else:
            await message.answer(API_ERROR)
    
    elif action == 'download_file':
        await state.update_data(url=url)
        await message.answer(
            "🎯 " + ENTER_SELECTOR,
            reply_markup=get_browser_keyboard()
        )
        await state.set_state(BrowserStates.waiting_for_selector)
        return
    
    await state.clear()

@router.message(BrowserStates.waiting_for_selector)
async def process_selector(message: Message, state: FSMContext):
    """Обработка CSS селектора"""
    selector = message.text.strip()
    data = await state.get_data()
    url = data.get('url')
    
    if url:
        download_path = api_client.download_from_site(url, selector)
        if download_path:
            await message.answer(f"📥 Файл скачан: {download_path}")
        else:
            await message.answer(API_ERROR)
    
    await state.clear() 