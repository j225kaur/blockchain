#importing modules and libraries needed
import sys

import hashlib 
import json

from time import time
from uuid import uuid4

from flask import Flask, jsonify, request

import requests
from urllib.parse import urlparse

#Declarations
class Blockchain(object):
    difficulty_target = "0000"
    def hash_block(self, block):
        # encode the block into bytes and then hashes it;
        # ensure that the dictionary is sorted, or you'll
        # have inconsistent hashes
        block_encoded = json.dumps (block,sort_keys=True) .encode ()
        return hashlib.sha256(block_encoded).hexdigest()
    def init (self):
        self.nodes = set ()
        # stores all the blocks in the entire blockchain
        self.chain = []
        # temporarily stores the transactions for the current
        # block
        self.current_transactions = []
        # create the genesis block with a specific fixed hash
        # of previous block genesis block starts with index o
        genesis_hash = self.hash_block("genesis block")
        self.append_block(
            hash_of_previous _block = genesis _hash,
            nonce = self.proof _of work(O, genesis _hash, [])
        )
    
    # use Pow to find the nonce for the current block
    def proof_of_work(self, index, hash_of_previous _block, transactions):
        # try with nonce = 0
        nonce = 0
        # try hashing the nonce together with the hash of the
        while self.valid_proof(index, hash_of_previous_block, transactions, nonce) is False:
            nonce+=1
        return nonce
    #checking if the hash block meets the difficulty target
    def valid_proof(self, index, hash_of_previous_block, transactions,nonce):
        

