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
    index = 0
    for weight in weights:
        hash_table_insert(ht, weight, index)
        index += 1

    counter = 0
    pairing_index = None
    weight_index = None
    for weight in weights:
        pairing = limit - weight
        if hash_table_retrieve(ht, pairing):
            pairing_index = hash_table_retrieve(ht, pairing)
            weight_index = hash_table_retrieve(ht, weight)
            if pairing == weight:
                return (1, 0)
            if pairing_index > weight_index:
                return (pairing_index, weight_index)
            elif pairing_index < weight_index:
                return (weight_index, pairing_index)
        counter += 1

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
