# django-official-tutorial

The famous **polls app** from the official Django tutorial.

The tutorial is available [here](https://docs.djangoproject.com/en/5.1/intro/tutorial01/). The code in this repository reflects the state of the tutorial as of **November 23, 2024**.

This repository serves as a **project starter** for those who need a quick Django setup with a simple app. To enhance its utility, some additional tooling has been included:

- **uv** for dependency management
- [**prek**](https://github.com/j178/prek?tab=readme-ov-file#installation) for running & managing git hooks, incorporating:
  - [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)
  - [pyproject-fmt](https://github.com/tox-dev/pyproject-fmt)
  - [uv-pre-commit](https://github.com/astral-sh/uv-pre-commit)
  - [ruff](https://github.com/astral-sh/ruff-pre-commit)
  - [django-upgrade](https://github.com/adamchainz/django-upgrade)
  - [yamlfmt](https://github.com/google/yamlfmt)
  - [codespell](https://github.com/codespell-project/codespell)
- **GitHub Actions** for prek and test pipelines
- **Renovate** for automated dependency updates

The resulting Django project has some changes from the original tutorial:

- Uses `src/` as the source folder name
- Uses `core/` for the core configuration folder
- Removes default docstrings from initial files
- Adds `# noqa` comments where it's needed

## Installation

1. Clone the repository
2. Set up the virtual environment using uv:
    ```bash
    uv venv
    source .venv/bin/activate
    uv sync
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
