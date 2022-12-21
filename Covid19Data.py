import pandas as pd
import matplotlib.pyplot as plt
from faker import Faker

fake = Faker()

# Generate fake data for multiple districts
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
    print(f"{district['district_name']}: {district['new_cases']} new cases , {district['active_cases']} active cases , {district['new_deaths']} newDeaths ,{district['new_recovery']} newRecovery ,{district['total_recovery']} totalRecovery ,"
          f"{district['total_deaths']} totalDeaths ,{district['recovery_rate']} recoveryRate ")

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
# plt.xlabel("District")
plt.show()


