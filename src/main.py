from src.FUNCTION.utility import divider, header_message, search_excel
from src.FUNCTION import validate, dataframe, generate
import src.SETTING.template as template
def main():
    eib = __getEIB()
    header_message(eib + " Template")
    xlsFile = __templateFile()
    if eib != None and xlsFile != None:
        objectDF = dataframe.generate(xlsFile, eib)
        if __validateTemplate(objectDF, eib):   
            generate.template(objectDF, eib)
            header_message("EIB TEMPLATE CREATED, PLEASE CHECK THE DOWNLOAD FOLDER")


def __getEIB():
    header_message("Workday EIB Generate Template")

    print ("\nPlease select EIB Template to generate:\n")
    return __getObject(template.EIB_TEMPLATE)

def __getObject(dictionary):
    for key, value in dictionary.items():
        print("Press {} - {}".format(key, value.upper()))

    option = input("\nSelect an option and press <Enter>: ")
    option = int(option)

    if option in dictionary.keys():
        return dictionary[option]
    else:
        print ("\nInvalid Option Entered!")
        return None

def __templateFile():
    xlsFile = search_excel()
    fileSelected = ""

    if len(xlsFile) > 1:    
        print ("\nMultiple Excel sheet found, Please select appropriate file: ")
        fileSelected = __getObject(xlsFile)
    elif len(xlsFile) == 1:
        fileSelected = xlsFile[1]
    else:
        print("\nNo Excel File Found, Please add the File and re-run the script.")

    if len(fileSelected) > 0:
        print ("\nExcel Template Selected: {}".format(fileSelected))
        return fileSelected
    else:
        return None

def __validateTemplate(dataframe, eib):
    if bool(dataframe):
        if validate.template(dataframe, eib) == True:
            return True
        else:
            header_message("TEMPLATE VALIDATION ERROR: Please find Validate.xlsx file from DOWNLOAD folder")
            return False   
    else:
        print("\nDATAFRAME NOT GENERATED: Something went wrong!\n")
        util.divider()
        return False


if __name__ == "__main__":
    main()