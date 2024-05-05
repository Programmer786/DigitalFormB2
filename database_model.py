from app import app
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta, datetime
from sqlalchemy import create_engine, Numeric, text
import os
from flask_migrate import Migrate

# Session configuration
app.permanent_session_lifetime = timedelta(hours=5)

# Database configuration for the online MySQL database on cPanel
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://cmsfarca_app:Pakistan007!!!@cp6.mywebsitebox.com/digital_form_b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/digital_form_b'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
# Set the upload folder
UPLOAD_FOLDER = 'static/files'

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
# Set the upload folder for Registered Finger Print
UPLOAD_REG_FINGER = 'static/reg_finger'
# Ensure the upload folder exists
if not os.path.exists(UPLOAD_REG_FINGER):
    os.makedirs(UPLOAD_REG_FINGER)

# Set the upload folder for Registered Finger Print
UPLOAD_SAMPLE_FINGER = 'static/sample_finger'
# Ensure the upload folder exists
if not os.path.exists(UPLOAD_SAMPLE_FINGER):
    os.makedirs(UPLOAD_SAMPLE_FINGER)

# Configure the Flask app with the upload folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_REG_FINGER'] = UPLOAD_REG_FINGER
app.config['UPLOAD_SAMPLE_FINGER'] = UPLOAD_SAMPLE_FINGER
db = SQLAlchemy(app)
# Model Migrate into database tables Automatically
# First initialize only one time command (flask db init)
# apply those command Step:1(flask db migrate)Step:2 (flask db upgrade)
migrate = Migrate(app, db)


class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=True)
    phone = db.Column(db.String(50), unique=True, nullable=True)
    cnic = db.Column(db.String(20), unique=True, nullable=True)
    gender = db.Column(db.String(20), unique=False, nullable=True)
    rol_name = db.Column(db.String(20), unique=False, nullable=True)  # Can be 'admin', 'parent', 'manager', 'employee', 'DeliveryBoy'
    employee_province_sno = db.Column(db.Integer, db.ForeignKey('province.province_sno'), nullable=True)
    employee_district_sno = db.Column(db.Integer, db.ForeignKey('district.district_sno'), nullable=True)
    delivery_status = db.Column(db.String(20), default='Available', nullable=True)  # e.g., 'Available', 'Pending', 'OutOfDelivery', 'NotAvailable'
    password = db.Column(db.String(256))
    photo = db.Column(db.String(256))  # e.g., db.Column(db.LargeBinary) for LONGBLOB).
    isActive = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # Define relationships if needed
    province = db.relationship('Province', backref=db.backref('users', lazy=True))
    district = db.relationship('District', backref=db.backref('users', lazy=True))


class Requests(db.Model):
    __tablename__ = 'requests'
    r_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    request_type = db.Column(db.String(50), nullable=False)  # e.g., 'form_b', 'complaint'
    status = db.Column(db.String(50), nullable=False)  # e.g., 'pending', 'accepted', 'rejected'
    details = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # Define relationships if needed
    users = db.relationship('Users', backref=db.backref('requests', lazy=True))


class Documents(db.Model):
    __tablename__ = 'documents'
    doc_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=True)
    content = db.Column(db.String(255), nullable=True)
    expiry_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Complaints(db.Model):
    __tablename__ = 'complaints'
    comp_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    send_details = db.Column(db.String(255), nullable=False)
    received_details = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(50), nullable=False)  # e.g., 'pending', 'corrected', 'rejected', 'finalized'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # Define relationships if needed
    users = db.relationship('Users', backref=db.backref('complaints', lazy=True))


class Contacts(db.Model):
    __tablename__ = 'contacts'
    cont_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    contact_type = db.Column(db.String(30), nullable=True)  # e.g., 'mother', 'father'
    contact_number = db.Column(db.String(50), nullable=True)
    # Define relationships if needed
    users = db.relationship('Users', backref=db.backref('contacts', lazy=True))


class ParentData(db.Model):  # This table use for a Apply Form
    __tablename__ = 'parent_data'
    par_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    crc_no = db.Column(db.Integer, unique=True, nullable=True)
    father_name = db.Column(db.String(30), nullable=True)
    father_cnic = db.Column(db.String(50), unique=True, nullable=True)
    father_finger = db.Column(db.String(255), nullable=True)
    mother_name = db.Column(db.String(30), nullable=True)
    mother_cnic = db.Column(db.String(50), unique=True, nullable=True)
    mother_finger = db.Column(db.String(255), nullable=True)
    send_comment = db.Column(db.String(255), nullable=True)
    received_comment = db.Column(db.String(255), nullable=True)
    address = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(50), nullable=False)  # e.g., 'Pending', 'Processing', 'Complete', 'Rejected'
    delivery_status = db.Column(db.String(20), default='No', nullable=True)  # e.g., 'No', 'Not_Received', 'Received' No:- its means no any process for delivery
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    forward_to_admin = db.Column(db.Boolean, default=False, nullable=False)
    # Define relationships if needed
    users = db.relationship('Users', backref=db.backref('parent_data', lazy=True))
    # child_data = db.relationship('ChildData', backref='parent')


class ChildData(db.Model):
    __tablename__ = 'child_data'
    chi_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    par_id = db.Column(db.Integer, db.ForeignKey('parent_data.par_id'), nullable=False)
    child_name = db.Column(db.String(30), nullable=True)
    child_birth_date = db.Column(db.Date, nullable=False)
    child_gender = db.Column(db.String(20), nullable=True)
    new_cnic = db.Column(db.String(50), unique=True, nullable=True)
    disability = db.Column(db.String(30), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # Define relationships if needed
    users = db.relationship('Users', backref=db.backref('child_data', lazy=True))
    parent_data = db.relationship('ParentData', backref=db.backref('child_data', lazy=True))


# Create province model. The table name "province" will automatically be assigned to the model’s table.
class Province(db.Model):
    __tablename__ = 'province'
    province_sno = db.Column(db.Integer, primary_key=True)
    province_name = db.Column(db.String(50), unique=True, nullable=False)


# Create District model. The table name "district" will automatically be assigned to the model’s table.
class District(db.Model):
    __tablename__ = 'district'
    district_sno = db.Column(db.Integer, primary_key=True)
    district_province_sno = db.Column(db.Integer, db.ForeignKey('province.province_sno'), nullable=False)
    district_name = db.Column(db.String(100), unique=True, nullable=False)
    # Define the relationships
    province = db.relationship('Province', backref=db.backref('districts', lazy=True))


class DeliveryBoyHandover(db.Model):
    __tablename__ = 'delivery_boy_handover'
    ho_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    par_id = db.Column(db.Integer, db.ForeignKey('parent_data.par_id'), nullable=False)
    drop_address = db.Column(db.String(50), nullable=True)
    status = db.Column(db.String(50), default='OnTheWay', nullable=True)  # e.g., 'OnTheWay', 'Deliver', 'Return'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # Define relationships if needed
    users = db.relationship('Users', backref=db.backref('delivery_boy_handover', lazy=True))
    parent_data = db.relationship('ParentData', backref=db.backref('delivery_boy_handover', lazy=True))
