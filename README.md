# Bankruptcy Risk Prediction with Machine Learning

This repository contains a Machine Learning-based model for predicting corporate bankruptcy risk. The project analyzes financial indicators and other relevant features to build a predictive model that can serve as an early warning system for financial distress.

## Features
- Data preprocessing and feature engineering.
- Machine Learning model training and evaluation.
- Performance metrics to assess model accuracy and interpretability.
- Easy setup and dependency management with `uv`.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/yourrepo.git
   cd BankruptcyML
   ```

2. **Install dependencies using `uv` (recommended):**
   ```bash
   uv venv  # Create a virtual environment
   uv pip install -r requirements.txt  # Install dependencies
   ```
   If you don’t have `uv` installed, you can install it via:
   ```bash
   pip install uv
   ```

3. **Activate the virtual environment:**
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows:
     ```powershell
     .venv\Scripts\activate
     ```

## Usage

Once the environment is set up, navigate to the `ml-web-app/src` directory and run the application:
```bash
cd ml-web-app/src
python app.py
```

The application will start a Flask development server, typically running at `http://127.0.0.1:5000/`. Open your browser and navigate to this URL to access the web interface.

## Contributing
Feel free to open issues or submit pull requests to improve the project!

## License
This project is licensed under the MIT License.
