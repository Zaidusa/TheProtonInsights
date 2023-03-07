# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 10:17:07 2021

@author: Andi5
"""
import streamlit as st
#from streamlit_lottie import st_lottie
import time
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go



st.set_page_config(page_title='ProtonInsights',  layout='wide', page_icon=':Bar chart fill:')

#this is the header
 

t1, t2 = st.columns((0.7,1))

t1.image('images/Pie.jpg', width = 60)
#t2.title("ProtonInsights - we work on data projects!!!")
st.markdown("""
    <style>
    .big-font {
        font-size:100px !important;
    }
    </style>
    """, unsafe_allow_html=True)
#lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
st.markdown('<p class="big-font">The Proton Insights</p>', unsafe_allow_html=True)
left_column, right_column = st.columns(2)
with right_column:
    st.write("The Proton Insights is pioneering what AI and analytics can do to solve some of the toughest problems faced by organizations globally. We develop bespoke solutions powered by data and technology for several Fortune 500 companies. We have offices in multiple cities across the US, UK, India, and Singapore, and a substantial remote global workforce. ")
    #st_lottie(lottie_coding, height=600, key="coding0")
with right_column:
    t2.markdown('''**Tel:** 040 24443076 **| Address:** 705,Amrutha castle, near Telecom colony,Gachibowli,Hyderabad,India,500032
            |email: you_contactus@proton.me''')



## Data

with st.spinner('Updating Report...'):
    
    #Metrics setting and rendering

    hosp_df = pd.read_excel('DataforMock.xlsx',sheet_name = 'Hospitals')
    hosp = st.selectbox('Choose Healthcare provider', hosp_df, help = 'Filter report to show only one stock')
    
    m1, m2, m3, m4, m5 = st.columns((1,1,1,1,1))
    
    todf = pd.read_excel('DataforMock.xlsx',sheet_name = 'metrics')
    to = todf[(todf['Hospital Attended']==hosp) & (todf['Metric']== 'Total Outstanding')]   
    ch = todf[(todf['Hospital Attended']==hosp) & (todf['Metric']== 'Current Handover Average Mins')]   
    hl = todf[(todf['Hospital Attended']==hosp) & (todf['Metric']== 'Hours Lost to Handovers Over 15 Mins')]
    
    m1.write('')
    m2.metric(label ='Total Outstanding Handovers',value = int(to['Value']), delta = str(int(to['Previous']))+' Compared to 1 hour ago', delta_color = 'inverse')
    m3.metric(label ='Current Handover Average',value = str(int(ch['Value']))+" Mins", delta = str(int(ch['Previous']))+' Compared to 1 hour ago', delta_color = 'inverse')
    m4.metric(label = 'Time Lost today (Above 15 mins)',value = str(int(hl['Value']))+" Hours", delta = str(int(hl['Previous']))+' Compared to yesterday')
    m1.write('')
     
    # Number of Completed Handovers by Hour
    
    g1, g2, g3 = st.columns((1,1,1))
    
    fgdf = pd.read_excel('DataforMock.xlsx',sheet_name = 'Graph')
    
    fgdf = fgdf[fgdf['Hospital Attended']==hosp] 
    
    fig = px.bar(fgdf, x = 'Arrived Destination Resolved', y='Number of Handovers', template = 'seaborn')
    
    fig.update_traces(marker_color='#264653')
    
    fig.update_layout(title_text="Number of Completed Handovers by Hour",title_x=0,margin= dict(l=0,r=10,b=10,t=30), yaxis_title=None, xaxis_title=None)
    
    g1.plotly_chart(fig, use_container_width=True) 
    
    # Predicted Number of Arrivals
    
    fcst = pd.read_excel('DataforMock.xlsx',sheet_name = 'Forecast')
    
    fcst = fcst[fcst['Hospital Attended']==hosp]
    
    fig = px.bar(fcst, x = 'Arrived Destination Resolved', y='y', template = 'seaborn')
    
    fig.update_traces(marker_color='#7A9E9F')
    
    fig.update_layout(title_text="Predicted Number of Arrivals",title_x=0,margin= dict(l=0,r=10,b=10,t=30), yaxis_title=None, xaxis_title=None)
    
    g2.plotly_chart(fig, use_container_width=True)  
    
    # Average Completed Handover Duration by hour

    fig = px.bar(fgdf, x = 'Arrived Destination Resolved', y='Average Duration',color = "Average Duration", template = 'seaborn', color_continuous_scale=px.colors.diverging.Temps)
    
    fig.add_scatter(x=fgdf['Arrived Destination Resolved'], y=fgdf['Target'], mode='lines', line=dict(color="black"), name='Target')
    
    fig.update_layout(title_text="Average Completed Handover Duration by hour",title_x=0,margin= dict(l=0,r=10,b=10,t=30), yaxis_title=None, xaxis_title=None, legend=dict(orientation="h",yanchor="bottom",y=0.9,xanchor="right",x=0.99))
    
    g3.plotly_chart(fig, use_container_width=True) 
      
    # Waiting Handovers table
    
    cw1, cw2 = st.columns((2.5, 1.7))
    
    whdf = pd.read_excel('DataforMock.xlsx',sheet_name = 'WaitingHandovers')
      
    colourcode = []
                             
    for i in range(0,9):
        colourcode.append(whdf['c'+str(i)].tolist())   
    
    whdf = whdf[['Hospital Attended ',	'Expected',	'Inbound ',	'Arrived ',	'Waiting',	'0 - 15 Mins',	'15 - 30 Mins ',	'30 - 60 Mins ',	'60 - 90 Mins',	'90 + Mins ',
]]
    
       
    fig = go.Figure(
            data = [go.Table (columnorder = [0,1,2,3,4,5,6,7,8,9], columnwidth = [30,10,10,10,10,15,15,15,15,15],
                header = dict(
                 values = list(whdf.columns),
                 font=dict(size=12, color = 'white'),
                 fill_color = '#264653',
                 line_color = 'rgba(255,255,255,0.2)',
                 align = ['left','center'],
                 #text wrapping
                 height=20
                 )
              , cells = dict(
                  values = [whdf[K].tolist() for K in whdf.columns], 
                  font=dict(size=12),
                  align = ['left','center'],
                  fill_color = colourcode,
                  line_color = 'rgba(255,255,255,0.2)',
                  height=20))])
     
    fig.update_layout(title_text="Current Waiting Handovers",title_font_color = '#264653',title_x=0,margin= dict(l=0,r=10,b=10,t=30), height=480)                                                           
        
    cw1.plotly_chart(fig, use_container_width=True)    
    
    # Current Waiting Table
    
    cwdf = pd.read_excel('DataforMock.xlsx',sheet_name = 'CurrentWaitingCallsigns')
    
    # if hosp == 'All':
    #     cwdf = cwdf
    # elif hosp != 'All':
    #     cwdf = cwdf[cwdf['Hospital Attended']==hosp]
    
    
    fig = go.Figure(
            data = [go.Table (columnorder = [0,1,2,3], columnwidth = [15,40,20,20],
                header = dict(
                 values = list(cwdf.columns),
                 font=dict(size=12, color = 'white'),
                 fill_color = '#264653',
                 align = 'left',
                 height=20
                 )
              , cells = dict(
                  values = [cwdf[K].tolist() for K in cwdf.columns], 
                  font=dict(size=12),
                  align = 'left',
                  fill_color='#F0F2F6',
                  height=20))]) 
        
    fig.update_layout(title_text="Current Waiting Callsigns",title_font_color = '#264653',title_x=0,margin= dict(l=0,r=10,b=10,t=30), height=480)
        
    cw2.plotly_chart(fig, use_container_width=True)
       
with st.spinner('Report updated!'):
    time.sleep(1)     
    
# Performance Section  
    
with st.expander("Previous Performance"):
        
    hhc24 = pd.read_excel('DataforMock.xlsx',sheet_name = 'HospitalHandoversCompleted')  
    
    colourcode = []
                          
    for i in range(0,13):
        colourcode.append(hhc24['c'+str(i)].tolist())    
    
    hhc24 = hhc24[['Hospital Attended','Handovers','In Progress','Average','Hours Lost','0 to 15 mins','15 to 30 mins','30 to 60 mins','60 to 90 mins','90 to 120 mins','120 mins','% 15 Mins','% 30 Mins']]   
    
    fig = go.Figure(
            data = [go.Table (columnorder = [0,1,2,3,4,5,6,7,8,9,10,11,12], columnwidth = [18,12],
                header = dict(
                 values = list(hhc24.columns),
                 font=dict(size=11, color = 'white'),
                 fill_color = '#264653',
                 line_color = 'rgba(255,255,255,0.2)',
                 align = ['left','center'],
                 #text wrapping
                 height=20
                 )
              , cells = dict(
                  values = [hhc24[K].tolist() for K in hhc24.columns], 
                  font=dict(size=10),
                  align = ['left','center'],
                  fill_color = colourcode,
                  line_color = 'rgba(255,255,255,0.2)', 
                  height=20))])
     
    fig.update_layout(title_text="Handovers Completed in the Past 24 Hours",title_font_color = '#264653',title_x=0,margin= dict(l=0,r=10,b=10,t=30), height=400)
    
    st.plotly_chart(fig, use_container_width=True)      
    
    p1,p2 = st.columns((3, 1.7))   
        
    #  Current Waiting Handovers
        
    hhc = pd.read_excel('DataforMock.xlsx',sheet_name = 'HospitalHandoverCompletedByHour')  
    
    hhc = hhc[hhc['Hospital Attended']==hosp]
    
    colourcode = []
                             
    for i in range(0,13):
        colourcode.append(hhc['c'+str(i)].tolist())    
    
    hhc = hhc[['dst','Handovers','In Progress','Average','Hours Lost','0 to 15 mins','15 to 30 mins','30 to 60 mins','60 to 90 mins','90 to 120 mins','120 mins','% 15 Mins','% 30 Mins']]
        
    fig = go.Figure(
            data = [go.Table (columnorder = [0,1,2,3,4,5,6,7,8,9,10,11,12], columnwidth = [18,12],
                header = dict(
                 values = list(hhc.columns),
                 font=dict(size=11, color = 'white'),
                 fill_color = '#264653',
                 line_color = 'rgba(255,255,255,0.2)',
                 align = ['left','center'],
                 #text wrapping
                 height=20
                 )
              , cells = dict(
                  values = [hhc[K].tolist() for K in hhc.columns], 
                  font=dict(size=10),
                  align = ['left','center'],
                  fill_color = colourcode,
                  line_color = 'rgba(255,255,255,0.2)',
                  height=20))])
     
    fig.update_layout(title_text="Handovers Completed by Hour",title_font_color = '#264653',title_x=0,margin= dict(l=0,r=10,b=10,t=30), height=600)
    
    p1.plotly_chart(fig, use_container_width=True)  
    

    #  Longest Completed Handovers    
    
    lch = pd.read_excel('DataforMock.xlsx',sheet_name = 'LongestCompletedHandover')
        
    if hosp == 'All':
            lch = lch
    elif hosp != 'All':
        lch = lch[lch['Hospital Attended']==hosp]

    fig = go.Figure(
                data = [go.Table (columnorder = [0,1,2,3,4], columnwidth = [10,35,20,20,10],
                                  header = dict(
                                      values = list(lch.columns),
                                      font=dict(size=12, color = 'white'),
                                      fill_color = '#264653',
                                      align = 'left',
                                      height=20
                                          )
              , cells = dict(
                  values = [lch[K].tolist() for K in lch.columns], 
                  font=dict(size=11),
                  align = 'left',
                  fill_color='#F0F2F6',
                  height=20))])
        
    fig.update_layout(title_text="Longest Completed Handovers",title_font_color = '#264653',title_x=0,margin= dict(l=0,r=10,b=10,t=30), height=600)
        
    p2.plotly_chart(fig, use_container_width=True)


# Contact Form
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

with st.expander("Contact us"):
    contact_form = """
        <form action="https://formsubmit.co/you_contactus@proton.me" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
        
        
        
        
        
        
        
        
        
        