<p align="right"><a href="README.md">TR</a> | <b>EN</b></p>

<p align="center">
  <img src="static/images/og-image.png" width="680" alt="umutkilictas.tr — Django Personal Portfolio"/>
</p>

# 🌐 Umut Kılıçtaş — Django Personal Portfolio

<p>
  <a href="https://umutkilictas.tr"><img src="https://img.shields.io/badge/Live_Site-umutkilictas.tr-2563eb?style=flat-square&logo=googlechrome&logoColor=white" alt="Live Site"/></a>
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Django-5.2_LTS-092E20?style=flat-square&logo=django&logoColor=white" alt="Django"/>
  <img src="https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=flat-square&logo=bootstrap&logoColor=white" alt="Bootstrap"/>
  <img src="https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License"/>
</p>

Dynamic personal portfolio web application built with **Django 5.2 LTS** and **Bootstrap 5**, featuring admin-managed content, light/dark theme support, a comprehensive unit test suite, and automated **GitHub Actions CI/CD** deployment to [umutkilictas.tr](https://umutkilictas.tr).

---

## ✨ Key Features

- **Dynamic Content Management (Django Admin):** Projects, work/internship experiences, education history, and certificates are managed and reordered directly via Django Admin (`display_order`, `is_published`, `featured`).
- **Light & Dark Theme:** Instant theme switching persisted in `localStorage` and synchronized with OS `prefers-color-scheme`.
- **Centralized Context Processor:** Owner metadata and social links are injected globally across templates via `portfolio.context_processors.portfolio_context`.
- **Custom Data Seeding Command:** Includes `python manage.py load_initial_data` to populate initial projects, experience, education, and certificates with a single command.
- **Automated Test Suite (`portfolio/tests.py`):** **10 unit tests** covering views, slug routing, `404` enforcement on unpublished items, featured project limits, and model helper methods.
- **CI/CD Pipeline (`.github/workflows/deploy.yml`):** Every push to `main` runs `manage.py check` and the unit test suite in GitHub Actions before running `collectstatic` and deploying to the live production server.
- **Production Hardening:** Automatically enables `HSTS`, `SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`, and `NOSNIFF` headers when `DEBUG=False`.

---

## 🏗️ Data Models

```mermaid
erDiagram
    PROJECT {
        string title
        slug slug
        string short_description
        text description
        string technologies
        url github_url
        url live_demo_url
        boolean featured
        boolean is_published
        int display_order
    }
    EXPERIENCE {
        string title
        string organization
        string location
        string date_text
        text description
        date start_date
        date end_date
        boolean is_current
        int display_order
    }
    EDUCATION {
        string institution
        string faculty
        string degree
        string gpa
        string date_text
        int display_order
    }
    CERTIFICATE {
        string name
        string issuer
        string certificate_no
        date issue_date
        file certificate_file
        boolean is_published
        int display_order
    }
```

---

## 📁 Project Structure

```text
django-portfolio/
├── .github/workflows/
│   └── deploy.yml                           # CI (Django check & test) + CD (collectstatic & FTP deploy)
├── config/
│   ├── settings.py                          # Environment-driven configuration & production security
│   ├── urls.py                              # Root URL routing & custom 404 handler
│   └── wsgi.py / asgi.py
├── portfolio/
│   ├── management/commands/
│   │   └── load_initial_data.py             # Custom management command to seed portfolio data
│   ├── migrations/
│   ├── admin.py                             # Customized ModelAdmin configurations
│   ├── context_processors.py                # Global template context variables
│   ├── models.py                            # Project, Experience, Education, Certificate models
│   ├── tests.py                             # 10 unit tests covering views & models
│   ├── urls.py                              # App URL patterns
│   └── views.py                             # Views (Home, About, Projects, Experience, Certificates, Contact)
├── static/                                  # Custom CSS, theme toggle JS, and SVG/PNG assets
├── templates/                               # Semantic HTML5 & Bootstrap 5 templates
├── .env.example
├── manage.py
├── requirements.txt
├── LICENSE
├── README.md                                # Turkish documentation (default)
└── README.en.md                             # English documentation
```

---

## ⚙️ Local Setup & Usage

```bash
# 1. Clone the repository
git clone https://github.com/umutkilictas/django-portfolio.git
cd django-portfolio

# 2. Create and activate a virtual environment
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# Linux / macOS:
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env

# 5. Run migrations and seed initial data
python manage.py migrate
python manage.py load_initial_data

# 6. Start the development server
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

---

## 🧪 Running Tests

```bash
python manage.py check
python manage.py test
```

---

## 📄 License

Licensed under the [MIT License](LICENSE).
