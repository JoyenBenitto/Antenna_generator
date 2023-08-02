# Contributing Guidelines

Thank you for considering contributing to our project! We welcome all contributions, big or small. Before you start, please take a moment to review the following guidelines.


## Code of Conduct
Please note that we have a Code of Conduct in place to ensure a respectful and inclusive community. By participating, you are expected to uphold this code. If you encounter any unacceptable behavior, please report it to maintainer-email@example.com.
Getting Started

Fork the repository and clone it to your local machine. Make sure you have Python 3.x installed on your system.Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Development Workflow

Create a new branch for your work:

```bash
git checkout -b feature/your-feature-name
```

## Install development dependencies:

```bash
pip install -r ant_gen/requirements.txt
```

Make your changes and ensure they follow our coding style (PEP 8).

Pull Requests
Before submitting a pull request, rebase your branch on the latest main/trunk:

```bash
git pull --rebase origin main
```

Push your changes to your fork:
```bash
git push origin feature/your-feature-name
```

Open a pull request to the main repository. Be descriptive about your changes and reference any related issues or pull requests.
Your pull request will be reviewed by maintainers, and feedback will be provided if needed. Please be patient as the review process may take some time.

## Code Style

We follow the PEP 8 style guide for Python code. Please ensure your contributions adhere to this standard.

## Documentation
All code contributions should be well-documented. Add/update docstrings and comments where appropriate.

##Issue Tracker
Feel free to open an issue if you encounter a bug, have a feature request, or want to suggest improvements. We'll do our best to respond and address the issues in a timely manner.

## License 
By contributing to this project, you agree that your contributions will be licensed under the project's LICENSE.

Thank you for your contributions! Together, we can make this project even better. 
