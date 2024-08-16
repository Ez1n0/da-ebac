import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('gasolina.csv',delimiter=',')
plt.figure(figsize=(8,6))
sns.lineplot(data=df,x='dia',y='venda',color='red')