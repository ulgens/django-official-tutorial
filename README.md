# django-official-tutorial

> [!IMPORTANT]
> **This repository is archived and no longer maintained.**
>
> It was created as a personal practice and a potential project starter for the official Django tutorial. Considering Django tutorial doesn't change much and I don't use Django as much as I used to, I decided to archive the repository.
>
> If you decide to fork and make use of the repo, make sure to update all your dependencies first.

The famous **polls app** from the official Django tutorial.

The tutorial is available [here](https://docs.djangoproject.com/en/5.1/intro/tutorial01/). The code in this repository reflects the state of the tutorial as of **November 23, 2024**.

> [!Warning]
> The project uses the current latest Django version (6.1.1), but I didn't review the latest state of the docs line by line. Beware of any inconsistencies.

This repository serves as a **project starter** for those who need a quick Django setup with a simple app. To enhance its utility, some additional tooling has been included:

- **uv** for dependency management
- [**prek**](https://github.com/j178/prek?tab=readme-ov-file#installation) for running & managing git hooks, incorporating:
  - [pre-commit-hooks](https://prek.j178.dev/builtin/)
  - [pyproject-fmt](https://github.com/tox-dev/pyproject-fmt)
  - [uv-pre-commit](https://github.com/astral-sh/uv-pre-commit)
  - [ruff](https://github.com/astral-sh/ruff-pre-commit)
  - [django-upgrade](https://github.com/adamchainz/django-upgrade)
  - [yamlfmt](https://github.com/google/yamlfmt)
  - [check-jsonschema](https://github.com/python-jsonschema/check-jsonschema)
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
