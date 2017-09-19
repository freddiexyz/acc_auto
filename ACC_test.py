vendor_id = 'G01937'
contract_number = '60 883 068'
facility_code = None

class TestData:
    def __init__(self):
        self.fname = 'Reeve'
        self.lname = 'Williams'
        self.dob = '01/05/2004' #date of birth
        self.nhi = None

        self.claim_num = 'YD77586'
        self.doa = '15/06/2015' #date of accident
        self.prov_id = '19BAGH'
        self.services = []

test_1 = TestData()

class TestService(TestData):
    def __init__(self):
        self.prov_id = ''
        
test_1.services.append(TestService())
test_1.services[0].service_code = 'DY1'
test_1.services[0].dos = '14/09/2017' #date of service
test_1.services[0].fee = 68.68
test_1.services[0].prov_id = test_1.prov_id
