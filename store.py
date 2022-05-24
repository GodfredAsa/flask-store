stores = [
    {'name': "ABnB",
    'items':[
        {'item_name': 'phones',
        'price': 50.0}

    ]}
]

def get_store(store_name):
    for store in stores:
        if store['name'] == store_name:
            return store
        else:
            return "store not found"

def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return store['items']
        else:
            return "store items not found"


# def add_store(name):
#     new_store = [ {'name': 'yam market', 'items': [ {'item_name': 'yams', 'price': 100 }]}]
#     if stores['name'] == name:
#         stores.append(new_store)
#     return stores







# print("------------------------------------------------------------------------")

# print(get_store("ABnB"))     

# print("------------------------------------------------------------------------")

# print(get_items_in_store("ABnB")) 


print("------------------------------------------------------------------------")

print(get_store("ABnB"))