# 🚀 Amazon Price Tracker & Email Alert – Python Automation Project

### A Python automation script that tracks Amazon product prices and sends you an email alert when the price drops below your target. Built to practice clean Python architecture, web scraping, security best practices, and automation workflows.

## ⚙️ What It Does

- 🔎 Scrapes live product prices from Amazon

- 📉 Detects when the price drops below your defined threshold

- 📩 Sends automatic email alerts

- 🔐 Secures credentials using .env

- ⚠️ Handles network, parsing, and email errors safely

## 🛠 Tech Stack

- Python 3

- requests

- BeautifulSoup (bs4)

- smtplib

- python-dotenv

## 📁 Project Structure

    amazon-price-tracker/
    │
    ├── main.py
    ├── .env.example
    ├── .gitignore
    └── README.md

## 🚀 How It Works (Flow)
    Fetch Amazon product page
            ↓
    Extract product price & name
            ↓
    Compare with target price
            ↓
         If lower → Send email alert

## 🔐 Security & Best Practices

Sensitive credentials are never stored in the code.

### Setup instructions:

**Copy .env.example → rename it to .env → fill in your credentials**

Example .env format:

    SMTP_ADDRESS=smtp.gmail.com
    EMAIL_ADDRESS=your_email@gmail.com
    EMAIL_PASSWORD=your_app_password


.env is excluded from GitHub using .gitignore, keeping secrets safe.

## ▶️ How To Run
    pip install requests beautifulsoup4 python-dotenv
    python main.py

## 🎯 What This Demonstrates

- Python automation logic

- Web scraping & parsing

- Error handling & debugging

- Secure credential handling

- Real-world workflow design

- Clean project structure

## 🧩 Future Improvements

- Track multiple products

- Add Telegram / WhatsApp alerts

- Schedule background execution

- Docker deployment

## 👨‍💻 Author

Built by **Fernando Ramirez**