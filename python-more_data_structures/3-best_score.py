def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_key = max(a_dictionary, key=a_dictionary.get)
    return best_key

#a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
#best_key = best_score(a_dictionary)
#print("Best score:", best_key)
