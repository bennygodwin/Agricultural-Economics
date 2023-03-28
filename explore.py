import streamlit as st
import numpy as np 
import pandas as pd 
import seaborn as sns
import plotly.express as px 
import plotly.graph_objects as go 
import matplotlib.pyplot as plt 
from chart_studio import plotly as py 
from plotly import tools 
from plotly.subplots import make_subplots as sub

def rice():
    temp = df.groupby(['Year'],as_index = False)['RICE PRODUCTION (1000 tons)'].sum()[['Year','RICE PRODUCTION (1000 tons)']]
    fig = px.line(temp, 'Year', 'RICE PRODUCTION (1000 tons)',title='Line Plot Between Year and Rice Production')
    st.plotly_chart(fig)

    fig = sub(rows=1,cols=2,
                        subplot_titles=('Highest Rice producing districts', 'Least overall Rice producing districts'))


    temp = df.groupby(['Dist Name'],as_index = False)['RICE PRODUCTION (1000 tons)'].sum().sort_values('RICE PRODUCTION (1000 tons)',ascending=False).reset_index()[['Dist Name','RICE PRODUCTION (1000 tons)']]
    temp1 = temp.head()
    trace1 = go.Bar(x= temp1['Dist Name'], y=temp1['RICE PRODUCTION (1000 tons)'])

    temp1=temp.tail()
    trace2 = go.Bar(x= temp1['Dist Name'], y=temp1['RICE PRODUCTION (1000 tons)'])

    fig.append_trace(trace1,1,1)
    fig.append_trace(trace2,1,2)
    st.plotly_chart(fig)
    del temp,temp1

    temp = df.groupby(['State Name'],as_index = False)['RICE PRODUCTION (1000 tons)'].sum()

    fig = px.bar(temp, 'State Name', 'RICE PRODUCTION (1000 tons)', color='RICE PRODUCTION (1000 tons)',title='Bar Plot Between States and Rice Production')
    st.plotly_chart(fig)
    fig1 = px.pie(temp, values='RICE PRODUCTION (1000 tons)', names='State Name',title='Pie Plot Between States and Rice Production')
    st.plotly_chart(fig1)

def wheat():
    temp = df.groupby(['Year'],as_index = False)['WHEAT PRODUCTION (1000 tons)'].sum()[['Year','WHEAT PRODUCTION (1000 tons)']]
    fig = px.line(temp, 'Year', 'WHEAT PRODUCTION (1000 tons)',title='Line Plot Between Year and Wheat Production')
    st.plotly_chart(fig)

    fig = sub(rows=1,cols=2,
                        subplot_titles=('Highest Wheat producing districts', 'Least overall Wheat producing districts'))


    temp = df.groupby(['Dist Name'],as_index = False)['WHEAT PRODUCTION (1000 tons)'].sum().sort_values('WHEAT PRODUCTION (1000 tons)',ascending=False).reset_index()[['Dist Name','WHEAT PRODUCTION (1000 tons)']]
    temp1 = temp.head()
    trace1 = go.Bar(x= temp1['Dist Name'], y=temp1['WHEAT PRODUCTION (1000 tons)'])

    temp1=temp.tail()
    trace2 = go.Bar(x= temp1['Dist Name'], y=temp1['WHEAT PRODUCTION (1000 tons)'])

    fig.append_trace(trace1,1,1)
    fig.append_trace(trace2,1,2)
    st.plotly_chart(fig)
    del temp,temp1

    temp = df.groupby(['State Name'],as_index = False)['WHEAT PRODUCTION (1000 tons)'].sum()

    fig = px.bar(temp, 'State Name', 'WHEAT PRODUCTION (1000 tons)', color='WHEAT PRODUCTION (1000 tons)',title='Bar Plot Between States and Wheat Production')
    st.plotly_chart(fig)
    fig1 = px.pie(temp, values='WHEAT PRODUCTION (1000 tons)', names='State Name',title='Pie Plot Between States and Wheat Production')
    st.plotly_chart(fig1)

