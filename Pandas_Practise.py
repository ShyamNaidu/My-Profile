import pandas as pd

## Creating a dataset
# mydataset = {
#     'family_member' : ["Syam","Urmila","Rushanth","Yoswika"],
#     'age' : [40,30,10,5]       
#     }

# myvar = pd.DataFrame(mydataset)
# print(myvar)

##Prints the version of pandas
# print(pd.__version__)

##Series - like a column in a Table
# series_name = ['SNo','Name','Age','Sex']
# seriesvariable = pd.Series(series_name)
# print(seriesvariable)

##Working with Labels
# print("Label Value at index 0 = " + seriesvariable[0])
# print("Label Value at index 1 = " + seriesvariable[1])

# # Creating own Labels:
# a = [1,7,2]
# myseries = pd.Series(a,["x","y","z"])
# print(myseries)
# print("Label Value at index 0 = " + str(myseries["x"]))

# # Creating Series with key / value objects
# person_details = {"SNo":1, "Name":'Syam', "Age":40}
# person_series = pd.Series(person_details)
# print(person_series)

# # Creating Series with parts of the Labels
# person_details = {"SNo":1, "Name":'Syam', "Age":40}
# person_series = pd.Series(person_details, index = ["SNo","Name"])
# print(person_series)

# # Creating Data Frames
# data = {
#     "SNo" : [1,2,3,4],
#     "Names" :   ["Syam","Urmila","Rushanth","Yoswika"],
#     'Ages' : [40,30,10,5]
# }

# myfamily = pd.DataFrame(data)
# print(myfamily)
# print("Printing Row:")
# print(myfamily.loc[1])  #prints the 2nd record in a DataFrame
# print("Printing First Two Rows:")
# print(myfamily.loc[[0,1]])  #prints the first 2 records in a DataFrame

# #Creating own indexes instead of number indexing
# myfamily = pd.DataFrame(data,index=["Father","Mother","Son","Daughter"])
# print(myfamily)
# print("Printing Father Record:")
# print(myfamily.loc["Father"])  #prints the 2nd record in a DataFrame
# print("Printing children records:")
# print(myfamily.loc[["Son","Daughter"]])  #prints the first 2 records in a DataFrame


# # Reading csv file
# df = pd.read_csv('/workspaces/My-Profile/datastore/employees.txt')
# print(df)
# pd.options.display.max_rows = 9999
# print(pd.options.display.max_rows) 

# # Reading json file
# df = pd.read_json('/workspaces/My-Profile/datastore/jsondata.json')
# print(df.to_string())
# print(df.head())
# print(df.tail()) 
# print(df.info()) 

# Reading excercise.csv file
df = pd.read_csv('/workspaces/My-Profile/datastore/exercisecal.csv')
pd.options.display.max_rows = 200

# new_df = df.dropna()
# df.fillna(30,inplace=True)
# print(df)

x =  df["Calories"].mode()[0]
df["Calories"].fillna(x,inplace=True)
print(df)


