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
