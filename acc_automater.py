from mysql_link import SQLgetter
from acc_form_entry import FormEntry

def main():
    with SQLgetter() as opendental, FormEntry() as webdriver:
        try:
            while opendental.get_available():
                opendental.submit_claim(webdriver.enter_data(opendental.get_procs()))
        except KeyboardInterrupt:
            pass
            

if __name__ == '__main__':
    main()
