Disaster Relief Resource Allocator
📌 Project Overview

The Disaster Relief Resource Allocator is a Streamlit-based application designed to manage disaster relief requests and efficiently allocate limited resources such as food, water, and shelter.

The system validates NGO identities, detects duplicate requests, prioritizes vulnerable groups, and allocates available resources based on priority.

🎯 Objectives
Verify registered NGO requester IDs
Submit and manage disaster relief requests
Detect duplicate requests
Identify high-priority requests for vulnerable groups
Allocate limited relief resources efficiently
Track remaining resources
Provide a real-time operations dashboard
🚀 Key Features
1. NGO Identity Validation

Only registered NGO IDs can submit relief requests.

Example:

NGO001
NGO002
NGO003
NGO004
NGO005
2. Relief Request Management

NGOs can submit:

Disaster location
Resource required
Quantity required
Vulnerable group status
3. Duplicate Detection

The system prevents the same NGO from submitting the same resource request for the same location multiple times.

4. Priority Management

Requests for vulnerable groups are automatically assigned:

HIGH Priority

Other requests are assigned:

NORMAL Priority

5. Resource Allocation

Available resources include:

🍚 Food Kits
💧 Water Bottles
🏠 Shelter Spaces

High-priority requests are processed before normal-priority requests.

6. Dashboard

The dashboard displays:

Total Requests
High Priority Requests
Allocated Requests
Pending Requests
Remaining Resources
🛠️ Technologies Used
Python
Streamlit
GitHub
Python data structures
Session State
📂 Project Structure
Disaster-Relief-Allocator/
│
├── app.py
├── allocator.py
├── validation.py
└── README.md
▶️ How to Run

Install Streamlit:

python -m pip install streamlit

Run the application:

python -m streamlit run app.py

The application will open in your browser.

🔄 System Workflow
NGO Request
     ↓
Identity Validation
     ↓
Location Validation
     ↓
Duplicate Check
     ↓
Priority Assignment
     ↓
Resource Allocation
     ↓
Allocation Status
     ↓
Dashboard & Remaining Resources
👩‍💻 Project Purpose

This project demonstrates how software and AI-oriented decision-support concepts can be used to improve disaster relief resource management by prioritizing urgent needs and efficiently distributing limited resources.

📌 Future Enhancements
Database integration
Real-time disaster data
GPS-based disaster location tracking
NGO registration system
Admin authentication
Email/SMS notifications
AI-based demand prediction
Cloud deployment
