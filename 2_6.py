"""
 придумайте 3 різних ф-ції(немає різниці які)
"""

person_list = {
    "John": {
        "gender": "men",
        "age": 25,
        "marital_status": "not-married",
        "high_educated": "educated"
    },
    "Emma": {
        "gender": "women",
        "age": 25,
        "marital_status": "not-married",
        "high_educated": "educated"
    },
    "Rosa": {
        "gender": "women",
        "age": 35,
        "marital_status": "married",
        "high_educated": "educated"
    },
    "Mery": {
        "gender": "women",
        "age": 18,
        "marital_status": "not-married",
        "high_educated": "not-educated"
    },
    "Tom": {
        "gender": "men",
        "age": 28,
        "marital_status": "married",
        "high_educated": "not-educated"
    },
    "Susan": {
        "gender": "women",
        "age": 30,
        "marital_status": "not-married",
        "high_educated": "educated"
    },
    "Michel": {
        "gender": "men",
        "age": 16,
        "marital_status": "not-married",
        "high_educated": "not-educated"
    },
    "Ellis": {
        "gender": "women",
        "age": 1,
        "marital_status": "not-married",
        "high_educated": "not-educated"
    },
    "Wilson": {
        "gender": "men",
        "age": 8,
        "marital_status": "not-married",
        "high_educated": "not-educated"
    },
    "Dorothy": {
        "gender": "women",
        "age": 23,
        "marital_status": "not-married",
        "high_educated": "educated"
    },
    "Bruce": {
        "gender": "men",
        "age": 29,
        "marital_status": "married",
        "high_educated": "educated"
    },
    "Hector": {
        "gender": "men",
        "age": 102,
        "marital_status": "married",
        "high_educated": "educated"
    },
}

# function will return age of chosen person
# input data: name - string, interested person name
# return number type - person age
def age(name):
    return person_list[name]["age"]

# function will return marital status of chosen person
# input data: name - string, interested person name
# return string type - marital status of interested person
def does_married(name):
    return person_list[name]["marital_status"]

# function will return high educated status of chosen person
# input data: name - string, interested person name
# return string type - high educated status of interested person
def does_high_educated(name):
    return person_list[name]["high_educated"]

# function will return all information in dictionary of chosen person
# input data: name - string, interested person name
# return dict type
def full_person_info(name):
    return person_list[name]

print (full_person_info("Hector"))
