@echo off
python -m venv venv

call venv\Scripts\activate.bat

python -m pip install --upgrade pip

pip install ultralytics insightface onnxruntime opencv-python numpy

echo.
echo ✅ Setup complete! To activate later: call venv\Scripts\activate.bat
pause