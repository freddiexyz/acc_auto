from auto_variables import css_selectors, acc_addr
from acc_auto_class import PatientEntry
from selenium import webdriver, common
from mysql_link import get_procs
import logging as lg

auto_gen_warning = "This form has been filled out automatically and is still in testing!\nDO NOT SUBMIT"

class FormEntry():
    def __init__(self, *patients):
        self.chrome = chrome_setup()
        for patient in patients:
            self.enter_data(PatientEntry.fromMySQL(patient))
            #handle completed entry or error
        self.chrome.quit()

    @classmethod
    def chrome_setup():
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
            self.css_enter('provider_id_n',  patient.provider_id)
            self.css_enter('service_date_n', service['service_date'], patient.services.index(service))
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
    #FormEntry(get_procs()) <-- make this work
    pass

if __name__ == '__main__':
    main()