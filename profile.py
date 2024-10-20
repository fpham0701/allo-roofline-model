import allo
import numpy as np
import sys
import hcl_mlir

from hcl_mlir import Module, Context, Location
from hcl_mlir.dialects import hcl as hcl_d





# Context
class GlobalContext(object):
    def __init__(self):
        self.ctx = None
        self.loc = None

    def get_context(self):
        return self.ctx

    def set_context(self):
        self.ctx = Context()
        hcl_d.register_dialect(self.ctx)
        self.loc = Location.unknown(self.ctx)

    def get_location(self):
        return self.loc
        

# Global Context Object
global_ctx = GlobalContext()
get_context = global_ctx.get_context
set_context = global_ctx.set_context
get_location = global_ctx.get_location

"""
utility function takes a filename and outputs its respecting mlir module
"""
def load_mlir(file):
    set_context()

    with open(filename, 'r') as file:
        with get_context() as ctx, get_location():
            module = Module.parse(file.read(), ctx)

            return module


if __name__ == "__name__":
    # checking if num of sys args are correct
    if len(sys.argv) != 2:
        print("Usage: python profile.py <filename>")
        exit(1)
    else:
        filename = sys.argv[1]


    # Note Operational Intensity = Total Ops / Total External Memory Accesses
    

