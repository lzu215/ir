# Imports

from core import config, configs
from re import match


# Config

config(
    server_ip = "localhost",
    server_port = 9200,
    scheme = "http",
    username = "",
    password = ""
)


# Functions

def getSearch(_):
    return sorted([system for system in configs.modules if match("search\d", system)])