def fusionner_dicts(dict1, dict2):
    for key, value in dict2.items():
        if key in dict1:
            dict1[key] += value
        else:
            dict1[key] = value
    return dict1

# Tests
dict1 = {"x": 1, "y": 2}
dict2 = {"y": 3, "z": 4}
print(fusionner_dicts(dict1, dict2));