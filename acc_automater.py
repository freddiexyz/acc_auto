from mysql_link import SQLgetter
from acc_form_entry import FormEntry

def main():
    with SQLgetter() as opendental:
        claim = opendental.get_available()
        FormEntry(opendental.get_procs(claim))
        input('...')

if __name__ == '__main__':
    main()
