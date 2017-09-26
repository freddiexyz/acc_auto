css_selectors = {
    'vendor_id'             : '#vendorId',
    'contract_number'       : '#contractNumber',
    'first_name'            : '#firstName',
    'last_name'             : '#surname',
    'date_birth'            : '#DOB',
    'NHI'                   : '#NHI',
    'claim_number'          : '#claimNumber',
    'date_accident'         : '#DOA',
    'create_invoice'        : '#tertiary-nav > li:nth-child(1) > a',
    'service_line_n'        : '#header-container-{}', #str.format()
    'provider_id_n'         : '#providerId_{}', #str.format()
    'service_date_n'        : '#serviceDate_{}', #str.format()
    'service_code_n'        : '#serviceCodes_{}-code_0', #str.format()
    'service_fee_n'         : '#fee_{}', #str.format
    'facility_code_n'       : '#facilityCode_{}', #str.format()
    'service_comments_n'    : '#service_comments_{}', #str.format()
    'add_service_button'    : '#addserviceBtn',
    'hide_tab_n'            : '#header-container-{} > span.service-header-chevron.glyphicon.glyphicon-chevron-up', #str.fromat()
    'additional_comments'   : '#additionalComments',
    'submit_button'         : '#submit-button',
    'invoice_number'        : '#invoiceNumber',
    'based_on_n'            : '#serviceCodes_{}-feeBasedOn_0', #str.format()
    'units_n'               : '#serviceCodes_{}-feeBasedOn_0 > option:nth-child(4)',
    'units_entry_n'         : '#serviceCodes_{}-units_0', #str.format()
    'create_another_button' : '#create-invoice-btn',
    'download_pdf_button'   : '#pdf-btn'
    }

acc_addr = 'https://health.myacc.co.nz/portal/secure/ebusiness/invoicing'

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

set_claim_as_sent = """
UPDATE claim
SET ClaimStatus='S', ClaimNote = '{}'
WHERE ClaimNum = {}
"""
