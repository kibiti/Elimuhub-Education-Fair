import csv
from datetime import datetime

class ContactManager:
    def __init__(self):
        self.categories = {
            'universities': 'contacts_db/institutions/universities.csv',
            'sponsors': 'contacts_db/sponsors/title_sponsors.csv',
            'madrassas': 'contacts_db/madrassas/nairobi_county.csv'
        }
    
    def get_contacts(self, category, tier=None):
        contacts = []
        with open(self.categories[category], 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if not tier or row.get('tier') == tier:
                    contacts.append(row)
        return contacts

    def log_contact(self, name, phone, contact_type):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
        with open('contact_log.csv', 'a') as f:
            f.write(f"{timestamp},{name},{phone},{contact_type}\n")

# Example usage:
manager = ContactManager()
priority_universities = manager.get_contacts('universities', tier='Tier 1')
