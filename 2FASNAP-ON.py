from flask import Flask, render_template, request, redirect, url_for, session
from utils import assess_risk

app = Flask(_name_)
app.secret_key = 's3cr3t'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        device = request.form['device']
        ip = request.remote_addr or '127.0.0.1'

        if username == "jane" and password == "password123":
            risk = assess_risk(username, device, ip)
            session['username'] = username
            session['risk'] = risk

            if risk == 'low':
                return f"✅ Login Successful (Low Risk - No 2FA)"
            elif risk == 'medium':
                return redirect(url_for('otp'))
            else:
                return redirect(url_for('approve'))

        return "❌ Invalid Credentials"
    return render_template('login.html')

@app.route('/otp', methods=['GET', 'POST'])
def otp():
    if request.method == 'POST':
        otp = request.form['otp']
        if otp == '123456':
            return f"✅ OTP Verified. Login Successful (Medium Risk)"
        return "❌ Invalid OTP"
    return render_template('otp.html')

@app.route('/approve', methods=['GET', 'POST'])
def approve():
    if request.method == 'POST':
        if request.form['approve'] == 'yes':
            return f"✅ Access Approved (High Risk - Manual)"
        else:
            return "❌ Access Denied"
    return render_template('approve.html')

if _name_ == '_main_':
    app.run(debug=True)