def kharif():
    temp = df.groupby(['Year'],as_index = False)['KHARIF SORGHUM PRODUCTION (1000 tons)'].sum()[['Year','KHARIF SORGHUM PRODUCTION (1000 tons)']]
    fig = px.line(temp, 'Year', 'KHARIF SORGHUM PRODUCTION (1000 tons)',title='Line Plot Between Year and Kharif Production')
    st.plotly_chart(fig)

    fig = sub(rows=1,cols=2,
                        subplot_titles=('Highest Kharif Sorghum producing districts', 'Least overall Kharif Sorghum producing districts'))


    temp = df.groupby(['Dist Name'],as_index = False)['KHARIF SORGHUM PRODUCTION (1000 tons)'].sum().sort_values('KHARIF SORGHUM PRODUCTION (1000 tons)',ascending=False).reset_index()[['Dist Name','KHARIF SORGHUM PRODUCTION (1000 tons)']]
    temp1 = temp.head()
    trace1 = go.Bar(x= temp1['Dist Name'], y=temp1['KHARIF SORGHUM PRODUCTION (1000 tons)'])

    temp1=temp.tail()
    trace2 = go.Bar(x= temp1['Dist Name'], y=temp1['KHARIF SORGHUM PRODUCTION (1000 tons)'])

    fig.append_trace(trace1,1,1)
    fig.append_trace(trace2,1,2)
    st.plotly_chart(fig)
    del temp,temp1

    temp = df.groupby(['State Name'],as_index = False)['KHARIF SORGHUM PRODUCTION (1000 tons)'].sum()

    fig = px.bar(temp, 'State Name', 'KHARIF SORGHUM PRODUCTION (1000 tons)', color='KHARIF SORGHUM PRODUCTION (1000 tons)',title='Bar Plot Between States and Kharif Production')
    st.plotly_chart(fig)
    fig1 = px.pie(temp, values='KHARIF SORGHUM PRODUCTION (1000 tons)', names='State Name',title='Pie Plot Between States and Kharif Production')
    st.plotly_chart(fig1)

def rabi():
    temp = df.groupby(['Year'],as_index = False)['RABI SORGHUM PRODUCTION (1000 tons)'].sum()[['Year','RABI SORGHUM PRODUCTION (1000 tons)']]
    fig = px.line(temp, 'Year', 'RABI SORGHUM PRODUCTION (1000 tons)',title='Line Plot Between Year and Rabi Production')
    st.plotly_chart(fig)

    fig = sub(rows=1,cols=2,
                        subplot_titles=('Highest Rabi Sorghum producing districts', 'Least overall Rabi Sorghum producing districts'))


    temp = df.groupby(['Dist Name'],as_index = False)['RABI SORGHUM PRODUCTION (1000 tons)'].sum().sort_values('RABI SORGHUM PRODUCTION (1000 tons)',ascending=False).reset_index()[['Dist Name','RABI SORGHUM PRODUCTION (1000 tons)']]
    temp1 = temp.head()
    trace1 = go.Bar(x= temp1['Dist Name'], y=temp1['RABI SORGHUM PRODUCTION (1000 tons)'])

    temp1=temp.tail()
    trace2 = go.Bar(x= temp1['Dist Name'], y=temp1['RABI SORGHUM PRODUCTION (1000 tons)'])

    fig.append_trace(trace1,1,1)
    fig.append_trace(trace2,1,2)
    st.plotly_chart(fig)
    del temp,temp1

    temp = df.groupby(['State Name'],as_index = False)['RABI SORGHUM PRODUCTION (1000 tons)'].sum()

    fig = px.bar(temp, 'State Name', 'RABI SORGHUM PRODUCTION (1000 tons)', color='RABI SORGHUM PRODUCTION (1000 tons)',title='Bar Plot Between States and Rabi Production')
    st.plotly_chart(fig)
    fig1 = px.pie(temp, values='RABI SORGHUM PRODUCTION (1000 tons)', names='State Name',title='Pie Plot Between States and Rabi Production')
    st.plotly_chart(fig1)

def all():
    temp = df.groupby(['Year'],as_index = False)['RICE PRODUCTION (1000 tons)','WHEAT PRODUCTION (1000 tons)','KHARIF SORGHUM PRODUCTION (1000 tons)','RABI SORGHUM PRODUCTION (1000 tons)'].sum()
    fig = px.line(temp,x="Year", y=['RICE PRODUCTION (1000 tons)','WHEAT PRODUCTION (1000 tons)','KHARIF SORGHUM PRODUCTION (1000 tons)','RABI SORGHUM PRODUCTION (1000 tons)'],width=1000,height=400,title='Line Plot')
    st.plotly_chart(fig)



def q1():
    temp = df1.groupby(['State Name'],as_index = False)['Total Production (1000 tons)'].sum()
    fig = px.bar(df1, 'State Name', 'Total Production (1000 tons)', color='Total Production (1000 tons)',title='Bar Plot Between States and Total Crop Production')
    fig1 = px.pie(temp, values='Total Production (1000 tons)', names='State Name',title='Pie Plot Between States and Total Crop Production')
    st.plotly_chart(fig)
    st.plotly_chart(fig1)

