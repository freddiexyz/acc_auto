from mysql_link import SQLgetter
from acc_form_entry import FormEntry, css_selectors

def main():
    with SQLgetter() as opendental:
    	another = True
    	while another:
    		form = FormEntry(opendental.main())
    		input('Press enter to submit...')
    		form.css_click('submit_button' )
    		opendental.submit_claim(css_selectors[<invoice_reference>].text)
    		another = 'n' not in input('Enter another? [Y/N]: ').strip().lower()

    	
if __name__ == '__main__':
    main()
