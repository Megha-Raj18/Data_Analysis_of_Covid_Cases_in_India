import pandas as pd
data1=pd.read_csv('COVID-19 Cases(11-08-2021).csv')
data=data1.copy()
data.head(5)


# In[3]:


data.shape


# In[4]:


data.columns


# In[5]:


data['Date'][0]


# In[6]:


type(data['Date'][0])


# In[7]:


data.tail()


# In[8]:


data_k=data[data['Region']=='Karnataka']
k_data=data_k.copy()
k_data.tail(10)


# In[9]:


daily_cases_list=[]
daily_cases_list.append(0)
for row in range(0,len(k_data)):
    if row!=len(k_data)-1:
        daily_cases_list.append(k_data.iloc[row+1]['Confirmed Cases']-k_data.iloc[row]['Confirmed Cases'])
k_data['Daily Confirmed Cases']=daily_cases_list   


# In[10]:


daily_death_list=[]
daily_death_list.append(0)
for row in range(0,len(k_data)):
    if row!=len(k_data)-1:
        daily_death_list.append(k_data.iloc[row+1]['Death']-k_data.iloc[row]['Death'])
k_data['Daily Deaths']=daily_death_list


# In[11]:


daily_active_list=[]
daily_active_list.append(0)
for row in range(0,len(k_data)):
    if row!=len(k_data)-1:
        daily_active_list.append(k_data.iloc[row+1]['Active Cases']-k_data.iloc[row]['Active Cases'])
k_data['Daily Active Cases']=daily_active_list


# In[12]:


daily_cured_list=[]
daily_cured_list.append(0)
for row in range(0,len(k_data)):
    if row!=len(k_data)-1:
        daily_cured_list.append(k_data.iloc[row+1]['Cured/Discharged']-k_data.iloc[row]['Cured/Discharged'])
k_data['Daily Cured/Discharged']=daily_cured_list


# In[13]:


k_data


# In[14]:


import datetime as dt
test_date='24/08/2021'
date_obj=dt.datetime.strptime(test_date,'%d/%m/%Y')


# In[15]:


date_obj


# In[16]:


k_data['Date'].iloc[0]


# In[17]:


import datetime as dt
new_date_list=[]
for row in range(len(k_data)):
    new_date_list.append(dt.datetime.strptime(k_data['Date'].iloc[row],'%d/%m/%Y'))
k_data['New Dates']=new_date_list


# In[18]:


k_data


# In[19]:


k_data_copy=k_data.copy()


# In[20]:


k_data_copy.drop('Date',axis=1,inplace=True)


# In[21]:


k_data_copy


# In[22]:


weekday_numbers=[]
for row in range(len(k_data_copy)):
    weekday_numbers.append(k_data_copy['New Dates'].iloc[row].isoweekday())
k_data_copy['Weekday Number']=weekday_numbers


# In[23]:


k_data_copy


# In[24]:



