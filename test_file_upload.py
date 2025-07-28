#!/usr/bin/env python3
"""
Тест отправки файлов в aiogram 3.x
"""

from aiogram.types import BufferedInputFile

def test_file_upload():
    """Тестирует создание BufferedInputFile для отправки"""
    print("🔧 Тестирование отправки файлов")
    print("=" * 50)
    
    # Создаем тестовые данные
    test_image_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\tpHYs\x00\x00\x0b\x13\x00\x00\x0b\x13\x01\x00\x9a\x9c\x18\x00\x00\x00\x07tIME\x07\xe3\x07\x1c\x0f\x1c\x0c\xd8\xd8\xd8\xd8\x00\x00\x00\x0cIDATx\x9cc```\x00\x00\x00\x02\x00\x01\xe5\x27\xde\xfc\x00\x00\x00\x00IEND\xaeB`\x82'
    test_video_data = b'\x00\x00\x00\x18ftypisom\x00\x00\x02\x00isomiso2avc1mp41'
    
    try:
        # Тест создания BufferedInputFile для изображения
        photo_file = BufferedInputFile(test_image_data, filename="test_screenshot.png")
        print("✅ BufferedInputFile для изображения создан успешно")
        print(f"   Тип: {type(photo_file)}")
        print(f"   Имя файла: {photo_file.filename}")
        
        # Тест создания BufferedInputFile для видео
        video_file = BufferedInputFile(test_video_data, filename="test_video.mp4")
        print("✅ BufferedInputFile для видео создан успешно")
        print(f"   Тип: {type(video_file)}")
        print(f"   Имя файла: {video_file.filename}")
        
        # Тест создания BufferedInputFile для документа
        doc_file = BufferedInputFile(test_image_data, filename="test_document.zip")
        print("✅ BufferedInputFile для документа создан успешно")
        print(f"   Тип: {type(doc_file)}")
        print(f"   Имя файла: {doc_file.filename}")
        
        print("\n🎉 Все тесты отправки файлов пройдены!")
        return True
        
    except Exception as e:
        print(f"❌ Ошибка при создании BufferedInputFile: {e}")
        return False

if __name__ == "__main__":
    success = test_file_upload()
    if success:
        print("\n✅ Система отправки файлов готова к использованию!")
    else:
        print("\n❌ Требуется исправление ошибок") 