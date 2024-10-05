
# SET09103 Project

This repository contains the project files for the SET09103 coursework.

## Requirements

To run this project, you'll need the following:

- Python 3.6 or later
- Flask
- Virtual environment (`venv`)
- Git

## Setting Up the Development Environment

Follow these steps to set up the development environment locally:

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/iambariz/SET09103.git
cd SET09103
```

### 2. Set Up the Virtual Environment

Before running the project, it's recommended to use a virtual environment to isolate dependencies.

#### Install python3-venv (if not already installed):
On Ubuntu/Debian systems:

```bash
sudo apt install python3-venv
```

### 3. Create and Activate the Virtual Environment

Create the virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

Once the virtual environment is active, install the required dependencies from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

If `requirements.txt` doesn't exist yet, you can manually install Flask and other dependencies:

```bash
pip install Flask
```

### 5. Run the Flask Application

To start the Flask development server:

```bash
python run.py
```

The app will be accessible at `http://127.0.0.1:5000/` in your browser.