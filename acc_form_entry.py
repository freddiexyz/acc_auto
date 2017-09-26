from auto_variables import css_selectors, acc_addr
from acc_auto_class import PatientEntry
from selenium import webdriver, common
from mysql_link import SQLgetter, query_patient, query_procs
from time import sleep

auto_gen_warning = "Please check info before submitting"

class FormEntry():
    providers = {'1' : '19BAGH', '2' : '12BCJW', '5' : '25CANA'}
    def __init__(self):
        self.chrome = self.chrome_setup()
        self.css_click('create_invoice')
    
    def __enter__(self):
        return self
    
    def __exit__(self,*exc):
        self.chrome.quit()

    
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
        patient = PatientEntry.fromMySQL(patient)
        
        for key, attr in zip(list(css_selectors.keys())[:8], patient):
            self.css_enter(key, attr)
        
        for index, service in enumerate(patient.services):
            self.css_enter('provider_id_n',  self.providers[patient.provider_id], index)
            #self.css_enter('service_date_n', service['service_date'], patient.services.index(service))
            dos_split = service['service_date'].split('-')
            self.css_enter('service_date_n', '{}/{}/{}'.format(dos_split[2], dos_split[1],dos_split[0]), index)
            self.css_enter('service_code_n', service['service_code'], index)
            self.css_enter('service_fee_n' , service['service_fee' ], index)
            self.css_click('based_on_n', index)
            self.css_click('units_n', index)
            self.css_enter('units_entry_n', '1', index)
            sleep(0.25)
            
            if (index < len(patient.services) - 1):
                self.css_click('add_service_button')
            else:
                self.css_click('hide_tab_n', index)
        
        invoice_number = self.chrome.find_element_by_css_selector('#invoiceNumber').get_attribute('value').upper()
        
        input('Continue?')
        
        self.css_click('submit_button')
        sleep(5)
        self.css_click('download_pdf_button')
        sleep(1)
        self.css_click('create_another_button')
        sleep(5)
        
        return invoice_number
        
        
