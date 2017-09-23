import pymysql as sql

query_patient = """
select p.FName, p.LName, p.BirthDate, p.SSN, ins.subscriberid, c.AccidentDate, c.ProvTreat
from claim c inner join patient p on c.PatNum = p.PatNum inner join inssub ins on c.inssubnum = ins.inssubnum 
where c.ClaimNum = {}"""

query_procs = """
select pl.ProcDate, pc.ProcCode, pl.ProcFee
from claim c inner join claimproc cp on c.ClaimNum = cp.ClaimNum inner join procedurelog pl on cp.ProcNum = pl.ProcNum inner join procedurecode pc on pl.CodeNum = pc.CodeNum
where c.ClaimNum = {}
"""

query_available = """
SELECT c.ClaimNum, concat(p.FName, ' ', p.LName)
FROM claim c
INNER JOIN patient p on c.Patnum = p.patnum
WHERE ClaimStatus='W'
AND PlanNum=68
"""

class SQLgetter:
    def __init__(self):
        conv=sql.converters.conversions.copy()
        for i in range(246):
                conv[i]=str
        self.opendental = sql.connect("bsse12", "root","", "opendental", conv=conv)
        self.od = self.opendental.cursor()

    def close_connection(self):
        self.opendental.close()

    def get_available(self):
        self.od.execute(query_available)
        available_claims = self.od.fetchall()
        for claim in available_claims:
            print(f'[{available_claims.index(claim) + 1:02d}] - {claim[1]}')
        choice = int(input('>'))
        return available_claims[choice-1][0]

    def get_procs(self, claimnum):
        self.od.execute(query_patient.format(claimnum))
        patient = self.od.fetchone()

        self.od.execute(query_procs.format(claimnum))
        procs = self.od.fetchall()

        return patient, procs


if __name__ == '__main__':
    opendental = SQLgetter()
    print(*opendental.get_procs(32308), sep='\n')
    opendental.close_connection()




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
