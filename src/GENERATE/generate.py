import pandas as pd

from src.SETTING.template import TEMPLATE_SHEET, EIB, EIB_SHEET, EFFECTIVE_DATE
from src.SETTING.generate import TEMPLATE_GENERATE
from src.SETTING.master import MASTER
from src.FUNCTION.utility import copy_file, generate_excel

PATH = "__DOWNLOAD__"
FILENAME = ""
SUPERVISORY = ""
POSITION = ""
EMPLOYEE = ""

def template(dataframe, eib):
    for sheet in EIB_SHEET[eib]:
        df = dataframe[sheet["T"]]
        if not df.empty:
            objectDF = __templateEIB(df, eib, sheet)
            if not objectDF.empty:
                generate_excel(FILENAME, objectDF, sheet["E"])
                # print(objectDF)

def __templateEIB(df, eib, sheet):
    # print(sheet)
    if sheet["F"] in ["Supervisory", "Position", "Hire"]:
        global FILENAME
        filepath = copy_file(EIB[sheet["F"]], PATH)
        FILENAME = filepath

    # print("FILEPATH = {}".format(FILENAME))
    objDF =  __dataframe(sheet["E"])
    # if sheet["F"] == "Hire":
    #     for key in objDF.keys():
    #         print(key)
    return __generateEIB(df, objDF, sheet, eib)

def __dataframe(sheet):
    df =  pd.read_excel(FILENAME, sheet_name = sheet, header = 4)
    if len(df.keys()) > 0:
        col = __createColumn(df.keys())
        df.rename(columns=col, inplace=True)
        return df

def __createColumn(keys):
    return {keys[i]: str(keys[i]) + "_" + str(i) for i in range(len(keys))}

def __generateEIB(dataframe, objectDF, sheet, eib):
    dfLength = len(dataframe.index)
    if len(TEMPLATE_GENERATE[sheet["E"]]) > 0:
        for key, values in TEMPLATE_GENERATE[sheet["E"]].items():
            if values["eib"] in objectDF.keys():
                if values["type"] == "key":
                    objectDF[values["eib"]] = range(1, (dfLength + 1))
                elif values["type"] == "edate":
                    objectDF[values["eib"]] = [EFFECTIVE_DATE] * dfLength
                elif values["type"] == "data":
                    objectDF[values["eib"]] = [values["template"]] * dfLength
                elif values["type"] == "template":
                    objectDF[values["eib"]] = dataframe[values["template"]]
                elif values["type"] == "master":
                    masterDF = MASTER[values["master"]]
                    objectDF[values["eib"]] = dataframe[values["template"]].replace(masterDF.set_index("Instance")["ID"])
                    del masterDF
                elif values["type"] == "id":
                    str = "SUP" if sheet["E"] == "Organization Add Update" else "POS"
                    objectDF[values["eib"]] = ["{}_{:0>4}".format(str, i) for i in range(1, (dfLength + 1))]

        if sheet["F"] == "Supervisory":
            global SUPERVISORY
            SUPERVISORY = objectDF.set_index("Organization Name_7")["Organization Reference ID_3"]
            objectDF["Superior Organization_15"] = objectDF["Superior Organization_15"].replace(SUPERVISORY)
        elif sheet["F"] == "Position":
            global POSITION
            POSITION = objectDF.set_index("Job Posting Title_5")["Position ID_4"]
            objectDF["Supervisory Organization*_2"] = objectDF["Supervisory Organization*_2"].replace(SUPERVISORY)
        elif sheet["F"] == "Hire":
            global EMPLOYEE
            EMPLOYEE = dataframe.set_index("Employee ID")["Serial No"]
            objectDF["Organization_383"] = objectDF["Organization_383"].replace(SUPERVISORY)
            objectDF["Position_384"] = objectDF["Position_384"].replace(POSITION)
        elif sheet["E"] in ["Propose Compensation for Hire", "Maintain Employee Contracts Sub", "Edit Notice Periods"]:
            objectDF["Spreadsheet Key_1"] = objectDF["Spreadsheet Key_1"].replace(EMPLOYEE)

        return objectDF
    else:
        return pd.DataFrame()