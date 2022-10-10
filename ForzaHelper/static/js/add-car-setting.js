import car_brands_n_models from './models_and_brands.js';
import brands from './brands.js';

var brandList = brands.brands

// console.log(brandList)

document.getElementById('car-brand').addEventListener('input', function(evt){
    let val = this.value.trim().toLowerCase();
    let datalistItems = document.querySelectorAll('#models option');
    
    if(brandList.includes(val) ) {
        
        let modelList = car_brands_n_models[val]
        console.log(modelList)
        datalistItems.forEach(function(elem){
            
            if ( !(modelList.includes(elem.value)) ) {
                elem.setAttribute('disabled', '');
            }
            else {
                elem.removeAttribute('disabled');
            }
        });
    }
    else {
        datalistItems.forEach(function(elem){
            elem.removeAttribute('disabled');
        });
    }
});

document.getElementById('car-brand').addEventListener('input', function(evt){
    let val = this.value.trim().toLowerCase();
    let datalistItems = document.querySelectorAll('#models option');

    console.log() 
    
    if(brandList.includes(val) ) {
        
        let modelList = car_brands_n_models[val]
        console.log(modelList)
        datalistItems.forEach(function(elem){
            
            if ( !(modelList.includes(elem.value)) ) {
                elem.setAttribute('disabled', '');
            }
            else {
                elem.removeAttribute('disabled');
            }
        });
    }
    else {
        datalistItems.forEach(function(elem){
            elem.removeAttribute('disabled');
        });
    }
});