def q2():
    fig = sub(rows=1,cols=2,
                    subplot_titles=('Highest crop producing districts', 'Least overall crop producing districts'))


    temp = df.groupby(['Dist Name'],as_index = False)['Total Production (1000 tons)'].sum().sort_values('Total Production (1000 tons)',ascending=False).reset_index()[['Dist Name','Total Production (1000 tons)']]
    temp1 = temp.head()
    trace1 = go.Bar(x= temp1['Dist Name'], y=temp1['Total Production (1000 tons)'])

    temp1=temp.tail()
    trace2 = go.Bar(x= temp1['Dist Name'], y=temp1['Total Production (1000 tons)'])

    fig.append_trace(trace1,1,1)
    fig.append_trace(trace2,1,2)
    st.plotly_chart(fig)
    del temp,temp1

def q3():
    temp = df1.groupby(['State Name'],as_index = False)['Total Area (1000 ha)'].sum()
    fig = px.bar(df1, 'State Name', 'Total Area (1000 ha)', color='Total Area (1000 ha)',title='Bar Plot Between States and Total Agriculture Land Area')
    st.plotly_chart(fig)
    fig1 = px.pie(temp, values='Total Area (1000 ha)', names='State Name',title='Pie Plot Between States and Total Agriculture Land Area')
    st.plotly_chart(fig1)

def q4():
    fig = sub(rows=1,cols=2,
                    subplot_titles=('Highest crop field districts', 'Least overall crop field districts'))


    temp = df.groupby(['Dist Name'],as_index = False)['Total Area (1000 ha)'].sum().sort_values('Total Area (1000 ha)',ascending=False).reset_index()[['Dist Name','Total Area (1000 ha)']]
    temp1 = temp.head()
    trace1 = go.Bar(x= temp1['Dist Name'], y=temp1['Total Area (1000 ha)'])

    temp1=temp.tail()
    trace2 = go.Bar(x= temp1['Dist Name'], y=temp1['Total Area (1000 ha)'])

    fig.append_trace(trace1,1,1)
    fig.append_trace(trace2,1,2)
    st.plotly_chart(fig)
    del temp,temp1

def q5():
    fig = px.scatter(df,"Total Area (1000 ha)","Total Production (1000 tons)",title='Scatter Plot Between Total Agriculture Land Area and Total Crop Production')
    st.plotly_chart(fig)
    fig1 = plt.figure(figsize=(10,6))
    st.write('Correlation Heatmap Between Total Agriculture Land Area and Total Crop Production')
    sns.heatmap(df[["Total Area (1000 ha)","Total Production (1000 tons)"]].corr(),annot=True)
    st.pyplot(fig1)

def q6():
    temp = df.groupby(by='Year')['Total Production (1000 tons)'].sum().reset_index()
    fig = px.line(temp, 'Year', 'Total Production (1000 tons)',title='Line Plot Between Year and Total Crop Production')
    st.plotly_chart(fig)

def q7():
    temp = df1.sort_values(by='Total Yield (Kg per ha)')
    fig = px.bar(temp, 'State Name', 'Total Yield (Kg per ha)', color='Total Yield (Kg per ha)',title='Bar Plot Between States and Total Yield')
    st.plotly_chart(fig)

