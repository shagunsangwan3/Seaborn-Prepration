import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset("penguins")
print(df)

# 1
sns.barplot(x="island",y="bill_length_mm",data=df,hue="sex",palette="Accent")
plt.show()
