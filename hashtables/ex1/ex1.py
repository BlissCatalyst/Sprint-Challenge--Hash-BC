#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # if len(weights) <= 1:
    #     return None
    # else:
    weight_index = 0
    print("WEIGHTS:", weights)
    for i in weights:
        hash_table_insert(ht, i, weight_index)
        weight_index += 1

    weight_index = 0
    for i in weights:
        limit_minus_weight = limit - i
        if hash_table_retrieve(ht, limit_minus_weight):
            if hash_table_retrieve(ht, limit_minus_weight) > hash_table_retrieve(ht, i):
                print_answer(
                    (str(hash_table_retrieve(ht, limit_minus_weight)), str(hash_table_retrieve(ht, i))))
                return (hash_table_retrieve(ht, limit_minus_weight), hash_table_retrieve(ht, i))
            elif limit_minus_weight == i:
                return (hash_table_retrieve(ht, limit_minus_weight), weight_index)
            else:
                print_answer(
                    (str(hash_table_retrieve(ht, i)), str(hash_table_retrieve(ht, limit_minus_weight))))
                return (hash_table_retrieve(ht, i), hash_table_retrieve(ht, limit_minus_weight))
            weight_index += 1
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
