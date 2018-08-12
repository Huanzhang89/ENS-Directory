import json
from collections import defaultdict
import pymongo
from pymongo import InsertOne
from web3 import Web3

data = []
print( 'Loading data from json...' )
with open( './data/ens-3327417-to-5787413-decoded.json' ) as f:
    i = 0
    for line in f:
        data.append( json.loads( line ) )
        i += 1

print( 'Humanizing block nos...' )
for rec in data:
    rec[ 'blockNumberHuman' ] = int( rec[ 'blockNumber' ], 16 )


def hashname( node, label ):
    try:
        args = [ arg if '0x' != arg[ :2 ] else arg[ 2: ] for arg in [ node, label ] ]
        h = Web3.soliditySha3( [ 'bytes32' for _ in args ], tuple( bytes.fromhex( arg ) for arg in args ) )
    except Exception as e:
        print( args )
        raise
    return h.hex()


def new_owner( node, owner, label, block_no ):
    h = hashname( node, label )
    if h in nodes:
        previous_address = nodes[ h ].transfer( owner, block_no )
    else:
        nodes[ h ] = Node( h )
        previous_address = nodes[ h ].transfer( owner, block_no )
    addresses[ owner ].own( h, block_no )
    if previous_address is not None:
        addresses[ previous_address ].lose( h, block_no )


def transfer( node, owner, block_no ):
    h = node
    if h in nodes:
        previous_address = nodes[ h ].transfer( owner, block_no )
    else:
        nodes[ h ] = Node( h )
        previous_address = nodes[ h ].transfer( owner, block_no )
    addresses[ owner ].own( h, block_no )
    if previous_address is not None:
        addresses[ previous_address ].lose( h, block_no )

class Address:
    def __init__( self, address ):
        self.address = address
        self.history = []
        self.current_nodes = []


    def own( self, node_hash, block_no ):
        self.current_nodes.append( node_hash )
        self.history.append( ( block_no, f'owns {node_hash}' ) )


    def lose( self, node_hash, block_no ):
        self.current_nodes = [ node for node in self.current_nodes if node != node_hash ]
        self.history.append( ( block_no, f'lost {node_hash}' ) )


    def to_json( self ):
        return {
            'address': self.address,
            'history': self.history,
            'current_nodes': self.current_nodes
        }


class Node:
    def __init__( self, node_hash ):
        self.node_hash = node_hash
        self.current_address = None
        self.history = []


    def transfer( self, new_owner, block_no ):
        self.history.append( ( block_no, new_owner ) )
        previous_owner = self.current_address
        self.current_address = new_owner
        return previous_owner

    def to_json( self ):
        return {
            'hash': self.node_hash,
            'history': self.history,
            'current_address': self.current_address
        }

print( 'Creating address records...' )
nodes = {}
addresses = { address: Address( address ) for address in set( [ x[ 'args' ][ 'owner' ] for x in data if 'owner' in x[ 'args' ] ] ) }

print( 'Creating node records...' )
for rec in sorted( data, key = lambda rec: rec[ 'blockNumberHuman' ] ):
    if rec[ 'event' ] == 'NewOwner':
        new_owner( rec[ 'args' ][ 'node' ], rec[ 'args' ][ 'owner' ], rec[ 'args' ][ 'label' ], rec[ 'blockNumberHuman' ] )
    elif rec[ 'event' ] == 'Transfer':
        transfer( rec[ 'args' ][ 'node' ], rec[ 'args' ][ 'owner' ], rec[ 'blockNumberHuman' ] )


d = {
    'addresses': { key: value.to_json() for key, value in addresses.items() },
    'nodes': { key: value.to_json() for key, value in nodes.items() }
}


# nkeys = list( nodes.keys() )
# akeys = list( addresses.keys() )

# print( 'Dumping data' )
# for i in range( 0, len( nodes ), 1000 ):
#     with open( f'./nodes/nodes-{i}.json', 'w+' ) as f:
#         json.dump( { key: nodes[ key ].to_json() for key in nkeys[ i:i+1000 ] }, f )
# 
# for i in range( 0, len( addresses ), 1000 ):
#     with open( f'./addresses/addr-{i}.json', 'w+' ) as f:
#         json.dump( { key: addresses[ key ].to_json() for key in akeys[ i:i+1000 ] }, f )

with open( './dump.json', 'w+' ) as f:
    json.dump( d, f )


# print( 'Populating MongoDB with data...' )
# db = pymongo.MongoClient('mongodb://localhost').ens
# db_addr = db.addresses
# db_node = db.nodes

# print()
# for i, ( _, address ) in enumerate( addresses.items() ):
#     if int( address.address, 16 ) == 0:
#         continue
#     if len( address.history ) < 8:
#         db_addr.insert_one( address.to_json() )
#     else:
#         to_add = []
#         for j in range( 0, len( address.history ), 8 ):
#             to_add.append( InsertOne( dict( address.to_json(), history = address.history[ j:j+8 ] ) ) )
#         db_addr.bulk_write( to_add )
#     if i % 1000 == 0:
#         print( round( 100 * ( i / len( addresses ) ) ), '%' )
# 
# print()
# for i, ( _, node ) in enumerate( nodes.items() ):
#     db_node.insert_one( node.to_json() )
#     if i % 1000 == 0:
#         print( round( 100 * ( i / len( nodes ) ) ), '%' )
