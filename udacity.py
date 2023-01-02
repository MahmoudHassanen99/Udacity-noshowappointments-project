# Use this cell to set up import statements for all of the packages that you
#   plan to use.

import numpy as np
import pandas as pd
"import matplotlib.pyplot as plt
import seaborn as snb
% matplotlib inline"

# Load your data and print out a few lines. Perform operations to inspect data
#   types and look for instances of missing or possibly errant data.
df=pd.read_csv('noshowappointments-kagglev2-may-2016.csv')

##Data Wrangling

#to get some quick information about data
df.info()
df.describe()
#sum duplicated values in data
df.duplicated().sum()
#find unique values in data
df.nunique()
#find unique patients in data
df['PatientId'].nunique()
#find sum of duplicated Patients in data
df['PatientId'].duplicated().sum()
#check if the same patient with the same No-Show
df.duplicated(['PatientId' , 'No-show']).sum()


## Data Cleaning

#remove row which age=-1
mask= df.query('Age == "-1"')
df.drop(index = 99832 ,inplace=True)

df['Age'].describe()
df.rename(columns ={'No-show' : 'no_show'} , inplace=True)
df.rename(columns = {'Hipertension':'Hypertension'} ,inplace =True)

#remove duplicated values in data
df.drop_duplicates(['PatientId','No_show'] ,inplace=True)
df.shape

#remove unnecessary data
df.drop(['PatientId' , 'AppointId' , 'ScheduledDay' ,'AppointmentDay' ],axis=1,inplace=True )
df.head()

##Exploratory Data Analysis
# Use this, and more code cells, to explore your data. Don't forget to add
#   Markdown cells to document your observations and findings.
df.hist(figsize=(16,6));

#dividing the patients to 2 groups to showing or not
show=df.No_show=='No'
noshow=df.No_show == 'Yes'
df[show].count() , df[noshow].count()

df[show].mean() , df[noshow].mean()


## factors which are important for us to know in order to predict if a patient will show up for their scheduled appointment
#does age affect the attendence

def attendence(df,col_name ,attend,absent):
    plt.figure(figsize=((16,4))
    df[col_name][show].hist(alpha=0.5 ,bins=-10,color='blue' ,label='show')
    df[col_name][noshow].hist(alpha=0.5 ,bins=-10,color='red' ,label='noshow')
    plt.legend();
    plt.title('comparison acc. to age')
    plt.xlabel('Age')
    plt.ylabel('Patients Number');
attendence(df,'Age',show,noshow)

#does age chronic aiseases affect the attendence together
plt.figure(figsize=[16,8])
df[show].groupby(['Hypertension','Diabetes']).mean()['Age'].plot(kind='bar',color='blue' , label='show')
df[noshow].groupby(['Hypertension','Diabetes']).mean()['Age'].plot(kind='bar',color='blue' , label='noshow')
plt.legend();
plt.title('comprison acc. to age , chronic diabetes')
plt.xlabel('chronic diseases')
plt.ylabel('mean age');

df[show].groupby(['Hypertension', 'Diabetes']).mean()['Age'],df[show].groupby(['Hypertension','Diabetes']).mean()['Age']

#what is percentage of sexes attending
def attendence (df,col_name,attend,absent):
    plt.figure(figsize=[12,4])
    df[col_name][show].value_counts(normalize=True).plot(kind='pie',label= 'show')
    plt.legend();
    plt.title('Comparison between attendence by gender')
    plt.xlabel('Gender')
    plt.ylabel('Patients Numbers');
attendence[df,'Gender',shoe,noshow]

#what is percentage of sexes absent
def attendence (df,col_name,attend,absent):
    plt.figure(figsize=[12,4])
    df[col_name][noshow].value_counts(normalize=True).plot(kind='pie',label= 'show')
    plt.legend();
    plt.title('Comparison between attendence by gender')
    plt.xlabel('Gender')
    plt.ylabel('Patients Numbers');
attendence[df,'Gender',show,noshow]
#gender has no effect on attendence

#does age & chronic gender affect the attendence together

plt.figure(figsize=[12,4])
df[show].groupby('Gender').Age.mean().plot(kind='bar',color='blue',label='show')
df[noshow].groupby('Gender').Age.mean().plot(kind='bar',color='red',label='show')
plt.legend();
plt.tirle('Comparison acc. to age & chronic diseases')
plt.xlabel('Gender')
plt.ylabel('Mean age');

print( df[show].groupby('Gender').Age.mean() , df[noshow].groupby('Gender').Age.mean())
df[show].groupby('Gender').Age.mean() , df[noshow].groupby('Gender').Age.mean()

#does receiving SMS affect the attendence
def attendence(df,col_name ,attend,absent):
    plt.figure(figsize=((16,4))
    df[col_name][show].hist(alpha=0.5 ,bins=-10,color='blue' ,label='show')
    df[col_name][noshow].hist(alpha=0.5 ,bins=-10,color='red' ,label='noshow')
    plt.legend();
    plt.title('comparison acc. to receiving SMS')
    plt.xlabel('Age')
    plt.ylabel('Patients Number');
attendence(df,'SMS_received',show,noshow)

#does neighbourhood affect the attendence
plt.figure(figsize=[14,8])
df.Neighbourhood[show].value_counts(n).plot(kind='bar',color='red ',label= 'show')
df.Neighbourhood[noshow].value_counts(n).plot(kind='bar',color='blue',label= 'noshow')
plt.legend();
plt.title('Comparison acc. to neighbourhood')
plt.xlabel('Neighbourhood')
plt.ylabel('Patients Numbers');

#'neighbourhood has no effect on attendence'

plt.figure(figsize=[18,4])
df[show].groupby('Neighbourhood').Age.mean().plot(kind='bar',color='blue',label='show')
df[noshow].groupby('Gender').Age.mean().plot(kind='bar',color='red',label='show')
plt.legend();
plt.tirle('Comparison acc. to age & chronic diseases')
plt.xlabel('Gender')
plt.ylabel('Mean age');


##Limitations
from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])
