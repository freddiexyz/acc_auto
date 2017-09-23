import pymysql as sql

class SQLgetter:
	def __init__(self):
		self.opendental = sql.connect("db4free.net", "freddiexyz","hunter2", "acc_auto_test")
		self.od = self.opendental.cursor()

	def close_connection(self):
		self.opendental.close()

	def get_procs(self, patnum):
		# self.opendental = sql.connect("db4free.net", "freddiexyz","hunter2", "acc_auto_test")

		# self.od = opendental.cursor()

		query_patient_test = f"""SELECT fname, lname, dob, nhi, accidentnumner, accidentdate, provid FROM patient WHERE patnum = {patnum}"""
		query_procs_test = f"""SELECT serdate, sercode, serfee FROM proc WHERE patnum = {patnum}"""

		self.od.execute(query_patient_test)
		patient = self.od.fetchone()

		self.od.execute(query_procs_test)
		procs = self.od.fetchall()

		# opendental.close()

		return patient, procs


if __name__ == '__main__':
	for patnum in range(1,4):
		print(*get_procs(patnum), sep='\n')


















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