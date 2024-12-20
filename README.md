# Flask and HTMX Web Application Boilerplate

This repository provides a boilerplate setup for building a web application using Flask and HTMX, following the MVC (Model-View-Controller) design method.

---

## Features

- **Flask Framework**: Lightweight backend development.
- **HTMX Integration**: Add dynamic behavior with minimal JavaScript.
- **MVC Design**: Clear separation of Models, Views, and Controllers for scalable development.

---

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/aidngonz/flaskhtmx-boilerplate.git
   ```
   
2. Rename the folder:
   ```bash
   mv flaskhtmx-boilerplate new_name
   cd new_name
   ```

4. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

5. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

6. Run the application:
   ```bash
   python app.py
   ```

7. Open your browser and navigate to `http://127.0.0.1:5000/`.

---

## Directory Structure

```
├── README.md           # Documentation
├── app.py              # Main entry point
├── controllers
│   └── test.py         # Example controller
├── models
│   └── counter.py      # Example model
└── templates
    ├── counter.html    # Example template
    └── index.html      # Homepage template
```

---

## License

This project is licensed under the MIT License.
