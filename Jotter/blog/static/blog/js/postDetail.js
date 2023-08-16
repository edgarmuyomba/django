const commentURL = document.querySelector('.commentURL').textContent;
const form = document.querySelector('#commentForm');
const newComment = document.querySelector('.newComment')

form.addEventListener('submit', (event) => {
    event.preventDefault();

    let data = new FormData(form);

    fetch(commentURL,
        {
            method: 'POST',
            body: data,
        })
        .then(response => response.json())
        .then(success => {
            let inputField = document.querySelector('#commentForm > input:last-child');
            inputField.value = '';
            let feedback = document.querySelector('.commentState');
            feedback.textContent = success.success;
            feedback.classList.add('success');
            feedback.style.display = '';
            setTimeout(() => feedback.style.display = "none", 5000);
        })
        .catch(error => console.log(error));
});

const reply = document.querySelector('.reply');

reply.onclick = () => {
    newComment.style.display = '';
}

const like = document.querySelector('.feedback .like');
const thumb = document.querySelector('.feedback img');

like.onclick = async () => {
    try {
        let result = await fetch(likeUrl);
        let data = await result.json();
        like.classList.remove('like');
        like.classList.add('.dislike');
        like.textContent = 'dislike';
        thumb.style.display = '';
    } catch (e) {
        console.error(e);
    }

}


const dislike = document.querySelector('.feedback .dislike');

dislike.onclick = async () => {
    try {
        let result = await fetch(unlikeUrl);
        let data = await result.json();
        dislike.classList.remove('dislike');
        dislike.classList.add('.like');
        dislike.textContent = 'like';
        thumb.style.display = 'none';
    } catch (e) {
        console.error(e);
    }

}