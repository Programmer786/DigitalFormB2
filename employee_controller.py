from sqlalchemy.orm import joinedload
from app import app
from sqlalchemy.exc import IntegrityError
from sqlalchemy import asc, desc
from database_model import *
# from database_model import db, Users,Rol
from flask import render_template, flash, session, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date


def notification_data_send_into_session():
    notification_data_retrieve = Notification.query.all()
    # Check the status of each notification and convert them to dictionaries
    notification_dicts = []
    if notification_data_retrieve:
        for entry in notification_data_retrieve:
            if entry.end_date >= date.today():
                entry.status = "Live"
            else:
                entry.status = "Ended"
            notification_dict = {
                'n_id': entry.n_id,
                'notification_info': entry.notification_info,
                'end_date': entry.end_date.strftime('%d-%m-%Y'),  # Convert a datetime object to string '%Y-%m-%d'
                'status': entry.status
            }
            notification_dicts.append(notification_dict)

    # Store the list of dictionaries in the session
    session['notification_data'] = notification_dicts


@app.route("/employee_dashboard")
def employee_dashboard():
    if 'cnic' and 'rol_name' in session:
        # Remove the 'notification_data' item from the session for new data
        session.pop('notification_data', None)
        # notification data send to session
        notification_data_send_into_session()

        # Get today's date
        today = date.today()
        # Fetch real data from the database complaint.status == 'Pending'
        total_request = Requests.query.count()
        total_complaints_pending = Complaints.query.filter_by(status='Pending').count()
        total_complaints = Complaints.query.count()
        total_parent_data = ParentData.query.count()
        total_form_b_request = ParentData.query.filter_by(forward_to_admin=False).count()
        total_form_b_forward = ParentData.query.filter_by(forward_to_admin=True).count()
        total_child_data = ChildData.query.count()
        total_delivery_boy = DeliveryBoyHandover.query.count()
        total_users = Users.query.filter(Users.rol_name != 'parent').count()
        total_manager = Users.query.filter_by(rol_name='Manager').count()
        total_employee = Users.query.filter_by(rol_name='Employee').count()

        return render_template('Employee/index.html',
                               total_request=total_request,
                               total_complaints_pending=total_complaints_pending,
                               total_complaints=total_complaints,
                               total_parent_data=total_parent_data,
                               total_child_data=total_child_data,
                               total_delivery_boy=total_delivery_boy,
                               total_users=total_users,
                               total_manager=total_manager,
                               total_employee=total_employee,
                               total_form_b_request=total_form_b_request,
                               total_form_b_forward=total_form_b_forward)
    else:
        return render_template('Administrator/login.html')


@app.route('/employee_role', methods=['POST', 'GET'])
def employee_role():
    if 'cnic' and 'rol_name' in session:
        try:
            # role_with_Cnic_data_retrieve = Users.query.order_by(Users.user_id).all()
            cell_values = ["Parent", "DeliveryBoy"]
            role_with_rol_name_data_retrieve = Users.query.filter(
                Users.rol_name.in_(cell_values)
            ).all()

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
                                    rol_name=r_user_role,
                                    password=change_to_hashed_password,
                                    created_at=datetime.now(),
                                    isActive=1
                                )
                                db.session.add(new_entry_register_user)
                                db.session.commit()
                                flash("Successfully Register.", "success")
                                return redirect('/employee_role')
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
                    return redirect('/employee_role')
            else:
                return render_template('Employee/employee_role.html', role_with_Cnic_data=role_with_rol_name_data_retrieve)
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Administrator/login.html')
    else:
        return render_template('Administrator/login.html')


@app.route('/employee_profile', methods=['POST', 'GET'])
def employee_profile():
    if 'cnic' and 'rol_name' in session:
        try:
            # role_with_Cnic_data_retrieve = Users.query.order_by(Users.user_id).all()
            session_UserId = session['UserId']
            one_record_by_cnic_data_retrieve = Users.query.filter_by(user_id=session_UserId).first()

            return render_template('Employee/employee_profile.html', one_record_data_retrieve=one_record_by_cnic_data_retrieve)
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Administrator/login.html')
    else:
        return render_template('Administrator/login.html')


@app.route('/employee_for_update/<int:UserId>', methods=['POST', 'GET'])
def employee_for_update(UserId):
    if 'cnic' and 'rol_name' in session:
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
            session['name'] = get_name
            session['cnic'] = get_cnic
            session['ContactNo'] = get_phone

            db.session.add(update_user)
            db.session.commit()
            flash("Record Successfully Updated", "success")
            return redirect('/employee_role')
        except IntegrityError:
            db.session.rollback()
            flash("Error. Duplicate CNIC and Phone Number Not Acceptable", "danger")
            return redirect('/employee_role')  # Add return statement here
    else:
        return render_template('Administrator/login.html')


