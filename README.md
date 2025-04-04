# Fake Check Generator and Database Integration

This project generates fake retail check data, stores it in CSV files, and automatically inserts it into a PostgreSQL database. Designed for testing and demonstration purposes.

## Features

- 🛍️ Random check generation with realistic products/prices
- 📁 Automatic CSV file management
- 🗄️ PostgreSQL database integration
- 🧹 Automatic cleanup of processed files
- ⚙️ Configurable database connection

## Project Structure
├── data/ # CSV files storage (auto-generated)
├── sql/
│ └── create_table.sql # DDL script for cheque table
├── img/ # Screenshots for automation setup
├── config.ini # Database credentials
├── generate_data.py # Random check generator
├── database_class.py # PostgreSQL connection handler
├── run.py # CSV to database importer
└── README.md

## Prerequisites

- Python 3.8+
- PostgreSQL 12+
- Required packages:
  ```bash
  pip install psycopg2-binary configparser

## Installation

1. Clone repository:
git clone [your-repository-url]
cd fake-check-generator

2. Create and activate virtual environment:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. Install dependencies:
pip install -r requirements.txt

## Configuration
1. Create config.ini in project root:
[database_info]
DATABASE = your_db_name
USER = postgres
PASSWORD = your_password
HOST = localhost
PORT = 5432

2. Create PostgreSQL database:
CREATE DATABASE your_db_name;

## Usage

1. Generate test data:
python data_generator.py

Creates CSV files in data/ directory with structure:
doc_id,item,category,amount,price,discount
vn0khIlo1E,Microwave,Appliances,2,89.99,0
uqbAj8UFcY,Loaf Pan,Bakeware,3,12.99,0

2. Import to database:

python db_importer.py




