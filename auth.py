from flask import Blueprint, render_template, request, flash, redirect, url_for
import smtplib

auth = Blueprint('auth', __name__)

@auth.route('/about')
def about():
    return render_template('about.html')

@auth.route('/research')
def research():
    return render_template('research.html')

@auth.route('/publication')
def publication():
    return render_template('publication.html')

@auth.route('/news')
def news():
    return render_template('news.html')

@auth.route('/contact')
def contact():
    return render_template('contact.html')

@auth.route('/submit-form', methods=['GET','POST'])
def submit_form():
    if request.method == 'POST': 
     email = request.form.get('email')
     first_name = request.form.get('firstName')
     last_name = request.form.get('lastName')
     location=request.form.get('address')
     message = request.form.get('Message')
    if any(char in first_name for char in 'àâçéèêëîïôûùüÿñæœ') or any(char in last_name for char in 'àâçéèêëîïôûùüÿñæœ') or any(char in location for char in 'àâçéèêëîïôûùüÿñæœ'):
          flash('Please do not use French characters in the name or location fields.', category='error')
    else:
         # Set up the email server and message
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
            smtp_username = 'jinhanlin6330@gmail.com'
            smtp_password = 'anwwoyzaqospofsj'
            email_subject = 'New message from your website'
            email_body = f'Name: {first_name} {last_name}\nEmail: {email}\nLocation: {location}\nMessage: {message}'
                
             # Send the email
            with smtplib.SMTP(smtp_server, smtp_port) as server:
             server.starttls()
             server.login(smtp_username, smtp_password)
             server.sendmail(smtp_username, smtp_username, f'Subject: {email_subject}\n\n{email_body}')
                        
            flash('Submitted successfully!', category='success')
            return redirect(url_for('views.home'))
    return render_template('contact.html')