def q8():
    crops = (
        "Rice","Wheat","Kharif","Rabi","Year wise Analysis for All Four Crops Production"
    )
    crop = st.selectbox("Select Crop: ",crops)
    if crop == "Rice":
        rice()
        st.write('''
        ### **Inference:**
- The visualisation takes attributes 'Year' and 'RICE PRODUCTION (1000 tons)' from the dataframe to display a line plot. It shows us the production of rice in terms of 1000 tons every year. From the above visualisation we can infer that  the rice production was at it's highest peak on the year 2016 whereas it was at the lowest in the year 2009.
- The visualisation takes attributes 'Dist Name' and 'RICE PRODUCTION (1000 tons)' from the dataframe to display two bar charts. It shows us the total production of RICE in terms of 1000 tons district wise. From the above visualisation we can infer that Burdwan district has produced the most numbber of RICE crop than any other district. The other plot lists the names of the district which have no production of rice.
- The visualisation takes attributes 'State Name' and df'RICE PRODUCTION (1000 tons)' from the dataframe to display a bar plot and a pie chart. It shows us the production of rice in terms of 1000 tons for each state in India. From the above visualisation we can infer that rice is produced the most in the state of uttar pradesh whereas the lowest production is found in the state of Himachal Pradesh''')
    elif crop == "Wheat":
        wheat()
        st.write('''
        ### **Inference:**
- The visulaisation takes attributes 'Year' and 'WHEAT PRODUCTION (1000 tons)' from the dataframe to display a line plot. It shows us the production of wheat in terms of 1000 tons every year. From the above visualisation we can infer that  the rice production was at it's highest peak on the year 2016 whereas it was at the lowest in the year 2014.
- The visualisation takes attributes 'Dist Name' and 'WHEAT PRODUCTION (1000 tons)' from the dataframe to display two bar charts. It shows us the total production of WHEAT in terms of 1000 tons district wise. From the above visualisation we can infer that Karnal district has produced the most number of Wheat crop than any other district. The other plot lists the names of the district which have no production of WHEAT.
- The visualisation takes attributes 'State Name' and 'WHEAT PRODUCTION (1000 tons)' from the dataframe to display a bar plot and a pie chart. It shows us the production of wheat in terms of 1000 tons for each state in India. From the above visualisation we can infer that rice is produced the most in the state of uttar pradesh.''')
    elif crop == "Kharif":
        kharif()
        st.write('''
        ### **Inference:**
- The visulaisation takes attributes 'Year' and 'KHARIF SORGHUM PRODUCTION (1000 tons)' from the dataframe to display a line plot. It shows us the production of kharif sorghum in terms of 1000 tons every year. From the above visualisation we can infer that  the kharif sorghum production was at it's highest peak on the year 2010 whereas it was at the lowest in the year 2015.
- The visualisation takes attributes 'Dist Name' and 'KHARIF SORGHUM PRODUCTION (1000 tons)' from the dataframe to display two bar charts. It shows us the total production of KHARIF SORGHUM in terms of 1000 tons district wise. From the above visualisation we can infer that Jalgaon district has produced the most numbber of KHARIF SORGHUM crop than any other district.
- The visualisation takes attributes 'State Name' and 'KHARIF SORGHUM PRODUCTION (1000 tons)' from the dataframe to display a bar plot and a pie chart. It shows us the production of kharif sorghum in terms of 1000 tons for each state in India. From the above visualisation we can infer that kharif sorghum is produced the most in the state of Maharashtra.''')
    elif crop == "Rabi":
        rabi()
        st.write('''
        ### **Inference:**
- The visulaisation takes attributes 'Year' and 'RABI SORGHUM PRODUCTION (1000 tons)' from the dataframe to display a line plot. It shows us the production of rabi sorghum in terms of 1000 tons every year. From the above visualisation we can infer that  the rabi sorghum production was at it's highest peak on the year 2009 whereas it was at the lowest in the year 2015.
- The visualisation takes attributes 'Dist Name' and 'RABI SORGHUM PRODUCTION (1000 tons)' from the dataframe to display two bar charts. It shows us the total production of RABI SORGHUM in terms of 1000 tons district wise. From the above visualisation we can infer that Solapur district has produced the most numbber of RABI SORGHUM crop than any other district whereas there also exists districts where there are no production of RABI SORGHUM
- The visualisation takes attributes 'State Name' and 'RABI SORGHUM PRODUCTION (1000 tons)' from the dataframe to display a bar plot and a pie chart. It shows us the production of rabi sorghum in terms of 1000 tons for each state in India. From the above visualisation we can infer that rabi sorghum is produced the most in the state of Maharashtra.''')
    else:
        all()
        st.write('''
        ### **Inference:**
The visualisation takes attributes 'Year','RICE PRODUCTION (1000 tons)','WHEAT PRODUCTION (1000 tons)','KHARIF SORGHUM PRODUCTION (1000 tons)' and 'RABI SORGHUM PRODUCTION (1000 tons)' from the dataframe to display a line plot. It shows us the year wise production of all the four crops including RICE,WHEAT,KHARIF SORGHUM and RABI SORGHUM. From the above visualisation we can infer that Rice and wheat are very high as compared to the production of kharif sorghum and rabi sorghum. We can also observe the peak production of crops RICE and WHEAT are on the year 2016.''')



def q9():
    fig = px.scatter(df,'Rainfall(mm)','Total Production (1000 tons)',title='Scatter Plot Between Rainfall and Total Crop Production')
    st.plotly_chart(fig)
    fig1 = plt.figure(figsize=(10,6))
    st.write('Correlation Between Rainfall and Total Crop Production')
    sns.heatmap(df[["Rainfall(mm)","Total Production (1000 tons)"]].corr(),annot=True)
    st.pyplot(fig1)

