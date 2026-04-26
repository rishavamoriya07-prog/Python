from fpdf import FPDF

# Create PDF object
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Helvetica", size=12)

# Title
pdf.set_font("Helvetica", 'B', 16)
pdf.cell(0, 10, "12-Week Programming Project Roadmap (Python or C++)", ln=True, align="C")
pdf.ln(10)

content = """
WEEKS 1–3: FOUNDATIONS (Basics & Syntax)
---------------------------------------
Week 1: Hello + Calculator
- Learn: Variables, I/O, functions
- Project: Basic Calculator

Week 2: Number Guessing Game
- Learn: Loops, conditionals, random numbers
- Project: Guess the number game

Week 3: Lists, Loops, and File Basics
- Learn: Lists/arrays, reading/writing files
- Projects: To-Do List, Temperature Converter

WEEKS 4–7: CORE PROGRAMMING (Intermediate Concepts)
----------------------------------------------------
Week 4: Data Structures and Quiz
- Learn: Dictionaries/maps, functions
- Project: Basic Quiz App

Week 5: File Manipulation
- Learn: File I/O, string processing
- Project: File Analyzer

Week 6: Classes and Objects
- Learn: Classes, objects, encapsulation
- Project: Bank Account Simulator

Week 7: CRUD Operations and Persistence
- Learn: File handling, JSON/CSV parsing
- Projects: Contact Book, Rock–Paper–Scissors

WEEKS 8–10: APPLIED PROJECTS (Problem-Solving)
----------------------------------------------
Week 8: Expense Tracker
- Learn: Modular programming, reporting
- Project: Expense Tracker

Week 9: Chatbot
- Learn: String matching, branching logic
- Project: Text Chatbot

Week 10: Games
- Learn: 2D arrays/lists, game loops
- Project: Tic-Tac-Toe

WEEKS 11–12: ADVANCED / REAL-WORLD PROJECTS
-------------------------------------------
Week 11: APIs and Networking
- Learn: HTTP requests, JSON parsing
- Project: Weather App

Week 12: Security & Data
- Learn: Encryption, web scraping, data visualization
- Projects: Password Manager, Mini Web Scraper / Dashboard

RESOURCES
---------
Python:
- Automate the Boring Stuff with Python
- Python Crash Course (Eric Matthes)

C++:
- Programming: Principles and Practice Using C++ (Bjarne Stroustrup)
- The Cherno C++ YouTube Series

After Week 12:
- 15 complete projects
- Strong understanding of syntax, OOP, APIs, and data handling
- Ready for open source or freelance projects
"""

pdf.set_font("Helvetica", size=12)
pdf.multi_cell(0, 8, content)

# Save the PDF
pdf.output("12_Week_Programming_Project_Roadmap.pdf")
print("PDF saved as 12_Week_Programming_Project_Roadmap.pdf")

