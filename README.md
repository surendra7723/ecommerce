# Ecommerce Project

This is a Django-based ecommerce backend project.

## Features
- Product management
- Customer management
- Order processing
- Likes and tags system
- Modular app structure (core, store, likes, tags, playground)

## Project Structure
- `core/` – Core business logic and models
- `store/` – Storefront, products, and related features
- `likes/` – Likes functionality
- `tags/` – Tagging system
- `playground/` – Experimental and demo code
- `storefront/` – Django project settings and configuration

## Getting Started

### Prerequisites
- Python 3.12+
- pip
- (Recommended) Virtual environment

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/surendra7723/ecommerce.git
   cd ecommerce
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv new_env
   source new_env/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Running Tests
```bash
pytest
```

## License
This project is licensed under the MIT License.
