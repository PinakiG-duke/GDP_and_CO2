import pandas as pd
import matplotlib.pyplot as plt
var_data = pd.read_csv("https://github.com/nickeubank/MIDS_Data/raw/refs/heads/master/World_Development_Indicators/wdi_small_tidy_2015.csv")
var_data.head()
var_data.columns
columns = var_data[['Mortality rate, infant (per 1,000 live births)','GDP per capita (constant 2010 US$)', 'Country Name']]
plt.figure(figsize = (15,9))
plt.scatter(columns['GDP per capita (constant 2010 US$)'], columns['Mortality rate, infant (per 1,000 live births)'], alpha= 0.4)
plt.xlabel('GDP per capita')
plt.ylabel('Mortality rate, infant')
plt.title('GDP vs Mortality rate')
plt.grid(True)
plt.show()
