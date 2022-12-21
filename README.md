
📝 Introduction
This code generates fake data for five districts in the state of Karnataka in India, and then creates a bar plot to visualize the data. The data includes the district names, number of new cases, number of new deaths, number of new recoveries, total number of recoveries, number of active cases, total number of deaths, and recovery rate for each district.

Overview :
The code uses the Faker library to generate random integers for each of these data points. It then stores the data for each district in a dictionary and appends the dictionaries to a list called districts.

Next, the code creates an empty Pandas DataFrame with columns for each of the data points and uses a for loop to iterate through the districts list and append the data for each district to the DataFrame.

Finally, the code uses the plot method of the DataFrame to create a bar plot and displays it using matplotlib. The plot shows the data for each district on the x-axis and the values for each data point on the y-axis.

Here is a step-by-step breakdown of the code:
1.Import the required libraries: pandas for creating and manipulating data frames, matplotlib for creating plots, and faker for generating fake data.


import pandas as pd
import matplotlib.pyplot as plt
from faker import Faker
2.Initialize the Faker object to generate fake data.


fake = Faker()
3.Create a list called districts to store the data for each district. Iterate through a range of 5 and generate fake data for each district and print the data to confirm.


districts = []
k = 0
for i in range(5):
    district_names = ["Banglore","Mysore","Hubli","Udupi","Gadag"]

    district_name = district_names[k]
    new_cases = fake.pyint(min_value=0, max_value=400)
    new_deaths = fake.pyint(min_value=0, max_value=100)
    new_recovery = fake.pyint(min_value=0, max_value=300)
    total_recovery =  fake.pyint(min_value=0, max_value=2000) + new_recovery
    active_cases = fake.pyint(min_value=0, max_value=10000) + new_cases
    total_deaths = fake.pyint(min_value=0, max_value=700) + new_deaths
    recovery_rate = (total_recovery / active_cases )
    recovery_rate = "{:.2%}".format(recovery_rate)
    
    district_data = {
        "district_name":district_name,
        "new_cases":new_cases,
        "new_deaths":new_deaths,
        "new_recovery":new_recovery,
        "total_recovery":total_recovery,
        "active_cases":active_cases,
        "total_deaths":total_deaths,
        "recovery_rate":recovery_rate
    }
    districts.append(district_data)
    k += 1
    
for district in districts:
    print(f"{district['district_name']}: {district['new_cases']} new cases , {district['active_cases']} active cases , 
          {district['new_deaths']} newDeaths ,{district['new_recovery']} newRecovery ,{district['total_recovery']} totalRecovery ,"
          f"{district['total_deaths']} totalDeaths ,{district['recovery_rate']} recoveryRate ")    
    
4 .Creating the dataframe and plotting the generated data using matplotlib.


# Create a dataframe to store the data
df = pd.DataFrame(columns=["District","New_cases","New_deaths","New_recovery","Total_recovery","Active_cases","Total_deaths","Recovery%"])


for district in districts:
    df = df.append({
        "District": district["district_name"],
        "New_cases" : district["new_cases"],
        "New_deaths": district[ "new_deaths"],
        "New_recovery": district["new_recovery"],
        "Total_recovery":district["total_recovery"],
        "Active_cases": district["active_cases"],
        "Total_deaths": district["total_deaths"],
        "Recovery%": district["recovery_rate"]
    }, ignore_index=True)

# Print the dataframe
print(df)

# Set the plot title and labels
df.plot(kind="bar")
plt.title("Covid data")
plt.show()
