from src.SETTING.validation import OBJECT_VALIDATE_COLUMN
from src.SETTING.template import TEMPLATE_SHEET, BLANK_COLUMN_CHECK
from src.SETTING.master import MASTER
from .utility import header_message, blank_column, error_message, duplicate_data, unavailable_data

SUPERVISORY_LIST = []
HEADER_FLAG = True 

def template(dataframe, eib):
    TEMPLATE_VALIDATION = {}

    for sheet in TEMPLATE_SHEET[eib]:
        if  sheet != "Position" and eib.upper() != "UPLOAD ALL (SUPERVISORY, POSITION, HIRE)":
            if not dataframe[sheet].empty:
                TEMPLATE_VALIDATION[sheet] = __sheetValidation(dataframe[sheet], sheet, eib)
                __checkBlank(dataframe[sheet], sheet, eib)
            else:
                print ("{} DATA NOT AVAILABLE!\n".format(sheet.upper()))

    if all(data == True for data in list(TEMPLATE_VALIDATION.values())):
        header_message("Template Validation Complete, Status: Success")
        return True

    return False

def __sheetValidation(dataframe, sheet, eib):
    validateColumn = OBJECT_VALIDATE_COLUMN[sheet]
    if bool(validateColumn):
        validation = {}

        for key, value in validateColumn.items():
            title, objDF = value[0], MASTER[value[1]]

            if sheet == "Supervisory" and key == "Organization":
                validation[title] = duplicate_data(dataframe[title], objDF)
            elif sheet == "Supervisory" and key == "Superior":
                supDF = objDF["Instance"].append(dataframe["Organization Name"])
                validation[title] = unavailable_data(dataframe[title], supDF)

                if eib.upper() == "UPLOAD ALL (SUPERVISORY, POSITION, HIRE)":
                    global SUPERVISORY_LIST
                    SUPERVISORY_LIST = supDF

                del supDF
            elif eib.upper() == "UPLOAD ALL (SUPERVISORY, POSITION, HIRE)" and sheet == "Hire" and key == "Organization":
                validation[title] = unavailable_data(dataframe[title], SUPERVISORY_LIST)
            else:
                if sheet == "Organization" and key == "CostCenter":
                    objDF["Instance"] = objDF["Instance"].str.split(" ", 1, expand = True)[0]
                validation[title] = unavailable_data(dataframe[title], objDF, value[2])

        if all(len(data) == 0 for data in list(validation.values())):
            # header_message("Template Validation Complete, Status: Success")
            return True

        global HEADER_FLAG
        if HEADER_FLAG == True:
            HEADER_FLAG = False
            header_message("Template Validation Complete, Status: Error")
        return error_message(validation, dataframe, sheet)
    else:
        return True

def __checkBlank(dataframe, sheet, eib):
    if not "Hire" in eib and sheet == "Position":
        blank_column(dataframe, BLANK_COLUMN_CHECK[sheet], sheet)
        



