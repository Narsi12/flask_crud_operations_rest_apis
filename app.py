# app.py
from flask import Flask, request, jsonify
from extensions import db
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
# Now import the Employee model from models.py
from models import Employee

# CRUD operations and endpoints go here...

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    employee_id = data['employee_id']
    name = data['name']
    address = data['address']
    phone = data['phone']
    new_user = Employee(employee_id=employee_id, name=name, address=address, phone=phone)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'})



if __name__=='__main__':
    app.run()