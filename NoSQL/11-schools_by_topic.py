#!/usr/bin/env python3
""" Function that returns the list of school having a specific topic """

def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools having a specific topic
    
    Args:
        mongo_collection: pymongo collection object
        topic (str): the topic searched
        
    Returns:
        List of school documents (dictionaries)
    """
    # Find all documents where the 'topics' array contains the specific topic
    schools = mongo_collection.find({ "topics": topic })
    
    return list(schools)
