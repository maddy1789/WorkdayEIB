import pandas as pd
import openpyxl

from src.FUNCTION.utility import list_compare, divider, header_message
from src.SETTING.template import TEMPLATE_SHEET, TEMPLATE_COLUMN

SHEET = []

def generate(filename, eib):
    if __validateSheet(filename, eib):
        return __readExcel(filename, eib)
    else:
        print("Something went wrong, Dataframe cannot be generated!")
        return pd.DataFrame()

def __validateSheet(file, eib):
    global SHEET
    SHEET = TEMPLATE_SHEET[eib]

    workbook = openpyxl.load_workbook(file, read_only=True)
    unavailable_sheet = list_compare(SHEET, workbook.get_sheet_names())
    workbook.close()

    if len(unavailable_sheet) > 0:
        divider()
        print ("INCORRECT TEMPLATE, Sheet Unavailable: {}".format(sheet_unavailable))
        return False
    
    return True

def __readExcel(filepath, eib):
    dataframe = pd.read_excel(filepath, sheet_name=SHEET, header = 4)
    if not __columnValidation(dataframe):
        return pd.DataFrame()        
    return __updateData(dataframe)

def __columnValidation(dataframe):
    for sheet in SHEET:
        unavailable_column = list_compare(TEMPLATE_COLUMN[sheet], list(dataframe[sheet].columns))
        if len(unavailable_column) > 0:
            divider()
            print ("\nINCORRECT TEMPLATE, Column Unavailable: {}".format(unavailable_column))
            return False

        return True

def __updateData(dataframe):
    if "Hire" in dataframe.keys():
        hire_df = dataframe["Hire"]
        hire_df["Marital Status"] = hire_df['Marital Status'].str.cat(hire_df["Country of Birth"], sep="_")
        hire_df["Religion"] = hire_df['Religion'].str.cat(hire_df["Country of Birth"], sep="_")
        hire_df["ID Type*"] = hire_df["ID Type*"].apply(lambda x: "Payroll_ID" if "Payroll" in x else x)
        hire_df["Blood Type"] = hire_df["Blood Type"].apply(__updateBlood)
        dataframe["Hire"] = hire_df
    if "Organization" in dataframe.keys():
        org_df = dataframe["Organization"]
        org_df["Company Assignments+"] = org_df["Company Assignments+"].apply(lambda x: "DNEG India Media Services Limited (DIMSL)" if "DNEG India Media" in x else x)
        dataframe["Organization"] = org_df

    # print("DATAFRAME GENERATED, Status: Success, time required: {}".format(time.time() - START_TIME))
    header_message("Reading Excel File, Status: Complete")
    return dataframe

def __updateBlood(bg):
    if "O" in str(bg):
        return __bloodType("O", str(bg))
    elif "AB" in str(bg):
        return __bloodType("AB", str(bg))
    elif "A" in str(bg):
        return __bloodType("A", str(bg))
    elif "B" in str(bg):
        return __bloodType("B", str(bg))
    else:
        return "HH"

def __bloodType(btype, data):
    if "-" in data:
        return btype + "-"
    return btype + "+"



