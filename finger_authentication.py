import cv2
import numpy as np
from sqlalchemy.orm import joinedload
from app import app
from sqlalchemy.exc import IntegrityError
from sqlalchemy import asc, desc
from database_model import *
# from database_model import db, Users,Rol
from flask import render_template, flash, session, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date


@app.route("/parent_dashboard")
def parent_dashboard():
    if 'p_cnic' and 'p_rol_name' in session:
        return render_template('Parent/index.html')
    else:
        return render_template('Parent/parent_login.html')


@app.route('/parent_login', methods=['POST', 'GET'])
def parent_login():
    if 'p_cnic' and 'p_rol_name' in session:
        session_rol_name = session['p_rol_name']
        if session_rol_name == 'Parent':
            return redirect('/parent_dashboard')
        else:
            return redirect('/logout_parent')
    else:
        if request.method == 'POST':
            a_cnic = request.form['cnic']
            a_password = request.form['password']
            try:
                # query = "select 1 from Users where cnic=cnic"
                user = Users.query.filter_by(cnic=a_cnic, isActive=1).first()
                # If no record found by this email
                if user is not None:
                    if user.isActive == 1:
                        passwd = user.password
                        # If password decrypt and record do not match with password
                        if check_password_hash(passwd, a_password):  # if passwd == a_password: without encryption
                            session.permanent = True  # <--- makes the permanent session
                            session['p_name'] = user.name
                            session['p_cnic'] = user.cnic
                            session['p_ContactNo'] = user.phone
                            session['p_UserId'] = user.user_id
                            session['p_photo'] = user.photo
                            session['p_rol_name'] = user.rol_name

                            if user.rol_name == 'Parent':
                                return redirect('/parent_dashboard')
                            elif user.rol_name == 'DeliveryBoy':
                                return redirect('/delivery_boy_dashboard')
                            else:
                                return redirect('/logout_parent')

                        else:
                            flash("Error! Invalid Password, Please try Again!", "danger")
                            return render_template('Parent/parent_login.html')
                    else:
                        flash("Error! Please Register Your Account and Then Login!", "danger")
                        return render_template('Parent/parent_login.html')
                else:
                    flash("Error! Invalid CNIC, Please Contact to Administrator!", "danger")
                    return render_template('Parent/parent_login.html')
            except Exception as e:
                # If an error occurs during database connection, display error message
                db.session.rollback()
                flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
                return render_template('Parent/parent_login.html')
        return render_template('Parent/parent_login.html')


@app.route('/parent_register', methods=['POST', 'GET'])
def parent_register():
    if request.method == 'POST':
        try:
            r_name = request.form.get('name')
            r_user_role = request.form.get('user_role')
            r_phone = request.form.get('phone')
            r_cnic = request.form.get('cnic')
            r_gender = request.form.get('gender')
            r_password = request.form.get('password')
            r_conform_password = request.form.get('conform_password')
            if (r_name != "") and (r_phone != "") and (r_cnic != "") and (r_password != "") and (
                    r_conform_password != ""):
                register_user = Users.query.filter_by(cnic=r_cnic).count()
                if r_password == r_conform_password:
                    if register_user < 1:
                        # change_to_hashed_password = generate_password_hash(r_password, "sha256") #old method
                        change_to_hashed_password = generate_password_hash(r_password, method='scrypt')  # new method

                        new_entry_register_user = Users(
                            name=r_name,
                            phone=r_phone,
                            cnic=r_cnic,
                            gender=r_gender,
                            rol_name='Parent',
                            password=change_to_hashed_password,
                            created_at=datetime.now(),
                            isActive=1
                        )
                        db.session.add(new_entry_register_user)
                        db.session.commit()
                        flash("Successfully Register.", "success")
                        return redirect('/parent_register')
                    else:
                        flash(
                            "Error! The Account is Already Registered So goto Login otherwise Contact to your Administrator. "
                            "Thank you",
                            "danger")
                else:
                    flash("Error! Your conform password is wrong please try again", "danger")
            else:
                flash("Error! Please fill out this field.", "danger")
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash("Error. Duplicate CNIC and Phone Number Not Acceptable", "danger")
            return redirect('/parent_register')
    return render_template('Parent/parent_register.html')


