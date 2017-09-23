from mysql_link import SQLgetter, query_available
from acc_form_entry import FormEntry

def main():
    opendental = SQLgetter()
    claim = opendental.get_available()
    FormEntry(opendental.get_procs(claim))
    opendental.close_connection()

if __name__ == '__main__':
    main()
