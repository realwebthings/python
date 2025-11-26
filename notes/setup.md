# Python Environment Setup

## Virtual Environment Setup
Date: $(date +%Y-%m-%d)

### Steps Completed:
1. Created virtual environment: `python3 -m venv venv`
2. Activated virtual environment: `source venv/bin/activate`

### Commands Reference:
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment (macOS/Linux)
source venv/bin/activate

# Deactivate virtual environment
deactivate

# Check Python version
python --version

# Install packages
pip install package_name

# List installed packages
pip list

# Create requirements file
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt
```

### Notes:
- Always activate the virtual environment before working on Python projects
- Use `pip freeze > requirements.txt` to save dependencies
- The `venv/` directory should be added to `.gitignore`