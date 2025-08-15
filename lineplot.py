import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset("penguins")
print(df)

# 1
sns.lineplot(x="body_mass_g",y="sex",data=df)
plt.show()

# 2
var = [1,2,3,5,6,9,8]
var1 = [1,2,3,4,6,7,8]
xy1 = pd.DataFrame({"var":var,"var1":var1})
sns.lineplot(x="var",y="var1",data=xy1)
plt.show()