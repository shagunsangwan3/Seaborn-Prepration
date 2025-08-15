import seaborn as sns 
import pandas as pd
import matplotlib.pyplot as plt 

df = sns.load_dataset("penguins")
print(df)

# 1
sns.displot(df["bill_length_mm"])
plt.show()

# 2
sns.displot(df["flipper_length_mm"],bins=[170,180,190,200,210,220,230,240])
plt.show()

# 3 
sns.displot(df["bill_length_mm"],kde=True)
plt.show()

# 4
sns.displot(df["bill_length_mm"],kde=True,color="r",log_scale=True)
plt.show()
