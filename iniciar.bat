@echo off
cd /d "%~dp0"

IF NOT EXIST "venv\" (
    echo Creando entorno virtual...
    python -m venv venv
    venv\Scripts\python -m pip install --upgrade pip
    venv\Scripts\pip install -r requirements.txt
)

echo =========================================================
echo    EconoMetrics AI - Evaluador de Rentabilidad
echo    Iniciando servidor FastAPI en http://127.0.0.1:8000
echo =========================================================

venv\Scripts\uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload