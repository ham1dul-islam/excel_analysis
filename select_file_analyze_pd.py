import pandas as pd
import logging
from datetime import datetime
import os
import xlsxwriter
import tkinter as tk
from tkinter import filedialog

 

program_name = "file_analysis"
log_file_name = f"log/{program_name}/{program_name}{datetime.now().strftime('%Y-%m-%d-%H_%M_%S')}.log"
OUTPUT_FOLDER='output'
INPUT_FOLDER='input'




logging.basicConfig(

    filename=log_file_name,  # Specify the log file name
    level=logging.INFO,   # Set the logging level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format

)

 

def log(message):
    logging.info(message)

 

# Function to select folder (default to 'input' folder in working directory)

def select_folder():
    # Set the default folder to 'input' in the working directory
    default_folder = os.path.join(os.getcwd(), INPUT_FOLDER)

def return_select_excel_as_df():

    folder_path = select_folder()

    print(f"Using Folder: {folder_path}")

    log(f"Using Folder: {folder_path}")

   

    file_path = select_file(folder_path)
    if file_path:
        print(f"Selected File: {file_path}")
        log(f"Selected File: {file_path}")

        sheet_names = get_sheet_names(file_path)
        if sheet_names:
            print("Sheet Names Available:")
            log("Sheet Names Available:")
            for idx, sheet in enumerate(sheet_names, start=1):
                print(f"{idx}. {sheet}")

            # Allow the user to select a sheet by index
            sheet_index = int(input(f"Select a sheet by number (1-{len(sheet_names)}): "))
            selected_sheet = sheet_names[sheet_index - 1]
            print(f"Selected Sheet: {selected_sheet}")
            log(f"Selected Sheet: {selected_sheet}") 

            # Load the selected sheet into a DataFrame
            df = load_sheet_into_dataframe(file_path, selected_sheet)
            if df is not None:
                print(f"DataFrame loaded from sheet '{selected_sheet}':")
                log(f"DataFrame loaded from sheet '{selected_sheet}':")
                print(df.head())  # Display the first 5 rows of the DataFrame
                log(df.head())  # Display the first 5 rows of the DataFrame
                log(df.columns.tolist())
                return df

        else:
            print("No sheets found in the file.")
            log("No sheets found in the file.")
            return "no sheets found"

    else:
        print("No file selected.")
        log("No file selected.")
        return "no file selected"

 

# Function to count non-empty values in a user-selected column of a DataFrame

def count_non_empty_selected_column(df):
    # Display column names for user selection
    print("Available columns:")
    for idx, column in enumerate(df.columns, start=1):
        print(f"{idx}. {column}")
  
    # Ask the user to select a column by number
    column_index = int(input(f"Select a column by number (1-{len(df.columns)}): "))

    # Get the selected column name
    selected_column = df.columns[column_index - 1]

    # Count non-null values in the selected column
    non_empty_count = df[selected_column].notnull().sum()

    # Print the result
    print(f"Number of non-empty values in '{selected_column}': {non_empty_count}")
    log(f"Number of non-empty values in '{selected_column}': {non_empty_count}")

 

def main():

    log("-----------Start of Program-----------") 
    df = return_select_excel_as_df()
 
    log(f"number of rows = {len(df)}")
    #count_non_empty_selected_column(df)
    count_non_empty_selected_column(df)  

    log("-----------End of Program-----------")

 

if __name__ == '__main__':

    main()# -*- coding: utf-8 -*-