def get_weekday(num):
    weekdays={1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday',7:'Sunday'}
    return weekdays[num]


# In[ ]:





# In[25]:


k_data_copy['Weekday']=list(map(get_weekday,list(k_data_copy['Weekday Number'])))


# In[26]:


k_data_copy


# In[27]:


avg_cases_per_day=k_data_copy.groupby(['Weekday','Weekday Number']).mean().round(2)


# In[28]:


avg_cases_per_day


# In[29]:


type(list(avg_cases_per_day.index))


# In[30]:


avg_cases_per_day=avg_cases_per_day.sort_values('Weekday Number')


# In[31]:


avg_cases_per_day


# # On which day are the most number of cases recorded daily in Karnataka?
# 

# In[32]:


import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot(x = list(avg_cases_per_day.index.get_level_values(0)),
            y = 'Daily Confirmed Cases',
            data = avg_cases_per_day)

plt.show()


# # On what day is the most number of deaths recorded in Karnataka?

# In[33]:


sns.barplot(x = list(avg_cases_per_day.index.get_level_values(0)),
            y = 'Daily Deaths',
            data = avg_cases_per_day)

plt.show()


# In[34]:


k_data_copy


# In[35]:


k_data


# In[36]:


k_data_copy['New Dates'].iloc[0]


# In[ ]:





# In[37]:



month_number_list=[]
for row in range(len(k_data_copy)):
    month_number_list.append(k_data_copy['New Dates'].iloc[row].month)
k_data_copy['Month Number']=month_number_list
k_data_copy


# In[38]:


year_list=[]
for row in range(len(k_data_copy)):
    year_list.append(k_data_copy['New Dates'].iloc[row].year)
k_data_copy['Year']=year_list
k_data_copy


# In[39]:


def get_month(num):
    weekdays={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
    return weekdays[num]

k_data_copy['Month']=list(map(get_month,list(k_data_copy['Month Number'])))
k_data_copy


# In[40]:


avg_cases_per_month=k_data_copy.groupby(['Year','Month','Month Number']).mean().round()


# In[41]:


avg_cases_per_month


# In[42]:


avg_cases_per_month_2020=avg_cases_per_month.loc[2020]
avg_cases_per_month_2020


# In[43]:


avg_cases_per_month_2020=avg_cases_per_month_2020.sort_values('Month Number')
avg_cases_per_month_2020


# In[44]:


avg_cases_per_month_2020['Month Name']=list(avg_cases_per_month_2020.index.get_level_values(0))
avg_cases_per_month_2020


# # Which month in the year 2020 had the most average number of cases per day in Karnataka?

# In[45]:


sns.barplot(x = list(avg_cases_per_month_2020.index.get_level_values(0)),
            y = 'Daily Confirmed Cases',
            data = avg_cases_per_month_2020)

plt.show()


# In[46]:


avg_cases_per_month_2021=avg_cases_per_month.loc[2021]


# In[ ]:





# In[47]:


avg_cases_per_month_2021['Month Name']=list(avg_cases_per_month_2021.index.get_level_values(0))
avg_cases_per_month_2021


# In[48]:


avg_cases_per_month_2021=avg_cases_per_month_2021.sort_values('Month Number')


# In[49]:


avg_cases_per_month_2021


# # Which month in the year 2021 had the most average number of cases per day in Karnataka?

# In[50]:


sns.barplot(x = list(avg_cases_per_month_2021.index.get_level_values(0)),
            y = 'Daily Confirmed Cases',
            data = avg_cases_per_month_2021)

plt.show()


# In[51]:


k_data_copy


# In[52]:


len(data[data['Region']=='State assignment pending'])


# In[53]:




# sns.lineplot( x=list(avg_cases_per_month_2020.index.get_level_values(0)), y='Daily Confirmed Cases',data=avg_cases_per_month_2020, palette="tab10", linewidth=2.5)
# plt.show()


# In[54]:


data.drop(data[data['Region']=='State assignment pending'].index,axis=0,inplace=True)


# In[55]:


data


# In[56]:


def get_daily(df,col_name):
    daily_list=[]
    daily_list.append(0)
    for row in range(0,len(df)):
        if row!=len(df)-1:
            daily_list.append(df.iloc[row+1][col_name]-df.iloc[row][col_name])
    df[col_name]=daily_list 


# In[57]:


test=data.copy()
len(test)


# In[58]:


test.drop(test[test['Region']=='India'].index,axis=0,inplace=True)


# In[59]:


test.drop(test[test['Region']=='World'].index,axis=0,inplace=True)


# In[60]:


list_of_states=list(test.groupby('Region').mean().index)


# In[61]:


test2=test[test['Region']=='Karnataka']
test


# In[62]:


daily_cases=[]
for state in range(len(list_of_states)):
    daily_cases.append(0)
    state_df=test[test['Region']==list_of_states[state]]
    for row in range(0,len(state_df)):
        if row!=len(state_df)-1:
            daily_cases.append(state_df.iloc[row+1]['Confirmed Cases']-state_df.iloc[row]['Confirmed Cases'])
            
print(len(daily_cases))


# In[63]:


print(len(test))


# In[64]:


test['Daily Cases']=daily_cases


# In[65]:


daily_deaths=[]
for state in range(len(list_of_states)):
    daily_deaths.append(0)
    state_df=test[test['Region']==list_of_states[state]]
    for row in range(0,len(state_df)):
        if row!=len(state_df)-1:
            daily_deaths.append(state_df.iloc[row+1]['Death']-state_df.iloc[row]['Death'])
print(len(daily_deaths))


# In[66]:


test['Daily Deaths']=daily_deaths


# In[67]:


test


# In[68]:


dates=[]
for row in range(len(test)):
    dates.append(dt.datetime.strptime(test['Date'].iloc[row],'%d/%m/%Y'))
test['Date']=dates


# In[69]:


#2020-03-12 to 2021-08-09


# In[70]:


pd.date_range(start="12 3 2020",end="9 8 2021",freq='D')


# In[71]:


#total dates are 502
graph_conf_cases_list=[]
for state in range(len(list_of_states)):
    temp_list=[]
    temp_list.append(0)
    state_df=test[test['Region']==list_of_states[state]]
    for row in range(0,len(state_df)):
        if row!=len(state_df)-1:
            temp_list.append(state_df.iloc[row+1]['Confirmed Cases']-state_df.iloc[row]['Confirmed Cases'])
    graph_conf_cases_list.append(temp_list)


# In[72]:


test


# In[73]:


dt.datetime(2021,9,8)


# In[74]:


test[test['Date']==dt.datetime(2020,3,12)]


# In[75]:


test.groupby('Date').sum()


# In[76]:


test[test['Region']=='Sikkim']


# In[77]:


len(min(graph_conf_cases_list))


# In[ ]:





# In[78]:



# dates = pd.date_range(start="12 3 2020",end="9 8 2021",freq='D')
# data = pd.DataFrame(graph_arr, dates, columns=list_of_states)
# sns.lineplot(data=data, palette="tab10", linewidth=2.5)


# In[ ]:





# In[79]:


test


# In[80]:


k_data_copy


# In[ ]:





# In[82]:


test.groupby('Date').sum()


# In[83]:


test.groupby('Date').sum().index


# In[84]:


import plotly.graph_objects as go

import pandas as pd


# Create figure
fig = go.Figure()

fig.add_trace(
    go.Scatter(x=list(test.groupby('Date').sum().index), y=list(test.groupby('Date').sum()['Daily Cases'])))

# Set title
fig.update_layout(
    title_text="Total Number of Daily COVID Cases in India(From 2020-03-12 To 2021-08-09)"
)

# Add range slider
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

fig.show()


# In[85]:


test.groupby('Date').sum()


# In[ ]:





# In[86]:


plot=sns.boxplot(x=test.groupby('Date').sum()['Daily Cases'])


# In[87]:


#could use MICE(Multiple Imputation by Chained Equations) but not much knowledge in that.
#hence just used the average of that week's cases(why?)


# In[88]:


outliers=test.groupby('Date').sum()


# In[89]:


outliers


# In[90]:


outliers['Dates']=outliers.index


# In[91]:


dates_in_string=[]
for row in range(len(outliers['Dates'])):
    dates_in_string.append(outliers['Dates'].iloc[row].strftime("%Y%m%d"))
outliers['Date String']=dates_in_string


# In[92]:


outliers


# In[93]:


outliers_week=outliers[(outliers['Date String']>='20210511') & (outliers['Date String']<='20210518')]


# In[94]:


outliers_week.drop(index=dt.datetime(2021,5,14),inplace=True,axis=0)


# In[95]:


outliers_week.drop(index=dt.datetime(2021,5,16),inplace=True,axis=0)
outliers_week


# In[96]:


replacement_value=outliers_week['Daily Cases'].mean()


# In[97]:


group_by_date=test.groupby('Date').sum()


# In[98]:


group_by_date


# In[99]:


group_by_date.loc[dt.datetime(2021,5,14),'Daily Cases']=replacement_value


# In[100]:


group_by_date.loc[dt.datetime(2021,5,14),'Daily Cases']


# In[101]:


group_by_date.loc[dt.datetime(2021,5,16),'Daily Cases']=replacement_value


# In[102]:


group_by_date.loc[dt.datetime(2021,5,16),'Daily Cases']


# In[103]:


group_by_date


# In[104]:


import plotly.graph_objects as go

import pandas as pd


# Create figure
new_fig= go.Figure()

new_fig.add_trace(
    go.Scatter(x=list(group_by_date.index), y=list(group_by_date['Daily Cases'])))

# Set title
new_fig.update_layout(
    title_text="Total Number of Daily COVID Cases in India(From 2020-03-12 To 2021-08-09)"
)

# Add range slider
new_fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

new_fig.show()


# In[105]:


newplot=sns.boxplot(x=group_by_date['Daily Cases'])  #now we have dealt with the outlier
