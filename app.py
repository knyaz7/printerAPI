from flask import Flask, request, send_file
from flask_cors import CORS
from database import db
from Controllers.PrinterController import *

app = Flask(__name__)
CORS(app) # Включаем поддержку CORS для всего приложения

# Настройка подключения к базе данных MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:root@db:5432/dbuild'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# Роуты пользователя
app.route('/api/users/', methods=['GET'])(get_users)
app.route('/api/users/<int:item_id>', methods=['GET'])(get_user)
app.route('/api/users/', methods=['POST'])(add_user)
app.route('/api/users/<int:item_id>', methods=['PUT'])(update_user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)