<template>
  <div
    class="dark h-screen w-screen bg-white dark:bg-dark flex items-center justify-center flex-col"
  >
    <div class="m-3 rounded-md border-2 border-gray-500">
      <div class="py-1 font-bold w-full border-b-2 border-gray-500">
        <div class="pl-2 py-1 font-bold w-full border-b-2 border-gray-500">
          <h1 class="text-lg">Registrar</h1>
        </div>
        <form
          @submit.prevent="submitForm"
          class="flex-col grid justify-items-end mb-2 p-3 font-medium"
        >
        <div class="flex flex-col">
            <p class="text-base">Usuário:</p>
          <input
          type="text"
          name="username"
          v-model="username"
          class="rounded-md mb-1 text-black bg-lchat border p-0.5 border-gray-700 text-base"
          />
          <p class="text-base">Senha:</p>
          <input
          type="password"
          name="password"
          v-model="password"
          class="rounded-md mb-2 text-black bg-lchat border p-0.5 border-gray-700 text-base"
          />
          <p class="text-base">Confirme a senha:</p>
          <input
          type="password"
          name="password"
          v-model="passwordCopy"
          class="rounded-md mb-2 text-black bg-lchat border p-0.5 border-gray-700 text-base"
          />
        </div>
          <button
            type="submit"
            class="mt-3 text-black px-2 border-2 bg-gray-100 hover:bg-gray-300 rounded-xl"
          >
            Enviar
          </button>
        </form>
      </div>
    </div>
    <div class="mt-4">
      <p class="text-red-500 text-sm" v-for="msg in errorMsgArray">
        - {{ msg }} 
      </p>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

const name = "SignUp";
let username = ref("");
let password = ref("");
let passwordCopy = ref("");
const errorMsgArray = ref([]);

function submitForm(e) {
  const usernameRegex = /^[a-zA-Z0-9_]+$/;

  const formData = {
    username: username.value,
    password: password.value,
  };

  if (password.value !== passwordCopy.value) {
    errorMsgArray.value = ["As senhas não coincidem"];
    return;
  }

  if (!usernameRegex.test(username.value)) {
    errorMsgArray.value = ["O nome de usuário só pode conter letras, números e os caracteres: _ -"];
    return;
  }

  axios
    .post("api/v1/users/", formData)
    .then((response) => {
      router.replace("/login");
    })
    .catch((error) => {
      errorMsgArray.value = error.response.data.password;
    });
}
</script>
