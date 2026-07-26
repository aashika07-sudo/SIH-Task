Village Water Point Monitoring System

Project Overview

The Village Water Point Monitoring System is a web-based application developed to monitor and manage the status of water points in villages.

The system allows users to register water point readings, view all recorded water points, search for specific water points, filter records based on their working status, and delete individual records when required.

The main purpose of this project is to help identify water points that are working properly and quickly prioritize water points that have failed or require attention.


Objectives

- Monitor the status of village water points.
- Register new water point readings.
- Identify working and failed water points.
- Search water points using Water Point ID or habitation name.
- Filter water points based on their status.
- Display failed water points for easy identification.
- Delete individual records when required.
- Store water point data using an SQLite database.
- Provide a simple and user-friendly web interface.


Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript

Requirements
Before running the project, make sure the following are installed on your computer:
- Python 3.x
- Flask
- A web browser
- Git (optional, for version control)

Project Execution Steps
Step 1: Clone the Repository
Open the terminal and clone the GitHub repository:
git clone https://github.com/aashika07-sudo/SIH-Task.git

Step 2: Open the Project Folder
Navigate to the project directory:
cd SIH-Task

Step 3: Create a Virtual Environment
Create a Python virtual environment:
python -m venv venv

Step 4: Activate the Virtual Environment
For Windows:
venv\Scripts\activate

Step 5: Install Flask
Install Flask using:
pip install flask

Step 6: Initialize the Database
Run the database file:
python database.py
This will create the SQLite database and the required database table.
If the database has already been created, this step may not be required.

Step 7: Run the Flask Application
Start the Flask application:
python app.py
The terminal will show a local URL similar to:
http://127.0.0.1:5000

Step 8: Open the Application
Open your web browser and enter:
http://127.0.0.1:5000
The Village Water Point Monitoring System will now be available.

Application Features

1. Dashboard

The dashboard provides an overview of the water point records.

It displays:

- Total number of records
- Number of working water points
- Number of failed water points


2. Register Water Point Reading

Users can register a new water point reading by providing details such as:

- Water Point ID
- Habitation
- Flow Status
- Usage Count

After submitting the form, the new record is stored in the SQLite database.


3. Water Point Listing

The listing page displays all registered water point readings.

The records include:

- Reading ID
- Water Point ID
- Habitation
- Status
- Usage Count
- Recorded Date and Time


4. Search

Users can search for a specific water point using:

- Water Point ID
- Habitation name


5. Filter

Users can filter the records based on their status:

- All
- Working
- Failed

The failed water points are prioritized and displayed first.


6. Delete Record

Each record has a Delete button.

Users can delete a specific water point record when required.

A confirmation message is displayed before deleting the record.


Database

The project uses SQLite for storing water point readings.

The database file is:

water_points.db

The main table used in the project is:

readings

The table stores information such as:

- Reading ID
- Water Point ID
- Habitation
- Flow Status
- Usage Count
- Recorded Date and Time


Sample Data

Water Point ID: WP001
Habitation: North Colony
Status: Working
Usage Count: 45

Water Point ID: WP002
Habitation: South Colony
Status: Working
Usage Count: 32

Water Point ID: WP003
Habitation: East Colony
Status: Failed
Usage Count: 0

Water Point ID: WP004
Habitation: West Colony
Status: Working
Usage Count: 50


Running the Project

The basic commands to run the project are:

python database.py

Then:

python app.py

Open the application in the browser:

http://127.0.0.1:5000


Future Enhancements

The following features can be added in future versions:

- User authentication and login
- Admin dashboard
- Water point location using GPS
- Map-based water point visualization
- Automatic notifications for failed water points
- Data export to CSV
- Data visualization and charts
- Mobile-friendly application
- Role-based access control
- Cloud database integration


Project Information

Project Name: Village Water Point Monitoring System

Domain: Smart Village / Water Resource Management

Technology: Python Flask and SQLite

Repository: SIH Task

