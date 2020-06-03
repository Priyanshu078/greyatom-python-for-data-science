# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=np.array([[50,  9,  4,  1,  0,  0, 40,  0]])

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census=np.concatenate([data,new_record])

age=np.array(census[:,0])
max_age=age.max()
min_age=age.min()
age_mean=round(age.mean(),2)
age_std=round(np.std(age),2)

race_0=np.array([])
race_1=np.array([])
race_2=np.array([])
race_3=np.array([])
race_4=np.array([])
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]

len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

minority_race=3

senior_citizens=np.array([])
senior_citizens=census[census[:,0]>60]

working_hours_sum=senior_citizens.sum(axis=0)[6]

senior_citizens_len=len(senior_citizens)
avg_working_hours=(working_hours_sum/senior_citizens_len)

print(round(avg_working_hours,2))

high=np.array([])

low=np.array([])

high=census[census[:,1]>10]
low=census[census[:,1]<=10]

avg_pay_high=high.mean(axis=0)[7]   
avg_pay_low=low.mean(axis=0)[7]   

print(round(avg_pay_high,2))
print(round(avg_pay_low,2))




