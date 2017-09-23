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
        dob_split = dateBirth.split('-')
        self.birth_date = '{}/{}/{}'.format(dob_split[2],dob_split[1],dob_split[0])
        self.NHI = NHI
        self.accident_number = accidentNumber
        doa_split = dateAccident.split('-')
        self.accident_date = '{}/{}/{}'.format(doa_split[2],doa_split[1],doa_split[0])
        self.provider_id = provId
        
        self.services = [{key : value
                          for (key, value)
                          in zip(['service_date',
                                  'service_code',
                                  'service_fee'], service)} for service in claim]

    @classmethod
    def fromMySQL(cls, patient):
        return cls(*patient[0],*patient[1])

    def __iter__(self):
        return (i for i in [self.vendor_id,
                self.contract_number,
                self.first_name,
                self.last_name,
                self.birth_date,
                self.NHI,
                self.accident_number,
                self.accident_date])
    
    def __next__(self):
        for i in self:
            return i

    def __repr__(self):
        return '{}'.format(self.__dict__)
    
    
    # def __str__(self):
    #     return 'hi'    
    

# test_entry = PatientEntry('Shylah', 'Adams', '03/06/2007', '', 'YD57518', '13/09/2017', '12BCJW', ['13/09/2017', 'DY1', '68.68'], ['13/09/2017', 'DX1', '26.37'], ['13/09/2017', 'DX4', '10.41']) 
    

