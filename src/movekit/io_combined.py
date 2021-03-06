

import pandas as pd
import numpy as np
from pandas.api.types import is_numeric_dtype, is_string_dtype
from pandas.errors import EmptyDataError


"""
IMPORTANT NOTE:

To process Microsoft Excel file, file extensions- '.xlsx', '.xls',
pleas install Python 3.X package 'xlrd' using 'pip', 'anaconda',
or any other relevant package manager!
"""




def parse_csv(path_to_file):
    '''
    A function to read CSV file into a Pandas DataFrame-
    Expects complete path/relative path to CSV file along with file name
    '''
    try:

        if path_to_file[-3:] == 'csv':
            data = pd.read_csv(path_to_file)
        else:
            data = pd.read_csv(path_to_file + '.csv')

        # change column names all to lower case values
        data.columns = map(str.lower, data.columns)

        # check if all required columns are there in the right format
        if 'time' in data and 'animal_id' in data and 'x' in data and 'y' in data:
            # Check if 'time' attribute is integer-
            if is_numeric_dtype(data['time']):
                data.sort_values('time', ascending=True, inplace=True)
                # Check if 'time' attribute is string-
            elif is_string_dtype(data['time']):
                data['time'] = pd.to_datetime(data['time'])
                data.sort_values('time', ascending=True, inplace=True)

            # Check if 'heading_angle' attribute is given in CSV file-
            if 'heading_angle' in data and np.issubdtype(data['heading_angle'].dtype, np.number):
                print("\n'heading_angle' attribute is found (numeric type) and will be processed\n")
                # do nothing, as 'heading_angle' attribute exists
            else:
                print("\nWARNING: 'heading_angle' attribute is not found in the given CSV data file. Continuing without it!\n")


            return data
    except FileNotFoundError:
        print(
            "Your file below could not be found.\nPath given: {0}\n\n".format(
                path_to_file))
    except EmptyDataError:
        print(
            'Your file is empty, has no header, or misses some required columns.'
        )


def parse_excel(path_to_file):
    '''
    Function to read Excel file into a Pandas DataFrame-
    Expects complete path/relative path to CSV file along with file name

    Expects package 'xlrd' to be installed for this to work!
    '''
    try:

        if path_to_file[-3:] == 'xls' or path_to_file[-4:] == 'xlsx':
            data = pd.read_excel(path_to_file)
        else:
            data = pd.read_excel(path_to_file + '.xlsx')

        # change column names all to lower case values
        data.columns = map(str.lower, data.columns)

        # check if all required columns are there in the right format
        if 'time' in data and 'animal_id' in data and 'x' in data and 'y' in data:
            # Check if 'time' attribute is integer-
            if is_numeric_dtype(data['time']):
                data.sort_values('time', ascending=True, inplace=True)
                # Check if 'time' attribute is string-
            elif is_string_dtype(data['time']):
                data['time'] = pd.to_datetime(data['time'])
                data.sort_values('time', ascending=True, inplace=True)

            # Check if 'heading_angle' attribute is given in CSV file-
            if 'heading_angle' in data and np.issubdtype(data['heading_angle'].dtype, np.number):
                print("\n'heading_angle' attribute is found (numeric type) and will be processed\n")
                # do nothing, as 'heading_angle' attribute exists
            else:
                print("\nWARNING: 'heading_angle' attribute is not found in the given CSV data file. Continuing without it!\n")


            return data

    except FileNotFoundError:
        print(
            "Your file below could not be found.\nPath given: {0}\n\n".format(
                path_to_file))
    except EmptyDataError:
        print(
            'Your file is empty, has no header, or misses some required columns.'
        )




def read_data(parse_csv_fn = False, parse_excel_fn = False, path_to_file = ""):
    """
    Function containing all of Input Output (IO) functions
    as function arguments (which by default are False).

    NOTE:
    Currently, only two file extensions are recognised and
    processed, viz., 'csv' and '.xlsx'
    """

    # Call appropriate IO function based on file extencsion
    # Split string based on '.' (dot)-
    file_split = path_to_file.split(".")

    print(file_split)

    if file_split[-1] == 'csv':
        return parse_csv(path_to_file)
    elif file_split[-1] == 'xlsx':
        return parse_excel(path_to_file)

