import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from utils.config import BOT_TOKEN

# Импортируем роутеры
from handlers.start import router as start_router
from handlers.menu import router as menu_router
from handlers.media import router as media_router
from handlers.power import router as power_router
from handlers.processes import router as processes_router
from handlers.monitor import router as monitor_router
from handlers.logs import router as logs_router
from handlers.system import router as system_router
from handlers.browser import router as browser_router

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def main():
    """Главная функция бота"""
    # Проверяем наличие токена
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN не найден в переменных окружения!")
        return
    
    # Создаем бота и диспетчер
    bot = Bot(token=BOT_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    
    # Регистрируем роутеры
    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(media_router)
    dp.include_router(power_router)
    dp.include_router(processes_router)
    dp.include_router(monitor_router)
    dp.include_router(logs_router)
    dp.include_router(system_router)
    dp.include_router(browser_router)
    
    # Запускаем бота
    logger.info("Бот запускается...")
    try:
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        logger.info("Бот остановлен пользователем")
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main()) 