import {getVariableFromDjango} from "/static/js/utils.mjs";

const tweeker_username = getVariableFromDjango('tweeker_username');
const tweeker_avatar = getVariableFromDjango('tweeker_avatar');
const liked_tweeks = JSON.parse(getVariableFromDjango('liked_tweeks'));
const disliked_tweeks = JSON.parse(getVariableFromDjango('disliked_tweeks'));
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
            liked_tweeks: liked_tweeks,
            disliked_tweeks: disliked_tweeks,
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
        toggleLike(tweek_id){
            if(this.disliked_tweeks.includes(tweek_id)){
                this.undislikeTweek(tweek_id);
            }
            if(this.liked_tweeks.includes(tweek_id)){
                this.unlikeTweek(tweek_id);
            }else{
                this.likeTweek(tweek_id);
            }
        },
        likeTweek(tweek_id){
            this.liked_tweeks.push(parseInt(tweek_id));
            let tweek = {
                'tweek_id': tweek_id,
            };
            fetch('/api/add_like/',{
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

                const el = document.getElementById('likes-' + tweek_id);
            const likes = parseInt(el.innerHTML) + 1;
            el.innerHTML = likes;
        },
        unlikeTweek(tweek_id){
            this.liked_tweeks = this.liked_tweeks.filter(item => item !== tweek_id)
            var tweek = {
                'tweek_id': tweek_id,
            };
            fetch('/api/remove_like/',{
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

            const el = document.getElementById('likes-' + tweek_id);
            const likes = parseInt(el.innerHTML) - 1;
            el.innerHTML = likes;
        },
        toggleRetweek(tweek_id){
            if(this.retweeked_tweeks.includes(tweek_id)){
                this.unretweekTweek(tweek_id);
            }else{
                this.submitTweek(tweek_id);
            }
            window.location.reload();
        },
        unretweekTweek(tweek_id){
            this.retweeked_tweeks = this.retweeked_tweeks.filter(item => item !== tweek_id)
            var tweek = {
                'tweek_id': tweek_id,
            };
            fetch('/api/remove_retweek/',{
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
        toggleDislike(tweek_id){
            if(this.liked_tweeks.includes(tweek_id)){
              this.unlikeTweek(tweek_id);
            }
            if(this.disliked_tweeks.includes(tweek_id)){
              this.undislikeTweek(tweek_id);
            }else{
              this.dislikeTweek(tweek_id);
            }
        },
        dislikeTweek(tweek_id){
            this.disliked_tweeks.push(parseInt(tweek_id));
            let tweek = {
                'tweek_id': tweek_id,
            };
            fetch('/api/add_dislike/',{
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

                const el = document.getElementById('dislikes-' + tweek_id);
            const dislikes = parseInt(el.innerHTML) + 1;
            el.innerHTML = dislikes;
        },
        undislikeTweek(tweek_id){
            this.disliked_tweeks = this.disliked_tweeks.filter(item => item !== tweek_id)
            var tweek = {
                'tweek_id': tweek_id,
            };
            fetch('/api/remove_dislike/',{
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
            const el = document.getElementById('dislikes-' + tweek_id);
            const dislikes = parseInt(el.innerHTML) - 1;
            el.innerHTML = dislikes;
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
        submitTweek(tweek_id=null){
            if (this.body.length > 0 || tweek_id != null){
                let tweek = {
                    'body': this.body,
                    'tweeker': this.tweeker,
                    'created_at': this.created_at,
                    'avatar': this.avatar,
                    'retweek_id': tweek_id,
                };
                // Send to backend
                fetch('/api/add_tweek/',{
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