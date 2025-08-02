from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ussd', methods=['POST'])
def ussd_handler():
    data = request.get_json()
    session_id = data['sessionId']
    phone_number = data['phoneNumber']
    text = data['text'].strip()
    
    response = ""
    if text == "":
        # Initial request
        response = "CON Welcome to ElimuHub Education Fair\n1. Register\n2. Event Info\n3. Contact"
    elif text == "1":
        response = "CON Enter your full name:"
    elif text.startswith("1*"):
        parts = text.split('*')
        if len(parts) == 2:
            response = "CON Select institution:\n1. Al-Azhar\n2. IIUM\n3. Darul Uloom"
        elif len(parts) == 3:
            response = "CON Enter WhatsApp number:"
        elif len(parts) == 4:
            # Save registration to database
            response = "END Registration complete! Event details sent to your WhatsApp."
            
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
