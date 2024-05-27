# Flask-Blog
It's a blog where you can post and also comment and like others posts. Enjoy :))

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Description](#description)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with this project, follow the steps below:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/flask-project.git
    cd flask-project
    ```

2. **Set up a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Flask application:**
    ```bash
    flask run
    ```

2. Open your web browser and go to `http://127.0.0.1:5000` to see the running application.

## Description

It's a simple blog app. You can create one or multiple accounts. You have the possibilitty to delete posts or comments add like posts if you want to apprecciate them. This project is with learning scope so treat it as like and I've tried to use only python and obvious HTML, NO JavaScript, despite the fact that I like working in JavaScript.

## Project Structure

Here's a brief overview of the project's structure:

flask-project/
├── app/
│ ├── init.py
│ ├── routes.py
│ └── templates/
│ └── index.html
├── venv/
├── .gitignore
├── requirements.txt
├── README.md
└── run.py

markdown
Copy code

- `app/`: Contains the application modules.
- `venv/`: Virtual environment directory.
- `.gitignore`: Specifies files and directories to be ignored by git.
- `requirements.txt`: Lists the Python dependencies.
- `README.md`: This file.
- `run.py`: The entry point for the Flask application.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
