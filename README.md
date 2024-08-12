# Payment Calculator Flask App

This Flask application calculates the total gross payment for an individual based on hourly rates and hours worked, including bonuses for weekends and night shifts expressed as percentages.

## Features

- **Hourly Rate Input**: Users can input their standard hourly rate.
- **Weekday Hours**: Users input how many hours they worked during weekdays.
- **Weekend Hours and Bonus**: Users input weekend hours worked and the bonus percentage they receive.
- **Night Shift Hours and Bonus**: Users input night shift hours worked and the bonus percentage for those hours.
- **Total Gross Payment Calculation**: The app calculates the total gross payment without considering any taxes.

## Setup and Installation

To run this application, you will need Python and Flask installed on your machine.

### Prerequisites

- Python 3
- pip
- Flask

### Installing Python and Flask

If you don't have Python installed, download and install it from [python.org](https://python.org). Flask can be installed using pip:

```bash
pip install Flask

### Clone the Repository
Clone this repository to your local machine:
git clone https://github.com/your-repository/payment-calculator.git
cd payment-calculator

### Run the Application
To start the server, run:
python app.py
Navigate to http://127.0.0.1:5000/ in your web browser to view and use the application.

Usage
Input your hourly rate in the field labeled 'Hourly Rate'.
Enter the hours you worked during weekdays in the 'Hours Worked on Weekdays' field.
For weekend work, provide the hours and the bonus percentage in the respective fields.
For night shifts, do the same by entering hours worked and the bonus percentage.
Submit the form to see the calculated total gross payment displayed on a new page.
Development
This app is built using Flask, a lightweight WSGI web application framework in Python. It is designed to be easy to use and extend.

File Structure
app.py: The main Python file with Flask routes.
templates/: This folder contains the HTML templates for the app.
index.html: The main form page.
result.html: Displays the calculated payment.
static/: Contains CSS stylesheets (if any).
Contributing
Contributions to this project are welcome! Please fork the repository and open a pull request with your improvements.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.

This README provides a detailed guide on how to set up and use your Flask application, along with some additional information about contributing and licensing. You can replace the repository URL and any other specific details with your actual project's data.
