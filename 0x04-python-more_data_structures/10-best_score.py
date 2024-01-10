#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None

    result = 0
    for item in a_dictionary:
        if a_dictionary[item] > result:
            best_score = item
            result = a_dictionary[item]
    return best_score

# a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
# best_key = best_score(a_dictionary)
# print("Best score: {}".format(best_key))

# best_key = best_score(None)
# print("Best score: {}".format(best_key))
