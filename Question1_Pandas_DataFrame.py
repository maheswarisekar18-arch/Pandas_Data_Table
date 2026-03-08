import pandas as pd
data = {"student_id":[101,102,103,104,105,106,107,108,109,110],
         "name":["Alice","Bob","Charlie","Diana","Ethan","Fiona","George","Hannah","Ivan","Julia"],
         "age":[20,21,19,22,20,21,23,19,22,20],
         "marks":[88,75,92,65,78,85,70,95,60,80],
         "grade":["A","B","A","C","B","A","B","A","C","B"]}
df = pd.DataFrame(data)
print(df)
with open("students.csv","w") as f:
    f.write(df.to_csv(index=False)) # writing the dataframe to a csv file without the index
print("Data written to students.csv")

reload_data = pd.read_csv("students.csv") # reading the csv file into a dataframe
first_3data = reload_data.head(3) # accessing the first 3 rows of the dataframe
print("First 3 rows of the dataframe:\n", first_3data)
summary_data = reload_data.describe() # accessing the statistical summary of the dataframe
print("Statistical summary of the dataframe:\n", summary_data)
shape_data = reload_data.shape # accessing the shape of the dataframe
print("Shape of the dataframe:", shape_data)
info_data = reload_data.info() # accessing the information about the dataframe
print("Information about the dataframe:\n", info_data)

