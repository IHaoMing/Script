#file_io.py

import os

def wirte_file(file_name):
    """
    :type flie_name: str
    """
    with open(file_name, "a") as f:
        f.write('---\ntitle: \ndate:')
        f.close

def main():
    wirte_file('test.md')

if __name__ == '__main__':
    main()