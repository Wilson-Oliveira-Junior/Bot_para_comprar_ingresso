# Ticket Purchasing Bot

This project automates the process of purchasing tickets from a website using Selenium.

## Project Structure

```
ticket-purchasing-bot
├── src
│   ├── main.py
│   ├── bot
│   │   ├── __init__.py
│   │   ├── ticket_purchaser.py
│   └── utils
│       ├── __init__.py
│       └── helpers.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ticket-purchasing-bot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Ensure you have the appropriate WebDriver installed for your browser (e.g., ChromeDriver for Google Chrome).

## Usage Guidelines

1. Open `src/main.py` to configure your ticket purchasing preferences.
2. Run the script:
   ```
   python src/main.py
   ```

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.