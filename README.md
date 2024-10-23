# DialogueDock

## Description

**This project is an introduction to Django Channels, focusing on building real-time web applications like chat systems. It covers the use of WSGI and ASGI interfaces, enabling the creation of both synchronous and asynchronous consumers for real-time data handling. The project explores integrating Channels with Django views, facilitating real-time event transmission, and managing targeted messaging for users and groups. Additionally, it addresses consumer scope and session management through the ASGI interface, including accessing user data, and demonstrates how to use JavaScript for client-side real-time connections.**

## Features

- Realtime Chats
- Messages stored in database


### Technologies Used

| HTML | CSS | Python | Django | SQLite |
|------|-----|--------|--------|--------|
| <img src="https://upload.wikimedia.org/wikipedia/commons/6/61/HTML5_logo_and_wordmark.svg" width="50"> | <img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/CSS3_logo_and_wordmark.svg" width="50"> | <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="50"> | <img src="https://upload.wikimedia.org/wikipedia/commons/7/75/Django_logo.svg" width="50"> | <img src="https://upload.wikimedia.org/wikipedia/commons/3/38/SQLite370.svg" width="50"> |



## Setup Locally
- **First clone repo locally**  
  **Run below command in terminal**  
  `git clone https://github.com/Mehmood007/dialoguedock.git`  

-  **ADD SECRET_KEY TO ENV**  
  Rename `.sample-env` to `env` and Assign value to `SECRET_KEY`  

- **Install Dependencies**  
  First make sure virtual environment is activated  
  `pip install -r requirements.txt`

- **Run Migrations in app directory**   
  `python manage.py migrate`

- **Run Server**  
  `python manage.py runserver`