from sqlalchemy.orm import joinedload
from app import app
from sqlalchemy.exc import IntegrityError
from sqlalchemy import asc, desc, and_
from database_model import *
# from database_model import db, Users,Rol
from flask import render_template, flash, session, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date


@app.route("/")
def home():
    if 'cnic' and 'rol_name' in session:
        # Get today's date
        today = date.today()
        # Fetch real data from the database complaint.status == 'Pending'
        total_request = Requests.query.count()
        total_complaints_pending = Complaints.query.filter_by(status='Pending').count()
        total_complaints = Complaints.query.count()
        total_parent_data = ParentData.query.count()
        total_child_data = ChildData.query.count()
        total_delivery_boy = DeliveryBoyHandover.query.count()
        total_users = Users.query.filter(Users.rol_name != 'parent').count()
        total_manager = Users.query.filter_by(rol_name='Manager').count()
        total_employee = Users.query.filter_by(rol_name='Employee').count()

        return render_template('Administrator/index.html',
                               total_request=total_request,
                               total_complaints_pending=total_complaints_pending,
                               total_complaints=total_complaints,
                               total_parent_data=total_parent_data,
                               total_child_data=total_child_data,
                               total_delivery_boy=total_delivery_boy,
                               total_users=total_users,
                               total_manager=total_manager,
                               total_employee=total_employee)
    else:
        return render_template('Administrator/login.html')


@app.route('/admin_login', methods=['POST', 'GET'])
def admin_login():
    if 'cnic' and 'rol_name' in session:
        session_rol_name = session['rol_name']
        if session_rol_name == 'Administrator':
            return redirect('/')
        elif session_rol_name == 'Manager':
            return redirect('/manager_dashboard')
        elif session_rol_name == 'Employee':
            return redirect('/employee_dashboard')
        else:
            return redirect('/logout')
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
                            session['name'] = user.name
                            session['cnic'] = user.cnic
                            session['ContactNo'] = user.phone
                            session['UserId'] = user.user_id
                            session['photo'] = user.photo
                            session['rol_name'] = user.rol_name

                            if user.rol_name == 'Administrator':
                                return redirect('/')
                            elif user.rol_name == 'Manager':
                                return redirect('/manager_dashboard')
                            elif user.rol_name == 'Employee':
                                return redirect('/employee_dashboard')
                            else:
                                return redirect('/logout')

                        else:
                            flash("Error! Invalid Password, Please try Again!", "danger")
                            return render_template('Administrator/login.html')
                    else:
                        flash("Error! Please Register Your Account and Then Login!", "danger")
                        return render_template('Administrator/login.html')
                else:
                    flash("Error! Invalid CNIC, Please Contact to Administrator!", "danger")
                    return render_template('Administrator/login.html')
            except Exception as e:
                # If an error occurs during database connection, display error message
                db.session.rollback()
                flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
                return render_template('Administrator/login.html')
        return render_template('Administrator/login.html')


@app.route('/role', methods=['POST', 'GET'])
def role():
    if 'cnic' and 'rol_name' in session:
        try:
            # role_with_Cnic_data_retrieve = Users.query.order_by(Users.user_id).all()
            cell_values = ["Manager", "Employee", "Parent", "DeliveryBoy"]
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
                                return redirect('/role')
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
                    return redirect('/role')
            else:
                return render_template('Administrator/role.html', role_with_Cnic_data=role_with_rol_name_data_retrieve)
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Administrator/login.html')
    else:
        return render_template('Administrator/login.html')


@app.route('/profile', methods=['POST', 'GET'])
def user_profile():
    if 'cnic' and 'rol_name' in session:
        try:
            # role_with_Cnic_data_retrieve = Users.query.order_by(Users.user_id).all()
            session_UserId = session['UserId']
            one_record_by_cnic_data_retrieve = Users.query.filter_by(user_id=session_UserId).first()

            return render_template('Administrator/profile.html', one_record_data_retrieve=one_record_by_cnic_data_retrieve)
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Administrator/login.html')
    else:
        return render_template('Administrator/login.html')


@app.route('/user_for_update/<int:UserId>', methods=['POST', 'GET'])
def user_for_update(UserId):
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
            return redirect('/profile')
        except IntegrityError:
            db.session.rollback()
            flash("Error. Duplicate CNIC and Phone Number Not Acceptable", "danger")
            return redirect('/profile')  # Add return statement here
    else:
        return render_template('Administrator/login.html')


@app.route("/update_role_user_get/<int:UserId>")
def update_role_user_get(UserId):
    if 'cnic' and 'rol_name' in session:
        try:
            # get specific user SNo from Office Table and then check date with SNo related
            specific_user_data = Users.query.filter_by(user_id=UserId).first()
            return render_template('Administrator/user_for_update.html', user_for_update=specific_user_data)
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Administrator/login.html')
    else:
        return render_template('Administrator/login.html')


