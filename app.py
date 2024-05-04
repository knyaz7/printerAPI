from flask import Flask, request, send_file
from flask_cors import CORS
from database import db
from Controllers.PrinterController import PrinterController
from Controllers.PrintController import PrintController

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app)  # Поддержка CORS для всего приложения

# Подключения к базе данных PostreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/PrintersProject'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/api/printers/', methods=['GET', 'POST'])
def printers():
    if request.method == 'GET':
        return PrinterController.get_printers()
    elif request.method == 'POST':
        return PrinterController.add_printer()


@app.route('/api/printers/<int:item_id>', methods=['GET'])
def printer(item_id):
    return PrinterController.get_printer(item_id)


@app.route('/api/prints/', methods=['GET', 'POST'])
def prints():
    if request.method == 'GET':
        return PrintController.get_prints()
    elif request.method == 'POST':
        return PrintController.add_print(app)


@app.route('/api/prints/<int:item_id>', methods=['GET'])
def user_print(item_id):
    return PrintController.get_print(item_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
