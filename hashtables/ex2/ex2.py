#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for ticket in tickets:
        hash_table_insert(ht, ticket.source, ticket.destination)

    i = 0
    while i < length:
        if route[0] is None:
            route[0] = hash_table_retrieve(ht, "NONE")
        else:
            route[i] = hash_table_retrieve(ht, route[i - 1])
        i += 1

    return route
