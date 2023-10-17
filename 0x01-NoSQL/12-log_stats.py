#!/usr/bin/env python3
"""
Module that has a Python function which provides some stats about Nginx logs
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')

    logs_stats = client.logs.nginx
    
    cou_doc = logs_stats.count_documents({})
    get_doc = logs_stats.count_documents( { "method": "GET" } )
    post_doc = logs_stats.count_documents( {"method": "POST"} )
    put_doc = logs_stats.count_documents( { "method": "PUT" } )
    patch_doc = logs_stats.count_documents( { "method": "PATCH" } )
    del_doc = logs_stats.count_documents( { "method": "DELETE" } )
    status_doc = logs_stats.count_documents( { "method": "GET",
                                              "path": "/status" } )

    print('{} logs'.format(cou_doc))
    print("Methods:")
    print('    method GET: {}'.format(get_doc))
    print('    method POST: {}'.format(post_doc))
    print('    method PUT: {}'.format(put_doc))
    print('    method PATCH: {}'.format(patch_doc))
    print('    method DELETE: {}'.format(del_doc))
    print('{} status check'.format(status_doc))