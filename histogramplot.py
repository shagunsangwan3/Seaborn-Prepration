import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt 

df = sns.load_dataset("penguins")
print(df)

# 1
sns.displot(df["bill_length_mm"])
plt.show()