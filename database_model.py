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
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/cms_application'
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
    rol_name = db.Column(db.String(20), unique=False, nullable=True)  # Can be 'admin', 'parent', 'manager', 'employee', 'delivery_boy'
    password = db.Column(db.String(256))
    photo = db.Column(db.String(256))  # e.g., db.Column(db.LargeBinary) for LONGBLOB).
    isActive = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


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
    father_name = db.Column(db.String(30), nullable=True)
    father_cnic = db.Column(db.String(50), unique=True, nullable=True)
    father_finger = db.Column(db.String(255), nullable=True)
    mother_name = db.Column(db.String(30), nullable=True)
    mother_cnic = db.Column(db.String(50), unique=True, nullable=True)
    mother_finger = db.Column(db.String(255), nullable=True)
    send_comment = db.Column(db.String(255), nullable=True)
    received_comment = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(50), nullable=False)  # e.g., 'Pending', 'Processing', 'Complete', 'Rejected'
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
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # Define relationships if needed
    users = db.relationship('Users', backref=db.backref('child_data', lazy=True))
    parent_data = db.relationship('ParentData', backref=db.backref('child_data', lazy=True))
