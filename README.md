
# Cricbuzz Live Stats Dashboard

A Streamlit-based dashboard for visualizing live cricket scores and player statistics, powered by data from Cricbuzz. This application provides real-time match updates and detailed player performance metrics through an interactive web interface.

## Features

- **Live Match Scores**: View real-time scores and match details for ongoing cricket matches.
- **Player Statistics**: Explore top batting and bowling statistics from various matches and series.
- **SQL Query Interface**: Run custom SQL queries on MySQL cricket databases for advanced analytics.
- **CRUD Operations**: Perform Create, Read, Update, and Delete operations on player statistics in the MySQL database.
- **Multi-page Interface**: Navigate through different sections using the sidebar menu.

## Project Structure

```
cricbuzz_livestats/
├── app.py                 # Main Streamlit application entry point
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
│
├── pages/                # Streamlit multi-page modules
│   ├── home.py           # Home page with project overview
│   ├── live_matches.py   # Live match scores and details
│   ├── top_stats.py      # Top batting/bowling statistics
│   ├── sql_queries.py    # SQL query interface for analytics
│   └── crud_operations.py # CRUD operations for player stats
│
├── utils/                # Utility functions
│   └── db_connection.py  # MySQL database connection management
│
└── notebooks/            # Jupyter notebooks for development
    └── data_fetching.ipynb # API testing and database operations
```

## Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd cricbuzz_livestats
   ```
2. **Install required dependencies**

   ```bash
   pip install -r requirements.txt
   ```
3. **Set up MySQL Database**

   - Install MySQL Server on your system
   - Create a database for the project
   - Update the database connection details in `utils/db_connection.py`
4. **Run the application**

   ```bash
   python -m streamlit run app.py
   ```
5. **Access the dashboard**

   - The application will open automatically in your default web browser
   - Alternatively, navigate to `http://localhost:8501`

## Usage

1. **Home Page**: Start here for an overview of the project and its capabilities.
2. **Live Matches**: View current matches with real-time score updates.
3. **Player Stats**: Explore detailed batting and bowling statistics.
4. **SQL Queries**: Execute custom SQL queries on the MySQL cricket database.
5. **CRUD Operations**: Manage player statistics through create, read, update, and delete operations.

## Dependencies

- streamlit
- pandas
- requests
- beautifulsoup4
- mysql-connector-python

## Database Configuration

Update the MySQL connection details in `utils/db_connection.py`:

```python
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="cricbuzz_stats"
    )
```

## Setup Notes

- Ensure you have Python 3.7+ installed
- MySQL Server must be installed and running
- Create the necessary database tables before running the application
- API calls are made to Cricbuzz for live match data
- Configure your MySQL credentials in the database connection utility

## Navigation

Use the sidebar menu to switch between different sections of the application. Each page provides specific functionality for viewing and managing cricket data.
