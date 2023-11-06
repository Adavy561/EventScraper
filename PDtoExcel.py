from datetime import datetime
import os
import pandas as pd
import Retrieval
import pytz
from openpyxl import Workbook
import xlsxwriter

def dataframe_to_excel(dataframe):
    # Create a new Workbook object
    wb = Workbook()

    # Create a new worksheet and add the data to it
    ws = wb.active
    ws.title = "Data"
    for row in dataframe.values:
        ws.append(row)

    # Save the workbook to a file
    date = datetime.now().strftime("%Y-%m-%d")
    filename = f"data_{date}.xlsx"
    filepath = os.path.join("OutputExcel", filename)
    wb.save(filepath)

    print(f"DataFrame written to {filename}")

clabs = Retrieval.getCampusLabsFromRSS()
# sports = Retrieval.getSportsFromRSS()
# library = Retrieval.getLibraryFromRSS()

df = pd.concat([clabs], axis=1)

dataframe_to_excel(df)