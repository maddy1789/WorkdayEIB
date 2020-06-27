from .utility import file_exist, divider

def master(filepath):
    if file_exist(filepath):
        from pandas import read_excel
        objdata = read_excel(filepath)
        return __update_column(objdata)
    else:
        divider()
        print("FILE NOT FOUND: {}".format(filepath))

def __update_column(dataframe):
    if "Integration IDs" in list(dataframe.columns):
        dataframe.rename(columns = dataframe.iloc[1].to_dict(), inplace = True)
        dataframe = dataframe.iloc[2:]
    elif "Reference IDs" in list(dataframe.columns):
        dataframe.rename(columns = dataframe.iloc[0].to_dict(), inplace = True)
        dataframe = dataframe.iloc[1:]
    return __shrink_column(dataframe)

def __shrink_column(dataframe):
    b_object = dataframe["Business Object"].unique()[0]

    if (b_object in ["Company", "Cost Center"]):
        return dataframe[(dataframe["Type"] == "Organization_Reference_ID")][["Instance", "ID"]]
    elif b_object == "Marital Status": 
        return dataframe[(dataframe["Type"] == "Marital_Status_ID")][["Instance", "ID"]]
    elif b_object == "Country Region":
        return dataframe[(dataframe["Type"] == "Country_Region_ID")][["Instance", "ID"]]
    elif b_object == "Country":
        return dataframe[(dataframe["Type"] == "ISO_3166-1_Alpha-2_Code")][["Instance", "ID"]]
    elif b_object == "Currency":
        return dataframe[(dataframe["Type"] == "Currency_ID")][["Instance", "ID"]]
    else:
        return dataframe[["Instance", "ID"]]
