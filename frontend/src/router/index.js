import { createWebHistory, createRouter } from "vue-router"
import Main from "../views/Main.vue"
import Feed from "../components/Feed.vue"
import Conversations from "../components/Conversations.vue"
import Notifications from "../components/Notifications.vue"
import Profile from "../components/Profile.vue"
import Users from "../components/Users.vue"
import Globalchat from "../components/GlobalChat.vue"
import rSideBar from '../components/rSideBar.vue';

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
        path: "/",
        name: "Feed",
        components: {
          default: Feed,
          right: rSideBar,
        },
      },
      {
        path: "/conversations",
        name: "Conversations",
        components: {
          default: Conversations,
          right: rSideBar, 
        },
      },
      {
        path: "/conversation/:id",
        name: "Conversation",
        props: true,
        components: {
          default: () => import("../components/Conversation.vue"),
          right: rSideBar,
        },
      },
      {
        path: "/notifications",
        name: "Notifications",
        components: {
          default: Notifications,
          right: rSideBar,
        },
      },
      {
        path: "/users",
        name: "Users",
        components: {
          default: Users,
          right: rSideBar,
        },
      },
      {
        path: "/profile",
        name: "SelfProfile",
        components: {
          default: Profile,
          right: rSideBar,
        },
      },
      {
        path: "/profile/:username",
        name: "Profile",
        components: {
          default: Profile,
          right: rSideBar,
        },
      },
      {
        path: "/globalchat",
        name: "GlobalChat",
        components: {
          default: Globalchat,
          right: rSideBar,
        },
      },
      {
        path: "/tweek/:id",
        name: "Tweek",
        props: true,
        components: {
          default: () => import("../components/TweekPage.vue"),
          right: rSideBar,
        },
      },
    ]
  },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router