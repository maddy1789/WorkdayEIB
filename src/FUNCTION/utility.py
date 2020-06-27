import os
import shutil
from openpyxl import load_workbook
import pandas as pd

# DOWNLOAD = "***DOWNLOAD***"

def terminal_column_width():
    return os.get_terminal_size().columns

def divider():
    print("/" * terminal_column_width())

def header_message(msg):
    divider()
    print(msg.center(terminal_column_width()).upper())
    divider()

def file_exist(filepath):
    if os.path.isfile(filepath):
        return True
    return False

def search_excel():
    xls_list = [obj for obj in os.listdir() if os.path.isfile(obj) and obj[-5:] == ".xlsx"]
    return {(i + 1): xls_list[i] for i in range(len(xls_list))}

def list_compare(sourceList, compareList):
    return list(set(sourceList) - set(compareList))

def duplicate_data(objList, masterList):
    return list(set(objList).intersection(set(masterList)))

def unavailable_data(seriesDF, objectDF, column = ""):
    if column == "":
        return seriesDF[~seriesDF.isin(objectDF)].dropna().unique().tolist()
    return seriesDF[~seriesDF.isin(objectDF[column])].dropna().unique().tolist()

def error_message(errDict, dataframe, obj = None):
    for key, value in errDict.items():
        message = "Not Available"
        if len(value) > 0:
            print("<{}> {} not found: {}\n".format(obj.upper(), key, value))
            if obj == "Supervisory" and key == "Organization Name":
                message = "Already Exists"

            dataframe[key] = dataframe[key].apply(lambda s: "{} |{}".format(s, message) if s in value else s)
    return False

def blank_column(dataframe, column, sheet):
    nullColumns = dataframe.columns[dataframe.isnull().any()]
    nullColumns = set(column).intersection(set(nullColumns))
    if len(nullColumns) > 0:
        print("\n{} TEMPLATE, BLANK COLUMN FOUND: ".format(sheet.upper()))
        print(dataframe[nullColumns].isnull().sum())
        print("\n")

def remove_folder(dirPath):
    if os.path.isdir(dirPath):
        shutil.rmtree(dirPath)

def create_folder(dirPath):
    if not os.path.isdir(dirPath):
        os.mkdir(dirPath)

def copy_file(source, destination):
    create_folder(destination)
    return shutil.copy(source, destination)

def generate_excel(filepath, dataframe, sheetname):
    if file_exist(filepath):
        book = load_workbook(filepath)
        writer = pd.ExcelWriter(filepath, engine="openpyxl")
        writer.book = book
        writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
        dataframe.to_excel(writer, sheetname, header=False, startrow=5, index=False)
        writer.save()

