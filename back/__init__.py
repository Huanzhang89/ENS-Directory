import json
import web3

from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source
from web3.contract import ConciseContract

w3 = Web3(TestRPCProvider())
