function formatDate(date) {
    const day = date.getDate();
    const month = date.toLocaleString('default', { month: 'short' });
    const year = date.getFullYear();

    let daySuffix;
    if (day === 1 || day === 21 || day === 31) {
        daySuffix = 'st';
    } else if (day === 2 || day === 22) {
        daySuffix = 'nd';
    } else if (day === 3 || day === 23) {
        daySuffix = 'rd';
    } else {
        daySuffix = 'th';
    }

    return `${day}${daySuffix} ${month} ${year}`;
}

const currentDate = new Date();
const formattedDate = formatDate(currentDate);

function formatTime(date) {
    const hours = String(date.getHours()).padStart(2, '0');
    const minutes = String(date.getMinutes()).padStart(2, '0');
    const seconds = String(date.getSeconds()).padStart(2, '0');

    return `${hours}:${minutes}:${seconds}`;
}

const formattedTime = formatTime(currentDate);

const time = document.querySelector('.time > .content');
time.textContent = formattedTime;

const date = document.querySelector('.date > .content');
date.textContent = formattedDate;

const title = document.querySelector('.post-title');
const header = document.querySelector('.postmain > .title');

title.oninput = () => {
    header.textContent = title.value;
}