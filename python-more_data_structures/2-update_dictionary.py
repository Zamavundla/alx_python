def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    best_key = max(a_dictionary, key=lambda k: (isinstance(a_dictionary[k], int), a_dictionary[k]))
    return best_key

#dictionary1 = {'name': 'John', 'age': 25}
#best_key = update_dictionary(dictionary1, 'age', 30)
#print("Updated dictionary:", dictionary1)
#print("Best key:", best_key)

#dictionary2 = {'name': 'Alice'}
#best_key = update_dictionary(dictionary2, 'age', 20)
#print("Updated dictionary:", dictionary2)
#print("Best key:", best_key)

#dictionary3 = {}
#best_key = update_dictionary(dictionary3, 'subject', 'Math')
#print("Updated dictionary:", dictionary3)
#print("Best key:", best_key)
