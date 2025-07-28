import requests
import time
from typing import Optional, List, Dict, Any
from .config import API_BASE_URL

class APIClient:
    """Клиент для работы с API сервером"""
    
    def __init__(self, base_url: str = API_BASE_URL):
        self.base_url = base_url.rstrip('/')
    
    def _make_request(self, method: str, endpoint: str, **kwargs) -> Optional[Any]:
        """Выполняет HTTP запрос к API"""
        try:
            response = requests.request(method, f"{self.base_url}{endpoint}", **kwargs)
            if response.status_code == 200:
                return response.json() if response.headers.get('content-type', '').startswith('application/json') else response.content
            else:
                print(f"Ошибка API запроса: {response.status_code} {response.reason} для url: {response.url}")
                return None
        except Exception as e:
            print(f"Ошибка подключения к API серверу: {e}")
            return None

    # Media endpoints
    def get_screenshot(self) -> Optional[bytes]:
        """Получает скриншот экрана"""
        return self._make_request('GET', '/media/screenshot')

    def get_active_screenshot(self) -> Optional[bytes]:
        """Получает скриншот активного окна"""
        return self._make_request('GET', '/media/screenshot-active')

    def record_video(self, duration: int = 5, fps: int = 30) -> Optional[bytes]:
        """Записывает видео"""
        try:
            # Используем GET запрос с query параметрами
            response = requests.get(f"{self.base_url}/media/record-video", params={
                'duration': duration,
                'fps': fps
            })
            
            if response.status_code == 200:
                return response.content
            else:
                print(f"Ошибка записи видео: {response.status_code}")
                return None
        except Exception as e:
            print(f"Ошибка при записи видео: {e}")
            return None

    def record_audio(self, duration: int = 5) -> Optional[bytes]:
        """Записывает аудио"""
        try:
            # Используем GET запрос с query параметрами
            response = requests.get(f"{self.base_url}/media/record-audio", params={
                'duration': duration
            })
            
            if response.status_code == 200:
                return response.content
            else:
                print(f"Ошибка записи аудио: {response.status_code}")
                return None
        except Exception as e:
            print(f"Ошибка при записи аудио: {e}")
            return None

    def interval_photo(self, interval: int = 1000, count: int = 10) -> Optional[bytes]:
        """Делает интервальные фото"""
        try:
            # Используем GET запрос с query параметрами
            response = requests.get(f"{self.base_url}/media/interval-photo", params={
                'interval': interval,
                'count': count
            })
            
            if response.status_code == 200:
                return response.content
            else:
                print(f"Ошибка создания интервальных фото: {response.status_code}")
                return None
        except Exception as e:
            print(f"Ошибка при создании интервальных фото: {e}")
            return None

    # Power endpoints
    def shutdown_pc(self) -> bool:
        """Выключает компьютер"""
        return self._make_request('POST', '/power/shutdown') is not None

    def reboot_pc(self) -> bool:
        """Перезагружает компьютер"""
        return self._make_request('POST', '/power/reboot') is not None

    def sleep_pc(self) -> bool:
        """Переводит в сон"""
        return self._make_request('POST', '/power/sleep') is not None

    def lock_pc(self) -> bool:
        """Блокирует экран"""
        return self._make_request('POST', '/power/lock') is not None

    def logout_pc(self) -> bool:
        """Завершает сеанс"""
        return self._make_request('POST', '/power/logout') is not None

    def get_current_user(self) -> Optional[str]:
        """Получает текущего пользователя"""
        return self._make_request('GET', '/power/current-user')

    def switch_user(self) -> bool:
        """Сменяет пользователя"""
        return self._make_request('POST', '/power/switch-user') is not None

    # Process endpoints
    def list_processes(self) -> Optional[List[Dict[str, Any]]]:
        """Получает список процессов"""
        return self._make_request('GET', '/processes/list')

    def get_process_pid(self, process_name: str) -> Optional[int]:
        """Получает PID процесса по имени"""
        result = self._make_request('GET', f'/processes/pid/{process_name}')
        return result if isinstance(result, int) else None

    def kill_process(self, pid: int) -> bool:
        """Убивает процесс по PID"""
        return self._make_request('DELETE', f'/processes/kill/{pid}') is not None

    def start_process(self, process_path: str) -> bool:
        """Запускает процесс"""
        return self._make_request('POST', '/processes/start', json={
            'path': process_path
        }) is not None

    # Monitor endpoints
    def get_cpu_usage(self) -> Optional[float]:
        """Получает загрузку CPU"""
        result = self._make_request('GET', '/monitor/cpu')
        if isinstance(result, dict) and 'usage' in result:
            return result['usage']
        return result

    def get_ram_usage(self) -> Optional[float]:
        """Получает загрузку RAM"""
        result = self._make_request('GET', '/monitor/ram')
        if isinstance(result, dict) and 'usage' in result:
            return result['usage']
        return result

    def get_disk_usage(self) -> Optional[Dict[str, Any]]:
        """Получает использование диска"""
        return self._make_request('GET', '/monitor/disk')

    # Log endpoints
    def get_system_log(self) -> Optional[List[Dict[str, Any]]]:
        """Получает системный лог"""
        return self._make_request('GET', '/logs/system')

    def get_network_log(self) -> Optional[List[Dict[str, Any]]]:
        """Получает сетевой лог"""
        return self._make_request('GET', '/logs/network')

    def get_event_log(self) -> Optional[List[Dict[str, Any]]]:
        """Получает лог событий"""
        return self._make_request('GET', '/logs/event')

    def get_error_log(self) -> Optional[List[Dict[str, Any]]]:
        """Получает лог ошибок"""
        return self._make_request('GET', '/logs/error')

    def get_login_log(self) -> Optional[List[Dict[str, Any]]]:
        """Получает лог входов"""
        return self._make_request('GET', '/logs/login')

    def get_file_open_log(self) -> Optional[List[Dict[str, Any]]]:
        """Получает лог открытия файлов"""
        return self._make_request('GET', '/logs/file-open')

    # System endpoints
    def get_os_version(self) -> Optional[str]:
        """Получает версию ОС"""
        result = self._make_request('GET', '/system/version')
        if isinstance(result, dict) and 'version' in result:
            return result['version']
        return result

    def get_arch(self) -> Optional[str]:
        """Получает архитектуру"""
        result = self._make_request('GET', '/system/arch')
        if isinstance(result, dict) and 'arch' in result:
            return result['arch']
        return result

    def clear_temp(self) -> bool:
        """Очищает временные файлы"""
        return self._make_request('POST', '/system/clear-temp') is not None

    def clear_recycle_bin(self) -> bool:
        """Очищает корзину"""
        return self._make_request('POST', '/system/clear-recycle') is not None

    # Browser endpoints
    def get_browser_history(self) -> Optional[List[Dict[str, Any]]]:
        """Получает историю браузера"""
        return self._make_request('GET', '/browser/history')

    def clear_browser_cache(self) -> bool:
        """Очищает кэш браузера"""
        return self._make_request('POST', '/browser/clear-cache') is not None

    def clear_cookies(self) -> bool:
        """Очищает куки"""
        return self._make_request('POST', '/browser/clear-cookies') is not None

    def save_site_screenshot(self, url: str) -> Optional[str]:
        """Делает скриншот сайта"""
        result = self._make_request('POST', '/browser/site-screenshot', json={
            'url': url
        })
        return result if isinstance(result, str) else None

    def open_site(self, url: str) -> bool:
        """Открывает сайт"""
        return self._make_request('POST', '/browser/open-site', json={
            'url': url
        }) is not None

    def save_page(self, url: str) -> Optional[str]:
        """Сохраняет страницу"""
        result = self._make_request('POST', '/browser/save-page', json={
            'url': url
        })
        return result if isinstance(result, str) else None

    def get_open_tabs(self) -> Optional[List[Dict[str, Any]]]:
        """Получает открытые вкладки"""
        return self._make_request('GET', '/browser/open-tabs')

    def close_tab(self, tab_id: int) -> bool:
        """Закрывает вкладку"""
        return self._make_request('DELETE', f'/browser/close-tab/{tab_id}') is not None

    def download_from_site(self, url: str, selector: str) -> Optional[str]:
        """Скачивает файл с сайта"""
        result = self._make_request('POST', '/browser/download', json={
            'url': url,
            'selector': selector
        })
        return result if isinstance(result, str) else None

    def run_headless_browser(self, url: str) -> Optional[str]:
        """Запускает headless браузер"""
        result = self._make_request('POST', '/browser/headless', json={
            'url': url
        })
        return result if isinstance(result, str) else None

    # User endpoints
    def get_user_by_telegram_id(self, telegram_id: str) -> Optional[Dict[str, Any]]:
        """Получает пользователя по Telegram ID"""
        users = self._make_request('GET', '/users')
        if users:
            for user in users:
                if user.get('telegramId') == telegram_id:
                    return user
        return None

    def create_user(self, username: str, telegram_id: str, role: str = 'user') -> Optional[Dict[str, Any]]:
        """Создает нового пользователя"""
        return self._make_request('POST', '/users', json={
            'username': username,
            'telegramId': telegram_id,
            'role': role
        })

    def update_user_role(self, telegram_id: str, role: str) -> Optional[Dict[str, Any]]:
        """Обновляет роль пользователя"""
        return self._make_request('PATCH', f'/users/{telegram_id}', json={'role': role})

    def set_admin_role(self, telegram_id: str) -> Optional[Dict[str, Any]]:
        """Назначает роль admin пользователю"""
        return self._make_request('POST', f'/users/{telegram_id}/admin')

    def delete_user(self, telegram_id: str) -> bool:
        """Удаляет пользователя"""
        return self._make_request('DELETE', f'/users/{telegram_id}') is not None

    def get_all_users(self) -> Optional[list]:
        """Получает всех пользователей"""
        return self._make_request('GET', '/users')

    def get_admins(self) -> Optional[list]:
        """Получает всех админов"""
        return self._make_request('GET', '/users/admins')

# Создаем глобальный экземпляр клиента
api_client = APIClient() 