# Telecom ETL Pipeline

## Project Overview
This project implements an ETL (Extract, Transform, Load) pipeline using Python, Prefect, Docker, and MySQL.

The pipeline reads telecom subscription data from a CSV file, performs basic transformations, and loads the cleaned data into a MySQL database.

## Dataset
Telecom Subscriptions Dataset

## Technologies Used
- Python
- Pandas
- Prefect
- MySQL
- Docker
- Docker Compose

## ETL Process

### Extract
Reads telecom subscription data from CSV file.

### Transform
- Renames columns
- Handles missing values
- Cleans the dataset

### Load
Loads the transformed data into MySQL database.

## Database
Database: telecom_db

Table: telecom_data

## Run Project

```bash
docker compose up --build
```

## Author
Wajd A