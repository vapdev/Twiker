import { createWebHistory, createRouter } from "vue-router"
import { useUserStore } from '../store/UserStore.js'
import Main from "../views/Main.vue"
import Feed from "../pages/Feed.vue"
import Conversations from "../components/Conversations.vue"
import Notifications from "../pages/Notifications.vue"
import Profile from "../pages/Profile.vue"
import Users from "../pages/Users.vue"
import Followers from "../pages/Followers.vue"
import Following from "../pages/Following.vue"
import Globalchat from "../pages/GlobalChat.vue"
import rSideBar from '../components/rSideBar.vue';
import noConversation from '../pages/noConversation.vue'
import EditProfile from '../pages/EditProfile.vue'
import Conversation from '../pages/Conversation.vue'
import TweekPage from '../pages/TweekPage.vue'

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
    path: "/logout",
    name: "Logout",
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
        path: "/edit",
        name: "EditProfile",
        components: {
          default: EditProfile,
          right: rSideBar,
        },
      },
      {
        path: "/conversation",
        name: "Conversations",
        components: {
          default: noConversation,
          right: Conversations,
        },
      },
      {
        path: "/conversation/:id",
        name: "Conversation",
        props: true,
        components: {
          default: Conversation,
          right: Conversations,
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
          default: TweekPage,
          right: rSideBar,
        },
      },
      {
        path: "/followers/:id",
        name: "Followers",
        props: true,
        components: {
          default: Followers,
          right: rSideBar,
        },
      },
      {
        path: "/following/:id",
        name: "Following",
        props: true,
        components: {
          default: Following,
          right: rSideBar,
        },
      },
    ]
  },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

router.beforeEach((to, from, next) => {

  const userStore = useUserStore();

  const isAuthenticated = userStore.isAuthenticated;

  // if user is not logged in and tries to access a page that requires authentication then redirect to login page
  if (!isAuthenticated && (to.name === 'Feed' || to.name === 'Notifications' ||
  to.name === 'Users' || to.name === 'GlobalChat' || to.name === 'Profile' || to.name === 'EditProfile' ||
  to.name === 'Conversation' || to.name === 'Tweek')) {
    next({ name: 'Login' })
  } else {
    next()
  }
});

export default router
