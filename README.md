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
- run `docker-compose up --build` (if its not the first time you dont need to build it)
- enter the container bash `docker exec -it twikker-web-1 bash`
- run db migrations `python manage.py migrate`

<h2> Prints </h2>

![image](https://user-images.githubusercontent.com/88452580/201464963-479c031f-0d06-405b-b0fb-0b4bd6781a61.png)
![image](https://user-images.githubusercontent.com/88452580/201464967-bde7576c-3b0a-4f89-9167-b449220706a6.png)
[![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=vapdev)](https://github.com/anuraghazra&hide=css/github-readme-stats)
