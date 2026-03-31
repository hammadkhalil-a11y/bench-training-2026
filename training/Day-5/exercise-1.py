import pandas as pd
data = pd.read_csv("titanic.csv")

# Q1)How many passengers survived?
total = data["Survived"].count()
survived = data["Survived"].value_counts()[1]
non_survived = data["Survived"].value_counts()[0]
print(f'Total Survived: {survived} with percentage : {(survived/total)*100:.2f} %')
print(f'Total Non Survived: {non_survived} with percentage : {(non_survived/total)*100:.2f} %')

# Q2)What was the survival rate by passenger class (1st, 2nd, 3rd)?
for i in [1,2,3]:
    p_class_survivers = data[(data["Pclass"]==i) & (data["Survived"]==1)].shape[0]
    p_class_total_survivers = (data["Pclass"]==i).sum()
    print(f'Survival Rate against Pclass :{i} : {(p_class_survivers/ p_class_total_survivers)*100:.2f} %')

# Q3)Average age of survivors vs. non-survivors?
all_survivals = data[data["Survived"]==1]
avg_survival_age = (all_survivals["Age"]).mean()
print(f'Average Survival Age : {avg_survival_age:.2f} %')
all_non_survivals = data[data["Survived"]==0]
avg_non_survival_age = (all_non_survivals["Age"]).mean()
print(f'Average Non Survival Age : {avg_non_survival_age:.2f} %')

# Q4) Which embarkation port had the highest survival rate?
ports = data["Embarked"].dropna().unique()
port=''
highest_rate = 0
for port in ports:
    survived_port = data[(data["Embarked"] == port) & (data["Survived"] == 1)].shape[0]
    port_total_survived = (data["Embarked"]==port).sum()
    survived_rate = survived_port / port_total_survived
    if survived_rate > highest_rate:
        highest_rate = survived_rate
        port=port
print(f'Highest Survival Rate is {survived_rate*100.:.2f} % and is against this port: {port}')

# Q5)How many passengers have missing age values?)
age_missing_passengers = (data["Age"]).isna().sum()
print(f'Numbers of passengers with age missing are {age_missing_passengers}')
passengers_average_age= (data["Age"]).mean()
data["Age_filled"] = data["Age"].fillna(passengers_average_age)

# Q6)Who was the oldest surviving passenger? Print their name, age, class
survived_passengers = data[data["Survived"]==1]
oldest_survivor = survived_passengers[survived_passengers['Age'] == survived_passengers["Age"].max()]
print(f'Oldest Survivor Name : {oldest_survivor["Name"].iloc[0]} Age : {oldest_survivor["Age"].iloc[0]} & Pclass : {oldest_survivor["Pclass"].iloc[0]}')

# Q7)What % of women survived vs. what % of men?
male_survivors = data[(data["Survived"] == 1) & (data["Sex"]=="male")].shape[0]
female_survivors = data[(data["Survived"] == 1) & (data["Sex"]=="female")].shape[0]
survived = data["Survived"].value_counts()[1]
print(f'Male survivors: {(male_survivors/survived)*100:.2f} %')
print(f'Feale survivors: {(female_survivors/survived)*100:.2f} %')

# Q8) Create a new column AgeGroup
def age_group(age):
    if age < 18:
        return "Child"
    elif age <= 60:
        return "Adult"
    else:
        return "Senior"
data["AgeGroup"] = data["Age"].apply(age_group)

# Q9)
third_class = data[data["Pclass"] == 3]
survival_rate = third_class.groupby("Sex")["Survived"].mean()
print(survival_rate)

# Q10) Drop all rows with missing Cabin data. How many rows remain?
original_rows = data.shape[0]
data_cabin = data.dropna(subset=["Cabin"])
remaining_rows = data_cabin.shape[0]
print("Rows remaining:", remaining_rows)








