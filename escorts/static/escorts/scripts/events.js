
const countyNames = document.querySelectorAll('.county-name');

countyNames.forEach(countyName => {
    countyName.addEventListener('click', () => {
        const towns = countyName.nextElementSibling;
        const caret = countyName.querySelector('.caret');

        if (towns && towns.classList.contains('towns')) {
            const isVisible = towns.style.display === 'block';
            towns.style.display = isVisible ? 'none' : 'block';

            if (caret) {
                caret.style.transform = isVisible ? 'rotate(0deg)' : 'rotate(180deg)';
            }
        }
    });
});

// Updated version using counties.querySelector('.towns')


const towns = document.querySelectorAll('li.town');

towns.forEach(town => {
    town.addEventListener('click', () => {
        const filterForm = document.getElementById('location-filter-form');
        const selectedTown = town.textContent;
        const formInput = filterForm.getElementsByTagName('input');
        formInput.value = selectedTown;
        filterForm.submit()
    })
})


const genderInputs = document.querySelectorAll('.input-gender');

genderInputs.forEach(gender => {
    gender.addEventListener('click', () => {
        const genderFilter = document.getElementById('gender-filter')
        genderFilter.submit()
    })
})

// const searchButton = document.getElementById('search-button');
// searchButton.addEventListener('click', (e) => {
//     e.preventDefault()
//     const searchForm = document.getElementById('search-box')
//     searchForm.submit()
// })
