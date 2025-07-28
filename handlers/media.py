from aiogram import Router, F
from aiogram.types import CallbackQuery, Message, BufferedInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.pc_control import get_media_keyboard, get_pc_control_keyboard
from texts.messages import (
    MEDIA_MENU, SCREENSHOT_SUCCESS, ACTIVE_SCREENSHOT_SUCCESS,
    VIDEO_RECORDING, AUDIO_RECORDING, INTERVAL_PHOTO,
    ENTER_DURATION, ENTER_FPS, ENTER_INTERVAL, ENTER_COUNT,
    ERROR_MESSAGE, API_ERROR
)
from utils.api_client import api_client

router = Router()

class MediaStates(StatesGroup):
    waiting_for_duration = State()
    waiting_for_fps = State()
    waiting_for_interval = State()
    waiting_for_count = State()

@router.callback_query(F.data == "media")
async def media_menu_handler(callback: CallbackQuery):
    """Обработчик меню медиа функций"""
    await callback.message.edit_text(
        MEDIA_MENU,
        reply_markup=get_media_keyboard()
    )

@router.callback_query(F.data == "screenshot")
async def screenshot_handler(callback: CallbackQuery):
    """Обработчик скриншота экрана"""
    await callback.answer(SCREENSHOT_SUCCESS)
    
    try:
        screenshot_data = api_client.get_screenshot()
        if screenshot_data and isinstance(screenshot_data, bytes):
            # Создаем BufferedInputFile из байтов
            photo_file = BufferedInputFile(screenshot_data, filename="screenshot.png")
            await callback.message.answer_photo(
                photo=photo_file,
                caption="📸 Скриншот экрана"
            )
        else:
            await callback.message.answer("❌ Не удалось получить скриншот")
    except Exception as e:
        await callback.message.answer(f"❌ Ошибка при создании скриншота: {str(e)}")

@router.callback_query(F.data == "screenshot_active")
async def screenshot_active_handler(callback: CallbackQuery):
    """Обработчик скриншота активного окна"""
    await callback.answer(ACTIVE_SCREENSHOT_SUCCESS)
    
    try:
        screenshot_data = api_client.get_active_screenshot()
        if screenshot_data and isinstance(screenshot_data, bytes):
            # Создаем BufferedInputFile из байтов
            photo_file = BufferedInputFile(screenshot_data, filename="active_screenshot.png")
            await callback.message.answer_photo(
                photo=photo_file,
                caption="🖼️ Скриншот активного окна"
            )
        else:
            await callback.message.answer("❌ Не удалось получить скриншот активного окна")
    except Exception as e:
        await callback.message.answer(f"❌ Ошибка при создании скриншота: {str(e)}")

@router.callback_query(F.data == "record_video")
async def record_video_handler(callback: CallbackQuery, state: FSMContext):
    """Обработчик записи видео"""
    await callback.message.edit_text(
        "🎥 Запись видео\n\n" + ENTER_DURATION,
        reply_markup=get_media_keyboard()
    )
    await state.set_state(MediaStates.waiting_for_duration)

@router.message(MediaStates.waiting_for_duration)
async def process_video_duration(message: Message, state: FSMContext):
    """Обработка длительности видео"""
    try:
        duration = int(message.text)
        if duration <= 0 or duration > 60:
            await message.answer("❌ Длительность должна быть от 1 до 60 секунд")
            return
        
        await state.update_data(duration=duration)
        await message.answer(
            "🎬 " + ENTER_FPS,
            reply_markup=get_media_keyboard()
        )
        await state.set_state(MediaStates.waiting_for_fps)
    except ValueError:
        await message.answer("❌ Введите корректное число")

@router.message(MediaStates.waiting_for_fps)
async def process_video_fps(message: Message, state: FSMContext):
    """Обработка FPS для видео"""
    try:
        fps = int(message.text)
        if fps < 1 or fps > 120:
            await message.answer("❌ FPS должен быть от 1 до 120")
            return
        
        data = await state.get_data()
        duration = data.get('duration', 5)
        
        video_data = api_client.record_video(duration, fps)
        if video_data and isinstance(video_data, bytes):
            # Создаем BufferedInputFile из байтов
            video_file = BufferedInputFile(video_data, filename="video.mp4")
            await message.answer_video(
                video=video_file,
                caption=f"🎥 Видео ({duration}с, {fps}fps)"
            )
        else:
            await message.answer("❌ Не удалось получить видео данные")
        
        await state.clear()
    except ValueError:
        await message.answer("❌ Введите корректное число")
    except Exception as e:
        await message.answer(f"❌ Ошибка при записи видео: {str(e)}")
        await state.clear()

@router.callback_query(F.data == "record_audio")
async def record_audio_handler(callback: CallbackQuery, state: FSMContext):
    """Обработчик записи аудио"""
    await callback.message.edit_text(
        "🎤 Запись аудио\n\n" + ENTER_DURATION,
        reply_markup=get_media_keyboard()
    )
    await state.set_state(MediaStates.waiting_for_duration)

@router.callback_query(F.data == "interval_photo")
async def interval_photo_handler(callback: CallbackQuery, state: FSMContext):
    """Обработчик интервальных фото"""
    await callback.message.edit_text(
        "📷 Интервальные фото\n\n" + ENTER_INTERVAL,
        reply_markup=get_media_keyboard()
    )
    await state.set_state(MediaStates.waiting_for_interval)

@router.message(MediaStates.waiting_for_interval)
async def process_interval(message: Message, state: FSMContext):
    """Обработка интервала между фото"""
    try:
        interval = int(message.text)
        if interval < 100 or interval > 10000:
            await message.answer("❌ Интервал должен быть от 100 до 10000 мс")
            return
        
        await state.update_data(interval=interval)
        await message.answer(
            "📸 " + ENTER_COUNT,
            reply_markup=get_media_keyboard()
        )
        await state.set_state(MediaStates.waiting_for_count)
    except ValueError:
        await message.answer("❌ Введите корректное число")

@router.message(MediaStates.waiting_for_count)
async def process_count(message: Message, state: FSMContext):
    """Обработка количества фото"""
    try:
        count = int(message.text)
        if count < 1 or count > 50:
            await message.answer("❌ Количество должно быть от 1 до 50")
            return
        
        data = await state.get_data()
        interval = data.get('interval', 1000)
        
        photo_data = api_client.interval_photo(interval, count)
        if photo_data and isinstance(photo_data, bytes):
            # Создаем BufferedInputFile из байтов
            photo_file = BufferedInputFile(photo_data, filename="interval_photos.zip")
            await message.answer_document(
                document=photo_file,
                caption=f"📷 Интервальные фото ({count} шт., интервал {interval}мс)"
            )
        else:
            await message.answer("❌ Не удалось получить данные фото")
        
        await state.clear()
    except ValueError:
        await message.answer("❌ Введите корректное число")
    except Exception as e:
        await message.answer(f"❌ Ошибка при создании фото: {str(e)}")
        await state.clear() 