#!/usr/bin/python3
import pandas as pd

tables = ['Table 1','Table 4','Table 7','Table 10','Table 13','Table 16']

############ ALL THE AMERICAS #########################
# cols = ['Anguilla','Antigua and Barbuda','Aruba','Bahamas','Barbados','Bonaire, Sint Eustatius and Saba','British Virgin Islands','Cayman Islands','Cuba','Curaçao','Dominica','Dominican Republic','Grenada','Guadeloupe','Haiti','Jamaica','Martinique','Montserrat','Puerto Rico','Saint Kitts and Nevis','Saint Lucia','Saint Vincent and the Grenadines','Sint Maarten (Dutch part)','Trinidad and Tobago','Turks and Caicos Islands','United States Virgin Islands','Belize','Costa Rica','El Salvador','Guatemala','Honduras','Mexico','Nicaragua','Panama','Argentina','Bolivia (Plurinational State of)','Brazil','Chile','Colombia','Ecuador','Falkland Islands (Malvinas)','French Guiana','Guyana','Paraguay','Peru','Suriname','Uruguay','Venezuela (Bolivarian Republic of)','Bermuda','Canada','Greenland','Saint Pierre and Miquelon','United States of America']
# rows = ['Anguilla','Antigua and Barbuda','Aruba','Bahamas','Barbados','Bonaire, Sint Eustatius and Saba','British Virgin Islands','Cayman Islands','Cuba','Curaçao','Dominica','Dominican Republic','Grenada','Guadeloupe','Haiti','Jamaica','Martinique','Montserrat','Puerto Rico','Saint Kitts and Nevis','Saint Lucia','Saint Vincent and the Grenadines','Sint Maarten (Dutch part)','Trinidad and Tobago','Turks and Caicos Islands','United States Virgin Islands','Belize','Costa Rica','El Salvador','Guatemala','Honduras','Mexico','Nicaragua','Panama','Argentina','Bolivia (Plurinational State of)','Brazil','Chile','Colombia','Ecuador','Falkland Islands (Malvinas)','French Guiana','Guyana','Paraguay','Peru','Suriname','Uruguay','Venezuela (Bolivarian Republic of)','Bermuda','Canada','Greenland','Saint Pierre and Miquelon','United States of America']

#################### OEA ##########################################
cols = ['Argentina','Bolivia (Plurinational State of)','Brazil','Chile','Colombia','Costa Rica','Cuba','Dominican Republic','Ecuador','El Salvador','Guatemala','Haiti','Honduras','Mexico','Nicaragua','Panama','Paraguay','Peru','United States of America','Uruguay','Venezuela (Bolivarian Republic of)','Barbados','Trinidad and Tobago','Jamaica','Grenada','Suriname','Dominica','Saint Lucia','Antigua and Barbuda','Saint Vincent and the Grenadines','Bahamas','Saint Kitts and Nevis','Canada','Belize','Guyana']
rows = ['Argentina','Bolivia (Plurinational State of)','Brazil','Chile','Colombia','Costa Rica','Cuba','Dominican Republic','Ecuador','El Salvador','Guatemala','Haiti','Honduras','Mexico','Nicaragua','Panama','Paraguay','Peru','United States of America','Uruguay','Venezuela (Bolivarian Republic of)','Barbados','Trinidad and Tobago','Jamaica','Grenada','Suriname','Dominica','Saint Lucia','Antigua and Barbuda','Saint Vincent and the Grenadines','Bahamas','Saint Kitts and Nevis','Canada','Belize','Guyana']

for table in tables:
    xls = pd.ExcelFile('UN_Migration.xlsx')
    df = xls.parse(table, header=0, skiprows=15)
    df.rename(columns={'Unnamed: 0': 'N°', 'Unnamed: 1': 'Destination', 'Unnamed: 2': 'Notes', 'Unnamed: 3': 'Country code', 'Unnamed: 4': 'Type'}, inplace=True)
    df1 = df.set_index('Destination')
    df2 = df1.loc[rows,cols]
    if (table == 'Table 1'):
        df2.insert(0, 'periodo', 1990)
        df2.to_csv('1990.csv', encoding='utf-8')
        pass
    elif (table == 'Table 4'):
        df2.insert(0, 'periodo', 1995)
        df2.to_csv('1995.csv', encoding='utf-8')
        pass
    elif (table == 'Table 7'):
        df2.insert(0, 'periodo', 2000)
        df2.to_csv('2000.csv', encoding='utf-8')
        pass
    elif (table == 'Table 10'):
        df2.insert(0, 'periodo', 2005)
        df2.to_csv('2005.csv', encoding='utf-8')
        pass
    elif (table == 'Table 13'):
        df2.insert(0, 'periodo', 2010)
        df2.to_csv('2010.csv', encoding='utf-8')
        pass
    elif (table == 'Table 16'):
        df2.insert(0, 'periodo', 2015)
        df2.to_csv('2015.csv', encoding='utf-8')
        pass
    print(table,'Done!')