@app.route('/parent_profile', methods=['POST', 'GET'])
def parent_profile():
    if 'p_cnic' and 'p_rol_name' in session:
        try:
            # role_with_Cnic_data_retrieve = Users.query.order_by(Users.user_id).all()
            session_UserId = session['p_UserId']
            one_record_by_cnic_data_retrieve = Users.query.filter_by(user_id=session_UserId).first()

            return render_template('Parent/parent_profile.html', one_record_data_retrieve=one_record_by_cnic_data_retrieve)
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Parent/parent_login.html')
    else:
        return render_template('Parent/parent_login.html')


@app.route('/disable_role_parent/<int:UserId>')
def disable_role_parent(UserId):
    if 'p_cnic' and 'p_rol_name' in session:
        try:
            # get specific user user_id from clerk Table and then check date with UserId related
            sel_one_user = Users.query.filter_by(user_id=UserId).first()
            sel_one_user.isActive = 0
            db.session.commit()
            flash("Record Successfully Disable", "success")
            return redirect('/parent_profile')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return redirect('/parent_profile')
    else:
        return render_template('Parent/parent_login.html')


@app.route('/enable_role_parent/<int:UserId>')
def enable_role_parent(UserId):
    if 'p_cnic' and 'p_rol_name' in session:
        try:
            # get specific user user_id from clerk Table and then check date with UserId related
            sel_one_user = Users.query.filter_by(user_id=UserId).first()
            sel_one_user.isActive = 1
            db.session.commit()
            flash("Record Successfully Enable", "success")
            return redirect('/parent_profile')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return redirect('/parent_profile')
    else:
        return render_template('Parent/parent_login.html')


@app.route('/change_password_parent/<int:UserId>', methods=['POST', 'GET'])
def change_password_parent(UserId):
    if 'p_cnic' and 'p_rol_name' in session:
        try:
            # Retrieve form data
            r_password = request.form.get('password')
            r_conform_password = request.form.get('conform_password')

            if r_password == r_conform_password:
                # change_to_hashed_password = generate_password_hash(r_password, "sha256") #old method
                change_to_hashed_password = generate_password_hash(r_password, method='scrypt')  # new method

                update_user_password = Users.query.filter_by(user_id=UserId).first()
                update_user_password.password = change_to_hashed_password
                db.session.add(update_user_password)
                db.session.commit()
                flash("Password changed successfully.", "success")
                return redirect('/parent_profile')
            else:
                flash("Error! Your confirm password is wrong, please try again", "danger")
                return redirect('/parent_profile')
        except IntegrityError:
            db.session.rollback()
            flash("Error. Duplicate CNIC Not Acceptable", "danger")
            return redirect('/parent_profile')  # Add return statement here
    else:
        # Render the form for GET requests
        return render_template('Parent/parent_login.html')


@app.route('/parent_for_update/<int:UserId>', methods=['POST', 'GET'])
def parent_for_update(UserId):
    if 'p_cnic' and 'p_rol_name' in session:
        try:
            # get specific user SNo from clerk Table and then check date with SNo related
            get_name = request.form['name']
            get_cnic = request.form['cnic']
            get_phone = request.form['phone']
            get_gender = request.form['gender']

            update_user = Users.query.filter_by(user_id=UserId).first()
            update_user.name = get_name
            update_user.cnic = get_cnic
            update_user.phone = get_phone
            update_user.gender = get_gender

            session.permanent = True  # <--- makes the permanent session
            session['p_name'] = get_name
            session['p_cnic'] = get_cnic
            session['p_ContactNo'] = get_phone

            db.session.add(update_user)
            db.session.commit()
            flash("Record Successfully Updated", "success")
            return redirect('/parent_profile')
        except IntegrityError:
            db.session.rollback()
            flash("Error. Duplicate CNIC and Phone Number Not Acceptable", "danger")
            return redirect('/parent_profile')  # Add return statement here
    else:
        return render_template('Parent/parent_login.html')


