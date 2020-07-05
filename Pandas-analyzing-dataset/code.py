# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')

#Reading file
bank = pd.read_csv(path)
#Code starts here
categorical_var=bank.select_dtypes(include = 'object')
#print(categorical_var)
numerical_var=bank.select_dtypes(include = 'number')
#print(numerical_var)
print(categorical_var.shape)
print(numerical_var.shape)
bank.drop('Loan_ID',inplace=True,axis=1)
banks = pd.DataFrame(bank)
print(banks.isnull().sum())
print(banks.shape)
bank_mode = banks.mode().iloc[0]
banks.fillna(bank_mode,inplace=True)
print(banks.isnull().sum().values.sum())
avg_loan_amount = pd.pivot_table(banks,index=('Gender','Married','Self_Employed'),values='LoanAmount').agg(np.mean)
print(avg_loan_amount)
loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')].count()  
loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')].count()
Loan_Status = 614
percentage_se = round((loan_approved_se/Loan_Status)*100,2)
percentage_nse = round((loan_approved_nse/Loan_Status)*100,2)
print(percentage_se)
print(percentage_nse)
loan_term = banks['Loan_Amount_Term'].apply(lambda x : int(x) / 12)
big_loan_term = len(loan_term[loan_term>=25])
print(big_loan_term)
columns_to_show = ['ApplicantIncome', 'Credit_History']
loan_groupby=banks.groupby(['Loan_Status'])
loan_groupby=loan_groupby[columns_to_show]
mean_values = loan_groupby.agg(np.mean)
print(mean_values)








