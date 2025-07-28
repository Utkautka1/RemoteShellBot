#!/usr/bin/env python3
"""
Тест API клиента
"""

from utils.api_client import api_client
import time

def test_api():
    """Тестирует API клиент"""
    print("🔧 Тестирование API клиента")
    print("=" * 50)
    
    # Тест скриншота
    print("📸 Тест скриншот...")
    screenshot = api_client.get_screenshot()
    if screenshot:
        print(f"✅ Скриншот получен: {len(screenshot)} байт")
    else:
        print("❌ Скриншот не получен")
    
    # Тест мониторинга
    print("\n📊 Тест мониторинга...")
    cpu = api_client.get_cpu_usage()
    if cpu is not None:
        print(f"✅ CPU: {cpu:.2f}%")
    else:
        print("❌ CPU не получен")
    
    ram = api_client.get_ram_usage()
    if ram is not None:
        print(f"✅ RAM: {ram:.2f}%")
    else:
        print("❌ RAM не получен")
    
    disk = api_client.get_disk_usage()
    if disk:
        print(f"✅ Диск: {disk}")
    else:
        print("❌ Диск не получен")
    
    # Тест системной информации
    print("\n💻 Тест системной информации...")
    os_version = api_client.get_os_version()
    if os_version:
        print(f"✅ ОС: {os_version}")
    else:
        print("❌ ОС не получена")
    
    arch = api_client.get_arch()
    if arch:
        print(f"✅ Архитектура: {arch}")
    else:
        print("❌ Архитектура не получена")
    
    print("\n🎉 Тест завершен!")

if __name__ == "__main__":
    test_api() 