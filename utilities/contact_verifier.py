import csv
import re

class ContactVerifier:
    def __init__(self):
        self.phone_pattern = re.compile(r'^\+254[17]\d{8}\$')
        self.email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\$')
    
    def verify_phone(self, phone):
        return bool(self.phone_pattern.match(phone))
    
    def verify_email(self, email):
        return bool(self.email_pattern.match(email))
    
    def verify_contacts_file(self, file_path):
        valid = []
        invalid = []
        
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                phone_valid = self.verify_phone(row['phone'])
                email_valid = self.verify_email(row['email']) if 'email' in row else True
                
                if phone_valid and email_valid:
                    valid.append(row)
                else:
                    invalid.append(row)
        
        print(f"Valid contacts: {len(valid)}")
        print(f"Invalid contacts: {len(invalid)}")
        return valid, invalid

# Example usage:
verifier = ContactVerifier()
verifier.verify_contacts_file('contacts_db/institutions/universities.csv')
