# apm-core
Asset Performance Managment (APM) - core

Installation.

python -m venv venv

pip install -r requirements.txt


Start.

source venv/Scripts/activate

uvicorn backend.main:app --port 8000
