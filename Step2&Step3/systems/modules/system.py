# Imports

import core # For importing modules (or would cause circular imports)
from core import config, configs
from re import match
from time import sleep


# Config

config = config(
    server_ip = "localhost",
    server_port = "9200",
    scheme = "http",
    username = "",
    password = ""
)


# Functions

def getSearch(_):
    return sorted([system for system in core.modules if match("search\d", system)])

def getConfigsList(_):
    return sorted(map(lambda x: x.title(), configs.keys()))

def getConfigs(receive):
    return configs[receive.config]

def updateConfig(receive):
    module = receive.pop("module__")
    if configs[module] == receive:
        return 1
    else:
        configs[module] = receive
        core.modules[module].config.save()
        return 0