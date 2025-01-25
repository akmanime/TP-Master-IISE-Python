import pandas as pd

df = pd.read_csv("employees.csv")

print("Cinq premiers lignes")
print(df.head())
moyenne_salaire = df['salary'].mean()
print(f'La moyenne : {moyenne_salaire}')