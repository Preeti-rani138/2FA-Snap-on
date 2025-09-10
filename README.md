



## 🔐 *Project Title:*

*Dynamic Two-Factor Authentication (2FA) Based on Contextual Risk Analysis*

---

## 📄 *Summary:*

Most current 2FA systems apply the same level of authentication regardless of the context of the login attempt. This project introduces a *dynamic 2FA system* that evaluates the *risk level of each login* based on factors such as *IP address, **time of access, and **device. Based on the risk score, the system adjusts the second layer of authentication — **from no 2FA, to **OTP, to **biometric/manual approval*.

---

## ⚙ *Procedure:*

### ✅ Step 1: Define Risk Factors

Use a rule-based system (or light ML model) to classify login attempts as:

* *Low Risk*: Known device, known IP, usual login time
* *Medium Risk*: New device, slightly unusual time, known location
* *High Risk*: Unknown device, unknown IP, unusual time

### ✅ Step 2: Define Risk Levels and Actions

| Risk Level | Conditions Example                         | 2FA Challenge                            |
| ---------- | ------------------------------------------ | ---------------------------------------- |
| *Low*    | Known device + IP + usual login time       | No 2FA                                   |
| *Medium* | New device + known IP                      | OTP to registered email/SMS              |
| *High*   | Unknown device + foreign IP + unusual time | Biometric or Manual Approval (simulated) |

### ✅ Step 3: Build the Components

#### 1. *Frontend:*

* Simple login page with:

  * Username & Password
  * Device/Browser fingerprinting
  * IP capture
  * Time of login

#### 2. *Backend (Python/Node.js):*

* Maintain user history: Known IPs, login times, devices

* Risk evaluator function:

  python
  def evaluate_risk(ip, device, time):
      if ip in known_ips and device in known_devices and time in usual_times:
          return 'low'
      elif ip in known_ips:
          return 'medium'
      else:
          return 'high'
  

* 2FA challenge manager:

  python
  def handle_2fa(risk_level):
      if risk_level == 'low':
          return "Login Successful"
      elif risk_level == 'medium':
          return send_otp()
      elif risk_level == 'high':
          return simulate_biometric_or_manual_approval()
  

#### 3. *OTP Module (Medium Risk):*

* Generate and send 6-digit OTP to simulated email/SMS

#### 4. *Biometric/Manual Approval (High Risk):*

* For demo: Simulate biometric scan with a fingerprint button or require admin approval

---

## 🧪 *Demo Plan:*

### ✅ *Simulated Scenarios:*

| Scenario | IP      | Device  | Time     | Risk Level | 2FA                |
| -------- | ------- | ------- | -------- | ---------- | ------------------ |
| A        | Known   | Known   | Usual    | Low        | None               |
| B        | Known   | New     | Odd      | Medium     | OTP                |
| C        | Unknown | Unknown | Midnight | High       | Biometric Approval |

Use buttons or pre-filled forms to simulate various login contexts.

---

## 💡 *Bonus Features (Optional):*

* Store user behavior history in a JSON file or database
* Graph login history and risks
* Add Geo-IP lookup to detect location

---

## 📁 *Project Structure:*


dynamic-2fa-project/
├── backend/
│   ├── app.py (Flask or Node backend)
│   └── risk_evaluator.py
├── frontend/
│   ├── index.html
│   ├── login.js
│   └── styles.css
├── utils/
│   └── otp_generator.py
├── db/
│   └── users.json
├── README.md


---

## ✅ *Result:*

A working demo web app with:

* *Risk-based login system*
* *3 dynamic 2FA levels*:

  * Low: Normal login
  * Medium: OTP
  * High: Simulated biometric/manual approval

---

Would you like me to generate the actual code for this in *Python (Flask)* with a simple frontend?
