import {getVariableFromDjango} from "/static/js/utils.mjs";

const tweeker_username = getVariableFromDjango('tweeker_username');
const tweeker_avatar = getVariableFromDjango('tweeker_avatar');
const retweeked_tweeks = JSON.parse(getVariableFromDjango('retweeked_tweeks'));

const {createApp} = Vue

document.body.addEventListener('keydown', function(e) {
  if(!(e.keyCode == 13 && (e.metaKey || e.ctrlKey))) return;
        let target = e.target;
        let submit_button = document.querySelector('#submit-tweet');
        if(target.form) {
            submit_button.click();
      }
  });

createApp({
    delimiters: ['[[', ']]'],
    data() {
        return {
            count: 0,
            tweeks: [],
            body: '',
            currentPage: 1,
            tweeker: tweeker_username,
            created_at: 'Now',
            avatar: tweeker_avatar,
            retweeked_tweeks: retweeked_tweeks,
        }
    },
    mounted() {
        this.getTweeks()
        window.onscroll = () => {
            let bottomOfWindow = document.documentElement.scrollTop + window.innerHeight === document.documentElement.offsetHeight

            if (bottomOfWindow && this.hasNext) {
                this.currentPage += 1
                this.getTweeks()
            }
        }
    },
    methods: {
        getTweeks() {
            fetch(`/api/get_tweeks/?page=${this.currentPage}`)
                .then(response => {
                    return response.json()
                })
                .then(data => {
                        this.hasNext = false
                        if (data.next) {
                            this.hasNext = true
                        }
                        for (let i = 0; i < data.results.length; i++) {
                            this.tweeks.push(data.results[i])
                        }
                }).catch(error => {
                    console.log(error)
                })
        },
        async toggleLike(tweek){
            if(tweek.retweek_id){
                await fetch(`/api/tweek/${tweek.retweek_id}/`)
                    .then(response => {
                        return response.json()
                    }
                ).then(data => {
                    tweek = data['tweek']
                });
            }
            if(tweek.is_disliked){
                this.undislikeTweek(tweek);
            }
            if(tweek.is_liked){
                this.unlikeTweek(tweek);
            }else{
                this.likeTweek(tweek);
            }
        },
        likeTweek(tweek){
            tweek.is_liked = true;
            tweek.likes_count += 1;
            let tweek_id = {
                'tweek_id': tweek.id
            };
            fetch('/api/add_like/',{
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': '{{ csrf_token }}',
                    },
                    credentials: 'same-origin',
                    body: JSON.stringify(tweek_id)
                })
                .then((response) => {
                    console.log(response);
                })
                .catch((error) => {
                    console.log(error);
                });x
        },
        unlikeTweek(tweek){
            tweek.is_liked = false;
            tweek.likes_count -= 1;
            var tweek_id = {
                'tweek_id': tweek.id
            };
            fetch('/api/remove_like/',{
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': '{{ csrf_token }}',
                },
                credentials: 'same-origin',
                body: JSON.stringify(tweek_id)
                })
                .then((response) => {
                    console.log(response);
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        async toggleRetweek(tweek_id){
            if(this.retweeked_tweeks.includes(tweek_id)){
                let el = document.getElementById(`retweek-${tweek_id}`);
                await this.unretweekTweek(tweek_id);
            }else{
                await this.submitTweek(tweek_id);
            }
            window.location.reload();
        },
        async unretweekTweek(tweek_id){
            this.retweeked_tweeks = this.retweeked_tweeks.filter(item => item !== tweek_id)
            var tweek = {
                'tweek_id': tweek_id,
            };
            await fetch('/api/remove_retweek/',{
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': '{{ csrf_token }}',
                },
                credentials: 'same-origin',
                body: JSON.stringify(tweek)
                })
                .then((response) => {
                    console.log(response);
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        async toggleDislike(tweek){
            if(tweek.retweek_id){
                await fetch(`/api/tweek/${tweek.retweek_id}/`)
                    .then(response => {
                        return response.json()
                    }
                ).then(data => {
                    tweek = data['tweek']
                });
            }
            if(tweek.is_liked){
              this.unlikeTweek(tweek);
            }
            if(tweek.is_disliked){
              this.undislikeTweek(tweek);
            }else{
              this.dislikeTweek(tweek);
            }
        },
        dislikeTweek(tweek){
            tweek.is_disliked = true;
            tweek.dislikes_count += 1;
            let tweek_id = {
                'tweek_id': tweek.id
            }
            fetch('/api/add_dislike/',{
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': '{{ csrf_token }}',
                    },
                    credentials: 'same-origin',
                    body: JSON.stringify(tweek_id)
                })
                .then((response) => {
                    console.log(response);
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        undislikeTweek(tweek){
            tweek.is_disliked = false;
            tweek.dislikes_count -= 1;
            var tweek_id = {
                'tweek_id': tweek.id
            };
            fetch('/api/remove_dislike/',{
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': '{{ csrf_token }}',
                    },
                    credentials: 'same-origin',
                    body: JSON.stringify(tweek_id)
                })
                .then((response) => {
                    console.log(response);
                })
                .catch((error) => {
                    console.log(error);
            });
        },
        deleteTweek(tweek_id){
            var tweek = {
                'tweek_id': tweek_id,
            };
            fetch('/api/delete_tweek/',{
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': '{{ csrf_token }}',
                },
                credentials: 'same-origin',
                body: JSON.stringify(tweek)
                })
                .then((response) => {
                    console.log(response);
                })
                .catch((error) => {
                    console.log(error);
                });

            const el = document.getElementById('tweek-' + tweek_id);
            el.remove();
        },
        async submitTweek(tweek_id=null){
            if (this.body.length > 0 || tweek_id != null){
                let tweek = {
                    'body': this.body,
                    'tweeker': this.tweeker,
                    'created_at': this.created_at,
                    'avatar': this.avatar,
                    'retweek_id': tweek_id,
                };
                // Send to backend
                await fetch('/api/add_tweek/',{
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': '{{ csrf_token }}',
                    },
                    credentials: 'same-origin',
                    body: JSON.stringify(tweek)
                })
                .then((response) => {
                    console.log(response)
                })
                .catch((error) => {
                    console.log(error)
                })
                window.location.reload();
            }
            this.body = '';
        }
}
}).mount('#feedapp')