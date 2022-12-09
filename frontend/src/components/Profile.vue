<template>
    <div class="flex-col w-full bg-white dark:bg-slate-900 border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0" id="twikkerprofileapp">
        <div class="flex flex-col p-4 border-solid border-b-2 border-gray-100 dark:border-gray-700">
            <div class="flex">
                <div class="flex flex-col">
                        <article>
                            <figure>
                                <p>
                                    IMG
                                </p>
                            </figure>
                        </article> 
                    <h1>Snoop Dogg</h1>
                </div>

                <div class="flex flex-col">
                    <a href="{% url 'followers' user.username %}">Followers: 11</a>
                    <a href="{% url 'follows' user.username %}">Follows: 12</a>
                        <a href="{% url 'conversation' user.id %}">Send message</a>
                        <span>
                            <a href="{% url 'unfollow_tweeker' user.username %}">Unfollow</a>
                            <a href="{% url 'follow_tweeker' user.username %}">Follow</a>
                        </span>
                </div>
            </div>
        </div>
        
            <div id="twikkerprofileapp" class="flex-col">
                <div class="flex flex-row h-fit w-full p-2 pt-3 pl-3 border-solid border-b-2 hover:bg-gray-100 dark:hover:bg-gray-700 border-gray-100 dark:border-gray-700">
                    <div class="flex mr-2">
                        <img class="rounded-full h-12 w-12" >
                    </div>
                    <div class="flex flex-col w-full">
                        <div>
                        <span class="font-semibold text-lg">[[ tweek.tweeker_name ]]</span><span class="ml-2">[[ tweek.formatted_time ]]</span>
                        <span class="flex text-xl break-all">[[ tweek.body ]]</span>
                        <div class="flex flex-row justify-between w-2/3 mt-3">
                            <div class="flex">
                                <div class="w-8 h-8 p-1 text-center hover:bg-yellow-200 hover:rounded-full">
                                    <i class="fa-regular fa-comment-dots"></i>
                                </div>
                                <span class="pt-1"></span>
                            </div>
                            <div class="flex">
                                <div class="w-8 h-8 p-1 text-center hover:bg-blue-300 hover:rounded-full">
                                    <i class="fa-solid fa-retweet"></i>
                                </div>
                                <span class="pt-1">25</span>
                            </div>
                            <div class="flex">
                                <div class="flex mx-2">
                                    <div class="w-8 h-8 p-1 text-center hover:bg-green-200 hover:rounded-full">
                                        <i class="fa-regular fa-thumbs-up"></i>
                                    </div>
                                    <span class="pt-1">[[ tweek.likes_count ]] [[ tweek.liked_tweeks ]]</span>
                                </div>
                                <div class="flex mx-2">
                                    <div class="w-8 h-8 p-1 text-center hover:bg-red-200 hover:rounded-full">
                                        <i class="fa-solid fa-thumbs-down"></i>
                                    </div>
                                    <span class="pt-1">[[ tweek.dislikes_count ]] [[ tweek.disliked_tweeks ]]</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
        </div>
    </div>
    </div>
</template>