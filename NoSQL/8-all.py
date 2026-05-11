#!/usr/bin/env python3
"""List all documents in a collection"""

def list_all(mongo_collection):
    """Returns all documents in a collection or empty list"""
    if mongo_collection is None:
        return []
    #  find() finds everything specific to mango_collection 
    #  list() list it as a python object.
    return list(mongo_collection.find())
