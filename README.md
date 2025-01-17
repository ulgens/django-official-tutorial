# django-official-tutorial

The famous **polls app** from the official Django tutorial.

The tutorial is available [here](https://docs.djangoproject.com/en/5.1/intro/tutorial01/). The code in this repository reflects the state of the tutorial as of **November 23, 2024**.

This repository serves as a **project starter** for those who need a quick Django setup with a simple app. To enhance its utility, some additional tooling has been included:

- **Poetry** for dependency management
- **pre-commit** for code quality, incorporating:
  - `pre-commit-hooks`
  - `ruff`
  - `django-upgrade`
  - `codespell`
- **GitHub Actions** for pre-commit and test pipelines
- **Dependabot** for automated dependency updates

The resulting Django project has some changes from the original tutorial:

- Uses `src/` as the source folder name
- Uses `core/` for the core configuration folder
- Removes default docstrings from initial files
- Adds `# noqa` comments where it's needed

## Installation

1. Clone the repository
2. Set up the virtual environment using Poetry:
    ```bash
    poetry install
    poetry env activate
    ```
3. Apply database migrations:
    ```bash
    python manage.py migrate
    ```
4. Create a superuser account:
    ```bash
    python manage.py createsuperuser
    ```
5. Start the development server:
    ```bash
    python manage.py runserver
    ```
