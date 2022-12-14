<template>
    <div class="flex flex-col w-full border-solid border-x-2 border-gray-100 dark:border-gray-700 max-[600px]:border-x-0">
        <div>
            <div>
                <div>
                    <h1>Followers - {{ user.username }}</h1>

                    <p>Num: {{ user.twikkerprofile.followed_by.count }}</p>
                </div>
            </div>

            <div>
                <div>
                    {% for tweeker in user.twikkerprofile.followed_by.all %}
                        <p><a href="{% url 'twikkerprofile' tweeker.user.username %}">{{ tweeker.user.username }}</a></p>
                    {% empty %}
                        {% if request.user == user %}
                            <p>Sorry, you don't have any followers!</p>
                        {% else %}
                            <p>{{ user.username }} doesn't have any followers!</p>
                        {% endif %}
                    {% endfor %}
                </div>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios'

    export default{
        data () {
            return {
                users: [],
            }
        },
        mounted() {
            this.getUsers();
        },
        methods: {
            getUsers(){
                axios.get(`/api/users/`,) 
                .then(response => {
                    this.users = response.data;
                }).catch(error => {
                    console.log('error' + error)
                })
            },
        }
    }
</script>