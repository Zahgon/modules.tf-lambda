import json
import logging
import random
import string
import uuid
from hashlib import md5
from pprint import pformat, pprint

import petname


# Class which represents modules.tf definition of resource
class Resource:
    def __init__(self, ref_id, type, text):
        self.ref_id = ref_id
        self.type = type
        self.text = text
        self.params = {}
        self.dependencies = []
        self.dynamic_params = {}

    def append_dependency(self, key):
        pass

    def update_dynamic_params(self, name, value):
        pass

    def update_params(self, value):
        pass

    def content(self):
        pass


# Generate human readable random names
def random_pet(words=2, separator="-"):
    pass


def random_password(length=12):
    pass


# Security group helper - port range
def convert_port_range(port_range):
    pass


# Security group helper - protocol
def convert_protocol(protocol):
    pass


def get_node(G, node_id):
    pass


def get_node_attr(G, node_id, attribute):
    pass


def get_node_data(G, node_id, attribute):
    pass


def convert_graph_to_modulestf_config(graph):  # noqa: C901

    pass
