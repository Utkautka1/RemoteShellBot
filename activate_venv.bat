@echo off
echo Активация виртуального окружения Python 3.13.5...
call venv\Scripts\activate.bat
echo.
echo Виртуальное окружение активировано!
echo Python версия: 
python --version
echo.
echo Для деактивации введите: deactivate
echo.
cmd /k 