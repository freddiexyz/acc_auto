from acc_auto_class import PatientEntry
from auto_variables import css_selectors
from auto_variables import acc_addr
from selenium import webdriver
from selenium import common
import logging as lg

auto_gen_warning = "This form has been filled out automatically and is still in testing!\nDO NOT SUBMIT"

def make_test_patient():
    return PatientEntry('Shylah', 'Adams', '03/06/2007', '', 'YD57518', '13/09/2017', '12BCJW', ['13/09/2017', 'DY1', '68.68'], ['13/09/2017', 'DX1', '26.37'], ['13/09/2017', 'DX4', '10.41']) 


def chrome_setup():
    """Initialises chrome webdriver api --> webdriver object"""
    chrome = webdriver.Chrome('./chromedriver.exe')
    chrome.maximize_window()
    chrome.get(acc_addr)
    
    return chrome


def css_click(chrome, selector):
    chrome.find_element_by_css_selector(css_selectors[selector]).click()


def css_enter(chrome, selector, entry, *formatting):
    chrome.find_element_by_css_selector(css_selectors[selector].format(*formatting)).send_keys(entry)


def enter_data(patient, chrome):
    """Fills in fields of claim form with attributes of
    instance of PatientEntry class"""
    chrome.find_element_by_css_selector(css_selectors['create_invoice']).click()
    chrome.find_element_by_css_selector(css_selectors['vendor_id']).send_keys(patient.vendor_id)
    chrome.find_element_by_css_selector(css_selectors['contract_number']).send_keys(patient.contract_number)
    chrome.find_element_by_css_selector(css_selectors['first_name']).send_keys(patient.first_name)
    chrome.find_element_by_css_selector(css_selectors['last_name']).send_keys(patient.last_name)
    chrome.find_element_by_css_selector(css_selectors['date_birth']).send_keys(patient.birth_date)
    chrome.find_element_by_css_selector(css_selectors['NHI']).send_keys(patient.NHI)
    chrome.find_element_by_css_selector(css_selectors['claim_number']).send_keys(patient.accident_number)
    chrome.find_element_by_css_selector(css_selectors['date_accident']).send_keys(patient.accident_date)

    for service in patient.services:
        chrome.find_element_by_css_selector(css_selectors['service_date_n'].format(patient.services.index(service))).send_keys(service['service_date'])
        chrome.find_element_by_css_selector(css_selectors['provider_id_n'].format(patient.services.index(service))).send_keys(patient.provider_id)
        chrome.find_element_by_css_selector(css_selectors['service_code_n'].format(patient.services.index(service))).send_keys(service['service_code'])
        chrome.find_element_by_css_selector(css_selectors['service_fee_n'].format(patient.services.index(service))).send_keys(service['service_fee'])
        if (patient.services.index(service) < len(patient.services) - 1):
            chrome.find_element_by_css_selector(css_selectors['add_service_button']).click()
        else:
            chrome.find_element_by_css_selector(css_selectors['hide_tab_n'].format(patient.services.index(service))).click()

    chrome.find_element_by_css_selector(css_selectors['additional_comments']).send_keys(auto_gen_warning)

    input('...')
    chrome.quit()
                                                 
    
    


def main():
    lg.basicConfig(level    =lg.INFO,
                   style    ='{',
                   format   ='{message}'
                   )
    patient = make_test_patient()
    enter_data(patient, chrome_setup())


if __name__ == '__main__':
    main()
    
