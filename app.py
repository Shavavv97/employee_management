from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

def load_employees():
    employees = []
    with open('data/sample.csv', 'r') as f:
        reader = csv.DictReader(f)
        employees = [row for row in reader]
    return employees


@app.route('/api/', methods=['GET'])
def get_employees():
    employees = load_employees()
    return jsonify(employees)


@app.route('/api/<string:field>/<string:value>', methods=['GET'])
def get_employee_by_field(field, value):
    """
    Get a specific employee by providing a field name and a value
    """
    employees = load_employees()
    filtered_employee = [employee for employee in employees if employee[field] == value]
    if filtered_employee:
        return jsonify(filtered_employee)
    return jsonify({'error': 'Employee not found'}), 404

@app.route('/api/', methods=['POST'])
def create_new_employee():
    return create_post_request_handler(request)

def create_post_request_handler(request):
    if request.method == 'POST':
        data = request.get_json()
        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        company_name = data.get('company_name', '')
        address = data.get('address', '')
        city = data.get('city','')
        state =  data.get('state','')
        zip = data.get('zip', '')
        phone1 = data.get('phone1', '')
        phone2 = data.get('phone2', '')
        email = data.get('email', '')
        department = data.get('department', '')

        if not first_name or not last_name or not email:
            return jsonify({'error': 'Wrong arguments'}), 400
        
        if len(state) != 2:
            return jsonify({"error": "State must be provided as two characters"}),  400

        employee = {
            'first_name': first_name, 
            'last_name': last_name, 
            'company_name': company_name,
            'address': address,
            'city': city,
            'state': state,
            'zip': zip,
            'phone1': phone1,
            'phone2': phone2,
            'email': email,
            'department': department
        }
        create_post_request(employee)

        return jsonify({'message': 'Employee created successfully'}), 201

def create_post_request(employee):
    with open('data/sample.csv', 'a') as f:
        fieldnames = ['first_name', 'last_name', 'company_name', 'address', 'city', 'state', 'zip', 'phone1', 'phone2', 'email', 'department']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if fieldnames != employee.keys():
            writer.writeheader()
        writer.writerow(employee)


if __name__ == '__main__':
    app.run()