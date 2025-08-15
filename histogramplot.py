import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt 

df = sns.load_dataset("penguins")
print(df)

# 1
sns.histplot(["bill_length_mm"])
plt.show