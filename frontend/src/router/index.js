import { createWebHistory, createRouter } from "vue-router"
import Main from "../views/Main.vue"
import Feed from "../components/Feed.vue"
import Conversations from "../components/Conversations.vue"
import Notifications from "../components/Notifications.vue"
import Profile from "../components/Profile.vue"
import Users from "../components/Users.vue"
import Globalchat from "../components/GlobalChat.vue"

const routes = [
  {
    path: "/signup",
    name: "SignUp",
    component: () => import("../views/SignUp.vue"),
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("../views/Login.vue"),
  },
  {
    path: "/",
    name: "Main",
    component: Main,
    children: [
      {
        path: "/feed",
        name: "Feed",
        component: Feed,
      },
      {
        path: "/conversations",
        name: "Conversations",
        component: Conversations,
      },
      {
        path: "/conversation/:id",
        name: "Conversation",
        props: true,
        component: () => import("../components/Conversation.vue")
      },
      {
        path: "/notifications",
        name: "Notifications",
        component: Notifications
      },
      {
        path: "/users",
        name: "Users",
        component: Users
      },
      {
        path: "/profile",
        name: "SelfProfile",
        component: Profile
      },
      {
        path: "/profile/:username",
        name: "Profile",
        component: Profile
      },
      {
        path: "/globalchat",
        name: "GlobalChat",
        component: Globalchat
      },
      {
        path: "/tweek/:id",
        name: "Tweek",
        props: true,
        component: () => import("../components/TweekPage.vue")
      },
    ]
  },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router