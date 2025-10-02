import pandas as di
import matplotlib.pyplot as mp 
print("-----IMPORTING THE DATASET-----")
titanic=di.read_csv("E:\DATA SCIENCE\week1\gender_submission.csv") 
print("Titanic data set:",titanic)
print("DATASET IMPORTED SUCCESSFULLY!...")

print("\n-----RENAMING THE COLUMN NAME-----")
titanic.rename(columns={"PassengerId":"Id","Survived":"Status for clarity"},inplace=True), 
print("Renamed column name:",titanic) 
print("COLUMN NAME RENAMED SUCCESSFULLY!...\n")

print("\n-----EXPLORING THE DATASET-----")
print("The Titanic data from the Top:",titanic.head()) 
print("The Titanic data from the Bottom:",titanic.tail()) 
print("Titanic dataset information:",titanic.info()) 
print("Count:",titanic.shape) 
print("DATASET EXPLORED SUCCESSFULLY!...\n")
 
print("\n-----FILTER DATA-----") 
Non_survived=titanic[titanic["Status for clarity"]==0].head(10) 
print("Top 10 Non-Survived:",Non_survived) 
survived=titanic[titanic["Status for clarity"]==1].head(10) 
print("Top 10 Survived:",survived)
print("DATA FILTERED SUCCESSFULLY!...\n")
 
print("\n-----COUNT THE TOTAL PASSENGERS-----")
Total_count=titanic["Status for clarity"].value_counts() 
survived_count=Total_count[1] 
Nonsurvived_count=Total_count[0] 
print("Total Survived:",survived_count) 
print("Total Not Survived:",Nonsurvived_count)
print("TOTAL NO.OF PASSENGERS CALCULATED SUCCESSFULLY!...\n")
 
print("\n-----PERCENTAGE OF THE TOTAL PASSENGERS-----")
Total_passengers=len(titanic) 
percentage_of_survived_passengers=(survived_count/Total_passengers)*100 
percentage_of_Nonsurvived_passengers=(Nonsurvived_count/Total_passengers)*100 
print("Percentage Survived:",percentage_of_survived_passengers) 
print("Percentage Not Survived:",percentage_of_Nonsurvived_passengers)
print("PERCENTAGE CALCULATED SUCCESSFULLY!...\n")
 
print("\n-----CREATING BARCHARTS-----")
Total_count.plot(kind='bar',color=["yellow","pink"]) 
mp.xlabel("Status 0=Not survived,1=survived") 
mp.ylabel("No of persons") 
mp.title("Survived vs non survived") 
mp.xticks(rotation=0) 
mp.show()
print("BARCHART CREATED SUCCESSFULLY!...\n")