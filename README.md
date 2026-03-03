LongView — A Personal Investment Tracking & Decision Reflection System

1. Project Description
The project will track each trade I make, including the asset, purchase date, quantity, and price, and calculate portfolio performance metrics such as total investment, current value, and profit/loss. Basic visualizations like line charts for portfolio value over time and pie charts for asset allocation will be included. Data will initially be stored in CSV files for simplicity.
In the long term, the project will evolve into a fully interactive web application with enhanced analytics, decision-reflection logs, and optional automation features for data analysis.


2. Purpose & Motivation
This project combines my interest in coding and investing. I aim to improve my programming and data analysis skills while creating a tool that helps me track and reflect on my investment decisions. 
Phase 0 will deliver a working MVP, while future phases will enhance the system with interactive features and analytics. 
My goal is to produce a portfolio-ready project that demonstrates my technical abilities and problem-solving skills, while also supporting my personal investment growth.


3. Intended Users or Audience
This project is primarily for beginner investors who want to track their investment activities and reflect on their decisions over time. It is designed for personal use but can be adapted for a small community of beginner investors.


4. Technologies and Tools
Frontend: HTML, CSS, JavaScript (maybe React later)
Backend / Web Framework: Python (Django)
Database: CSV for early prototype; Django ORM with SQLite for later phases
Data analysis & visualization: pandas, matplotlib / plotly


5. Stretch Goals (Optional)
- Automated portfolio updates from external APIs
- Logging investment rationale for reflection
- Enhanced visualizations or interactive dashboards
- Comparison with other investment strategies, e.g., dollar-cost averaging


6. Anticipated Challenges
Data cleaning and formatting (tracking trades consistently)
Creating visualizations that are clear and informative
Designing a system that is easy to maintain for long-term use


7. Milestone Plan
Sprint Number | Milestone Description
--------------|---------------------
1 (Weeks 1-2) | Research & setup: choose tools, design database structure, plan MVP features 
2 (Weeks 3-4) | Wireframe & Core Design: create sketches or wireframes for the interactive system, define core functionality and user flow
3 (Weeks 5-6) | Prototype Implementation: implement basic trade recording, calculate portfolio metrics, create simple visualizations (Phase 0 MVP)
4 (Weeks 7-8) | Enhancement #1: add asset allocation chart, profit/loss summary, improve data input workflow
5 (Weeks 9-10) | Enhancement #2: add decision reflection log, summary statistics for trade performance
6 (Weeks 11-12) | Cleanup, document code & write final reflection, prepare for demo / presentation



Week 2 Tasks:
Brainstorm basic functions (Phase 0 MVP):
1. Record trade details (asset, purchase date, quantity, price, personal notes)
2. Calculate portfolio metrics (average base prices, gain/loss, total investment changes)
3. Visualize portfolio (line chart for value over time, pie chart for asset allocation)
4. Data storage (CSV)

Future Enhancements / Stretch Goals:
1. Personal journal for investment decisions
2. Risk analysis
3. Comparison with other strategies, e.g., dollar-cost averaging
4. Automated data fetching from APIs

Week 3/4 Tasks:
1. Create wireframes for user interface
2. Define user flow for recording trades and viewing portfolio
3. Plan database structure
4. Set up project repository and initial file struture


Home / Dashboard:
- Portfolio Summary
    Total Investment
    Current Value
    Profit / Loss
- Charts Section
    Line Chart: Portfolio Value Over Time
    Pie Chart: Asset Allocation
- Actions
    “Add Trade” button
    “View Trade History” button

Add Trade Page:
    Asset (text)
    Purchase Date (date)
    Quantity (number)
    Price (number)
    Personal Notes (optional text)

Trade History Page
Table view:
Date | Asset | Quantity | Price | Notes

System Logic
    User Input
    ↓
    Django Model (Trade)
    ↓
    Data Processing (pandas)
    ↓
    Metrics Calculation
    - Total investment
    - Current value
    - Profit / Loss
    ↓
    Visualization Generation
    - Line chart
    - Pie chart
    ↓
    Rendered in Django Template

Fonts:
title: "Bree Serif", serif;
p: "Crimson Text", serif;

Color:
#5fa8d3
#cae9ff
#1b4965
#62b6cb
#bee9e8

Week 5/6 Tasks:
1. finish simple web
2. write simple function for calculation
3. set database

All trades and prices are manually entered
Portfolio metrics are calculated by the system

[ User Input ]
   ↓
Trades (CSV)
Prices (CSV)
   ↓
[ Python Calculation Layer ]
   ↓
Portfolio Metrics
   ↓
Charts / Dashboard

Week 7/8 Tasks:
1. Finilize calculation
2. Import Flask

Week 9/10:
1. Finalize Flask to make sure the website works
2. Add update price page