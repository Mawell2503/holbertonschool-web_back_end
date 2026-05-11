#!/usr/bin/env python3
"""Function that inserts a new doc"""

#  **kwargs > keyword arguments
#  kwargs passes 'x' number of variable without having to call them in your function definition
def insert_school(mango_collection, **kwargs):
    """
    Insert a  new document into a collection baswed on the provided kwargs

    args:
        mango_collection: the collection object
        **kwargs: keyword arguments representating document fields.

    returns:
        The _id of the newly inserted document.
    """
    #  insert_one() is a method that adds a single document into a collection.
    new_id = mango_collection.insert_one(kwargs)
    return new_id.inserted_id