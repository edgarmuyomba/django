function fetchDetails(username) {

    const detailUrl = `/accounts/profileDetails/${username}/`;

    let details = { 'none': null };

    fetch(detailUrl)
        .then(response => response.json())
        .then(success => {
            details = {
                'username': success.username,
                'posts': success.posts,
                'followers': success.followers
            }
        })
        .catch(error => {
            details = {
                'error': error
            }
        });
    return details;
}

const associates = document.querySelectorAll('.followers li');
associates.forEach((associate) => {
    let username = associate.textContent;

    let details = fetchDetails(username);
    console.log(details.none);
    loadDetails(details);
});

function loadDetails(details) {
    let profiles = document.querySelectorAll('.profileCard > .details');
    profiles.forEach((profile) => {
        let username = profile.querySelector('.name').textContent;

        if (username === details.username) {
            let extras = profile.querySelector('.extra-details');
            extras.textContent = `${details.posts} post(s) | ${details.followers} follower(s)`;
        }

    })
}