@app.route('/disable_role_employee/<int:UserId>')
def disable_role_employee(UserId):
    if 'cnic' and 'rol_name' in session:
        try:
            # get specific user user_id from clerk Table and then check date with UserId related
            sel_one_user = Users.query.filter_by(user_id=UserId).first()
            sel_one_user.isActive = 0
            db.session.commit()
            flash("Record Successfully Disable", "success")
            return redirect('/employee_role')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return redirect('/employee_role')
    else:
        return render_template('Administrator/login.html')


@app.route('/enable_role_employee/<int:UserId>')
def enable_role_employee(UserId):
    if 'cnic' and 'rol_name' in session:
        try:
            # get specific user user_id from clerk Table and then check date with UserId related
            sel_one_user = Users.query.filter_by(user_id=UserId).first()
            sel_one_user.isActive = 1
            db.session.commit()
            flash("Record Successfully Enable", "success")
            return redirect('/employee_role')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return redirect('/employee_role')
    else:
        return render_template('Administrator/login.html')


@app.route('/change_password_employee/<int:UserId>', methods=['POST', 'GET'])
def change_password_employee(UserId):
    if 'cnic' and 'rol_name' in session:
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
                return redirect('/employee_profile')
            else:
                flash("Error! Your confirm password is wrong, please try again", "danger")
                return redirect('/employee_profile')
        except IntegrityError:
            db.session.rollback()
            flash("Error. Duplicate CNIC Not Acceptable", "danger")
            return redirect('/employee_profile')  # Add return statement here
    else:
        # Render the form for GET requests
        return render_template('Administrator/login.html')


@app.route('/view_request_employee', methods=['POST', 'GET'])
def view_request_employee():
    if 'cnic' and 'rol_name' in session:
        try:
            # Retrieve the parent data where view_request_employee is False
            forward_to_admin_0 = ParentData.query.filter_by(forward_to_admin=False).all()

            # Initialize an empty list to store par_id values
            par_ids = []

            # Extract par_id values from the view_request_employee_0 list
            for parent_data in forward_to_admin_0:
                par_ids.append(parent_data.par_id)

            print("Par_ids: ",par_ids)
            # Query ChildData where par_id is in the list of extracted par_ids
            childs_formb_data_retrieve = (
                ChildData.query
                .join(ChildData.parent_data)
                .filter(ChildData.par_id.in_(par_ids))
                .all()
            )
            return render_template('Employee/view_request_employee.html', childs_formb_data_retrieve=childs_formb_data_retrieve,
                                   forward_to_admin_0=forward_to_admin_0)
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return redirect('/employee_dashboard')
    else:
        return render_template('Administrator/login.html')


@app.route('/view_forward_employee', methods=['POST', 'GET'])
def view_forward_employee():
    if 'cnic' and 'rol_name' in session:
        try:
            # Retrieve the parent data where view_forward_employee is False
            forward_to_admin_0 = ParentData.query.filter_by(forward_to_admin=True).all()

            # Initialize an empty list to store par_id values
            par_ids = []

            # Extract par_id values from the view_forward_employee_0 list
            for parent_data in forward_to_admin_0:
                par_ids.append(parent_data.par_id)

            print("Par_ids: ",par_ids)
            # Query ChildData where par_id is in the list of extracted par_ids
            childs_formb_data_retrieve = (
                ChildData.query
                .join(ChildData.parent_data)
                .filter(ChildData.par_id.in_(par_ids))
                .all()
            )
            return render_template('Employee/view_forward_employee.html', childs_formb_data_retrieve=childs_formb_data_retrieve,
                                   forward_to_admin_0=forward_to_admin_0)
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return redirect('/employee_dashboard')
    else:
        return render_template('Administrator/login.html')


@app.route('/form_forward_to_admin_by_employee/<int:ParId>')
def form_forward_to_admin_by_employee(ParId):
    if 'cnic' and 'rol_name' in session:
        try:
            sel_one_parent_data = ParentData.query.filter_by(par_id=ParId).first()
            sel_one_parent_data.forward_to_admin = True
            sel_one_parent_data.status = 'Processing'
            db.session.commit()
            flash("Record Successfully Forward to Admin", "success")
            return redirect('/view_request_employee')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Administrator/login.html')
    else:
        return render_template('Administrator/login.html')


@app.route('/rejected_submitted_form_by_employee/<int:ParId>')
def rejected_submitted_form_by_employee(ParId):
    if 'cnic' and 'rol_name' in session:
        try:
            sel_one_parent_data = ParentData.query.filter_by(par_id=ParId).first()
            sel_one_parent_data.status = 'Rejected'
            sel_one_parent_data.forward_to_admin = True
            db.session.commit()
            flash("Record Successfully Rejected", "success")
            return redirect('/view_request_employee')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Administrator/login.html')
    else:
        return render_template('Administrator/login.html')



