# 🚀 Amazon Price Tracker & Email Alert – Python Automation Project

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/HTTP-Requests-blue)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Web%20Scraping-brightgreen)
![SMTP](https://img.shields.io/badge/SMTP-Email%20Alerts-yellow)
![dotenv](https://img.shields.io/badge/Environment-dotenv-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)


### A Python automation script that tracks Amazon product prices and sends you an email alert when the price drops below your target. Built to practice clean Python architecture, web scraping, security best practices, and automation workflows.
> ⚠️ Note: Amazon uses dynamic page structures and anti-bot protections, so scraping results may vary depending on the product or region.

## ⚙️ What It Does

- 🔎 Scrapes live product prices from Amazon

- 📉 Detects when the price drops below your defined threshold

- 📩 Sends automatic email alerts

- 🔐 Secures credentials using .env

- ⚠️ Robust error handling for network, parsing, and email operations

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
    ├── README.md
    └── requirements.txt

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
    
    git clone https://github.com/fernandogrh/amazon-price-tracker-python.git
    cd amazon-price-tracker-python
    pip install -r requirements.txt
    python main.py

## 🎯 What This Demonstrates

- Python automation logic

- Web scraping & parsing

- Error handling & debugging

- Secure credential handling

- Real-world workflow design

- Clean project structure

## 🧩 Future Improvements

This project can be extended further with:

- Track multiple products simultaneously

- Add Telegram / WhatsApp alerts

- Schedule automated execution

- Containerize with Docker for deployment

## 👨‍💻 Author

Built by **Fernando Ramirez**