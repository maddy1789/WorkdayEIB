# This Speccified Date will be used as Effective Date
EFFECTIVE_DATE = "1990-01-01"

# This will display the Template to user
EIB_TEMPLATE = {
    1: "Supervisory",
    2: "Position",
    3: "Hire",
    4: "Compensation",
    5: "Time-Off",
    6: "Upload All (Supervisory, Position, Hire)"
}

TEMPLATE_SHEET = {
    "Supervisory": ["Supervisory"],
    "Position": ["Position"],
    "Hire": ["Hire", "Compensation", "Organization", "Contract", "Notice Period"],
    "Compensation": ["Compensation"],
    "Time-Off": ["Time-Off Balance"],
    "Upload All (Supervisory, Position, Hire)": ["Supervisory", "Position", "Hire", "Compensation", "Organization", "Contract", "Notice Period"]
}

TEMPLATE_COLUMN = {
    "Supervisory": ["Fields", "Serial No", "Organization Name", "Position Management", "Superior Organization", "Location"],

    "Position": ["Fields", "Serial No", "Organization Name", "Company", "Cost Center", "Position Title", "Job Profile", 
                "Location", "Position Time Type", "Number of Position"],

    "Hire": ["Fields", "Serial No", "Employee ID", "Title", "First Name", "Middle Name", "Last Name", "Gender",
             "Birth Date", "Country of Birth", "Region of Birth", "City of Birth", "Marital Status", "Religion",
             "Citizenship Status", "Primary Nationality", "Blood Type", "ID", "ID Type", "Country", "ID*", "ID Type*",
             "Address", "Municipality", "State", "Postal Code", "Public", "Primary", "Type", "Phone Code", "Phone Number",
             "Phone Device Type", "Public*", "Primary*", "Type*", "Email Address", "Public**", "Primary**", "Type**",
             "Organization", "Hire Date", "Employee Type", "Continous Service Date", "Probation Start Date", 
             "Probation End Date", "Position Title", "Location"],

    "Compensation": ["Fields", "Serial No", "Employee ID", "Compensation Package", "Compensation Grade", "Compensation Grade Profile",
                    "Pay Plan", "Amount*", "Currency*", "Frequency*", "Row ID*", "Allowance Plan", "Amount", "Currency", "Frequency"],

    "Organization": ["Fields", "Serial No", "Employee ID", "Company Assignments+", "Cost Center Assignments+", "Pay Group"],

    "Contract": ["Fields", "Serial No", "Employee ID", "Effective Date*", "Contract Start Date*", "Contract Status*"],

    "Notice Period": ["Fields", "Serial No", "Employee ID", "Duration", "Unit*"],
    
    "Time-Off": []
}

BLANK_COLUMN_CHECK = {
    "Supervisory": ["Organization Name", "Position Management", "Superior Organization", "Location"],

    "Position": [],

    "Hire": ["Employee ID", "Title", "First Name", "Last Name", "Gender", "Birth Date", "Country of Birth",
             "Region of Birth", "City of Birth", "Marital Status", "Religion", "Citizenship Status",
             "Primary Nationality", "Blood Type", "ID", "ID Type", "Address", "State", "Postal Code",
             "Phone Number", "Email Address", "Organization", "Hire Date", "Employee Type", "Continous Service Date",
             "Probation Start Date", "Probation End Date", "Position Title", "Location"],

    "Compensation": [],

    "Organization": ["Employee ID", "Company Assignments+", "Cost Center Assignments+", "Pay Group"],

    "Contract": ["Employee ID", "Effective Date*", "Contract Start Date*", "Contract Status*"],

    "Notice Period": ["Employee ID", "Duration", "Unit*"],

    "Time-Off": []
}

EIB = {
    "Supervisory": "src/FILES/TEMPLATE/EIB/Add_Update_Organization.xlsx",
    "Position": "src/FILES/TEMPLATE/EIB/Create_Position.xlsx",
    "Hire": "src/FILES/TEMPLATE/EIB/Hire_Employee.xlsx"
}

EIB_SHEET = {
    "Supervisory": [{"E": "Organization Add Update", "T": "Supervisory"}],
    "Position": ["Create Position", "Edit Assign Organization", "Assign Pay Group"],
    "Hire": ["Hire Employee", "Propose Compensation for Hire", "Edit Assign Organization", 
             "Assign Pay Group", "Maintain Employee Contracts Sub", "Edit Notice Periods"],
    "Compensation": [],
    "Time-Off": [],
    "Upload All (Supervisory, Position, Hire)": [{"E": "Organization Add Update", "T": "Supervisory", "F": "Supervisory"}, 
                                                 {"E": "Create Position", "T": "Hire", "F": "Position"}, 
                                                 {"E": "Edit Assign Organization", "T": "Organization", "F": ""}, 
                                                 {"E": "Assign Pay Group", "T": "Organization", "F": ""}, 
                                                 {"E": "Hire Employee", "T": "Hire", "F": "Hire"}, 
                                                 {"E": "Propose Compensation for Hire", "T": "Compensation", "F": ""},
                                                 {"E": "Edit Assign Organization", "T": "Organization", "F": ""}, 
                                                 {"E": "Assign Pay Group", "T": "Organization", "F": ""}, 
                                                 {"E": "Maintain Employee Contracts Sub", "T": "Contract", "F": ""},
                                                 {"E": "Edit Notice Periods", "T": "Notice Period", "F": ""}
                                                 ]
}
