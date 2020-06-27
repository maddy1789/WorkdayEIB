from .master import OBJECT

__SUPERVISORY={
    "Key": {"eib": "Spreadsheet Key*_1", "template": "", "type": "key"},
    "EffectiveDate": {"eib": "Effective Date_2", "template": "", "type": "edate"},
    "Id": {"eib": "Organization Reference ID_3", "template": "", "type": "id"},
    "Organization": {"eib": "Organization Name_7", "template": "Organization Name", "type": "template"},
    "Availability": {"eib": "Availability Date_8", "template": "", "type": "edate"},
    "OrgCode": {"eib": "Organization Code_10", "template": "", "type": "id"},
    "Position": {"eib": "Position Management Enabled_14", "template": "Position Management", "type": "template"},
    "Superior": {"eib": "Superior Organization_15", "template": "Superior Organization", "master": OBJECT.SUPERVISORY, "type": "master"},
    "OrgType": {"eib": "Organization Type Name*_16", "template": "Supervisory", "type": "data"},
    "OrgSub": {"eib": "Organization Subtype Name*_17", "template": "Department", "type": "data"},
    "Visible": {"eib": "Organization Visibility Name*_18", "template": "Everyone", "type": "data"},
    "Location": {"eib": "Primary Business Site_19", "template": "Location", "master": OBJECT.LOCATION, "type": "master"}
}

__POSITION={
    "Key": {"eib": "Spreadsheet Key*_1", "type": "key", "template": "", "master": ""},
    "Supervisory": {"eib": "Supervisory Organization*_2", "type": "master", "template": "Organization", "master": OBJECT.SUPERVISORY},
    "Id": {"eib": "Position ID_4", "type": "id", "template": "", "master": ""},
    "Position": {"eib": "Job Posting Title_5", "type": "template", "template": "Position Title", "master": ""},
    "Avaialability": {"eib": "Availability Date_57", "type": "template", "template": "Continous Service Date", "master": ""},
    "Earliest": {"eib": "Earliest Hire Date_58", "type": "template", "template": "Continous Service Date", "master": ""},
    "Profile": {"eib": "Job Profile+_60", "type": "master", "template": "Position Title", "master": OBJECT.JOB_PROFILE},
    "Location": {"eib": "Location+_61", "type": "master", "template": "Location", "master": OBJECT.LOCATION},
    "Worker": {"eib": "Worker Type_62", "type": "data", "template": "EE", "master": ""},
    "Time": {"eib": "Time Type_63", "type": "data", "template": "Full_time", "master": ""},
    "WType": {"eib": "Position Worker Type+_64", "type": "master", "template": "Employee Type", "master": OBJECT.EMP_TYPE}
}

__ORGANIZATION = {
    "Key": {"eib": "Spreadsheet Key_1", "type": "key", "template": "", "master": ""},
    "Company": {"eib": "Company Assignments+_2", "type": "master", "template": "Company Assignments+", "master": OBJECT.COMPANY},
    "CostCenter": {"eib": "Cost Center Assignments+_3", "type": "master", "template": "Cost Center Assignments+", "master": OBJECT.COSTCENTER}
}

__PAY_GROUP = {
    "Key": {"eib": "Spreadsheet Key_1", "type": "key", "template": "", "master": ""},
    "Pay": {"eib": "Pay Group*_2", "type": "master", "template": "Pay Group", "master": OBJECT.PAYGROUP},
    "Pay1": {"eib": "Pay Group_2", "type": "master", "template": "Pay Group", "master": OBJECT.PAYGROUP}
}

