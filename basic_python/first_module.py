print('Executed everytime')

def main():
    """
    User defined main function

    To execute this module directly
    """
    pass

if __name__ == '__main__':
    print('Executed directly')
    main()
else:
    print('Executed by import')

"""
Output:

In  [1]: python first_module.py
Out [1]: Executed everytime
         Exectued directly
"""
