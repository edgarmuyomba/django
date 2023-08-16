async function fetchDetails(username) {

    const detailUrl = `/accounts/profileDetails/${username}/`;

    let details = { 'none': null };
    try {
            let res = await fetch(detailUrl)
            let data = await res.json();
            return data;
    } catch (e) {
        console.log(e);
    }
    return details;
}

const associates = document.querySelectorAll('.followers li');
associates.forEach( async (associate) => {
    let username = associate.textContent;

    let details = await fetchDetails(username);
    loadDetails(details);
});

function loadDetails(details) {
    let profiles = document.querySelectorAll('.profileCard > .details');
    profiles.forEach((profile) => {
        let username = profile.querySelector('.handle').textContent;

        if (username === details.username) {
            let extras = profile.querySelector('.extra-details');
            extras.textContent = `${details.posts} post(s) | ${details.followers} follower(s)`;
        }

    })
}