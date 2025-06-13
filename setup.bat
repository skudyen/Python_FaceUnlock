# ======================= setup.bat (Windows) =======================
:: Create virtual environment and install dependencies
@echo off
python -m venv venv
call venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt
echo ✅ Setup complete! To activate: call venv\Scripts\activate.bat
pause