import unittest
from acc_auto_class import PatientEntry
from auto_variables import css_selectors
from auto_variables import acc_addr
from mysql_link import SQLgetter

auto_gen_warning = "This form has been filled out automatically and is still in testing!\nDO NOT SUBMIT"

def css_click(selector):
    return ('{} <click>'.format(selector))
    

def css_enter(selector, entry, *formatting):
    if formatting:
        return ('{} {} {}'.format(selector, entry, *formatting))
    return ('{} {}'.format(selector, entry))


def enter_data2(patient):
    out = []
    out.append(css_click('create_invoice'))
    
    for key, attr in zip(list(css_selectors.keys())[:8], patient): #dictionaries are ordered in python3
        out.append(css_enter(key, attr))
   
    for service in patient.services:
        out.append(css_enter('provider_id_n',  patient.provider_id))
        out.append(css_enter('service_date_n', service['service_date']))#, patient.services.index(service)))
        out.append(css_enter('service_code_n', service['service_code']))#, patient.services.index(service)))
        out.append(css_enter('service_fee_n' , service['service_fee' ]))#, patient.services.index(service)))
        
        if (patient.services.index(service) < len(patient.services) - 1):
            out.append(css_click('add_service_button'))
        else:
            out.append(css_click('hide_tab_n'))
    
    out.append(css_enter('additional_comments', auto_gen_warning))
    # print(out)
    return out


def fromMySQL(patient):
        return enter_data2(PatientEntry.fromMySQL(patient))


class TesterClass(unittest.TestCase):
    def setUp(self):
        self.test_patient1 = PatientEntry('Shylah',  'Adams', '03/06/2007', 'ABC1235', 'YD57518', '13/09/2017', '12BCJW', ['13/09/2017', 'DY1', '68.68'], ['13/09/2017', 'DX1', '26.37'], ['13/09/2017', 'DX4', '10.41'])
        self.test_patient2 = PatientEntry('Freddie', 'Lee',   '28/04/1993', 'ABC1235', 'YD11111', '04/07/2011', '19BAGH', ['05/07/2011', 'DY1', '68.68'], ['05/07/2011', 'DX1', '26.37'])
        self.test_patient3 = PatientEntry('Sam',     'Lee',   '29/08/1995', 'ABC1235', 'YD22222', '04/07/2011', '19BAGH', ['05/07/2011', 'DY1', '68.68'])   

        self.opendental = SQLgetter()
        self.gen1 = PatientEntry.fromMySQL(self.opendental.get_procs(1))
        self.gen2 = PatientEntry.fromMySQL(self.opendental.get_procs(2))
        self.gen3 = PatientEntry.fromMySQL(self.opendental.get_procs(3))

    def tearDown(self):
        self.opendental.close_connection()
 

    def test_gen_1(self):
        self.assertEqual(self.test_patient1.__repr__(), self.gen1.__repr__())   

    def test_gen_2(self):
        self.assertEqual(self.test_patient2.__repr__(), self.gen2.__repr__())   

    def test_gen_3(self):
        self.assertEqual(self.test_patient3.__repr__(), self.gen3.__repr__())   



if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)




















# def test_services_1(self):
#     for item, item2 in zip(self.test_patient1.services, PatientEntry.fromMySQL(self.gen1).services):
#         self.assertEqual(item, item2)

# def test_services_2(self):
#     for item, item2 in zip(self.test_patient2.services, PatientEntry.fromMySQL(self.gen2).services):
#         self.assertEqual(item, item2)

# def test_services_3(self):
#     for item, item2 in zip(self.test_patient3.services, PatientEntry.fromMySQL(self.gen3).services):
#         self.assertEqual(item, item2)
# self.test_gen1 = PatientEntry.fromMySQL(gen1)
# self.test_gen2 = PatientEntry.fromMySQL(gen2)
# self.test_gen3 = PatientEntry.fromMySQL(gen3)
# def css_enter(selector, entry, formatting='None'):
#     return ('{} {} {}'.format(selector, entry, formatting))

# def enter_data(patient):
#     out = []
#     out.append(css_click('create_invoice'))
    
#     out.append(css_enter('vendor_id',       patient.vendor_id))
#     out.append(css_enter('contract_number', patient.contract_number))
#     out.append(css_enter('first_name',      patient.first_name))
#     out.append(css_enter('last_name',       patient.last_name))
#     out.append(css_enter('date_birth',      patient.birth_date))
#     out.append(css_enter('NHI',             patient.NHI))
#     out.append(css_enter('claim_number',    patient.accident_number))
#     out.append(css_enter('date_accident',   patient.accident_date))
    
#     for service in patient.services:
#         out.append(css_enter( 'provider_id_n',  patient.provider_id))
#         out.append(css_enter( 'service_date_n', service['service_date'], patient.services.index(service)))
#         out.append(css_enter( 'service_code_n', service['service_code'], patient.services.index(service)))
#         out.append(css_enter( 'service_fee_n' , service['service_fee' ], patient.services.index(service)))
        
#         if (patient.services.index(service) < len(patient.services) - 1):
#             out.append(css_click( 'add_service_button'))
#         else:
#             out.append(css_click( 'hide_tab_n', patient.services.index(service)))
    
#     out.append(css_enter( 'additional_comments', auto_gen_warning))
#     # print(out)
#     return out

# def css_click(selector, formatting=None):
#     return('{} {}'.fomrat(selector, formatting))
# def test_patient_1(self):
#     self.assertEqual(enter_data(self.test_patient1),enter_data2(self.test_patient1))

# def test_patient_2(self):
#     self.assertEqual(enter_data(self.test_patient2),enter_data2(self.test_patient2))

# def test_patient_3(self):
#     self.assertEqual(enter_data(self.test_patient3),enter_data2(self.test_patient3))