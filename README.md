# 🛠️ Moduler & Packager – Multi-Utility Toolkit

A simple, menu-driven Python application that brings multiple useful utilities together in one place. This project demonstrates Python's built-in modules, custom modules, packages, file handling, and modular programming through practical, real-world examples.

## 📌 Project Overview

**Moduler & Packager** is a Python-based Multi-Utility Toolkit developed as a practical learning project for understanding Python modules and packages. It combines date and time operations, mathematical calculations, random data generation, unique identifier creation, and file management in a single console application.

The project follows a modular structure, keeping different functionalities in separate Python files to make the code easier to understand, maintain, and reuse.

## ✨ Features

### 🕒 1. Date and Time Operations
- Display the current date and time.
- Calculate the difference between two dates.
- Format dates using the `strftime()` function.
- Run a stopwatch and countdown timer.

### 🧮 2. Mathematical Operations
- Calculate the factorial of a number.
- Calculate compound interest.
- Perform trigonometric calculations.
- Calculate the area of geometric shapes.
- Use Python's `math` module for mathematical functions.

### 🎲 3. Random Data Generation
- Generate random numbers and lists.
- Create random passwords.
- Generate One-Time Passwords (OTPs).
- Simulate simple random games and sampling operations.

### 🔑 4. Unique Identifier Generation
- Generate unique identifiers using Python's `uuid` module.
- Create UUIDs for records, files, and sessions.

### 📁 5. File Operations
- Create new text files.
- Write content to files.
- Read existing file contents.
- Append additional data to files.

### 🔍 6. Dynamic Module Exploration
- Explore available attributes of built-in or custom modules using `dir()`.
- Understand how Python modules expose functions, variables, and other attributes.

## 🧰 Technologies Used

- **Programming Language:** Python 3
- **Built-in Modules:** `datetime`, `time`, `math`, `random`, `uuid`
- **File Handling:** Python file operations
- **Concepts:** Custom modules, packages, `__init__.py`, `__name__ == "__main__"`, and modular programming

No external libraries are required for the core features.

## 📂 Project Structure

The project can be organized into the following modular structure:

```text
Moduler-and-Packager/
│
├── main.py
├── utility_operations.py
├── file_operations.py
│
├── utilities/
│   ├── __init__.py
│   └── math_operations.py
│
├── files/
│   └── __init__.py
│
└── README.md
```

*Note: Adjust the filenames and folders to match your actual project files.*

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or later
- A code editor such as VS Code or PyCharm

### Installation

**1. Clone the repository**

```bash
git clone <your-repository-url>
```

**2. Open the project folder**

```bash
cd Moduler-and-Packager
```

**3. Run the application**

```bash
python main.py
```

Follow the on-screen menu to select an operation. Enter your choice, provide the requested inputs, and return to the main menu to explore other utilities. Select **Exit** to close the application.

## 💻 Main Menu

The application provides a simple console-based interface with options such as:

1. Date and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations
6. Explore Module Attributes (`dir()`)
7. Exit

## 🎯 Learning Objectives

This project demonstrates how to organize Python code into reusable modules, group related functionality into packages, work with standard libraries, handle files, and execute scripts using the `__name__ == "__main__"` convention.

## 🔮 Future Enhancements

- Add a graphical user interface (GUI).
- Improve input validation and error handling.
- Add more mathematical and date-related utilities.
- Introduce automated unit tests.
- Add logging and configuration options.

## 👨‍💻 Author

Developed as a **Python – Data Science practical project** to explore modular programming and Python's built-in capabilities.

---

⭐ If you find this project useful for learning Python, feel free to explore the code and build upon it.

**Made with Python 🐍**
