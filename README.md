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

WITHOUT DOCKER
- create virtual env `python -m venv venv`
- activate virtual env `venv\Scripts\activate`
- install requirements `pip install -r requirements.txt`
- run db migrations `python manage.py migrate`
- start the server `python manage.py runserver`

WITH DOCKER
- run `docker-compose up --build`
- enter the container bash `docker exec -it twikker-web-1 bash`
- run db migrations `python manage.py migrate`

OLD VERSION PRINTS

![image](https://user-images.githubusercontent.com/88452580/195798844-3de23718-9bf0-4f2e-893f-50445d71bd4e.png)

NEW VERSION

![image](https://user-images.githubusercontent.com/88452580/200156701-8b07dcbf-86cd-4084-9ea5-0ef81df9abc6.png)

