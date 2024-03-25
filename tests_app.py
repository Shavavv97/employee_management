import unittest
from app import app

class TestEmployeeAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_employees(self):
        response = self.app.get('/api/')
        self.assertEqual(response.status_code, 200)

    def test_get_employee_by_field(self):
        field = 'first_name'
        value = 'James'
        response = self.app.get(f'/api/{field}/{value}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)

    def test_get_nonexistent_employee(self):
        field = 'first_name'
        value = 'Dummy name'
        response = self.app.get(f'/api/{field}/{value}')
        self.assertEqual(response.status_code, 404)
        data = response.get_json()
        self.assertEqual(data['error'], 'Employee not found')

    def test_create_new_employee(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'state': 'CA'
        }
        response = self.app.post('/api/', json=data)
        self.assertEqual(response.status_code, 201)

    def test_create_new_employee_missing_required_fields(self):
        data = {
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'dummy_field': 'dummy'
        }
        response = self.app.post('/api/', json=data)
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['error'], 'Wrong arguments')

    def test_create_new_employee_invalid_state(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'state': 'California'
        }
        response = self.app.post('/api/', json=data)
        self.assertEqual(response.status_code, 400)
        data = response.get_json()
        self.assertEqual(data['error'], 'State must be provided as two characters')

if __name__ == '__main__':
    unittest.main()
