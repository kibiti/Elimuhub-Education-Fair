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
```txt
Elimuhub-Education-Fair/
│
├── 📂 messaging/
│   ├── templates/
│   │   ├── whatsapp_invite_template.md
│   │   └── reminder_template.md
│   ├── messaging_schedule.json
│   └── contacts.csv
│
├── 📂 registration/
│   ├── ussd_flow.json
│   ├── webhook_endpoint.py
│   └── sms_templates.md
│
├── 📂 maps/
│   ├── venue_layout.fig
│   ├── booth_coordinates.json
│   └── mapbox_integration.md
│
├── 📂 emails/
│   ├── mailchimp_templates/
│   │   ├── institution_invite.md
│   │   └── schedule_update.md
│   └── email_config.json
│
├── 📂 schedule/
│   ├── calendar_events.ics
│   └── public_schedule.md
│
├── 📂 assets/
│   ├── posters/
│   │   └── event_poster_template.jpg
│   ├── QR_codes/
│   │   └── registration_qr.png
│   └── social_graphics/
│       └── banner_template.png
│
├── 📂 api/
│   ├── registration_api.md
│   ├── contact_sync.py
│   └── booth_analytics.md
│
└── README.md
```
