import MySQLdb as sql

#made query work
patnum = 1
query_patient = f"""SELECT p.firstname, p.lastname, p.dob, p.ssn, ins.inssubnum, ins.doa
FROM patient p
INNER JOIN insuranceprovider ins on p.patnum = ins.patnum
where p.patnum = {patnum}
"""
query_procs = f"""SELECT pl.providerid, pl.procdate, pc.descript, pl.procfee, pl.patnum
FROM claim c
INNER JOIN claimproc cp on c.claimnum = cp.claimnum
INNER JOIN procedurelog pl on cp.procnum = pl.procnum
INNER JOIN procedurecode pc on pl.proccode = pc.procode
WHERE c.patnum = {patnum}
"""

#firstName, lastName, dateBirth, NHI, accidentNumber, dateAccident
opendental = sql.connect("bsse12", "root","", "opendental")

od = opendental.cursor()

od.execute(query_patient)

patient = od.fetchone()

od.execute(query_procs)

procs = od.fetchall()
