# Flask Calculator Project

A simple full-stack calculator web application built using **Python Flask**, **HTML**, **CSS**, and **JavaScript**.  
This project demonstrates **Object-Oriented Programming (OOP)** and **frontend–backend communication**.

---

## 📸 Calculator UI

![image alt](https://github.com/reiidon/calculator-flask-project/blob/a6b318fa6b700e95150dc34a184a63788e69dcb0/Screenshot%202026-02-02%20172941.png)

---

## 🧾 Project Description

This is a basic calculator web app where:
- Users click buttons to build a mathematical expression
- The expression is sent to the backend using an API
- Python (Flask) evaluates the expression
- The result is sent back and displayed on the screen

---

## 🛠 Technologies Used

- Python  
- Flask  
- HTML  
- CSS  
- JavaScript  

---

## ✨ Features

- Addition, Subtraction, Multiplication, Division
- Button-based calculator UI
- Backspace and Clear (AC)
- Answer reuse (Ans)
- Responsive design (works on mobile & desktop)
- Backend calculation using Flask API

---

## 🧠 OOP Concept Used

A `Calculator` class is used in Python to handle calculations.

```python
class Calculator:
    def calculate(self, expression):
        return eval(expression)
