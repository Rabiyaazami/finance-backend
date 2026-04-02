\# Finance Data Processing Backend



\## Overview

This is a backend system built using FastAPI for managing financial records, users, and role-based access control.



\## Features

\- User management with roles (Admin, Analyst, Viewer)

\- Role-based access control

\- Financial records (income \& expense)

\- Dashboard summary (total income, expense, balance)

\- Category-wise analytics



\## Tech Stack

\- Python

\- FastAPI

\- Uvicorn



\## How to Run

1\. Install dependencies:

&#x20;  pip install fastapi uvicorn



2\. Run the server:

&#x20;  python -m uvicorn main:app --reload



3\. Open in browser:

&#x20;  http://127.0.0.1:8000/docs



\## API Endpoints



\### Users

\- POST /users (Admin only)

\- GET /users



\### Records

\- POST /records (Admin only)

\- GET /records



\### Dashboard

\- GET /summary

\- GET /category-summary



\## Assumptions

\- Data is stored in memory (no database)

\- Role is passed as query parameter

\- No authentication implemented



\## Notes

This project focuses on backend logic, API design, and access control.