def q10():
    temp = df1.groupby(['Year'],as_index = False)['GROSS STATE VALUE ADDED BY ECONOMIC ACTIVITY-AGRICULTURE(Average Prices)','GROSS STATE DOMESTIC PRODUCT (Average Prices)','Total Production (1000 tons)'].sum()
    fig = px.line(temp,x="Year",y=['GROSS STATE VALUE ADDED BY ECONOMIC ACTIVITY-AGRICULTURE(Average Prices)','GROSS STATE DOMESTIC PRODUCT (Average Prices)'],width=1000,height=400,title='Line Plot To Analyse Economy')
    st.plotly_chart(fig)
    fig1 = px.bar(temp, 'Year', 'Total Production (1000 tons)', color='Total Production (1000 tons)',title='Bar Plot')
    st.plotly_chart(fig1)

    temp1 = df1.groupby(['State Name'],as_index = False)['GROSS STATE VALUE ADDED BY ECONOMIC ACTIVITY-AGRICULTURE(Average Prices)','GROSS STATE DOMESTIC PRODUCT (Average Prices)','Total Production (1000 tons)'].sum()
    fig = px.pie(temp1, values='GROSS STATE VALUE ADDED BY ECONOMIC ACTIVITY-AGRICULTURE(Average Prices)', names='State Name', title='Statewise Agricultural GDP Distribution')
    st.plotly_chart(fig)

    fig1 = px.pie(temp1, values='GROSS STATE DOMESTIC PRODUCT (Average Prices)', names='State Name', title='Statewise Overall GDP Distribution')
    st.plotly_chart(fig1)

    fig2 = px.pie(temp1, values='Total Production (1000 tons)', names='State Name', title='Statewise Crop Production')
    st.plotly_chart(fig1)

    fig5 = plt.figure(figsize=(15,15))
    st.write('Correlation Heatmap to Analyse Economy')
    sns.heatmap(df1.drop(['Year'],axis=1).corr(),annot=True)
    st.pyplot(fig5)



@st.cache_data
def load_data1():
    df = pd.read_csv("dataset.csv")

    return df

df = load_data1()

@st.cache_data
def load_data2():
    df1 = pd.read_csv("dataset1.csv")
    
    return df1

df1 = load_data2()

