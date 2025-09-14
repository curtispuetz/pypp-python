import os
import sys


def pypp_get_resource_dir() -> str:
    return os.path.join(sys.prefix, "..", "..", "resources")
