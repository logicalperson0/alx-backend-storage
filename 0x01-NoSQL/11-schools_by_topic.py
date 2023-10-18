#!/usr/bin/env python3
"""
Module that has a Python function which returns specific topic
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """function that returns the list of school having a specific topic"""
    if mongo_collection is None:
        return []
    find_id = mongo_collection.find( { "topics": topic } )
    return find_id