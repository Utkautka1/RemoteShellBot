import json
import os
from typing import Optional, Dict, Any
from datetime import datetime
from .api_client import api_client

class UserDatabase:
    """Класс для работы с пользователями через API"""
    
    @staticmethod
    def get_user(telegram_id: int) -> Optional[Dict[str, Any]]:
        """Получает пользователя по Telegram ID"""
        return api_client.get_user_by_telegram_id(str(telegram_id))
    
    @staticmethod
    def create_user(telegram_id: int, username: str = None, first_name: str = None, last_name: str = None) -> Optional[Dict[str, Any]]:
        """Создает нового пользователя"""
        # Используем username или first_name как имя пользователя
        user_name = username or first_name or f"user_{telegram_id}"
        return api_client.create_user(user_name, str(telegram_id), 'user')
    
    @staticmethod
    def update_user_role(telegram_id: int, role: str) -> bool:
        """Обновляет роль пользователя"""
        result = api_client.update_user_role(str(telegram_id), role)
        return result is not None
    
    @staticmethod
    def set_admin_role(telegram_id: int) -> bool:
        """Назначает роль admin пользователю"""
        result = api_client.set_admin_role(str(telegram_id))
        return result is not None
    
    @staticmethod
    def user_exists(telegram_id: int) -> bool:
        """Проверяет существование пользователя"""
        user = api_client.get_user_by_telegram_id(str(telegram_id))
        return user is not None
    
    @staticmethod
    def get_all_users() -> Optional[list]:
        """Получает всех пользователей"""
        return api_client.get_all_users()
    
    @staticmethod
    def get_admins() -> Optional[list]:
        """Получает всех админов"""
        return api_client.get_admins()
    
    @staticmethod
    def delete_user(telegram_id: int) -> bool:
        """Удаляет пользователя"""
        return api_client.delete_user(str(telegram_id))

# Создаем глобальный экземпляр базы данных
user_db = UserDatabase() 