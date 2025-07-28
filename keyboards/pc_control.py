from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_pc_control_keyboard() -> InlineKeyboardMarkup:
    """Создает клавиатуру управления ПК"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📸 Медиа", callback_data="media"),
                InlineKeyboardButton(text="⚡ Питание", callback_data="power")
            ],
            [
                InlineKeyboardButton(text="🔄 Процессы", callback_data="processes"),
                InlineKeyboardButton(text="📊 Мониторинг", callback_data="monitor")
            ],
            [
                InlineKeyboardButton(text="📋 Логи", callback_data="logs"),
                InlineKeyboardButton(text="⚙️ Система", callback_data="system")
            ],
            [
                InlineKeyboardButton(text="🌐 Браузер", callback_data="browser")
            ],
            [
                InlineKeyboardButton(text="🔙 Назад", callback_data="main_menu")
            ]
        ]
    )
    
    return keyboard

def get_media_keyboard() -> InlineKeyboardMarkup:
    """Создает клавиатуру медиа функций"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📸 Скриншот экрана", callback_data="screenshot"),
                InlineKeyboardButton(text="🖼️ Скриншот окна", callback_data="screenshot_active")
            ],
            [
                InlineKeyboardButton(text="🎥 Записать видео", callback_data="record_video"),
                InlineKeyboardButton(text="🎤 Записать аудио", callback_data="record_audio")
            ],
            [
                InlineKeyboardButton(text="📷 Интервальные фото", callback_data="interval_photo")
            ],
            [
                InlineKeyboardButton(text="🔙 Назад", callback_data="pc_control")
            ]
        ]
    )
    
    return keyboard

def get_power_keyboard() -> InlineKeyboardMarkup:
    """Создает клавиатуру управления питанием"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🔄 Перезагрузка", callback_data="reboot"),
                InlineKeyboardButton(text="⏰ Сон", callback_data="sleep")
            ],
            [
                InlineKeyboardButton(text="🔒 Блокировка", callback_data="lock"),
                InlineKeyboardButton(text="🚪 Выход", callback_data="logout")
            ],
            [
                InlineKeyboardButton(text="👤 Текущий пользователь", callback_data="current_user")
            ],
            [
                InlineKeyboardButton(text="🔄 Сменить пользователя", callback_data="switch_user")
            ],
            [
                InlineKeyboardButton(text="🔙 Назад", callback_data="pc_control")
            ]
        ]
    )
    
    return keyboard

def get_processes_keyboard() -> InlineKeyboardMarkup:
    """Создает клавиатуру управления процессами"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📋 Список процессов", callback_data="list_processes"),
                InlineKeyboardButton(text="🔍 Найти PID", callback_data="find_pid")
            ],
            [
                InlineKeyboardButton(text="▶️ Запустить процесс", callback_data="start_process")
            ],
            [
                InlineKeyboardButton(text="🔙 Назад", callback_data="pc_control")
            ]
        ]
    )
    
    return keyboard

def get_monitor_keyboard() -> InlineKeyboardMarkup:
    """Создает клавиатуру мониторинга"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🖥️ CPU", callback_data="cpu_usage"),
                InlineKeyboardButton(text="💾 RAM", callback_data="ram_usage")
            ],
            [
                InlineKeyboardButton(text="💿 Диск", callback_data="disk_usage")
            ],
            [
                InlineKeyboardButton(text="🔙 Назад", callback_data="pc_control")
            ]
        ]
    )
    
    return keyboard

def get_logs_keyboard() -> InlineKeyboardMarkup:
    """Создает клавиатуру логов"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📋 Системный лог", callback_data="system_log"),
                InlineKeyboardButton(text="🌐 Сетевой лог", callback_data="network_log")
            ],
            [
                InlineKeyboardButton(text="📝 Лог событий", callback_data="event_log"),
                InlineKeyboardButton(text="❌ Лог ошибок", callback_data="error_log")
            ],
            [
                InlineKeyboardButton(text="🔐 Лог входов", callback_data="login_log"),
                InlineKeyboardButton(text="📁 Лог файлов", callback_data="file_open_log")
            ],
            [
                InlineKeyboardButton(text="🔙 Назад", callback_data="pc_control")
            ]
        ]
    )
    
    return keyboard

def get_system_keyboard() -> InlineKeyboardMarkup:
    """Создает клавиатуру системных функций"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="ℹ️ Версия ОС", callback_data="os_version"),
                InlineKeyboardButton(text="🏗️ Архитектура", callback_data="arch")
            ],
            [
                InlineKeyboardButton(text="🗑️ Очистить temp", callback_data="clear_temp"),
                InlineKeyboardButton(text="🗑️ Очистить корзину", callback_data="clear_recycle")
            ],
            [
                InlineKeyboardButton(text="🔙 Назад", callback_data="pc_control")
            ]
        ]
    )
    
    return keyboard

def get_browser_keyboard() -> InlineKeyboardMarkup:
    """Создает клавиатуру браузера"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📚 История", callback_data="browser_history"),
                InlineKeyboardButton(text="🗑️ Очистить кэш", callback_data="clear_cache")
            ],
            [
                InlineKeyboardButton(text="🍪 Очистить куки", callback_data="clear_cookies"),
                InlineKeyboardButton(text="📸 Скриншот сайта", callback_data="site_screenshot")
            ],
            [
                InlineKeyboardButton(text="🌐 Открыть сайт", callback_data="open_site"),
                InlineKeyboardButton(text="💾 Сохранить страницу", callback_data="save_page")
            ],
            [
                InlineKeyboardButton(text="📑 Открытые вкладки", callback_data="open_tabs"),
                InlineKeyboardButton(text="📥 Скачать файл", callback_data="download_file")
            ],
            [
                InlineKeyboardButton(text="🔙 Назад", callback_data="pc_control")
            ]
        ]
    )
    
    return keyboard 