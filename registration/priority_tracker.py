import csv
from datetime import datetime, timedelta

class PriorityTracker:
    PRIORITY_LEVELS = {
        'high': {
            'deadline': 48,  # hours
            'categories': ['Tier 1 Universities', 'Title Sponsors', 'Key Stakeholders']
        },
        'medium': {
            'deadline': 168,  # hours (1 week)
            'categories': ['Tier 2 Universities', 'Gold Sponsors', 'Major Madrassas']
        },
        'standard': {
            'deadline': 336,  # hours (2 weeks)
            'categories': ['Tier 3 Institutions', 'Silver Sponsors', 'Regional Youth Orgs']
        }
    }
    
    def __init__(self):
        self.contacts = []
        
    def load_contacts(self, file_path):
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            self.contacts = list(reader)
    
    def get_priority_contacts(self, level):
        deadline = datetime.now() + timedelta(hours=self.PRIORITY_LEVELS[level]['deadline'])
        return [c for c in self.contacts if c['category'] in self.PRIORITY_LEVELS[level]['categories']]

# Example usage:
tracker = PriorityTracker()
tracker.load_contacts('contacts_db/institutions/universities.csv')
high_priority = tracker.get_priority_contacts('high')
