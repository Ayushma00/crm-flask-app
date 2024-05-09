
# Flask CRUD Application with Airtable Integration

This Flask application is a simple CRUD (Create, Read, Update, Delete) application that integrates with Airtable, a cloud-based service for managing databases.

## Features

- **Create:** Add new user data to the Airtable database.
- **Read:** Retrieve user data from the Airtable database and display it on the web interface.
- **Update:** Modify existing user data stored in the Airtable database.
- **Delete:** Remove user data from the Airtable database.

## Prerequisites

- Python 3.x
- Flask
- Requests library

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/Ayushma00/CRM.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Before running the application, make sure to set up your Airtable API key in the `config.py` file. You can obtain your API key from the Airtable account dashboard.

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Access the application in your web browser at `http://localhost:8888`.

3. You can perform CRUD operations through the web interface.

## API Endpoints

- `GET /`: Displays the home page with a list of users.
- `POST /users`: Adds a new user to the database.
- `POST /users_edit`: Updates an existing user in the database.
- `DELETE /delete/<string:rowId>`: Deletes a user from the database.

## Error Handling

- The application handles 404 errors by displaying a custom 404 page.

## Outputs

## Read the image from airtable database in the crm software
![image](https://github.com/Ayushma00/CRM/assets/34135400/2c27072a-9d41-49d3-a54c-1aa758209f48)
## Add new user
![image](https://github.com/Ayushma00/CRM/assets/34135400/838c6fb4-bb12-4ee2-b9e0-548ac95f5f31)
![image](https://github.com/Ayushma00/CRM/assets/34135400/84ad9591-78d7-4b81-9251-2e2c9129a33a)
## The result also updated in airtable database
![image](https://github.com/Ayushma00/CRM/assets/34135400/e3753db2-e031-4d18-b8c8-0d5b0a48ff4b)
## Edit and Delete the previous info
![image](https://github.com/Ayushma00/CRM/assets/34135400/73730d2e-0955-4b39-bd60-bbaf5547b3b6)
![image](https://github.com/Ayushma00/CRM/assets/34135400/2c38e8b5-0d45-48ac-ada6-f9fc6f1733d2)




