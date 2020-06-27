from src.FUNCTION.read import master

class FILE:
    ALLOWANCE = "src/FILES/MASTER/Allowance.xlsx"
    BLOOD = "src/FILES/MASTER/BloodType.xlsx"
    CITIZEN = "src/FILES/MASTER/Citizen.xlsx"
    COMPANY = "src/FILES/MASTER/Company.xlsx"
    COSTCENTER = "src/FILES/MASTER/CostCenter.xlsx"
    COUNTRY = "src/FILES/MASTER/Country.xlsx"
    CURRENCY = "src/FILES/MASTER/Currency.xlsx"
    EMP_TYPE = "src/FILES/MASTER/EmployeeType.xlsx"
    FREQUENCY = "src/FILES/MASTER/Frequency.xlsx"
    GENDER = "src/FILES/MASTER/Gender.xlsx"
    GRADE = "src/FILES/MASTER/Grade.xlsx"
    GRADE_PROFILE = "src/FILES/MASTER/GradeProfile.xlsx"
    JOBPROFILE = "src/FILES/MASTER/JobProfile.xlsx"
    LOCATION = "src/FILES/MASTER/Location.xlsx"
    MARITAL = "src/FILES/MASTER/MaritalStatus.xlsx"
    NATIONAL_ID = "src/FILES/MASTER/NationalIDs.xlsx"
    PACKAGE = "src/FILES/MASTER/Package.xlsx"
    PAYGROUP = "src/FILES/MASTER/PayGroup.xlsx"
    RELIGION = "src/FILES/MASTER/Religion.xlsx"
    STATE = "src/FILES/MASTER/State.xlsx"
    SUPERVISORY = "src/FILES/MASTER/Supervisory.xlsx"
    TITLE = "src/FILES/MASTER/Title.xlsx"

class OBJECT:
    ALLOWANCE = "Allowance"
    BLOOD = "Blood"
    CITIZEN = "Citizen"
    COMPANY = "Company"
    COSTCENTER = "CostCenter"
    COUNTRY = "Country"
    CURRENCY = "Currency"
    EMP_TYPE = "EmpType"
    FREQUENCY = "Frequency" 
    GENDER = "Gender"
    GRADE = "Grade" 
    GRADE_PROFILE = "GradeProfile" 
    JOB_PROFILE = "JobProfile"
    LOCATION = "Location"
    MARITAL = "Marital"
    NATIONAL_ID = "NationalID" 
    PACKAGE = "Package"
    PAYGROUP = "PayGroup"
    RELIGION = "Religion"
    STATE = "State" 
    SUPERVISORY = "Supervisory"
    TITLE = "Title" 

MASTER = {
    "Allowance": master(FILE.ALLOWANCE),
    "Blood": master(FILE.BLOOD),
    "Citizen": master(FILE.CITIZEN),
    "Company": master(FILE.COMPANY),
    "CostCenter": master(FILE.COSTCENTER),
    "Country": master(FILE.COUNTRY),
    "Currency": master(FILE.CURRENCY),
    "EmpType": master(FILE.EMP_TYPE),
    "Frequency": master(FILE.FREQUENCY),
    "Gender": master(FILE.GENDER),
    "Grade": master(FILE.GRADE),
    "GradeProfile": master(FILE.GRADE_PROFILE),
    "JobProfile": master(FILE.JOBPROFILE),
    "Location": master(FILE.LOCATION),
    "Marital": master(FILE.MARITAL),
    "NationalID": master(FILE.NATIONAL_ID),
    "Package": master(FILE.PACKAGE),
    "PayGroup": master(FILE.PAYGROUP),
    "Religion": master(FILE.RELIGION),
    "State": master(FILE.STATE),
    "Supervisory": master(FILE.SUPERVISORY),
    "Title": master(FILE.TITLE)
}