from .master import MASTER, OBJECT

__SUPERVISORY_VALIDATE = {
    "Organization": ["Organization Name", OBJECT.SUPERVISORY, "Instance"],
    "Superior": ["Superior Organization", OBJECT.SUPERVISORY, ""],
    "Location": ["Location", OBJECT.LOCATION, "Instance"]
}

__HIRE_VALIDATE = {
    "Title": ["Title", OBJECT.TITLE, "Instance"],
    "Gender": ["Gender", OBJECT.GENDER, "Instance"],
    "Country": ["Country of Birth", OBJECT.COUNTRY, "Instance"],
    "Region": ["Region of Birth", OBJECT.STATE, "Instance"],
    "Marital": ["Marital Status", OBJECT.MARITAL, "ID"],
    "Religion": ["Religion", OBJECT.RELIGION, "ID"],
    "Citizen": ["Citizenship Status", OBJECT.CITIZEN, "ID"],
    "Nationality": ["Primary Nationality", OBJECT.COUNTRY, "Instance"],
    "Blood": ["Blood Type", OBJECT.BLOOD, "Instance"],
    "National_ID": ["ID Type", OBJECT.NATIONAL_ID, "Instance"],
    "State": ["State", OBJECT.STATE, "Instance"],
    "Organization": ["Organization", OBJECT.SUPERVISORY, "Instance"],
    "EmpType": ["Employee Type", OBJECT.EMP_TYPE, "Instance"],
    "Position": ["Position Title", OBJECT.JOB_PROFILE, "Instance"],
    "Location": ["Location", OBJECT.LOCATION, "Instance"]
}

__ORGANIZATION_VALIDATE = {
    "Company": ["Company Assignments+", OBJECT.COMPANY, "Instance"],
    "CostCenter": ["Cost Center Assignments+", OBJECT.COSTCENTER, "Instance"],
    "PayGroup": ["Pay Group", OBJECT.PAYGROUP, "Instance"]
}

OBJECT_VALIDATE_COLUMN = {
    "Supervisory": __SUPERVISORY_VALIDATE,
    "Position": {},
    "Hire": __HIRE_VALIDATE,
    "Compensation": {},
    "Organization": __ORGANIZATION_VALIDATE,
    "Contract": {},
    "Notice Period": {}
}