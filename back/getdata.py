# from os import walk
import json


# def return_data_chunk( mypath ):
#     data = {}
#     f = []
#     for (dirpath, dirnames, filenames) in walk(mypath):
#         f.extend(filenames)
#         break
#     for fil in f:
#         try:
#             with open( mypath + '/' + fil, 'r' ) as file:
#                 data = dict( data, **json.load( file ) )
#         except:
#             print( mypath, fil )
#             raise
#     return data


def return_data():
    with open( './dump.json', 'r' ) as f:
        return json.load( f )
    return {
        'nodes': return_data_chunk( './nodes' ),
        'addresses': return_data_chunk( './addresses' )
    }