@app.route('/apply_to_formb', methods=['POST', 'GET'])
def apply_to_formb():
    if 'p_cnic' and 'p_rol_name' in session:
        try:
            # Retrieve the user ID from the session
            session_user_id = session.get('p_UserId')
            parent_data_retrieve = ParentData.query.filter_by(user_id=session_user_id).first()
            apply_to_formb_data_retrieve = (
                ChildData.query
                .filter_by(user_id=session_user_id)
                .join(ParentData)
                .options(joinedload(ChildData.parent_data))
                .all()
            )
            return render_template('Parent/apply_to_formb.html', parent_data_retrieve=parent_data_retrieve, apply_to_formb_data_retrieve=apply_to_formb_data_retrieve)
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return redirect('/parent_dashboard')
    else:
        return render_template('Parent/parent_login.html')


@app.route('/add_one_time_parent_data', methods=['POST', 'GET'])
def add_one_time_parent_data():
    if 'p_cnic' and 'p_rol_name' in session:
        try:
            if request.method == 'POST':
                try:
                    father_name = request.form['father_name']
                    father_cnic = request.form['father_cnic']
                    mother_name = request.form['mother_name']
                    mother_cnic = request.form['mother_cnic']
                    request_comment = request.form['request_comment']

                    # Validate if the required fields are not empty
                    if father_name and mother_name and father_cnic and mother_cnic and request_comment:
                        # Retrieve the user ID from the session
                        session_user_id = session.get('p_UserId')

                        # Check if there's already a record for the user
                        existing_parent_data = ParentData.query.filter_by(user_id=session_user_id).first()

                        if not existing_parent_data:
                            # No existing record, proceed to insert new data
                            new_entry_parent_data = ParentData(
                                father_name=father_name,
                                father_cnic=father_cnic,
                                mother_name=mother_name,
                                mother_cnic=mother_cnic,
                                send_comment=request_comment,
                                status='Pending',
                                user_id=session_user_id
                            )
                            db.session.add(new_entry_parent_data)
                            db.session.commit()
                            flash("Successfully Parent Data Save.", "success")
                            return redirect('/biometric_authentication')
                        else:
                            flash("Error! Parent data already exists for this user.", "danger")
                            return redirect('/biometric_authentication')
                    else:
                        flash("Error! Please fill out all required fields.", "danger")
                        return redirect('/biometric_authentication')
                except Exception as e:
                    # If an error occurs during database connection, display error message
                    db.session.rollback()
                    flash("Error. Duplicate CNIC Not Acceptable", "danger")
                    return redirect('/biometric_authentication')
            else:
                # return render_template('Administrator/biometric_authentication.html')
                return redirect('/biometric_authentication')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}", "danger")
            return redirect('/apply_to_formb')
    else:
        return render_template('Parent/parent_login.html')


@app.route('/add_new_child', methods=['POST', 'GET'])
def add_new_child():
    if 'p_cnic' and 'p_rol_name' in session:
        try:
            if request.method == 'POST':
                try:
                    child_name = request.form['child_name']
                    child_date_birth = request.form['child_date_birth']
                    child_gender = request.form['child_gender']

                    # Validate if the required fields are not empty
                    if child_name and child_date_birth and child_gender:
                        # Retrieve the user ID from the session
                        session_user_id = session.get('p_UserId')

                        existing_parent_data = ParentData.query.filter_by(user_id=session_user_id).first()
                        new_entry_child_data = ChildData(
                            child_name=child_name,
                            child_birth_date=child_date_birth,
                            child_gender=child_gender,
                            user_id=session_user_id,
                            par_id=existing_parent_data.par_id
                        )
                        db.session.add(new_entry_child_data)
                        db.session.commit()
                        flash("Successfully Child Data Save.", "success")
                        return redirect('/apply_to_formb')
                    else:
                        flash("Error! Please fill out all required fields.", "danger")
                        return redirect('/apply_to_formb')
                except Exception as e:
                    # If an error occurs during database connection, display error message
                    db.session.rollback()
                    flash("Error. Duplicate CNIC Not Acceptable", "danger")
                    return redirect('/apply_to_formb')
            else:
                return render_template('Administrator/apply_to_formb.html')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}", "danger")
            return redirect('/apply_to_formb')
    else:
        return render_template('Parent/parent_login.html')


