from flask import Flask, request, jsonify
from datetime import datetime
import csv

app = Flask(__name__)

REGISTRATIONS_FILE = 'registrations.csv'
CONTACTS_FILE = 'messaging/contacts.csv'

def save_registration(name, institution, phone, email):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
    with open(REGISTRATIONS_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, institution, phone, email, timestamp])

def update_contacts(name, phone, email, institution):
    with open(CONTACTS_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, phone, email, institution, 'attendee', datetime.now().strftime('%Y-%m-%d')])

@app.route('/ussd', methods=['POST'])
def ussd_handler():
    # Existing USSD flow with enhanced data collection
    # ...
    if current_step == 4:
        name = steps[1]
        institution = institutions.get(steps[2])
        phone = steps[3]
        email = f"{name.replace(' ', '.').lower()}@example.com"  # Placeholder
        
        save_registration(name, institution, phone, email)
        update_contacts(name, phone, email, institution)
        
        response = "END Registration complete! Event details sent to your WhatsApp. JazakAllah khair"
    
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
