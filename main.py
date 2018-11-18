import numpy as np
import argparse
from file_allocator import allocate
import file_mkdir_cper

def main(args):
    gtaDict = allocate(args)
    file_mkdir_cper.writeTxt(gtaDict, args.save_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', type=str, default='./test')
    parser.add_argument('-n', '--num_GTA', type=int, default=4)
    parser.add_argument('--cross_checking', type=bool, default=True)
    parser.add_argument('--split_evenly', type=bool, default=True, help='Split the courseworks evenly across all n GTAs. Default is True. If false, please enter field "split_proportion".')     
    parser.add_argument('--split_proportion', type=float, nargs='+', default=None, help='Proportion of splitting work among n GTAs. Leave as none if argument "--split_evenly  True".')        
    parser.add_argument('--GTA_names', type=str, nargs='+', default=['DA','MK','MJ','TN'], help='Names of GTAs in str arr form. Length of string array should be equal to num_GTA.\
                        If len(GTA_names) < n, integers starting from 1 would be automatically assigned. If len(GTA_names) > n, only the first n name would be assigned.')
    parser.add_argument('--pdf_only', action='store_true', default=False, help='Toggle if file loader only reads files ending with .pdf')
    parser.add_argument('--save_path', type=str, default='./example')
    args = parser.parse_args()

    # Trim or fill attribute: num_GTA list to match num_GTA
    if args.num_GTA > len(args.GTA_names):
        for i in range(0, args.num_GTA - len(args.GTA_names)):
            args.GTA_names.append(i+1)
    elif args.num_GTA < len(args.GTA_names):
        for j in range(len(args.GTA_names) - args.num_GTA):
            del args.GTA_names[-1]

    main(args)