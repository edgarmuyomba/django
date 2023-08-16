window.onload = (event) => {
    console.log(detailUrl);
    fetch(detailUrl)
    .then(response => response.json())
    .then(success => {
        let details = document.querySelector('.profileCard .extra-details');
        details.textContent = `${success.posts} post(s) | ${success.followers} follower(s)`;
    })
    .catch(error => console.error(error));
}