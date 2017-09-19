#acc_auto_class.py
#class for moving data inbetween database and web form

class PatientEntry:
    '''Class that holds all data relevant to ACC web form'''
    vendor_id = 'G01937'
    contract_number = '82'
    
    def __init__(self, firstName, lastName, dateBirth,
                 NHI, accidentNumber, dateAccident, provId, *claim):
        self.first_name = firstName
        self.last_name = lastName
        self.birth_date = dateBirth
        self.NHI = NHI
        self.accident_number = accidentNumber
        self.accident_date = dateAccident
        self.provider_id = provId
        
        self.services = [{key : value
                          for (key, value)
                          in zip(['service_date',
                                  'service_code',
                                  'service_fee'], service)} for service in claim]
    
"""    
    def __repr__(self):
        return '{}({})'.format(self.__class__, self.__dict__)
    
    
    def __str__(self):
        return 'hi
"""        
        