@app.route('/disable_role_user/<int:UserId>')
def disable_role_user(UserId):
    if 'cnic' and 'rol_name' in session:
        try:
            # get specific user user_id from clerk Table and then check date with UserId related
            sel_one_user = Users.query.filter_by(user_id=UserId).first()
            sel_one_user.isActive = 0
            db.session.commit()
            flash("Record Successfully Disable", "success")
            return redirect('/role')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Administrator/login.html')
    else:
        return render_template('Administrator/login.html')


@app.route('/enable_role_user/<int:UserId>')
def enable_role_user(UserId):
    if 'cnic' and 'rol_name' in session:
        try:
            # get specific user user_id from clerk Table and then check date with UserId related
            sel_one_user = Users.query.filter_by(user_id=UserId).first()
            sel_one_user.isActive = 1
            db.session.commit()
            flash("Record Successfully Enable", "success")
            return redirect('/role')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Administrator/login.html')
    else:
        return render_template('Administrator/login.html')


@app.route('/change_password/<int:UserId>', methods=['POST', 'GET'])
def change_password(UserId):
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
                return redirect('/role')
            else:
                flash("Error! Your confirm password is wrong, please try again", "danger")
                return redirect('/role')
        except IntegrityError:
            db.session.rollback()
            flash("Error. Duplicate CNIC Not Acceptable", "danger")
            return redirect('/role')  # Add return statement here
    else:
        # Render the form for GET requests
        return render_template('Administrator/login.html')


@app.route('/view_request_formb', methods=['POST', 'GET'])
def view_request_formb():
    if 'cnic' and 'rol_name' in session:
        try:
            # Retrieve the parent data where view_request is False
            forward_to_admin_0 = (
                ParentData.query
                .filter(ParentData.status == 'Processing', ParentData.forward_to_admin == True)
                .all()
            )

            # Initialize an empty list to store par_id values
            par_ids = []

            # Extract par_id values from the view_request_0 list
            for parent_data in forward_to_admin_0:
                par_ids.append(parent_data.par_id)

            print("Par_ids: ", par_ids)
            # Query ChildData where par_id is in the list of extracted par_ids
            childs_formb_data_retrieve = (
                ChildData.query
                .join(ChildData.parent_data)
                .filter(ChildData.par_id.in_(par_ids))
                .all()
            )
            return render_template('Administrator/view_request_formb.html', childs_formb_data_retrieve=childs_formb_data_retrieve,
                                   forward_to_admin_0=forward_to_admin_0)
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return redirect('/')
    else:
        return render_template('Administrator/login.html')


@app.route('/view_forward_formb', methods=['POST', 'GET'])
def view_forward_formb():
    if 'cnic' and 'rol_name' in session:
        try:
            # Retrieve the parent data where view_request is False
            forward_to_admin_0 = ParentData.query.filter_by(forward_to_admin=True).all()

            # Initialize an empty list to store par_id values
            par_ids = []

            # Extract par_id values from the view_request_0 list
            for parent_data in forward_to_admin_0:
                par_ids.append(parent_data.par_id)

            print("Par_ids: ", par_ids)
            # Query ChildData where par_id is in the list of extracted par_ids
            childs_formb_data_retrieve = (
                ChildData.query
                .join(ChildData.parent_data)
                .filter(ChildData.par_id.in_(par_ids))
                .all()
            )
            return render_template('Administrator/view_forward_formb.html', childs_formb_data_retrieve=childs_formb_data_retrieve,
                                   forward_to_admin_0=forward_to_admin_0)
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return redirect('/')
    else:
        return render_template('Administrator/login.html')


@app.route('/all_form_b_record', methods=['POST', 'GET'])
def all_form_b_record():
    delivery_boy = (
        Users.query
        .join(ChildData.parent_data)  # Assuming there's a relationship between Users and ChildData
        .filter(
            and_(
                Users.rol_name == 'DeliveryBoy',
                Users.delivery_status == 'Available'
            )
        ).all()
    )
    if 'cnic' and 'rol_name' in session:
        try:
            # Retrieve the parent data where view_request is False
            forward_to_admin_0 = ParentData.query.all()

            # Initialize an empty list to store par_id values
            par_ids = []

            # Extract par_id values from the view_request_0 list
            for parent_data in forward_to_admin_0:
                par_ids.append(parent_data.par_id)

            print("Par_ids: ", par_ids)
            # Query ChildData where par_id is in the list of extracted par_ids
            childs_formb_data_retrieve = (
                ChildData.query
                .join(ChildData.parent_data)
                .filter(ChildData.par_id.in_(par_ids))
                .all()
            )
            return render_template('Administrator/all_form_b_record.html', childs_formb_data_retrieve=childs_formb_data_retrieve,
                                   forward_to_admin_0=forward_to_admin_0,
                                   delivery_boy=delivery_boy)
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return redirect('/')
    else:
        return render_template('Administrator/login.html')


