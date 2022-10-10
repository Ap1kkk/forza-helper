import json

with open('ForzaHelper/static/json/car_brands.json', 'r') as f:
    brands_dictionary = json.load(f)

with open('ForzaHelper/static/json/car_models.json', 'r') as f:
    models_dictionary = json.load(f)

with open('ForzaHelper/static/json/car_models_n_names.json', 'r') as f:
    model_name = json.load(f)

with open('ForzaHelper/static/json/car_brands_n_models.json', 'r') as f:
    brands_and_models_dictionary = json.load(f)

with open('ForzaHelper/static/json/car_brands_n_models_lower.json', 'r') as f:
    brands_and_models_dictionary_lower = json.load(f)


class JsonFiles:
    brand_list = brands_dictionary["brands"]
    model_list = models_dictionary["models"]

    brands_and_models = brands_and_models_dictionary
    brands_and_models_lower = brands_and_models_dictionary_lower

    def get_models_by_brand(brand):
        return brands_and_models_dictionary[brand]


    def get_name_by_model(model):
        return model_name[model]
