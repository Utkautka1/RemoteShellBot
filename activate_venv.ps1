Write-Host "Активация виртуального окружения Python 3.13.5..." -ForegroundColor Green
& ".\venv\Scripts\Activate.ps1"

Write-Host "`nВиртуальное окружение активировано!" -ForegroundColor Green
Write-Host "Python версия:" -ForegroundColor Yellow
python --version

Write-Host "`nДля деактивации введите: deactivate" -ForegroundColor Cyan
Write-Host "Для запуска бота: python main.py" -ForegroundColor Cyan 