__HIRE = {
    "Key": {"eib": "Spreadsheet Key*_1", "template": "", "type": "key", "master": ""},
    "Country": {"eib": "Country*_10", "template": "Country of Birth", "type": "master", "master": OBJECT.COUNTRY},
    "Title": {"eib": "Title_11", "template": "Title", "type": "master", "master": OBJECT.TITLE},
    "Fname": {"eib": "First Name_14", "template": "First Name", "type": "template", "master": ""},
    "Mname": {"eib": "Middle Name_15", "template": "Middle Name", "type": "template", "master": ""},
    "Lname": {"eib": "Last Name_16", "template": "Last Name", "type": "template", "master": ""},
    "Gender": {"eib": "Gender_100", "template": "Gender", "type": "master", "master": OBJECT.GENDER},
    "DOB": {"eib": "Birth Date_101", "template": "Birth Date", "type": "template", "master": ""},
    "BirthCountry": {"eib": "Country of Birth_103", "template": "Country of Birth", "type": "master", "master": OBJECT.COUNTRY},
    "BirthRegion": {"eib": "Region of Birth_104", "template": "Region of Birth", "type": "master", "master": OBJECT.STATE},
    "BirthCity": {"eib": "City of Birth_106", "template": "City of Birth", "type": "template", "master": ""},
    "BirthRegCode": {"eib": "ISO 3166 1 Alpha 2 Code_108", "template": "Region of Birth", "type": "master", "master": OBJECT.STATE},
    "Marital": {"eib": "Marital Status_109", "template": "Marital Status", "type": "master", "master": OBJECT.MARITAL},
    "Religion": {"eib": "Religion_112", "template": "Religion", "type": "master", "master": OBJECT.RELIGION},
    "Citizenship": {"eib": "Citizenship Status+_138", "template": "Citizenship Status", "type": "master", "master": OBJECT.CITIZEN},
    "Nationality": {"eib": "Primary Nationality_139", "template": "Primary Nationality", "type": "master", "master": OBJECT.COUNTRY},
    "Blood": {"eib": "Blood Type_153", "template": "Blood Type", "type": "master", "master": OBJECT.BLOOD},
    "Row_1": {"eib": "Row ID*_162", "template": "1", "type": "data", "master": ""},
"Row_1_1": {"eib": "Row ID*.3_162", "template": "1", "type": "data", "master": ""},
    "ID_1": {"eib": "ID_165", "template": "ID", "type": "template", "master": ""},
    "IDType": {"eib": "ID Type_166", "template": "ID Type", "type": "master", "master": OBJECT.NATIONAL_ID},
    "IDCountry": {"eib": "Country_167", "template": "Country", "type": "master", "master": OBJECT.COUNTRY},
    "Row_2": {"eib": "Row ID*_223", "template": "1", "type": "data", "master": ""},
"Row_2_1": {"eib": "Row ID*.8_223", "template": "1", "type": "data", "master": ""},
    "PID": {"eib": "ID_226", "template": "ID*", "type": "template", "master": ""},
"PID1": {"eib": "ID.5_226", "template": "ID*", "type": "template", "master": ""},
    "Payroll": {"eib": "ID Type_227", "template": "ID Type*", "type": "template", "master": ""},
"Payroll1": {"eib": "ID Type.5_227", "template": "ID Type*", "type": "template", "master": ""},
    "Row_3": {"eib": "Row ID*_242", "template": "1", "type": "data", "master": ""},
"Row_3_1": {"eib": "Row ID*.10_242", "template": "1", "type": "data", "master": ""},
    "AddType": {"eib": "Type_244", "template": "ADDRESS_LINE_1", "type": "data", "master": ""},
    "Address": {"eib": "Address Line Data_245", "template": "Address", "type": "template", "master": ""},
    "Municipality": {"eib": "Municipality_246", "template": "Municipality", "type": "template", "master": ""},
    "Street": {"eib": "ISO 3166 1 Alpha 2 Code_248", "template": "State", "type": "master", "master": OBJECT.STATE},
"Street1": {"eib": "ISO 3166 1 Alpha 2 Code.1_248", "template": "State", "type": "master", "master": OBJECT.STATE},
    "Postal": {"eib": "Postal Code_259", "template": "Postal Code", "type": "template", "master": ""},
    "Row_4": {"eib": "Row ID*_260", "template": "1", "type": "data", "master": ""},
"Row_4_1": {"eib": "Row ID*.13_260", "template": "1", "type": "data", "master": ""},
    "AddPublic": {"eib": "Public_261", "template": "Public", "type": "template", "master": ""},
    "Row_5": {"eib": "Row ID**_262", "template": "1", "type": "data", "master": ""},
    "AddPrimary": {"eib": "Primary_263", "template": "Primary", "type": "template", "master": ""},
    "AddType1": {"eib": "Type*_264", "template": "Type", "type": "template", "master": ""},
    "Row_6": {"eib": "Row ID*_272", "template": "1", "type": "data", "master": ""},
"Row_6_1": {"eib": "Row ID*.14_272", "template": "1", "type": "data", "master": ""},
    "PhoneCode": {"eib": "International Phone Code_283", "template": "Phone Code", "type": "template", "master": ""},
    "PhoneNo": {"eib": "Phone Number_284", "template": "Phone Number", "type": "template", "master": ""},
    "PhoneDevice": {"eib": "Phone Device Type_286", "template": "Phone Device Type", "type": "template", "master": ""},
    "Row_7": {"eib": "Row ID*_287", "template": "1", "type": "data", "master": ""},
"Row_7_1": {"eib": "Row ID*.15_287", "template": "1", "type": "data", "master": ""},
    "PhonePublic": {"eib": "Public_288", "template": "Public*", "type": "template", "master": ""},
"PhonePublic_1": {"eib": "Public.1_288", "template": "Public*", "type": "template", "master": ""},
    "Row_8": {"eib": "Row ID**_289", "template": "1", "type": "data", "master": ""},
"Row_8_1": {"eib": "Row ID**.1_289", "template": "1", "type": "data", "master": ""},
    "PhonePrimary": {"eib": "Primary_290", "template": "Primary*", "type": "template", "master": ""},
"PhonePrimary_1": {"eib": "Primary.1_290", "template": "Primary*", "type": "template", "master": ""},
    "PhoneType": {"eib": "Type*_291", "template": "Type*", "type": "template", "master": ""},
"PhoneType_1": {"eib": "Type*.1_291", "template": "Type*", "type": "template", "master": ""},
    "Row_9": {"eib": "Row ID*_297", "template": "1", "type": "data", "master": ""},
"Row_9_1": {"eib": "Row ID*.16_297", "template": "1", "type": "data", "master": ""},
    "Email": {"eib": "Email Address_300", "template": "Email Address", "type": "template", "master": ""},
    "Row_10": {"eib": "Row ID*_302", "template": "1", "type": "data", "master": ""},
"Row_10_1": {"eib": "Row ID*.17_302", "template": "1", "type": "data", "master": ""},
    "EmailPublic": {"eib": "Public_303", "template": "Public**", "type": "template", "master": ""},
"EmailPublic_1": {"eib": "Public.2_303", "template": "Public**", "type": "template", "master": ""},
    "Row_11": {"eib": "Row ID**_304", "template": "1", "type": "data", "master": ""},
"Row_11_1": {"eib": "Row ID**.2_304", "template": "1", "type": "data", "master": ""},
    "EmailPrimary": {"eib": "Primary_305", "template": "Primary**", "type": "template", "master": ""},
"EmailPrimary_1": {"eib": "Primary.2_305", "template": "Primary**", "type": "template", "master": ""},
    "EmailType": {"eib": "Type*_306", "template": "Type**", "type": "template", "master": ""},
"EmailType_1": {"eib": "Type*.2_306", "template": "Type**", "type": "template", "master": ""},
    "Organization": {"eib": "Organization_383", "template": "Organization", "type": "master", "master": OBJECT.SUPERVISORY},
    "PositionTitle": {"eib": "Position_384", "template": "Position Title", "type": "template", "master": ""},
    "HireDate": {"eib": "Hire Date_386", "template": "Hire Date", "type": "template", "master": ""},
    "EmpType": {"eib": "Employee Type_390", "template": "Employee Type", "type": "master", "master": OBJECT.EMP_TYPE},
    "Continuous": {"eib": "Continuous Service Date_393", "template": "Continous Service Date", "type": "template", "master": ""},
    "ProbationStart": {"eib": "Probation Start Date_394", "template": "Probation Start Date", "type": "template", "master": ""},
    "ProbationEnd": {"eib": "Probation End Date_395", "template": "Probation End Date", "type": "template", "master": ""},
    "Job": {"eib": "Job Profile_400", "template": "Position Title", "type": "master", "master": OBJECT.JOB_PROFILE},
    "Position": {"eib": "Position Title_401", "template": "Position Title", "type": "template", "master": ""},
    "Business": {"eib": "Business Title_402", "template": "Position Title", "type": "template", "master": ""},
    "Location": {"eib": "Location_403", "template": "Location", "type": "master", "master": OBJECT.LOCATION},
    "PositionType": {"eib": "Position Time Type_405", "template": "Full_time", "type": "data", "master": ""}
}

