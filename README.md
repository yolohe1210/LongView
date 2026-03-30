# LongView – Portfolio Tracking Dashboard

LongView is a lightweight web-based portfolio tracker built with Flask.  
It allows users to record trades, update asset prices, and visualize portfolio performance through an interactive web dashboard.
This project is currently in Phase 0 (manual data input version), and future improvements aim to evolve it into a fully automated and scalable portfolio management system.

## Live Demo
https://longview-cv5j.onrender.com

## Features

- Record asset purchases and track trade history
- Update asset prices manually
- View portfolio value over time with a line chart
- Visualize asset allocation with a pie chart
- Simple and intuitive web dashboard

## Tech Stack

Backend:
- Python
- Flask

Frontend:
- HTML
- CSS
- JavaScript
- Chart.js

Deployment:
- Render (cloud hosting)
- GitHub (version control)

## How It Works

1. Users record asset purchases through the trade page.
2. Asset prices can be updated manually.
3. The backend calculates portfolio value and allocation.
4. The dashboard visualizes portfolio performance using charts.

## What I learned:

- Full-stack web development
- Data handling and calculations
- UI/UX design basics
- Deployment workflow

## Future Improvements

### 1. Automated Market Data Integration
Currently, asset prices are updated manually.  
In the future, I plan to integrate financial data APIs (such as Yahoo Finance or Alpha Vantage) to automatically fetch real-time or daily prices.

This would allow:
- Real-time portfolio valuation
- Reduced manual input
- More accurate performance tracking

---

### 2. Advanced Performance Metrics
The current system only calculates total return.  
Future versions will include more detailed financial metrics such as:

- Daily profit/loss tracking
- Percentage change over time
- Annualized return (CAGR)
- Volatility and drawdown analysis

These metrics would make the tool more useful for long-term investment analysis.

---

### 3. Database Integration
The current implementation uses CSV files for data storage.  
This will be replaced with a relational database (e.g., SQLite or PostgreSQL) to:

- Improve data reliability
- Support larger datasets
- Enable more complex queries

---

### 4. User Authentication System
Adding user accounts would allow:

- Multiple users to manage their own portfolios
- Secure data storage
- Personalized dashboards

This would transition the project from a personal tool to a multi-user web application.

---

### 5. Improved UI/UX Design
Future UI improvements include:

- More responsive design for mobile devices
- Better data visualization (e.g., interactive charts, tooltips)
- Cleaner layout inspired by modern FinTech dashboards

---

### 6. Transaction Management Features
Future versions may include:

- Editing or deleting trades
- Filtering and searching trade history
- Categorizing assets (e.g., stocks, crypto, ETFs)

This would improve usability and make the system more flexible.

## Author
Yin He
