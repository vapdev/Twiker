import { createWebHistory, createRouter } from "vue-router"
import Feed from "../views/Feed.vue"
import Conversations from "../views/Conversations.vue"
import Notifications from "../views/Notifications.vue"
import Profile from "../views/Profile.vue"
import Users from "../views/Users.vue"

const routes = [
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
    name: "Profile",
    component: Profile
  }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router