var buttons = document.querySelectorAll('button');

buttons.forEach((button) => {
    button.addEventListener('click', () => {
        let state = button.getAttribute('class');
        if (state === 'sub') {
            fetch(subUrl)
                .then(() => {
                    button.classList.remove('sub');
                    button.classList.add('unsub');
                    button.textContent = 'Unsubscribe';
                })
                .catch(error => {
                    console.log(error);
                });
        } else {
            fetch(unsubUrl)
                .then(() => {
                    button.classList.remove('unsub');
                    button.classList.add('sub');
                    button.textContent = 'Subscribe';
                })
                .catch(error => {
                    console.log(error);
                });
        }
    })
})