__COMPENSATION = {
    "Key": {"eib": "Spreadsheet Key_1", "template": "Employee ID", "type": "template", "master": ""},
    "Package": {"eib": "Compensation Package_3", "template": "Compensation Package", "type": "template", "master": ""},
    "Grade": {"eib": "Compensation Grade_4", "template": "Compensation Grade", "type": "master", "master": OBJECT.GRADE},
    "Profile": {"eib": "Compensation Grade Profile_5", "template": "Compensation Grade Profile", "type": "master", "master": OBJECT.GRADE_PROFILE},
    "ID1": {"eib": "Row ID*_9", "template": "Pay Plan", "type": "template", "master": ""},
    "Plan": {"eib": "Pay Plan_10", "template": "Pay Plan", "type": "template", "master": ""},
    "Amount": {"eib": "Amount*_11", "template": "Amount*", "type": "template", "master": ""},
    "Currency": {"eib": "Currency*_12", "template": "Currency*", "type": "master", "master": OBJECT.CURRENCY},
    "Frequency": {"eib": "Frequency*_13", "template": "Frequency*", "type": "master", "master": OBJECT.FREQUENCY},
    "ID2": {"eib": "Row ID*_25", "template": "Row ID*", "type": "template", "master": ""},
    "Allowance": {"eib": "Allowance Plan_26", "template": "Allowance Plan", "type": "master", "master": OBJECT.ALLOWANCE},
    "AllAmount": {"eib": "Amount_28", "template": "Amount", "type": "template", "master": ""},
    "AllCurrency": {"eib": "Currency_30", "template": "Currency", "type": "master", "master": OBJECT.CURRENCY},
    "AllFrequency": {"eib": "Frequency_31", "template": "Frequency", "type": "", "master": OBJECT.FREQUENCY}
}

