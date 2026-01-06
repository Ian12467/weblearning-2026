# Week 1: The Foundation (HTML, CSS, Git, & Python Refresher)

**Goal:** Establish the core web stack fundamentals and refresh Python logic logic to prepare for Django.

## 📋 Prerequisites
Before starting the week, ensure you have completed the following:
- [ ] Register for **CS50W** (CS50's Web Programming with Python and JavaScript).
- [ ] Ensure **VS Code** is installed and ready.

---

## 📅 Weekly Schedule

### **Monday: The Setup & HTML/CSS**
**Focus:** Getting started with the basics of structure and styling.

**Action Items (2-3 Hours):**
1.  **Lecture:** Watch **Lecture 0: HTML, CSS** (Start to `1:00:00`).
2.  **Setup:** Create a folder named `project0`.
3.  **Code:** Build a simple `.html` page about yourself.
    * *Requirement:* Must use headings (`<h1>`), lists (`<ul>` or `<ol>`), and an image (`<img>`).

### **Tuesday: Advanced CSS (Sass/Bootstrap)**
**Focus:** Responsive design and using libraries to speed up development.



**Action Items (2-3 Hours):**
1.  **Lecture:** Finish **Lecture 0** (`1:00:00` to End).
2.  **Tutorial:** Watch a 30-minute tutorial on **Bootstrap 5**.
    * *Note:* This is crucial for making UI look good quickly.
    * *Resource:* Bookmark the [Bootstrap 5 Components Documentation](https://getbootstrap.com/docs/5.0/components/accordion/).
3.  **Code:** Style your "About Me" page using Bootstrap classes.
    * *Requirement:* Add a Navbar and use the Grid system.

### **Wednesday: Git & GitHub**
**Focus:** Version control (Crucial for job readiness).

**Action Items (2-3 Hours):**
1.  **Lecture:** Watch **Lecture 1: Git** (Start to `0:45:00`).
2.  **Account:** Create a [GitHub](https://github.com/) account (if you don't have one).
3.  **Workflow:** Initialize a repo for `project0`, commit your code, and push it to GitHub.
    * *Goal:* See your green "contribution square" on your profile.



### **Thursday: Python Refresher (Logic)**
**Focus:** Python syntax and Object-Oriented Programming (OOP).

**Action Items (2-3 Hours):**
1.  **No Lecture:** Do not watch a lecture today. Focus purely on coding.
2.  **Code:** Open VS Code and write 3 Python scripts:
    * **Script A:** Takes a `name` as input and prints "Hello".
    * **Script B:** Loops through a list of numbers and prints *only* the even ones.
    * **Script C:** Defines a class called `Car` with a method `drive()`.
3.  **Important:** You *must* be comfortable with Python Classes before Django starts next week.

### **Friday: Project 0 - Search (Start)**
**Focus:** Translating specifications into code.

**Action Items (2-3 Hours):**
1.  **Read:** Read the full specification for **Project 0: Search**.
2.  **Setup:** Create the file structure:
    * `index.html` (Google Search)
    * `image.html` (Google Image Search)
    * `advanced.html` (Google Advanced Search)
3.  **Code:** Build the HTML structure (skeleton) for the Google Search clone.

### **Saturday: Project 0 - Search (Finish)**
**Focus:** CSS detailing and query parameters.

**Action Items (2-3 Hours):**
1.  **Style:** Focus heavily on CSS. Try to make it look *exactly* like Google.
2.  **Functionality:** Implement the query parameters.
    * *Goal:* When you click "Search," it should actually redirect to a real Google search result.
3.  **Submit:** Submit the project. Even if it isn't perfect, submit it to get the dopamine hit of completion.

### **Sunday: Rest & Review**
**Focus:** Recovery and priming.

**Action Items:**
1.  **No Coding:** Take a break from the screen.
2.  **Read:** Read one article about the "Django Framework" just to prime your brain for Week 2.

# Week 2: The Engine (Django & Project "Wiki")

**Theme:** Week 1 was about "making things look good" (HTML/CSS). Week 2 is about "making things work" (Logic/Python).

You are entering the world of **Back-End Development** using Django. This is the engine that will eventually power your AI tools.

## 📋 Prerequisites
- [ ] Ensure **Python** is installed.
- [ ] Ensure you are comfortable opening the **Terminal** in VS Code.

---

## 📅 Weekly Schedule

### **Monday: The Big Lecture (Django)**
**Focus:** Understanding how the web actually works (HTTP).

**Action Items (2-3 Hours):**
1.  **Lecture:** Watch **Lecture 3: Django** (Start to `1:15:00`).
2.  **Concept Check:** Do not just watch passively. You must understand what a "Request" and "Response" are.
    * *The Browser requests, the Server responds.*
3.  **Stop Point:** Stop when he starts talking about "Databases/Models". We will focus on Routes and Views first.



### **Tuesday: Hello World (The Setup)**
**Focus:** Configuration. This is often the most frustrating day for beginners—push through it.

**Action Items (2-3 Hours):**
1.  **The Hardest Part:** Set up your virtual environment. Run these commands in your terminal one by one:
    ```bash
    # Create the environment
    python -m venv venv
    
    # Activate it (Windows) -> .\venv\Scripts\activate
    # Activate it (Mac/Linux) -> source venv/bin/activate

    # Install Django
    pip install django
    ```
2.  **Project Setup:** Create your first project.
    ```bash
    django-admin startproject myproject
    ```
3.  **App Setup:** Create your first app inside the project.
    ```bash
    python manage.py startapp hello
    ```
4.  **Launch:** Make the server run.
    ```bash
    python manage.py runserver
    ```
    * *Win Condition:* If you see the "Rocket Ship" in your browser at `http://127.0.0.1:8000/`, you win.



### **Wednesday: Routes & Templates**
**Focus:** Template Inheritance (The DRY Principle).

**Action Items (2-3 Hours):**
1.  **Lecture:** Finish the **Lecture 3** video.
2.  **Practice:** Create a `layout.html` that contains your Navbar and Footer.
3.  **Refactor:** Make all other HTML pages "extend" this layout.
    * *Why:* This prevents you from copying the navbar code into every single HTML file.
    * *Key Concept:* `{% block body %}`



### **Thursday: Project 1 - Wiki (The Setup)**
**Focus:** Reading other people's code.

**Action Items (2-3 Hours):**
1.  **Download:** Download the distribution code for **Project 1: Wiki**.
2.  **Read:** Read the `util.py` file included in the folder.
    * *Warning:* Do not ignore this file. It has functions pre-written for you to save and get entries. You will need them.
3.  **Task:** Make the "Home Page" list all current encyclopedia entries (CSS, Django, Git, etc.).
    * *Hint:* You need to call `util.list_entries()` in your `views.py` and pass that data to your HTML template.

### **Friday: Wiki - The "Entry" Page**
**Focus:** Dynamic URL Routing.

**Action Items (2-3 Hours):**
1.  **The Logic:** When a user goes to `/wiki/CSS`, your app needs to:
    * Grab the content for "CSS" using the util function.
    * Convert it from Markdown to HTML (You will need the `markdown2` library).
    * Send it to the user.
2.  **Task:** Implement the function that converts Markdown to HTML and displays it on a page.

### **Saturday: Wiki - Search & Create**
**Focus:** Form handling and logic branching.

**Action Items (2-3 Hours):**
1.  **Search:** Build the search bar.
    * *Logic Branch 1:* If the query matches an entry exactly, redirect to that page.
    * *Logic Branch 2:* If it is a partial match (e.g., user types "Py"), show a list of results (e.g., "Python").
2.  **Create New Page:** Build a form where a user can type a Title and Content.
    * *Save:* Use `util.save_entry()` to save the data to disk.

### **Sunday: Wiki - Edit & Random**
**Focus:** Pre-populating forms and Python libraries.

**Action Items (2-3 Hours):**
1.  **Edit:** This is tricky. You must load an existing page's content into a form `textarea` so the user can edit what is already there.
2.  **Random Page:** Use Python’s `random` library to pick a random entry from the list and redirect the user there.
3.  **Submit:** Record your screencast (required for CS50) and submit your project!

## ⚠️ 3 Common "Stuck Points" in Week 2
**(Read this before you panic)**

### 1. Error: `ModuleNotFoundError: No module named 'django'`
* **The Cause:** You installed Django, but your VS Code terminal is not looking inside the virtual environment.
* **The Fix:** Look at your terminal line. If you don't see `(venv)` at the very start, you aren't "logged in" to your environment.



**Run this command to fix it:**
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
