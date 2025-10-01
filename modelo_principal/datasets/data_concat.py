import pandas as pd

df_train = pd.read_csv("modelo_principal/datasets/datathon_datasets_original/03_IBD_GTstudentproject_train.csv")
df_test = pd.read_csv("modelo_principal/datasets/datathon_datasets_original/03_IBD_GTstudentproject_test.csv")
print(df_train.head())