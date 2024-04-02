import math
import numpy as np
import pandas as pd

class Utils():
  
    # def infer_and_convert_data_types(df):
    #     # converted_df = df.copy()  # Create a copy to avoid modifying the original DataFrame
    #     date_formats = ['%d/%m/%Y', '%m/%d/%Y', '%Y-%m-%d', '%Y/%m/%d', '%d-%m-%Y']  # Add more date formats as needed
    #     print(df.columns)
        
    #     for col in df.columns:
    #         # Attempt to convert to numeric first
    #         print(col)
    #         df[col] = df[col].replace('Not Available', "null")
    #         numeric_count = pd.to_numeric(df[col], errors='coerce').notna().sum()
    #         total_count = len(df[col])
            
    #         # If majority of values are numeric, infer as numeric
    #         if numeric_count / total_count > 0.5:
    #             df[col] = pd.to_numeric(df[col], errors='coerce')
    #             continue

    #         # Attempt to convert to datetime
    #         try:
    #             df[col] = pd.to_datetime(df[col], format='%d/%m/%Y')
    #             # converted_df[col] = pd.to_datetime(converted_df[col], format=date_formats)
    #             # converted_df[col] = pd.to_datetime(converted_df[col], format=date_formats)
    #             # converted_df[col] = pd.to_datetime(converted_df[col], format=date_formats)
    #             break  # Stop trying formats once successful
    #         except (ValueError, TypeError):
    #             pass

    #         # Check if the column should be categorical
    #         unique_ratio = len(df[col].unique()) / len(df[col])
           
    #         # print(len(converted_df[col].unique()))
    #         # print(len(converted_df[col]))
    #         # print(unique_ratio)

    #         if unique_ratio < 0.5:  # Example threshold for categorization
    #             df[col] = df[col].astype('category')
    #         else:
    #             # If not categorized, convert to string
    #             df[col] = df[col].astype(str)
        
    #     # print("---------........------")
    #     # print(converted_df)
    #     # print("---------&======&------")


    #     return df
    
    def infer_and_convert_data_types(df):
        date_formats = ['%d/%m/%Y', '%m/%d/%Y', '%Y-%m-%d', '%Y/%m/%d', '%d-%m-%Y']  # Add more date formats as needed    
        date_formats = ['%d/%m/%Y', '%m/%d/%Y', '%Y-%m-%d', '%Y/%m/%d', '%d-%m-%Y']  # Add more date formats as needed    
        for col in df.columns:
            # Attempt to convert to numeric first
        
            df_converted = pd.to_numeric(df[col], errors='coerce')
            if not df_converted.isna().all():  # If at least one value is numeric
                df_converted = df_converted.fillna(0)
                # df_converted[col] = pd.to_numeric(df_converted[col], errors='coerce')
                df[col] = df_converted
                continue

            # Attempt to convert to datetime
            try:
                #this will fix all the mix formats for the dates
                df_dates = pd.to_datetime(df[col],format='mixed')
                df[col] = df_dates

                continue
            except (ValueError, TypeError):
                missing_strings = ['NotAvailable','Not Available', 'null', 'N/A', 'NA', 'Nell']  # Add any other strings as needed

                # Replace any string in the 'date' column that matches the missing_strings list with NaN
                df[col] = df[col].replace(missing_strings, np.nan, regex=True)
                pass

            # Check if the column should be categorical
            if len(df[col].unique()) / len(df[col]) < 0.5:  # Example threshold for categorization
                df[col] = pd.Categorical(df[col])
            print(df)
        return df