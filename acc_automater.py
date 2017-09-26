from mysql_link import SQLgetter
from acc_form_entry import FormEntry

def main():
    with SQLgetter(), FormEntry() as opendental, webdriver:
        while opendental.get_available():
            opendental.submit_claim(webdriver.enter_data(opendental.get_procs()))
            

if __name__ == '__main__':
    main()