# Function to perform fingerprint matching
def fingerprint_matching(sample_image, uploaded_image):
    sift = cv2.SIFT_create()

    keypoints_1, descriptors_1 = sift.detectAndCompute(sample_image, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(uploaded_image, None)

    matches = cv2.FlannBasedMatcher({'algorithm': 1, 'trees': 10}, {}).knnMatch(descriptors_1, descriptors_2, k=2)
    match_points = []

    for p, q in matches:
        if p.distance < 0.1 * q.distance:
            match_points.append(p)

    keypoints = min(len(keypoints_1), len(keypoints_2))

    score = len(match_points) / keypoints * 100 if keypoints > 0 else 0
    return score


@app.route('/Authentication', methods=['POST', 'GET'])
def Authentication():
    if 'p_cnic' and 'p_rol_name' in session:
        try:
            # Retrieve the user ID from the session
            session_user_id = session.get('p_UserId')
            existing_parent_data = ParentData.query.filter_by(user_id=session_user_id).first()

            file_path_reg = None  # Initialize file_path with a default value
            if existing_parent_data.mother_finger is not None:
                file_path_reg = os.path.join(app.config['UPLOAD_REG_FINGER'], existing_parent_data.mother_finger)  # Construct the full path to the file
            # Now Delete the file from the directory
            if file_path_reg is not None and os.path.exists(file_path_reg):
                # Read the uploaded image
                uploaded_image = cv2.imread(file_path_reg)

            # Read the sample image
            sample_image_file = "static/sample_finger/1__M_Left_index_finger_CR.BMP"
            # Read the sample fingerprint image using OpenCV
            sample_image = cv2.imread(sample_image_file)
            # sample_image = cv2.imdecode(np.fromstring(sample_image_file.read(), np.uint8), cv2.IMREAD_COLOR)

            # Perform fingerprint matching
            score = fingerprint_matching(sample_image, uploaded_image)
            if score != 0:
                flash(f"Biometric Authentication Successfully {score}", "success")
            else:
                flash(f"Biometric Authentication Field {score}", "danger")
                
            return redirect('/apply_to_formb')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Parent/parent_login.html')
    else:
        return render_template('Parent/parent_login.html')


@app.route('/update_child_data/<int:CompId>', methods=['POST', 'GET'])
def update_child_data(CompId):
    if 'p_cnic' and 'p_rol_name' in session:
        try:
            child_name = request.form['child_name']
            child_date_birth = request.form['child_date_birth']
            child_gender = request.form['child_gender']

            update_child_data = ChildData.query.filter_by(chi_id=CompId).first()
            update_child_data.child_name = child_name
            update_child_data.child_birth_date = child_date_birth
            update_child_data.child_gender = child_gender

            db.session.add(update_child_data)
            db.session.commit()
            flash("Record Successfully Updated", "success")
            return redirect('/apply_to_formb')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Error: {str(e)}", "danger")
            return redirect('/apply_to_formb')
    else:
        return render_template('Parent/parent_login.html')


@app.route('/request_for_formb/<int:UserId>', methods=['POST', 'GET'])
def request_for_formb(UserId):
    if 'p_cnic' and 'p_rol_name' in session:
        try:
            if request.method == 'POST':
                request_comment = request.form['request_comment']
                sel_one_parent_data = ParentData.query.filter_by(user_id=UserId).first()
                sel_one_parent_data.send_comment = request_comment
                sel_one_parent_data.status = 'Pending'
                sel_one_parent_data.forward_to_admin = False
                db.session.commit()
                flash("Request Send Successfully", "success")
                return redirect('/apply_to_formb')
            else:
                return redirect('/apply_to_formb')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return redirect('/parent_dashboard')
    else:
        return render_template('Parent/parent_login.html')


@app.route('/biometric_authentication', methods=['POST', 'GET'])
def biometric_authentication():
    if 'p_cnic' and 'p_rol_name' in session:
        try:
            # Retrieve the user ID from the session
            session_user_id = session.get('p_UserId')
            parent_data_retrieve = ParentData.query.filter_by(user_id=session_user_id).first()
            return render_template('Parent/biometric_authentication.html', parent_data_retrieve=parent_data_retrieve)
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return redirect('/parent_dashboard')
    else:
        return render_template('Parent/parent_login.html')


@app.route('/registered_parent_finger', methods=['POST', 'GET'])
def registered_parent_finger():
    if 'p_cnic' and 'p_rol_name' in session:
        try:
            if request.method == 'POST':
                try:
                    select_parent = request.form['select_parent']
                    uploaded_file_finger_print = request.files['finger_print']

                    # Validate if the required fields are not empty
                    if select_parent and uploaded_file_finger_print:
                        # Retrieve the user ID from the session
                        session_user_id = session.get('p_UserId')

                        existing_parent_data = ParentData.query.filter_by(user_id=session_user_id).first()

                        if select_parent == 'Father':
                            file_path = None  # Initialize file_path with a default value
                            if existing_parent_data.father_finger is not None:
                                file_path = os.path.join(app.config['UPLOAD_REG_FINGER'], existing_parent_data.father_finger)  # Construct the full path to the file
                            # Now Delete the file from the directory
                            if file_path is not None and os.path.exists(file_path):
                                os.remove(file_path)

                            # Get the original file extension
                            _, file_extension = os.path.splitext(uploaded_file_finger_print.filename)
                            # Combine  father_cnic, and file extension to create a custom filename
                            custom_filename = f"{existing_parent_data.father_cnic}{file_extension}"
                            # Save the file and update the database record with the file path
                            file_path_system = os.path.join(app.config['UPLOAD_REG_FINGER'], custom_filename)  # Set your upload folder path
                            file_full_name = os.path.join("", custom_filename)  # Set your No path for database column
                            uploaded_file_finger_print.save(file_path_system)
                            existing_parent_data.father_finger = file_full_name
                        else:
                            file_path = None  # Initialize file_path with a default value
                            if existing_parent_data.mother_finger is not None:
                                file_path = os.path.join(app.config['UPLOAD_REG_FINGER'],
                                                         existing_parent_data.mother_finger)  # Construct the full path to the file
                            # Now Delete the file from the directory
                            if file_path is not None and os.path.exists(file_path):
                                os.remove(file_path)

                            # Get the original file extension
                            _, file_extension = os.path.splitext(uploaded_file_finger_print.filename)
                            # Combine mother_cnic, and file extension to create a custom filename
                            custom_filename = f"{existing_parent_data.mother_cnic}{file_extension}"
                            # Save the file and update the database record with the file path
                            file_path_system = os.path.join(app.config['UPLOAD_REG_FINGER'], custom_filename)  # Set your upload folder path
                            file_full_name = os.path.join("", custom_filename)  # Set your No path for database column
                            uploaded_file_finger_print.save(file_path_system)
                            existing_parent_data.mother_finger = file_full_name

                        db.session.commit()
                        flash("Successfully Finger Data Save.", "success")
                        return redirect('/biometric_authentication')
                    else:
                        flash("Error! Please fill out all required fields.", "danger")
                        return redirect('/biometric_authentication')
                except Exception as e:
                    # If an error occurs during database connection, display error message
                    db.session.rollback()
                    flash(f"Error: Parent Data Not Available, Please Firstly Add the Parent data.", "danger")
                    return redirect('/biometric_authentication')
            else:
                return render_template('Administrator/apply_to_formb.html')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}", "danger")
            return redirect('/biometric_authentication')
    else:
        return render_template('Parent/parent_login.html')


@app.route("/logout_parent")
def logout_parent():
    session.pop('p_name', None)
    session.pop('p_cnic', None)
    session.pop('p_ContactNo', None)
    session.pop('p_UserId', None)
    session.pop('p_photo', None)
    session.pop('p_rol_name', None)
    return render_template('Parent/parent_login.html')
