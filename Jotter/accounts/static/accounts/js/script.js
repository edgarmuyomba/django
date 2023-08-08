var buttons = document.querySelectorAll('button');
var content = document.querySelector('.content');

buttons.forEach((button) => {
    button.addEventListener('click', () => {
        console.log(button.id);
        if (button.id === "0") {
            content.innerHTML = "{% include 'registration/dynamicContent.html' with contents=posts %}";
        } else if (button.id === "1") {
            content.innerHTML = "{% include 'registration/dynamicContent.html' with contents=comments %}";
        } else if (button.id === "2") {
            content.innerHTML = "{% include 'registration/dynamicContent.html' with contents=profile.topics %}";
        } else if (button.id === "3") {
            content.innerHTML = "{% include 'registration/dynamicContent.html' with contents=profile.following %}";
        } else {
            content.innerHTML = "{% include 'registration/dynamicContent.html' with contents=profile.followers %}";
        }
    })
})