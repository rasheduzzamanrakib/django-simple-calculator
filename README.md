# Simple Django Calculator

A simple web-based calculator built with Django that performs basic arithmetic operations.

## Features

- Basic arithmetic operations: addition (+), subtraction (-), multiplication (×), division (/)
- Clear (C) and Clear Entry (CE) functions
- Keyboard support for all operations
- Responsive design with a dark theme
- Error handling for invalid expressions
- CSRF protection for security

## Setup Instructions

1. **Install Python** (if not already installed)
   - Make sure Python 3.8+ is installed on your system

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Database Migrations**
   ```bash
   python manage.py migrate
   ```

4. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```

5. **Access the Calculator**
   - Open your web browser and go to `http://127.0.0.1:8000/`

## Usage

### Mouse/Touch Controls
- Click number buttons (0-9) to input numbers
- Click operation buttons (+, -, ×, /) to perform calculations
- Click = to calculate the result
- Click C to clear the entire display
- Click CE to clear the last entry

### Keyboard Controls
- Number keys (0-9): Input numbers
- +, -, *, /: Operations
- Enter or =: Calculate result
- Escape: Clear display
- Backspace: Delete last character

## Project Structure

```
calculator_project/
├── calculator/                 # Django app
│   ├── templates/
│   │   └── calculator/
│   │       └── index.html     # Calculator interface
│   ├── views.py               # View logic
│   ├── urls.py                # App URLs
│   └── ...
├── calculator_project/        # Django project settings
│   ├── settings.py           # Project configuration
│   ├── urls.py               # Main URL configuration
│   └── ...
├── manage.py                 # Django management script
└── requirements.txt          # Python dependencies
```

## Security Features

- Input validation to prevent code injection
- CSRF token protection
- Safe evaluation of mathematical expressions
- Character whitelist for allowed operations

## API Endpoints

- `GET /` - Calculator homepage
- `POST /calculate/` - Calculate mathematical expressions

## Error Handling

The calculator handles various error conditions:
- Invalid mathematical expressions
- Division by zero
- Invalid characters in input
- Network errors

## Development

To extend this calculator:

1. **Add new operations**: Modify the `calculate` view in `calculator/views.py`
2. **Update the UI**: Edit `calculator/templates/calculator/index.html`
3. **Add new endpoints**: Update `calculator/urls.py`

## License

This project is for educational purposes.
