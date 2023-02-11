<template>
    <div id="conversationapp" class="flex flex-col h-full">
        <div id="chatcontainer" class="flex flex-col h-full mx-3 mt-2">
            <div class="mb-1.5" v-for="message in messages" :class="message.tweeker_name == this.$store.state.username ? 'justify-end flex w-full' : 'flex w-full' ">
                <article class="flex h-fit w-fit max-w-md p-2 pt-3 pl-3 border-solid border-2 border-gray-100 dark:border-gray-700 bg-gray-700" :class="message.tweeker_name == this.$store.state.username ? 'rounded-tl-3xl rounded-tr-3xl  rounded-bl-3xl' : 'rounded-tl-3xl rounded-tr-3xl  rounded-br-3xl' ">
                    <figure class="shrink-0">
                        <img class="rounded-full h-12 w-12 bg-gray-300">
                    </figure>
                    <div class="flex-col ml-2.5">
                        <div>
                            <strong>
                                <a  href="">{{ message.tweeker_name }}</a>
                            </strong>
                            <small>{{ message.formatted_time }}</small>
                        </div>
                        <div class="break-all">
                            <span>{{ message.content }}</span>
                        </div>
                    </div>
                </article>
            </div>
        </div>
        <div class="p-2 sticky flex bg-white dark:bg-slate-900  bottom-0 w-full items-center">
                <div class="w-full">
                    <form class="m-0" v-on:submit.prevent="submitMessage()">
                        <input v-model="content" type="text" class="rounded-xl px-2 h-10 w-full text-base outline-none text-white bg-gray-700" placeholder="Your message...">
                    </form>
                </div>
                <div class="bg-gray-700 hover:bg-gray-500 ml-1 rounded-xl">
                    <button @click="submitMessage()" class="h-10 w-10 text-green-300 px-2 rounded-full hover:text-green-500"><i class="fa-regular fa-paper-plane"></i></button>
                </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

function scrollToBottom() {
    window.scrollTo(0, document.body.scrollHeight);
}

export default{
    props: ['user_id'],
    data () {
        return {
            conversation_id: '0',
            messages: [],
            content: '',
            tweeker: this.$store.state.username,
            formatted_time: 'Now',
            avatar: '',
            chatSocket: null,
            current_room: 'global',
        }
    },
    mounted() {
        this.getMessages();
        var loc = window.location, new_uri;
        if (loc.protocol === "https:") {
            new_uri = "wss:";
        } else {
            new_uri = "ws:";
        }
        new_uri += "//" + import.meta.env.VITE_SOCKET_HOST;
        this.chatSocket = new WebSocket(
            new_uri +
            '/ws/' +
            'chat/' +
            this.conversation_id +
            '/'
        );
        //append to messages when receive message
        this.chatSocket.onmessage = function (e) {
            const data = JSON.parse(e.data);
            console.log(data)
            // append message to messages
            this.messages.push(data);
            setTimeout(() => {
                scrollToBottom();
            }, 0);
        }.bind(this);
    },
    methods: {
        async getConversationId(){
            await axios.get(`/api/get_conversation/${this.user_id}`)
            .then(response => {
                this.conversation_id = response.data.conversation_id
            })
            .catch(error => {
            })
        },
        async getMessages(){
            if (this.user_id){
                await this.getConversationId();
            }
            await axios.get(`/api/messages/${this.conversation_id}`,) 
            .then(response => {
                for (let i = 0; i < response.data.messages.length; i++) {
                    this.messages.push(response.data.messages[i])
                }
            }).then(() => {
                setTimeout(() => {
                    scrollToBottom();
                }, 0);
            })
            .catch(error => {
                console.log('error 1' + error)
            })
        },
        submitMessage() {
            if (this.content.length > 0) {
                let message = {
                    'content': this.content,
                    'tweeker_name': this.$store.state.username,
                    'formatted_time': this.formatted_time,
                    'avatar_url': this.avatar,
                    'conversation_id': this.conversation_id,
                };
                this.chatSocket.send(JSON.stringify(message));
                this.content = '';
            }
        },
    }
}
</script>