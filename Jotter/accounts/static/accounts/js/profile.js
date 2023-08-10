var buttons = document.querySelectorAll('button');
var subFrames = document.querySelectorAll('.content > div');

buttons.forEach((button) => {
    button.addEventListener('click', () => {
        let state = button.getAttribute('class');
        if (state === 'unfollow') {
            fetch(unfollowUrl)
                .then(() => {
                    button.classList.remove('unfollow');
                    button.classList.add('follow');
                    button.textContent = 'Follow';
                })
                .catch(error, () => {
                    console.error(error);
                });
        } else if (state === 'follow') {
            fetch(followUrl)
                .then(() => {
                    button.classList.remove('follow');
                    button.classList.add('unfollow');
                    button.textContent = 'Unfollow';
                })
                .catch(error, () => {
                    console.error(error);
                });
        } else {
            buttons.forEach((button) => {
                if (button.classList.contains('selected')) button.classList.remove('selected');
            })
            button.classList.add('selected');
            subFrames.forEach((frame) => {
                let frameClass = frame.getAttribute('class');
                if (state !== frameClass) {
                    frame.style.display = 'none';
                }
                else {
                    frame.style.display = "";
                }
            })
        }
    })
})