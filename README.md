# Reddit Bot

A Python bot to search and display Reddit posts by keyword, with a modern web interface using Streamlit.

## 🚀 Features

- Searches Reddit posts by keyword, with options for result limit, sorting, and time filter.
- Organized code with a clear separation between configuration, main logic, and utilities.
- Interactive web interface built with Streamlit: easy to use, no programming required.
- Ready for free deployment on [Streamlit Community Cloud](https://streamlit.io/cloud).
- Environment management with `venv` and dependencies in `requirements.txt`.
- Structure prepared for expansion: easy to add cache, logging, database, or REST API.

## 🛠️ Technologies

- Python 3.12+
- Streamlit
- Requests
- python-dotenv
- pytest
- WSL (for Linux development on Windows)

## 📦 Installation

1. Clone the repository:
git clone https://github.com/yourusername/reddit-bot.git
cd reddit-bot

2. Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

3. Install the dependencies:
pip install -r requirements.txt

## 🚦 Usage

Run the Streamlit app:
streamlit run app.py

Enter the search term, choose the number of posts, and view the results in your browser.

## 🧩 Project Structure

reddit-bot/
├── config.py
├── reddit_searcher.py
├── utils.py
├── app.py
├── requirements.txt
└── README.md

### ⚠️ Important Note on Deployment and Usage ⚠️

Currently, this application is primarily designed for **local execution**. While the project is deployed on Streamlit Community Cloud, you might encounter issues when performing searches directly from the cloud deployment.
