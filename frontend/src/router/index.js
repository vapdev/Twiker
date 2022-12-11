import { createWebHistory, createRouter } from "vue-router"
import Feed from "../views/Feed.vue"
import Conversations from "../views/Conversations.vue"
import Notifications from "../views/Notifications.vue"
import Profile from "../views/Profile.vue"
import Users from "../views/Users.vue"

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
    name: "Feed",
    component: Feed,
  },
  {
    path: "/conversations",
    name: "Conversations",
    component: Conversations
  },
  {
    path: "/conversation/:id",
    name: "Conversation",
    props: true,
    component: () => import("../views/Conversation.vue")
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
    component: () => import("../views/GlobalChat.vue")
  }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router