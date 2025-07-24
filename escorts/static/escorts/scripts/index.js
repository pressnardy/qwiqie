
const caretSVG = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512" class="caret" color="white" fill="#f799d6">
    <!--!Font Awesome Free 6.6.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free Copyright 2024 Fonticons, Inc.-->
    <path d="M137.4 374.6c12.5 12.5 32.8 12.5 45.3 0l128-128c9.2-9.2 11.9-22.9 6.9-34.9s-16.6-19.8-29.6-19.8L32 192c-12.9 0-24.6 7.8-29.6 19.8s-2.2 25.7 6.9 34.9l128 128z"/></svg>`

const heartSVG = `<svg width="18" height="24" viewBox="0 0 24 24" fill="#f799d6" xmlns="http://www.w3.org/2000/svg" class="caret">
<path d="M12 21.35L10.55 20.03C5.4 15.36 2 12.28 2 8.5C2 5.41 4.42 3 7.5 3C9.24 3 10.91 3.79 12 5.05C13.09 3.79 14.76 3 16.5 3C19.58 3 22 5.41 22 8.5C22 12.28 18.6 15.36 13.45 20.03L12 21.35Z"/>
</svg>`


// const countiesContainer = document.getElementById('counties');

// counties.forEach(county => {
//     const countyElement = document.createElement('div');
//     countyElement.classList.add('county');
//     countyElement.innerHTML = `
//         <div class="county-name">
//             ${county.name.charAt(0).toUpperCase() + county.name.slice(1)}
//             ${heartSVG}
//         </div>
//         <ul class="towns" style="display: none;">
//             ${county.towns.map(town => `<li class="town">${town.charAt(0).toUpperCase() + town.slice(1)}</li>`).join('')}
//         </ul>
//     `;
//     countiesContainer.appendChild(countyElement);
// });
