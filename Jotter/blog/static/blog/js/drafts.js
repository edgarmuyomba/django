const newDraft = document.querySelector('.buttons > .draft');
const postForm = document.querySelector('form');

let data = new FormData(postForm);

let formSub = async () => {
    try {
        let response = await fetch(
            draftUrl,
            {
                'method': 'POST',
                'body': data
            });
        let success = await response.json();
        console.log(success);
    } catch (e) {
        console.error(e);
    }
}

newDraft.addEventListener('click', (event) => {
    formSub();
})