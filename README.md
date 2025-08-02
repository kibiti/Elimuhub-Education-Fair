# ElimuHub Islamic Education Fair Tech Suite

Complete technology solution for managing Islamic education fairs with USSD registration, WhatsApp communications, and venue mapping.

## ✨ Features
- USSD registration system (38655#)
- WhatsApp invitation templates
- Interactive venue map with institution booths
- Contact synchronization system
- Email campaign templates
- Schedule management

## 🚀 Setup
1. Clone repository: `git clone https://github.com/kibiti/Elimuhub-Education-Fair`
2. Install dependencies: `pip install -r requirements.txt`
3. Configure environment variables:
   ```env
   MAPBOX_TOKEN=your_token
   AT_API_KEY=africas_talking_key

## Repository: https://github.com/kibiti/Elimuhub-Education-Fair
```bash
Elimuhub-Education-Fair/
│
├── 📂 contacts_db/
│   ├── institutions/
│   │   ├── universities.csv
│   │   ├── colleges.csv
│   │   └── specialized_institutes.csv
│   ├── sponsors/
│   │   ├── title_sponsors.csv
│   │   ├── gold_sponsors.csv
│   │   └── silver_sponsors.csv
│   ├── madrassas/
│   │   ├── nairobi_county.csv
│   │   ├── central_kenya.csv
│   │   └── coast_region.csv
│   ├── stakeholders/
│   │   ├── government.csv
│   │   ├── religious_orgs.csv
│   │   └── educational_associations.csv
│   └── youth_associations/
│       ├── national.csv
│       └── regional.csv
│
├── 📂 messaging/
│   ├── templates/
│   │   ├── university_invite.md
│   │   ├── sponsor_proposal.md
│   │   ├── madrassa_invite.md
│   │   └── youth_association.md
│   └── contact_manager.py
│
├── 📂 registration/
│   ├── ussd_flow.json
│   ├── webhook_endpoint.py
│   └── priority_tracker.py
│
└── 📂 utilities/
    ├── csv_importer.py
    ├── contact_verifier.py
    └── response_tracker.py
├── 📂 api/
│   ├── registration_api.md
│   ├── contact_sync.py
│   └── booth_analytics.md
│
└── README.md
```