def show_explore_page():
    st.title("Analytics in Agricultural Economics")

    st.write("""### Developed By Benny Godwin J Davidson""")

    questions = (
        "Analyse Total Production With States",
        "Find Most and Least crop producting districts",
        "Analyse Total Area with States",
        "Find Most and Least crop field districts",
        "Find Relation Between Total Area and Total Production",
        "Find Overall producting through years",
        "Find Productivity in different states",
        "Make and analysis on Rice, Wheat, Kharif and Rabi Crops",
        "Is Rainfall Really Effects Production",
        "Try to Analyse Economy and Find an insightfull relation between Economy and Crop Production"
    )

    question = st.selectbox("Select Questionary: ",questions)

    if question == "Analyse Total Production With States":
        q1()
        st.write('''
        ### **Inference:**
The visualisation takes attributes 'State Name' and 'Total Production (1000 tons)' from the dataframe to display a bar diagram and a pie chart. It shows the total crop production in terms of 1000 tons for each state in India. From the above visualisation we can infer that the state of UTTAR PRADESH has the highest value of total crop production whereas the state of Kerala has the lowest value of the total crop production.''')
    elif question == "Find Most and Least crop producting districts":
        q2()
        st.write('''
        ### **Inference:**
The visualisation takes attributes 'Dist Name' and 'Total Production (1000 tons)' from the dataframe to display two bar charts. It shows us one bar chart for the top 5 highest total crops producing districs and the other bar chart shows us the lowest total crops producing districts. From the above visualisation we can infer that KARNAL district is producing most number of total crops as compared the other districts on the dataset whereas the KINNAUR district is producing the least number of total crops as compared to other districts present in the dataset. ''')
    elif question == "Analyse Total Area with States":
        q3()
        st.write('''
        ### **Inference:**
The visualisation takes 'State Name' and 'Total Area (1000 ha)' attributes from the dataframe to display a bar chart and a pie chart. It shows us the total area for production in terms of 1000 hectare of each state in India. From the above visualisation we can infer that the state of MAHARASHTRA and MADHYA PARDESH are the joint two states which are having the highest number of area for crop production whereas the state of UTTARAKHAND has the lowest number of area for crop production.''')
    elif question == "Find Most and Least crop field districts":
        q4()
        st.write('''
        ### **Inference:**
The visualisation takes 'Dist Name' and 'Total Area (1000 ha)' attributes from the dataframe to display two bar charts.  It shows us one bar chart for the top 5 highest total crops producing area per districs in terms of 1000 hectare and the other bar chart shows us the 5 lowest total crops producing  area per districts in terms of 1000 hectare. From the above visualisation we can infer that OSMANABAD district has the most area for production of total crops as compared to the other districts on the dataset, whereas the KINNAUR district has the least area for production of total crops as compared to other districts present in the dataset.''')
    elif question == "Find Relation Between Total Area and Total Production":
        q5()
        st.write('''
        ### **Inference:**
The visualisation takes 'Total Area (1000 ha)' and 'Total Production (1000 tons)' attributes from the dataframe to display a scatter plot and a correlation heatmap. It shows us the relationship between total area for crop production in terms of 1000 hectare and total crops produced in terms of 1000 tons. From the above visualisation we can infer that there is a positive moderate correlation between Total crop produced and Total area for crop production. We can also say that more area for crop production does not imply that the total crops produced will also be more.''')
    elif question == "Find Overall producting through years":
        q6()
        st.write('''
        ### **Inference:**
The visualisation takes attributes 'Year' and 'Total Production (1000 tons)' from the dataframe to display a line plot. It shows us the total crop production in terms of 1000 tons throughout the years. From the above visualisation we can infer that the crop production was at it's peak on the year of 2013 and the lowest at the year 2009. We can also see the line plot increasing slighlty after the year 2017.''')
    elif question == "Find Productivity in different states":
        q7()
        st.write('''
        ### **Inference:**
The visualisation takes attributes 'State Name' and 'Total Yield (Kg per ha)' from the dataframe to display a bar chart. It shows us the the measurement of the amount of crops grown for each state in India. From the above visulisation we can infer that the state of uttar pradesh have the maximum amount of crops grown than any other state in India. The state of kerela has the least amount of crops produced.''')
    elif question == "Make and analysis on Rice, Wheat, Kharif and Rabi Crops":
        q8()
    elif question == "Is Rainfall Really Effects Production":
        q9()
        st.write('''
        ### **Inference:**
The visualisation takes "Rainfall(mm)" and "Total Production (1000 tons)" attributes from the dataframe to display a scatter plot and a correlation heatmap. It shows us the relationship between total rainfall in terms of mm and total crops produced in terms of 1000 tons. From the above visualisation we can infer that there is a negative weak correlation between Total rainfall and Total crop production. We can also say that more rainfall does not imply that the total crops produced will also be more and vice versa.''')
    elif question == "Try to Analyse Economy and Find an insightfull relation between Economy and Crop Production":
        q10()
        st.write('''
        ### **Inference:**
- The visualsation takes attributes "Year",'GROSS STATE VALUE ADDED BY ECONOMIC ACTIVITY-AGRICULTURE(Average Prices)','GROSS STATE DOMESTIC PRODUCT (Average Prices)' from the dataframe to display a line plot and a bar plot. The line plot shows us the gross state value added by economic activity(agriculture) and gross state domestic product(average prices) throughout the year and the bar plot shows us the total production value throughout the year.
- The visualisation takes attributes 'State Name' with 'GROSS STATE VALUE ADDED BY ECONOMIC ACTIVITY-AGRICULTURE(Average Prices)','GROSS STATE DOMESTIC PRODUCT (Average Prices)' and 'Total Production (1000 tons)' from the dataframe to create three pie charts. The first pie chart shows us the Agricultural GDP distribution for each state from which we can infer uttar pradesh has the highest distribution. The second pie chart shows us Overall GDP Distribution for each state from which we can infer maharashtra has the highest distribution. The third pie chart shows us the total crop production in terms of 1000 tons for each state and from this we can infer that the state of uttar pradesh produces has the highest crop production among all states in india.
- The  visualisation takes all attributes of the dataframe except 'year' to create a correlation heatmap of all atttributes in the dataframe. Correlation values vary from 1 to -1. 1 is the point of strongest positive correlation whereas -1  is the point for strongest negative correlation. 0 is the point for no or 0 correlation. From the Correlation Heatmap we infer that Production,Rainfall,Area are not so much effecting economy as most of them has average positive correlation.''')
    
