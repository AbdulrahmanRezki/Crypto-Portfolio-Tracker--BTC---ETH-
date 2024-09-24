Crypto Portfolio Calculator

A Flask-based web application that allows users to calculate the value of their cryptocurrency portfolio. The app fetches the current Bitcoin and Ethereum prices from the CoinGecko API and multiplies them by the user-provided cryptocurrency amounts to display the total value.

Features
Real-time price fetch: The app fetches live Bitcoin and Ethereum prices from the CoinGecko API.
User-friendly interface: The simple, clean UI allows users to input the amounts of Bitcoin and Ethereum they own.
Instant calculation: The total value of the user's portfolio is calculated and displayed upon submission of the form.

Project Structure:
Crypto Portfolio Calculator/
│
├── templates/
│   └── index.html      # HTML file for the UI
│
├── main.py             # Python file containing Flask routes and logic
├── README.md           # This file
└── requirements.txt    # List of dependencies for the project

Installation
Clone the repository:
git clone https://github.com/yourusername/crypto-portfolio-calculator.git

Navigate into the project directory:
cd crypto-portfolio-calculator

Create a virtual environment and activate it:
python3 -m venv venv
source venv/bin/activate

Install the required dependencies:
pip install -r requirements.txt

Set up your CoinGecko API key (replace API KEY INSERT HERE in main.py with your API key).

Usage
Run the Flask app:

python main.py

Open your web browser and navigate to:
http://127.0.0.1:5000/

Enter the amount of Bitcoin and Ethereum you own and click "Calculate Portfolio Value" to see the total value of your portfolio.

Dependencies
Flask
Requests
To install all dependencies, simply run:
pip install -r requirements.txt

License
This project is licensed under the MIT License - see the LICENSE file for details.
