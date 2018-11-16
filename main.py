import os
import numpy as np
import argparse

def main(args):


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', type=str, default='../AllAssignments',required=True)
    parser.add_argument('-n', '--num_GTA', type=int, default=4, required=True)
    parser.add_argument('--cross_checking', type=bool, default=True, required=True)
    parser.add_argument('--split_evenly', type=bool, default=True, help='Split the courseworks evenly across all n GTAs. Default is True. If false, please enter field "split_proportion".')     
    parser.add_argument('--split_proportion', type=float, nargs='+', default=None, help='Proportion of splitting work among n GTAs. Leave as none if argument "--split_evenly  True".')        
    parser.add_argument('--GTA_names', type=str, nargs='+', default=[], help='Names of GTAs in str arr form. Length of string array should be equal to num_GTA. If not provided ["1"... "n"] would be automatically assigned',required=False)
    parser.add_argument('--pdf_only', type=bool, default=True, help='Toggle if file loader only reads files ending with .pdf')
    parser.add_argument('-- ')
    parser.add_argument('-- ')

    args = parser.parse_args()
    main(args)