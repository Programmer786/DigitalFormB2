import os
from flask import Flask

app = Flask(__name__)

# Set the secret key using an environment variable
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'Pakistan007$$$')

# Importing controllers and routes
from user_controller import *
from manager_controller import *
from parent_controller import *
from complaint_controller import *
from delivery_boy_controller import *
# from add_employee_control import *
# from employee_salary_slip import *
# from project_details_control import *
# from main_office_employee_record import *
# from over_all_report import *
# from project_invoices import *
# from investor_data import *

if __name__ == '__main__':
    app.run(debug=True)