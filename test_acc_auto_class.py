import unittest
from acc_auto_class import *

def setUp():
    pritn('hello')
    #test_patient = PatientEntry('Freddie', 'Lee', '28/04/1993', None, 'YD111111', '4/7/11', ['5/7/11', 'DY1', 10], ['6/7/11', 'DEXT1', 20])
    
class TestPatientEntry(unittest.TestCase):
    acc_vendor_id = 'vendorId'
    acc_agreement_number = 'agreementNumber'
    
    def setUp(self):
        self.test_patient1 = PatientEntry('Freddie', 'Lee', '28/04/1993', None, 'YD111111', '4/7/11', ['5/7/11', 'DY1', 10], ['6/7/11', 'DEXT1', 20])
        self.test_patient2 = PatientEntry('Sam', 'Lee', '29/08/1995', None, 'YD222222', '4/7/11', ['5/7/11', 'DY1', 10])   
    
    
    def test_1(self):
        self.assertEqual(len(self.test_patient1.services), 2)
        self.assertEqual(len(self.test_patient2.services), 1)
    
    def test_2(self):
        self.assertEqual(self.test_patient1.services[0]['service_fee'], 10)
        self.assertEqual(self.test_patient2.services[0]['service_code'], 'DY1')
        


        
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=0)