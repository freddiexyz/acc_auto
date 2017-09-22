from acc_auto_class import PatientEntry
from auto_variables import css_selectors
from auto_variables import acc_addr
from mysql_link import get_procs
from selenium import webdriver
from selenium import common
import logging as lg

auto_gen_warning = "This form has been filled out automatically and is still in testing!\nDO NOT SUBMIT"

def make_test_patient():
    return PatientEntry('Shylah', 'Adams', '03/06/2007', '', 'YD57518', '13/09/2017', '12BCJW',
	['13/09/2017', 'DY1', '68.68'], ['13/09/2017', 'DX1', '26.37'], ['13/09/2017', 'DX4', '10.41']) 


def chrome_setup():
    """Initialises chrome webdriver api --> webdriver object"""
    chrome = webdriver.Chrome('./chromedriver.exe')
    chrome.maximize_window()
    chrome.get(acc_addr)
    
    return chrome


def css_click(chrome, selector, *formatting):
    """Wrapper that finds an element by css selector and clicks on it, with optional formatting"""
    chrome.find_element_by_css_selector(css_selectors[selector].format(*formatting)).click()


def css_enter(chrome, selector, entry, *formatting):
    """Wrapper that finds an element by css selector and enters given text, with optional formatting"""
    chrome.find_element_by_css_selector(css_selectors[selector].format(*formatting)).send_keys(entry)


def enter_data(patient, chrome):
    """Fills in fields of claim form with attributes of instance of PatientEntry class"""    
    css_click(chrome, 'create_invoice')

    for key, attr in zip(list(css_selectors.keys())[:8], patient):#dictionaries are ordered in python3
        css_enter(chrome, key, attr)
    
    for service in patient.services:
        css_enter(chrome, 'provider_id_n',  patient.provider_id)
        
        css_enter(chrome, 'service_date_n', service['service_date'], patient.services.index(service))
        css_enter(chrome, 'service_code_n', service['service_code'], patient.services.index(service))
        css_enter(chrome, 'service_fee_n' , service['service_fee' ], patient.services.index(service))
        
        if (patient.services.index(service) < len(patient.services) - 1):
            css_click(chrome, 'add_service_button')
        else:
            css_click(chrome, 'hide_tab_n', patient.services.index(service))
    
    css_enter(chrome, 'additional_comments', auto_gen_warning)

    input('...')
    chrome.quit()


def main():
#     lg.basicConfig(level    =lg.INFO,
#                    style    ='{',
#                    format   ='{message}'
#                    )
#     # patient = make_test_patient()
#     # enter_data(patient, chrome_setup())
    pass


if __name__ == '__main__':
    main()
    