@app.route('/form_b_handover_to_db/<int:ParId>', methods=['GET', 'POST'])
def form_b_handover_to_db(ParId):
    if 'cnic' in session and 'rol_name' in session:
        if request.method == 'POST':
            try:
                sel_one_parent = ParentData.query.filter_by(par_id=ParId).first()
                sel_one_parent.delivery_status = 'Not_Received'

                get_delivery_boy_name = request.form.get('delivery_boy_name')
                new_entry_delivery_boy = DeliveryBoyHandover(
                    user_id=get_delivery_boy_name,
                    par_id=ParId,
                    drop_address=sel_one_parent.address,
                    status='OnTheWay'
                )
                db.session.add(new_entry_delivery_boy)
                db.session.commit()
                flash("Form-B successfully handed over to delivery boy.", "success")
                return redirect('/all_form_b_record')
            except Exception as e:
                # If an error occurs during database connection, display error message
                db.session.rollback()
                flash(f"Failed to connect to the database. -> Error: {str(e)}", "danger")
                return redirect('/all_form_b_record')
        else:
            return redirect('/all_form_b_record')
    else:
        return render_template('Administrator/login.html')


@app.route('/form_b_print/<int:ParId>')
def form_b_print(ParId):
    if 'cnic' and 'rol_name' in session:
        try:
            retrieve_parent_data = ParentData.query.filter_by(par_id=ParId).first_or_404()
            # Retrieve employee and their salary transactions
            child_form_b_retrieve = (
                ChildData.query
                .filter_by(par_id=ParId)
                .join(ParentData)
                .options(joinedload(ChildData.parent_data))
                .all()
            )

            # Now, formatted_date contains the month and year, e.g., "2024-04-09"
            current_datetime = datetime.now()
            formatted_date_time = current_datetime.strftime('%Y-%m-%d')
            return render_template('Administrator/form_b_design.html', child_form_b_retrieve=child_form_b_retrieve,
                                   formatted_date_time=formatted_date_time,
                                   retrieve_parent_data=retrieve_parent_data)
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Administrator/login.html')
    else:
        return render_template('Administrator/login.html')


@app.route('/all_delivery_boy', methods=['POST', 'GET'])
def all_delivery_boy():
    if 'cnic' and 'rol_name' in session:
        try:
            # Retrieve the parent data where view_request is False
            # all_delivery_boy_data_retrieve = Users.query.filter_by(rol_name='DeliveryBoy').all()
            all_delivery_boy_data_retrieve = (
                Users.query
                .filter_by(rol_name='DeliveryBoy')
                .join(District)
                .options(joinedload(Users.district))
                .all()
            )

            return render_template('Administrator/all_delivery_boy.html', all_delivery_boy_data_retrieve=all_delivery_boy_data_retrieve)
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return redirect('/')
    else:
        return render_template('Administrator/login.html')


@app.route('/admin_finalized_formb/<int:ParId>')
def admin_finalized_formb(ParId):
    if 'cnic' and 'rol_name' in session:
        try:
            sel_one_parent_data = ParentData.query.filter_by(par_id=ParId).first()
            sel_one_parent_data.status = 'Complete'
            db.session.commit()
            flash("Record Successfully Finalized By Admin", "success")
            return redirect('/view_request_formb')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Administrator/login.html')
    else:
        return render_template('Administrator/login.html')


@app.route('/rejected_submitted_form/<int:ParId>')
def rejected_submitted_form1(ParId):
    if 'cnic' and 'rol_name' in session:
        try:
            sel_one_parent_data = ParentData.query.filter_by(par_id=ParId).first()
            sel_one_parent_data.status = 'Rejected'
            sel_one_parent_data.forward_to_admin = True
            db.session.commit()
            flash("Record Successfully Rejected", "success")
            return redirect('/view_request_formb')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return render_template('Administrator/login.html')
    else:
        return render_template('Administrator/login.html')


@app.route("/logout")
def logout():
    session.pop('name', None)
    session.pop('cnic', None)
    session.pop('ContactNo', None)
    session.pop('UserId', None)
    session.pop('photo', None)
    session.pop('district', None)
    session.pop('rol_name', None)
    return render_template('Administrator/login.html')
