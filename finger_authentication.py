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


@app.route('/add_new_child_with_authentication', methods=['POST', 'GET'])
def add_new_child_with_authentication():
    if 'p_cnic' and 'p_rol_name' in session:
        try:
            select_parent_type = request.form['select_parent_type']
            uploaded_file_finger_print_sample = request.files['finger_print_sample']
            child_name = request.form['child_name']
            child_date_birth = request.form['child_date_birth']
            child_gender = request.form['child_gender']

            # Validate if the required fields are not empty
            if select_parent_type and uploaded_file_finger_print_sample and child_name and child_date_birth and child_gender:
                # Retrieve the user ID from the session
                session_user_id = session.get('p_UserId')
                existing_parent_data = ParentData.query.filter_by(user_id=session_user_id).first()
                if select_parent_type == 'Father':
                    file_path_reg = None  # Initialize file_path with a default value
                    if existing_parent_data.father_finger is not None:
                        file_path_reg = os.path.join(app.config['UPLOAD_REG_FINGER'], existing_parent_data.father_finger)  # Construct the full path to the file
                    # Now Delete the file from the directory
                    if file_path_reg is not None and os.path.exists(file_path_reg):
                        # Read the uploaded image
                        uploaded_image = cv2.imread(file_path_reg)
                else:
                    file_path_reg = None  # Initialize file_path with a default value
                    if existing_parent_data.mother_finger is not None:
                        file_path_reg = os.path.join(app.config['UPLOAD_REG_FINGER'], existing_parent_data.mother_finger)  # Construct the full path to the file
                    # Now Delete the file from the directory
                    if file_path_reg is not None and os.path.exists(file_path_reg):
                        # Read the uploaded image
                        uploaded_image = cv2.imread(file_path_reg)

                # Get the original file extension
                _, file_extension = os.path.splitext(uploaded_file_finger_print_sample.filename)
                # Combine father_cnic and file extension to create a custom filename
                custom_filename = f"{existing_parent_data.father_cnic}{file_extension}"
                # Save the file to a specified directory
                file_path_system = os.path.join(app.config['UPLOAD_SAMPLE_FINGER'], custom_filename)
                uploaded_file_finger_print_sample.save(file_path_system)
                # Now, you can retrieve the file from the same directory
                # Construct the full file path
                file_full_path = os.path.join(app.config['UPLOAD_SAMPLE_FINGER'], custom_filename)
                # Read the file using cv2.imread()
                sample_image = cv2.imread(file_full_path)

                # Perform fingerprint matching
                score = fingerprint_matching(sample_image, uploaded_image)

                # After matching, remove the file from the directory
                os.remove(file_full_path)
                if score != 0:
                    new_entry_child_data = ChildData(
                        child_name=child_name,
                        child_birth_date=child_date_birth,
                        child_gender=child_gender,
                        user_id=session_user_id,
                        par_id=existing_parent_data.par_id
                    )
                    db.session.add(new_entry_child_data)
                    db.session.commit()
                    flash(f"Biometric Authentication Successfully {score}", "success")
                else:
                    flash(f"Sorry Biometric Authentication Field {score}", "danger")

            return redirect('/apply_to_formb')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Parent/parent_login.html')
    else:
        return render_template('Parent/parent_login.html')
