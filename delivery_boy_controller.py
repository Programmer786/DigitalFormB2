from sqlalchemy.orm import joinedload
from app import app
from sqlalchemy.exc import IntegrityError
from sqlalchemy import asc, desc
from database_model import *
# from database_model import db, Users,Rol
from flask import render_template, flash, session, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date


@app.route("/delivery_boy_dashboard")
def delivery_boy_dashboard():
    if 'p_cnic' and 'p_rol_name' in session:
        return render_template('DeliveryBoy/index.html')
    else:
        return render_template('Parent/parent_login.html')


@app.route('/delivery_boy_profile', methods=['POST', 'GET'])
def delivery_boy_profile():
    if 'p_cnic' and 'p_rol_name' in session:
        try:
            # role_with_Cnic_data_retrieve = Users.query.order_by(Users.user_id).all()
            session_UserId = session['p_UserId']
            one_record_by_cnic_data_retrieve = Users.query.filter_by(user_id=session_UserId).first()

            return render_template('DeliveryBoy/delivery_boy_profile.html', one_record_data_retrieve=one_record_by_cnic_data_retrieve)
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Parent/parent_login.html')
    else:
        return render_template('Parent/parent_login.html')


@app.route('/disable_role_delivery_boy/<int:UserId>')
def disable_role_delivery_boy(UserId):
    if 'p_cnic' and 'p_rol_name' in session:
        try:
            # get specific user user_id from clerk Table and then check date with UserId related
            sel_one_user = Users.query.filter_by(user_id=UserId).first()
            sel_one_user.isActive = 0
            db.session.commit()
            flash("Record Successfully Disable", "success")
            return redirect('/delivery_boy_profile')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return redirect('/delivery_boy_profile')
    else:
        return render_template('Parent/parent_login.html')


@app.route('/enable_role_delivery_boy/<int:UserId>')
def enable_role_delivery_boy(UserId):
    if 'p_cnic' and 'p_rol_name' in session:
        try:
            # get specific user user_id from clerk Table and then check date with UserId related
            sel_one_user = Users.query.filter_by(user_id=UserId).first()
            sel_one_user.isActive = 1
            db.session.commit()
            flash("Record Successfully Enable", "success")
            return redirect('/delivery_boy_profile')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return redirect('/delivery_boy_profile')
    else:
        return render_template('Parent/parent_login.html')


@app.route('/change_password_delivery_boy/<int:UserId>', methods=['POST', 'GET'])
def change_password_delivery_boy(UserId):
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
                return redirect('/delivery_boy_profile')
            else:
                flash("Error! Your confirm password is wrong, please try again", "danger")
                return redirect('/delivery_boy_profile')
        except IntegrityError:
            db.session.rollback()
            flash("Error. Duplicate CNIC Not Acceptable", "danger")
            return redirect('/delivery_boy_profile')  # Add return statement here
    else:
        # Render the form for GET requests
        return render_template('Parent/parent_login.html')


@app.route('/delivery_boy_for_update/<int:UserId>', methods=['POST', 'GET'])
def delivery_boy_for_update(UserId):
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
            return redirect('/delivery_boy_profile')
        except IntegrityError:
            db.session.rollback()
            flash("Error. Duplicate CNIC and Phone Number Not Acceptable", "danger")
            return redirect('/delivery_boy_profile')  # Add return statement here
    else:
        return render_template('Parent/parent_login.html')


@app.route('/delivery_boy_register', methods=['POST', 'GET'])
def delivery_boy_register():
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
                            rol_name='DeliveryBoy',
                            password=change_to_hashed_password,
                            created_at=datetime.now(),
                            isActive=1
                        )
                        db.session.add(new_entry_register_user)
                        db.session.commit()
                        flash("Successfully Register.", "success")
                        return redirect('/delivery_boy_register')
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
            return redirect('/delivery_boy_register')
    return render_template('DeliveryBoy/delivery_boy_register.html')


@app.route('/delivery_boy_view_location_to_drop', methods=['POST', 'GET'])
def delivery_boy_view_location_to_drop():
    if 'p_cnic' and 'p_rol_name' in session:
        try:
            session_UserId = session['p_UserId']
            complaint_data_retrieve = Complaints.query.filter_by(user_id=session_UserId).all()

            if request.method == 'POST':
                try:
                    complaint_title = request.form['complaint_title']
                    complaint_details = request.form['complaint_details']
                    if (complaint_title != "") and (complaint_details != ""):
                        new_parent_complaint = Complaints(
                            user_id=session_UserId,
                            title=complaint_title,
                            send_details=complaint_details,
                            status='pending'
                        )
                        db.session.add(new_parent_complaint)
                        db.session.commit()
                        flash("Successfully Submitted.", "success")
                        return redirect('/parent_complaint')
                    else:
                        flash("Error! Please fill out this field.", "danger")
                except Exception as e:
                    # If an error occurs during database connection, display error message
                    db.session.rollback()
                    flash(f"Error: {str(e)}", "danger")
                    return redirect('/parent_complaint')
            else:
                return render_template('Parent/parent_complaint.html', complaint_data_retrieve=complaint_data_retrieve)
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return redirect('/parent_complaint')
    else:
        return render_template('Parent/parent_login.html')