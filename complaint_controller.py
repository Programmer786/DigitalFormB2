from sqlalchemy.orm import joinedload
from app import app
from sqlalchemy.exc import IntegrityError
from sqlalchemy import asc, desc
from database_model import *
# from database_model import db, Users,Rol
from flask import render_template, flash, session, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date


@app.route('/parent_complaint', methods=['POST', 'GET'])
def parent_complaint():
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


@app.route('/update_parent_complaint/<int:CompId>', methods=['POST', 'GET'])
def update_parent_complaint(CompId):
    if 'p_cnic' and 'p_rol_name' in session:
        try:
            complaint_title = request.form['complaint_title']
            complaint_details = request.form['complaint_details']

            update_complaints = Complaints.query.filter_by(comp_id=CompId).first()
            update_complaints.title = complaint_title
            update_complaints.send_details = complaint_details
            update_complaints.status = 'Pending'

            db.session.add(update_complaints)
            db.session.commit()
            flash("Record Successfully Updated", "success")
            return redirect('/parent_complaint')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Error: {str(e)}", "danger")
            return redirect('/parent_complaint')
    else:
        return render_template('Parent/parent_login.html')


@app.route('/finalized_parent_complaint/<int:CompId>')
def finalized_parent_complaint(CompId):
    if 'p_cnic' and 'p_rol_name' in session:
        try:
            # get specific user user_id from clerk Table and then check date with UserId related
            sel_one_complaint = Complaints.query.filter_by(comp_id=CompId).first()
            sel_one_complaint.status = "Finalized"
            db.session.commit()
            flash("Record Successfully Finalized", "success")
            return redirect('/parent_complaint')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return redirect('/parent_complaint')
    else:
        return render_template('Parent/parent_login.html')


@app.route('/delete_parent_complaint/<int:CompId>')
def delete_parent_complaint(CompId):
    if 'p_cnic' and 'p_rol_name' in session:
        try:
            # get specific user user_id from clerk Table and then check date with UserId related
            sel_one_complaint = Complaints.query.filter_by(comp_id=CompId).first()
            db.session.delete(sel_one_complaint)
            db.session.commit()
            flash("Complaint Successfully Deleted", "success")
            return redirect('/parent_complaint')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return redirect('/parent_complaint')
    else:
        return render_template('Parent/parent_login.html')


@app.route('/complaint_response', methods=['POST', 'GET'])
def complaint_response():
    if 'cnic' and 'rol_name' in session:
        try:
            complaint_data_retrieve = Complaints.query.all()
            return render_template('Administrator/complaint_response.html', complaint_data_retrieve=complaint_data_retrieve)
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Failed to connect to the database. -> Error: {str(e)}" "", "danger")
            return redirect('/complaint_response')
    else:
        return render_template('Administrator/login.html')


@app.route('/update_admin_complaint/<int:CompId>', methods=['POST', 'GET'])
def update_admin_complaint(CompId):
    if 'cnic' and 'rol_name' in session:
        try:
            complaint_response = request.form['complaint_response']
            status = request.form['status']

            update_complaints = Complaints.query.filter_by(comp_id=CompId).first()
            update_complaints.received_details = complaint_response
            update_complaints.status = status

            db.session.add(update_complaints)
            db.session.commit()
            flash("Record Successfully Updated", "success")
            return redirect('/complaint_response')
        except Exception as e:
            # If an error occurs during database connection, display error message
            db.session.rollback()
            flash(f"Error: {str(e)}", "danger")
            return redirect('/complaint_response')
    else:
        return render_template('Administrator/login.html')
