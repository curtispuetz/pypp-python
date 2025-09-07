import os
import sys


def pypp_get_resources(relative_path: str) -> str:
    return os.path.join(sys.prefix, "..", "..", "resources", relative_path)
