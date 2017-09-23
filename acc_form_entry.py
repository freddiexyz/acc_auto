from auto_variables import css_selectors, acc_addr
from acc_auto_class import PatientEntry
from selenium import webdriver, common
from mysql_link import SQLgetter, query_patient, query_procs
import logging as lg

auto_gen_warning = "This form has been filled out automatically and is still in testing!\nDO NOT SUBMIT"

class FormEntry():
    def __init__(self, *patients):
        self.providers = {'1' : '19BAGH', '2' : '12BCJW', '5' : '25CANA'}
        self.chrome = self.chrome_setup()
        for patient in patients:
            self.enter_data(PatientEntry.fromMySQL(patient))
            #handle completed entry or error
        #self.chrome.quit()

    
    def chrome_setup(self):
        """Initialises chrome webdriver api --> webdriver object"""
        chrome = webdriver.Chrome('./chromedriver.exe')
        chrome.maximize_window()
        chrome.get(acc_addr)

        return chrome


    def css_click(self, selector, *formatting):
        """Wrapper that finds an element by css selector and clicks on it, with optional formatting"""
        self.chrome.find_element_by_css_selector(css_selectors[selector].format(*formatting)).click()


    def css_enter(self, selector, entry, *formatting):
        """Wrapper that finds an element by css selector and enters given text, with optional formatting"""
        self.chrome.find_element_by_css_selector(css_selectors[selector].format(*formatting)).send_keys(entry)


    def enter_data(self, patient):
        """Fills in fields of claim form with attributes of instance of PatientEntry class"""    
        self.css_click('create_invoice')

        for key, attr in zip(list(css_selectors.keys())[:8], patient):
            self.css_enter(key, attr)
        
        for service in patient.services:
            self.css_enter('provider_id_n',  self.providers[patient.provider_id], patient.services.index(service))
            #self.css_enter('service_date_n', service['service_date'], patient.services.index(service))
            dos_split = service['service_date'].split('-')
            self.css_enter('service_date_n', '{}/{}/{}'.format(dos_split[2], dos_split[1],dos_split[0]), patient.services.index(service))
            self.css_enter('service_code_n', service['service_code'], patient.services.index(service))
            self.css_enter('service_fee_n' , service['service_fee' ], patient.services.index(service))
            
            if (patient.services.index(service) < len(patient.services) - 1):
                self.css_click('add_service_button')
            else:
                self.css_click('hide_tab_n', patient.services.index(service))
        
        self.css_enter('additional_comments', auto_gen_warning)


def main():
    lg.basicConfig(level    =lg.INFO,
                   style    ='{',
                   format   ='{message}')
    sql_getter = SQLgetter()
    patient = sql_getter.get_procs(32308)
    sql_getter.close_connection
    FormEntry(patient)


if __name__ == '__main__':
    main()
