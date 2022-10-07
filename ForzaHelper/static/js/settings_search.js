import car_brands_n_models from './models_and_brands.js';
import brands from './brands.js';

// let brandsModelsList = JSON.parse()
// let brandsList = JSON.parse(brands)
// console.log(Object.keys(car_brands_n_models))

document.getElementById('brand-search').addEventListener('input', function (evt) {
        let val = this.value.trim().toLowerCase();
        let datalistItems = document.querySelectorAll('#brands option');
        let carCardsList = document.querySelectorAll('.cards-block');

        if (val != '') {
            datalistItems.forEach(function(elem) {
                if (elem.value.search(val) == -1) {
                    elem.setAttribute('disabled', '');
                }
                else {
                    elem.removeAttribute('disabled');
                }
            });
            carCardsList.forEach(function(elem) {

                if (String(elem.classList).split('/')[0].search(val) == -1) {
                    elem.classList.add('d-none');
                }
                else {
                    elem.classList.remove('d-none');
                }
            });
        }
        else {
            datalistItems.forEach(function (elem) {
                elem.removeAttribute('disabled');
            });
            carCardsList.forEach(function(elem) {
                elem.classList.remove('d-none');
            });
        }
});

document.getElementById('model-search').addEventListener('input', function (evt) {
    let val1 = this.value.trim().toLowerCase();
    let datalistItems1 = document.querySelectorAll('#models option');
    let carCardsList = document.querySelectorAll('.cards-block');

    
    if (val1 != '') {
        datalistItems1.forEach(function(elem) {
            if (elem.value.search(val1) == -1) {
                elem.setAttribute('disabled', '');
            }
            else {
                elem.removeAttribute('disabled');
            }
        });
        carCardsList.forEach(function(elem) {

            if (String(elem.classList).split('/')[1].split('|')[0].search(val1) == -1) {
                elem.classList.add('dd-none');
            }
            else {
                elem.classList.remove('dd-none');
            }
        });
    }
    else {
        datalistItems1.forEach(function (elem) {
            elem.removeAttribute('disabled');
        });
        carCardsList.forEach(function(elem) {
            elem.classList.remove('dd-none');
        });
    }
});

document.getElementById('class-selector').addEventListener('change', function (evt) {

    let carCardsList = document.querySelectorAll('.cards-block');

    console.log(this.value.trim().toLowerCase())
    var select_value = this.value.trim().toLowerCase()

    if (select_value == 'class') {

        carCardsList.forEach(function(elem) {
            elem.classList.remove('ddd-none');
        });
    }
    else {
        carCardsList.forEach(function(elem) {
            if (elem.classList.contains(select_value)) {
                elem.classList.remove('ddd-none');
            }
            else {
                
                elem.classList.add('ddd-none');
            }
        });
    }

});

// console.log(car_brands_n_models)