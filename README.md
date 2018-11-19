# SAGTA - **S**pread **A**mong the **GTA**s

Imagine you are the GTA (Graduate Teaching Assistant) of a 3rd-year university course. Your supervisor is telling you to mark and give feedback to the courseworks. *`Nice, extra-bit of ££'* you think, until you see hundreds of courseworks submitted and you have absolutely no way of marking them by yourself. The only way-out is to ask for help from your fellow GTAs.

This is when SAGTA a.k.a. **S**pread **A**mong the **GTA**s comes into rescue. Simply get all the coursework files in a single directory and specify everything from the number of GTAs, names of them to the save path, SAGTA sorts it out for you and *voila*! Spreading workload among GTAs will never be a manual work again.

## Task List
- [x] Copying and distributing files automatically to target directory 
- [x] Regex matches that supports filtering out student IDs from raw-downloaded filenames (support for IC's BlackBoard Learn naming routines only)
- [x] Toggle for looking at pdf files only
- [] Uneven distribution of workload among several GTAs
- [] Automatic spreadsheet generation

## Install
No installation needed. Tested on:
* Python 3.7.0
* NumPy 1.15.1

## Run
Open terminal and type
```
python main.py -h
```
To see the details of each argument parsed. For example:
```
python main.py --file_path './test' -n 4 --GTA_names 'Homer' 'Simpson' 'Peter' 'Griffin' --save_path './example'
```
yields the results seen in the `example` folder. Inputting
```
python main.py --file_path './test' -n 4 --GTA_names 'Homer' 'Simpson' 'Peter' 'Griffin' --save_path './example' --pdf_only
```
yields empty folders and text files because the extra `--pdf_only` argument toggles the script to look at pdf files with file prefixes ending with `.pdf' only.