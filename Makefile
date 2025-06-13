# ======================= Makefile (Linux/macOS) =======================
# Usage:
#   make setup      → create venv and install requirements
#   make run        → run the Face Unlock system

setup:
	python3 -m venv venv
	source venv/bin/activate && pip install --upgrade pip
	source venv/bin/activate && pip install -r requirements.txt
	echo "✅ Setup complete! Activate with: source venv/bin/activate"

run:
	source venv/bin/activate && python3 main.py