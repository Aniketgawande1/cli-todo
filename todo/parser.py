import sys

def parse_args():
    if len(sys.argv) < 2:
        return None, []
    return sys.argv[1], sys.argv[2:]
