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

@app.route('/get_all_users',methods=['GET'])
def get_all_users():
    data = Employee.query.all()
    result = []
    for emp in data:
        result.append({
            "employee_id":emp.employee_id,
            "name":emp.name,
            "address":emp.address,
            "phone":emp.phone
        })
    print(result)
    return jsonify({'message':'fetch data'})

@app.route('/get_all_users/<int:id>',methods=['GET'])
def get_single_user(id):
    user =Employee.query.filter_by(employee_id= id).first()
    if not user :
        return jsonify({'message':'User not found'})
    
    return jsonify({
            "employee_id":user.employee_id,
            "name":user.name,
            "address":user.address,
            "phone":user.phone
        })

@app.route('/update_record/<int:id>', methods=['PUT'])
def update_user(id):
    user =Employee.query.filter_by(employee_id= id).first()
    if not user:
        return jsonify({'message':'User not found'})
    data = request.get_json()
    name = data['name']
    address = data['address']
    phone = data['phone']

    user.name = name
    user.address = address
    user.phone = phone

    # Commit the changes to the database
    db.session.commit()
    return jsonify({'message':'User record updated successfully ! '})

@app.route('/delete_record/<int:id>', methods=['DELETE'])
def delete_user(id):
    user =Employee.query.filter_by(employee_id= id).first()
    if not user:
        return jsonify({'message':'User not found'})
    
    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'User record deleted successfully!'})


if __name__=='__main__':
    app.run()