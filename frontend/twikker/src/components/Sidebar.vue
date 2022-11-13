<template>
    <div class="sticky top-0 left-0 px-2 h-screen max-[600px]:h-fit max-[600px]:w-screen bg-white dark:bg-slate-900">
        <div class="flex flex-col max-[600px]:flex-row justify-center">
            <div class="flex py-1 max-[600px]:hidden">
                <a class="flex justify-center font-semibold text-lg p-1 hover:bg-green-200 hover:rounded-full " href="{% url 'feed' %} ">
                    <div class="flex w-11 h-11">
                        <i class="text-4xl m-auto fa-solid fa-ankh"></i>
                    </div>
                </a>
            </div>
            <div class="flex py-1">
                <a class="flex justify-center  font-semibold text-lg p-1 hover:bg-gray-200 dark:hover:bg-gray-700 hover:rounded-full " href="{% url 'feed' %} ">
                    <div class="flex w-11 h-11">
                        <i class="text-lg m-auto fa-solid fa-house"></i>
                    </div>
                    <span class="m-auto mx-3 max-[850px]:hidden">Página Inicial</span>
                </a>
            </div>
            <div class="flex py-1">
                <a class="flex font-semibold text-lg p-1 hover:bg-gray-200 dark:hover:bg-gray-700 hover:rounded-full " href="{% url 'notifications' %} ">
                    <div class="flex w-11 h-11">
                        <i class="text-lg m-auto fa-solid fa-bell"></i>
                    </div>
                    <span id="notifications" class="m-auto mx-3 max-[850px]:hidden">Notificações</span>
                </a>
            </div>
            <div class="flex py-1">
                <a class="flex font-semibold text-lg p-1 hover:bg-gray-200 dark:hover:bg-gray-700 hover:rounded-full " href="{% url 'users' %} ">
                    <div class="flex w-11 h-11">
                        <i class="text-lg m-auto fa-solid fa-users"></i>
                    </div>
                    <span class="m-auto mx-3 max-[850px]:hidden">All users</span>
                </a>
            </div>
            <div class="flex py-1">
                <a class="flex font-semibold text-lg p-1 hover:bg-gray-200 dark:hover:bg-gray-700 hover:rounded-full " href="{% url 'global' %} ">
                    <div class="flex w-11 h-11">
                        <i class="text-lg m-auto fa-solid fa-earth-americas"></i>
                    </div>
                    <span class="break-keep m-auto mx-3 max-[850px]:hidden">Global chat</span>
                </a>
            </div>
            <div class="flex py-1">
                <a class="flex font-semibold text-lg p-1 hover:bg-gray-200 dark:hover:bg-gray-700 hover:rounded-full " href="{% url 'conversations' %} ">
                    <div class="flex w-11 h-11">
                        <i class="text-lg m-auto fa-solid fa-comments"></i>
                    </div>
                    <span class="m-auto mx-3 max-[850px]:hidden">Conversations</span>
                </a>
            </div>
            <div class="flex py-1">
                <a class="flex font-semibold text-lg p-1 hover:bg-gray-200 dark:hover:bg-gray-700 hover:rounded-full " href="{% url 'twikkerprofile' request.user.username %} ">
                    <div class="flex w-11 h-11">
                        <i class="text-lg m-auto fa-solid fa-user"></i>
                    </div>
                    <span class="m-auto mx-3 max-[850px]:hidden">Perfil</span>
                </a>
            </div>
            <div class="flex py-1">
                <a class="flex font-semibold text-lg p-1 hover:bg-gray-200 dark:hover:bg-gray-700 hover:rounded-full" onclick="toggleDarkMode()">
                    <div class="flex w-11 h-11">
                        <i class="text-xl m-auto fa-solid fa-moon"></i>
                    </div>
                </a>
            </div>
        </div>
    </div>
</template>

<script setup>

</script>
