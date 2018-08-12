from flask import Flask
import json
import getdata

data = getdata.return_data()

app = Flask( 'ENS-DIR' )
@app.route( '/' )
def index():
    return 'Welcome to ENS DIR API'

@app.route( '/address/<address>' )
def address_route( address ):
    if address in data[ 'addresses' ]:
        return json.dumps( data[ 'addresses' ][ address ] ), 200, { 'Content-Type': 'application/json' }
    else:
        return json.dumps( { 'error': f'Address {address} not found!' } ), 400, { 'Content-Type': 'application/json' }


@app.route( '/node/<node>' )
def node_route( node ):
    if node in data[ 'nodes' ]:
        return json.dumps( data[ 'nodes' ][ node ] ), 200, { 'Content-Type': 'application/json' }
    else:
        return json.dumps( { 'error': f'Node {node} not found!' } ), 400, { 'Content-Type': 'application/json' }


app.run( '0.0.0.0', 5000, False )
