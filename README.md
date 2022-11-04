# Twikker
Social network built with Django and Vue.js

Work in progress.

✅ Likes and Dislikes  <br>
✅ Feed  <br>
✅ DM <br>
✅ Profile <br>
✅ Global Chat <br>
✅ Real Time Chat <br> 
✅ Real Time Notifications <br>
⏳ Real Time Feed (Likes and dislikes count) (Will be implemented with Server Sent Events or Websockets) <br>
⏳ I may change some websockets to server sent events, only chat will remain with web sockets

<h2> Setup </h2>

- clone the repository  `git clone https://github.com/vapdev/Twikker.git`
- cd into directory `cd  Twikker`
- create virtual env `python -m venv venv`
- activate virtual env `venv\Scripts\activate`
- install requirements `pip install -r requirements.txt`
- run db migrations `python manage.py migrate`
- start the server `python manage.py runserver`
- access at `localhost:8000`

OLD VERSION PRINTS

![image](https://user-images.githubusercontent.com/88452580/195798844-3de23718-9bf0-4f2e-893f-50445d71bd4e.png)

NEW VERSION

![image](https://user-images.githubusercontent.com/88452580/198595978-fc31da70-b5ad-44cc-816c-9be0ce32d440.png)
