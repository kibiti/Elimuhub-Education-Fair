import csv
import requests
from datetime import datetime

def sync_contacts():
    # Load new registrations
    with open('registrations.csv', 'r') as f:
        registrations = list(csv.DictReader(f))
    
    # Load existing contacts
    with open('messaging/contacts.csv', 'r') as f:
        existing_contacts = {row['phone']: row for row in csv.DictReader(f)}
    
    # Merge and update
    updated = False
    for reg in registrations:
        phone = reg['phone'].strip()
        if phone not in existing_contacts:
            existing_contacts[phone] = {
                'name': reg['name'],
                'phone': phone,
                'institution': reg['institution'],
                'last_updated': datetime.now().strftime('%Y-%m-%d')
            }
            updated = True
    
    # Save if updates
    if updated:
        with open('messaging/contacts.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['name','phone','institution','last_updated'])
            writer.writeheader()
            writer.writerows(existing_contacts.values())
        
        print(f"Synced {len(registrations)} new contacts")
    else:
        print("No new contacts to sync")

if __name__ == "__main__":
    sync_contacts()
