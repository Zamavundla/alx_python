def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])

#print(multiple_returns("Hello"))  # Output: (5, 'H')
#print(multiple_returns(""))  # Output: (0, None)
#print(multiple_returns("Python"))  # Output: (6, 'P')
