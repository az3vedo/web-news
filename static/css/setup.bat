set FLASK_APP=app
set FLASK_ENV=%1
pip install -r requirements.txt
flask run --port 5001