__CONTRACT = {
    "Key": {"eib": "Spreadsheet Key_1", "template": "Employee ID", "type": "template", "master": ""},
    "ID": {"eib": "Row ID*_2", "template": "1", "type": "data", "master": ""},
    "Date": {"eib": "Effective Date*_6", "template": "Effective Date*", "type": "template", "master": ""},
    "Contract": {"eib": "Contract Start Date*_9", "template": "Contract Start Date*", "type": "template", "master": ""},
    "Status": {"eib": "Contract Status*_14", "template": "Employee_Contract_Status_Open", "type": "data", "master": ""}
}

__NOTICE = {
    "Key": {"eib": "Spreadsheet Key_1", "template": "Employee ID", "type": "template", "master": ""},
    "Duration": {"eib": "Duration_3", "template": "Duration", "type": "template", "master": ""},
    "Unit": {"eib": "Unit*_4", "template": "Unit*", "type": "template", "master": ""}
}

TEMPLATE_GENERATE = {
    "Organization Add Update": __SUPERVISORY,
    "Create Position": __POSITION,
    "Edit Assign Organization": __ORGANIZATION,
    "Assign Pay Group": __PAY_GROUP, 
    "Hire Employee": __HIRE,
    "Propose Compensation for Hire": __COMPENSATION,
    "Edit Assign Organization": __ORGANIZATION,
    "Assign Pay Group": __PAY_GROUP,
    "Maintain Employee Contracts Sub": __CONTRACT,
    "Edit Notice Periods": __NOTICE
}