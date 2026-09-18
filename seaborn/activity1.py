import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv("Iris.csv") 
print(df.columns)
sb.displot(df['PetalLengthCm'])
plt.show()