#!/usr/bin/env python3
"""
Module that has a Python function which lists all documents in a collection
"""
import pymongo


def list_all(mongo_collection):
    """function that lists all documents in a collection"""
    if not mongo_collection:
        return []
    colls = mongo_collection.find({})

    return list(colls)