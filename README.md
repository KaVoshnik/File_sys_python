# File_sys_python
1. Function:
- sort_data_by_type: Read data and check type (Int, float or str) and write in output files.

2. Code:
- Create parser with help argparse.
- User can use Flags:
-o (Path the save result)
-p (Name output files).
- Call the func sort_data_by_type, give a file and flags result.

3. Function sort_data_by_type:
- Open "input file" and create output files.
- Read all lines from file.
- Try to convert int(). If convert, write to Integer output file.
- If not convert, try convert to float(). If convert, write to Float output file.
- If not convert, write to String output file.
- Close all files.

# For run code use
python Main.py input_file.txt
- Can add flags:
-p Name_file
-o Path_to_save
