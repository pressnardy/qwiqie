
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


const towns = document.querySelectorAll('.town');

towns.forEach(town => {
    town.addEventListener('click', () => {
        const filterForm = document.getElementById('location-filter-form');
        const selectedTown = town.textContent.toLocaleLowerCase();
        console.log(selectedTown);
        const formInput = filterForm.querySelector('input#location');
        formInput.value = selectedTown;
        filterForm.submit();
    });
});

const genderInputs = document.querySelectorAll('.input-gender');

genderInputs.forEach(gender => {
    gender.addEventListener('click', () => {
        const genderFilter = document.getElementById('gender-filter')
        genderFilter.submit()
    })
})


const arrow = document.getElementById('arrow-up');

window.addEventListener('scroll', () => {
    const scrollPosition = window.scrollY;
    const halfway = document.documentElement.scrollHeight / 3;

    if (scrollPosition > halfway) {
    arrow.style.display = 'block';
    } else {
    arrow.style.display = 'none';
    }
});

arrow.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
});


const phoneNumbers = document.querySelectorAll('a.escort-phone');
console.log(phoneNumbers)
phoneNumbers.forEach(anchor => {
    const text = anchor.textContent.trim();
    const lastNine = text.slice(-9);
    const formattedPhone = `0${lastNine}`;
    
    anchor.innerText = formattedPhone;
    anchor.href = `tel:${formattedPhone}`;
    console.log(anchor)
});

