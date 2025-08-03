# GitHub Repository Setup Instructions

## Prerequisites
1. Install Git on your system if not already installed
2. Create a GitHub account if you don't have one
3. Configure Git with your credentials:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

## Step-by-Step Instructions

### 1. Create a new repository on GitHub
1. Go to [GitHub.com](https://github.com)
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Fill in the details:
   - **Repository name**: `django-simple-calculator`
   - **Description**: `A modern web-based calculator built with Django`
   - **Visibility**: Public (or Private if you prefer)
   - **Do NOT** initialize with README, .gitignore, or license (we already have these)
5. Click "Create repository"

### 2. Push your project to GitHub

Run these commands in your project directory (`d:\coding\django`):

```bash
# Initialize Git repository (if not already done)
git init

# Configure Git (replace with your details)
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Add all files to staging
git add .

# Create initial commit
git commit -m "Initial commit: Django Simple Calculator with modern UI"

# Add remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/django-simple-calculator.git

# Push to GitHub
git push -u origin main
```

### 3. Alternative: Using GitHub Desktop
If you prefer a GUI:
1. Download and install [GitHub Desktop](https://desktop.github.com/)
2. Open GitHub Desktop
3. Click "Add an Existing Repository from your Hard Drive"
4. Select your project folder: `d:\coding\django`
5. Publish to GitHub

### 4. Verify Upload
After pushing, you should see your project at:
`https://github.com/YOUR_USERNAME/django-simple-calculator`

## Project Structure on GitHub
```
django-simple-calculator/
├── .gitignore                 # Git ignore rules
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
├── manage.py                  # Django management script
├── calculator_project/        # Main Django project
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── calculator/                # Calculator app
    ├── templates/
    ├── views.py
    └── ...
```

## Next Steps
1. Add a screenshot of your calculator to make the README more attractive
2. Consider adding a demo link if you deploy it online
3. Add more features and create new branches for development
4. Set up GitHub Actions for CI/CD if needed

## Troubleshooting
- If you get authentication errors, set up a Personal Access Token
- Make sure your repository name matches exactly
- Check that Git is properly installed and configured
