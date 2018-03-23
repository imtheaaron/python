#GENERAL PYTHON FUNCTIONS
#_________________________

#to open and perform functions on a file:
with open(budget_path, newline='') as budget_csv:

#to iterate over rows (from a read csv, json, etc):
for row in employee_reader1:

#zip two lists together:
employee_list = zip(emp_id, first_name, last_name, formatted_dob, hidden_ssn, state_abbrev)

#write to a csv:
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(['Employee ID', 'First Name', 'Last Name', 'Date of Birth', 'SSN', 'State'])

    writer.writerows(employee_list)

#Use a function to create a list- "List Comprehension"
ex: odds = [ 2*i + i for i in range(10)]  #<--- this will return a list of odd numbers from 1 to 19

#PANDAS FUNCTIONS
#_________________________
.unique()
.value_counts()
.groupby('Column Name')
    #can also group by multiple columns:
    .groupby(['column 1', 'column 2'])
.drop_duplicates
.query('value>10000')
.dtypes #(shows the data types in the dataframe)
df.describe(include='all') #<--this will describe all data including text data in the df

#series methods add one series to another CAN DO THIS (the .add fxn) with dataframes too
series3 = series1.add(series2, fill_value=0) #<--fill_value=0 will put a 0 in empty entries (instead of NaN)

#exclude certain values from a dataframe
df = df[df.gender != 'stoptime'] #<--this grabs any value with entry 'stoptime' in the gender column and removes it

#construct a dataframe:
pd.DataFrame({'column name': column values, 'next column name': next column values})

#reorder dataframe columms
df = df[['column 2', 'column 1']] or
    df.columns = ['column 1', 'column 2']

#merge two dataframes
new_df = pd.merge(df1, df2, on='column name', how='outer')

#run arithmetic operations in a dataframe, ex:
age_counts_df['Percentage of Players'] = 100 * age_counts_df['Age'] / age_counts_df['Age'].sum()

#create and sort data by bins
bins = [0, 9, 14, 19, 24, 29, 34, 39, 100]
age_names = ['>10', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '>40']
age_column = pd.cut(df_unique['Age'], bins, labels=age_names)

#format a column - this will format into dollar value notation:
df['column'] = df['column'].map("${:,.2f}".format)

#rename a column
df = df.rename(columns={'original column name': 'new column name'})

#change the format of the entries in a column
pd.to_numeric(df.column) #to numeric
    pd.to_numeric(df.column, errors='coerce') #this will to any string values that can't be made numeric
        #and will just drop them and leave a NaN entry
    pd.to_datetime(df.column) #where the entries in the column are dates

#select data based on a condition
ex: df = df['column' < 10000] #<-- this will remove all the data above 10,000 in that column

#reset an index
.reset_index()

#set a column as the index
.set_index('column')

#sort values on values in a column
.sort_values('column', ascending=False)

#sort the index
.sort_index(axis=0)

#plot using matplotlib
df.column.plot #(will plot on the index as x axis)
df.plot(x=df.column, style='.-', figsize=(15,4)) #<-- this will plot using the specified column as the x axis

#NUMPY FUNCTIONS
#___________________

#create an array
x_axis = np.arange(0, 10, 0.1)  #will return an array of number from 0 to 9.9 by 0.1 intervals

#MATPLOTLIB FUNCTIONS

#can plot the results of Pandas functions like a .value_counts
df.column.value_counts().plot(kind='bar')

#change plot size
df.plot(figsize=(10,10))

