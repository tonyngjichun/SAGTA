import os
import numpy as np
import argparse

def main(config):


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', type=str, default='../AllAssignments',required=True)
    parser.add_argument('--num_GTA', type=int, default=4, required=True)
    parser.add_argument('--cross_checking', type=bool, default=True, required=True)
    parser.add_argument('--split_evenly', type=bool, default=True, help='Split the courseworks evenly across all n = num_GTA GTAs. Default is True. If false, please enter field "split_proportion".')     
    parser.add_argument('--split_proportion', type=, default=None, help='Proportion of splitting work among n = num_GTAs. Leave as none if argument "--split_evenly  True".')        
    parser.add_argument('-- ')
    parser.add_argument('-- ')
    parser.add_argument('-- ')
    parser.add_argument('-- ')

    config = parser.parse_args()
    main(config)