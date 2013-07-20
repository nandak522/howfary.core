import argparse
from .query import compute_howfar

def howfar():
    parser = argparse.ArgumentParser(description='Core Library for Distance Calculator')
    parser.add_argument('source', type=str, help='Source Place')
    parser.add_argument('destination', type=str, help='Destination Place')
    args = parser.parse_args()
    return compute_howfar(**(args.__dict__))
