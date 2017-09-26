from auto_variables import query_patient, query_procs, query_available, set_claim_as_sent
import pymysql

class SQLgetter:
    def __init__(self):
        conv=pymysql.converters.conversions.copy()
        for i in range(246):
                conv[i]=str
        self.conn = pymysql.connect("bsse12", "root","", "opendental", conv=conv)
        self.curs = self.conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.conn.commit()
        self.conn.close()

    def get_available(self):
        self.curs.execute(query_available)
        available_claims = self.curs.fetchall()
        for claim in available_claims:
            print(f'[{available_claims.index(claim) + 1:02d}] - {claim[1]}')
        self.claimnum = available_claims[int(input('>'))-1][0]
        return self.claimnum

    def get_procs(self):
        self.curs.execute(query_patient.format(self.claimnum))
        patient = self.curs.fetchone()
        self.curs.execute(query_procs.format(self.claimnum))
        procs = self.curs.fetchall()
        return patient, procs

    def submit_claim(self, invoice_reference):
        self.curs.execute(set_claim_as_sent.format(invoice_reference, self.claimnum))

    def main(self):
        return self.get_procs(self.get_available())


























# if __name__ == '__main__':
#     opendental = SQLgetter()
#     print(*opendental.get_procs(32308), sep='\n')
#     opendental.close_connection()
#self.opendental = sql.connect("db4free.net", "freddiexyz","hunter2", "acc_auto_test")
#opendental.close()
#query_patient_test = f"""SELECT fname, lname, dob, nhi, accidentnumner, accidentdate, provid FROM patient WHERE patnum = {patnum}"""
#query_procs_test = f"""SELECT serdate, sercode, serfee FROM proc WHERE patnum = {patnum}"""
# opendental = sql.connect("db4free.net", "freddiexyz","hunter2", "acc_auto_test")
# od = opendental.cursor()
# od.execute("update patient set provid = '12BCJW' where patnum = 1")
# opendental.commit()
# opendental.close()

# query_patient = f"""SELECT p.firstname, p.lastname, p.dob, p.ssn, ins.inssubnum, ins.doa
# FROM patient p
# INNER JOIN insuranceprovider ins on p.patnum = ins.patnum
# where p.patnum = {patnum}
# """

# query_procs = f"""SELECT pl.providerid, pl.procdate, pc.descript, pl.procfee, pl.patnum
# FROM claim c
# INNER JOIN claimproc cp on c.claimnum = cp.claimnum
# INNER JOIN procedurelog pl on cp.procnum = pl.procnum
# INNER JOIN procedurecode pc on pl.proccode = pc.procode
# WHERE c.patnum = {patnum}
# """
