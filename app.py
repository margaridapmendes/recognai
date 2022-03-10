import streamlit as st
import pandas as pd
import datetime
import altair as alt
# import datasets
# from datasets import load_dataset
# from bokeh.plotting import figure
import numpy as np
import time

# dataset = load_dataset("amazon_us_reviews",'Wireless_v1_00')
# df = pd.read_csv("/Users/nicolasmarechal/Desktop/Final_Tag_Fraud.csv")
# india = pd.read_csv("/Users/nicolasmarechal/Desktop/India Cities LatLng.csv")

df = pd.read_csv("Final_Tag_Fraud.csv")
india = pd.read_csv("India Cities LatLng.csv")

# st.image("/Users/nicolasmarechal/Desktop/IE-University.png", width = 180)
# st.image("/Users/nicolasmarechal/Desktop/Logo_Horizontal.png", width = 180)

st.write("""
# Fake Reviews Detection
### *Amazon Reviews Dataset*
""" )
st.text("")

@st.cache
def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
     label="Download data as CSV",
     data=csv,
     file_name='Final_Tag_Fraud.csv',
     mime='text/csv',)

st.text("")
st.write("""
### *Load Data*
""" )

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
     bytes_data = uploaded_file.read()
     st.write("filename:", uploaded_file.name)
     st.write(bytes_data)

st.balloons()


st.text("")
st.text("")
st.text("")
st.write("""
# Live Demo
""" )
st.write("""
### Input a specific Customer_Id
""" )

title = st.text_input('Input a Customer_Id', '34645354')
st.write('You inputed the Customer_Id:', title)

st.text("")
st.write("""
## Review(s) associated
""" )

st.text("")
with st.spinner('Wait for it...'):
    time.sleep(3)
st.success('Done!')

st.write("""
### _7 Reviews found_
""" )
st.text("")

txt = st.text_area('1 Review found:', ''' If you purchase Memphis Car Audio products on the Internet, be advised:  WE WILL NOT HONOR ANY WARRANTY CLAIMS ON PRODUCTS PURCHASED FROM INTERNET SELLERS.  WE WILL NOT ISSUE RETURN AUTHORIZATION FOR PRODUCTS PURCHASED ONLINE.    We do this to protect our customers and our retailers. We want you to enjoy the best performance possible from Memphis Car Audio products. Purchasing Memphis Car Audio products from an authorized retailer means you are guaranteed...    * Genuine Memphis Car Audio products, not a \\"knock-off\\" imitation  * The support of trained, professional installers  * Superb warranty service should you ever need it  * Reliable technical information and support from Memphis Car Audio & your retailer  * Smart product innovation and leading edge technology  * Excellent value for your money''',key=1)
txt = st.text_area('1 Review found:', ''' If you purchase Memphis Car Audio products on the Internet, be advised:  WE WILL NOT HONOR ANY WARRANTY CLAIMS ON PRODUCTS PURCHASED FROM INTERNET SELLERS.  WE WILL NOT ISSUE RETURN AUTHORIZATION FOR PRODUCTS PURCHASED ONLINE.    We do this to protect our customers and our retailers. We want you to enjoy the best performance possible from Memphis Car Audio products. Purchasing Memphis Car Audio products from an authorized retailer means you are guaranteed...    * Genuine Memphis Car Audio products, not a \\"knock-off\\" imitation  * The support of trained, professional installers  * Superb warranty service should you ever need it  * Reliable technical information and support from Memphis Car Audio & your retailer  * Smart product innovation and leading edge technology  * Excellent value for your money''',key=2)
txt = st.text_area('1 Review found:', ''' If you purchase Memphis Car Audio products on the Internet, be advised:  WE WILL NOT HONOR ANY WARRANTY CLAIMS ON PRODUCTS PURCHASED FROM INTERNET SELLERS.  WE WILL NOT ISSUE RETURN AUTHORIZATION FOR PRODUCTS PURCHASED ONLINE.    We do this to protect our customers and our retailers. We want you to enjoy the best performance possible from Memphis Car Audio products. Purchasing Memphis Car Audio products from an authorized retailer means you are guaranteed...    * Genuine Memphis Car Audio products, not a \\"knock-off\\" imitation  * The support of trained, professional installers  * Superb warranty service should you ever need it  * Reliable technical information and support from Memphis Car Audio & your retailer  * Smart product innovation and leading edge technology  * Excellent value for your money''',key=3)
txt = st.text_area('1 Review found:', ''' If you purchase Memphis Car Audio products on the Internet, be advised:  WE WILL NOT HONOR ANY WARRANTY CLAIMS ON PRODUCTS PURCHASED FROM INTERNET SELLERS.  WE WILL NOT ISSUE RETURN AUTHORIZATION FOR PRODUCTS PURCHASED ONLINE.    We do this to protect our customers and our retailers. We want you to enjoy the best performance possible from Memphis Car Audio products. Purchasing Memphis Car Audio products from an authorized retailer means you are guaranteed...    * Genuine Memphis Car Audio products, not a \\"knock-off\\" imitation  * The support of trained, professional installers  * Superb warranty service should you ever need it  * Reliable technical information and support from Memphis Car Audio & your retailer  * Smart product innovation and leading edge technology  * Excellent value for your money''',key=4)
txt = st.text_area('1 Review found:', ''' If you purchase Memphis Car Audio products on the Internet, be advised:  WE WILL NOT HONOR ANY WARRANTY CLAIMS ON PRODUCTS PURCHASED FROM INTERNET SELLERS.  WE WILL NOT ISSUE RETURN AUTHORIZATION FOR PRODUCTS PURCHASED ONLINE.    We do this to protect our customers and our retailers. We want you to enjoy the best performance possible from Memphis Car Audio products. Purchasing Memphis Car Audio products from an authorized retailer means you are guaranteed...    * Genuine Memphis Car Audio products, not a \\"knock-off\\" imitation  * The support of trained, professional installers  * Superb warranty service should you ever need it  * Reliable technical information and support from Memphis Car Audio & your retailer  * Smart product innovation and leading edge technology  * Excellent value for your money''',key=5)
txt = st.text_area('1 Review found:', ''' If you purchase Memphis Car Audio products on the Internet, be advised:  WE WILL NOT HONOR ANY WARRANTY CLAIMS ON PRODUCTS PURCHASED FROM INTERNET SELLERS.  WE WILL NOT ISSUE RETURN AUTHORIZATION FOR PRODUCTS PURCHASED ONLINE.    We do this to protect our customers and our retailers. We want you to enjoy the best performance possible from Memphis Car Audio products. Purchasing Memphis Car Audio products from an authorized retailer means you are guaranteed...    * Genuine Memphis Car Audio products, not a \\"knock-off\\" imitation  * The support of trained, professional installers  * Superb warranty service should you ever need it  * Reliable technical information and support from Memphis Car Audio & your retailer  * Smart product innovation and leading edge technology  * Excellent value for your money''',key=6)
txt = st.text_area('1 Review found:', ''' If you purchase Memphis Car Audio products on the Internet, be advised:  WE WILL NOT HONOR ANY WARRANTY CLAIMS ON PRODUCTS PURCHASED FROM INTERNET SELLERS.  WE WILL NOT ISSUE RETURN AUTHORIZATION FOR PRODUCTS PURCHASED ONLINE.    We do this to protect our customers and our retailers. We want you to enjoy the best performance possible from Memphis Car Audio products. Purchasing Memphis Car Audio products from an authorized retailer means you are guaranteed...    * Genuine Memphis Car Audio products, not a \\"knock-off\\" imitation  * The support of trained, professional installers  * Superb warranty service should you ever need it  * Reliable technical information and support from Memphis Car Audio & your retailer  * Smart product innovation and leading edge technology  * Excellent value for your money''',key=7)

# st.write('Sentiment:', run_sentiment_analysis(txt))

st.text("")
st.text("")
st.write("""
## Fake Review - Probability
""" )

fraud_st = st.slider('Probability',min_value=None, max_value=None,value=93)
st.write("There is a ", fraud_st, 'percent chance that this is a fake review')

st.warning('This is a Fake Review!')

st.text("")
st.text("")

searches_r = st.radio(
     "Do you want to make more searches?",
     ('Yes', 'No'))

if searches_r == 'Yes':
     st.write('You selected Yes')
else:
     st.write("You selected No")

st.text("")
st.write("""
### Second Search
""" )
st.text("")
st.write("""
### Input a specific Customer_Id
""" )

title = st.text_input('Input a Customer_Id', '52752079')
st.write('You inputed the Customer_Id:', title)

st.write("""
## Review(s) associated
""" )

with st.spinner('Wait for it...'):
    time.sleep(3)
st.success('Done!')

st.write("""
### _2 Reviews found_
""" )

txt = st.text_area('1 Review found:', '''The receiver works well - I use it fairly frequently.  You do need to be aware that on Windows 7, if the GPS is plugged in prior to the navigation software being launched, Win7 will *INSIST* on trying to install the &#34;serial ballpoint mouse&#34; driver, and if it ever succeeds, you will find your mouse pointer jumping all over the place as the idiot microsoft operating system interprets the GPS as an ancient mouse input.  Microsoft is clearly to blame as the serial ballpoint mouse was a piece of crap and *NO_ONE* uses any such thing today - but after all, it was microsoft branded, so we *must* make every modern device and person stand back and honor that.  Flame off.  Back to the GPS - it's quick to lock, has WAAS (extra precision/correction), and sticks fine to the car top or hood.  A long USB cable can be run to it - I have run it on 20' cables, even though USB isn't really supposed to go that far.''')

txt = st.text_area('1 Review found:', '''The Alpine head units with ipod cable work well with this cable.<br />This is attached to the ipod cable, and the head \\"Aux+\\" is set<br />to \\"ON\\", which will then cause the mini 3.5mm connector to be<br />the audio source when \\"aux\\" input is selected.<br /><br />Note that you will not hear audio if you do not set this to 'ON'.<br /><br />Works great, the only thing better would be if they added USB<br />power output on this cable (from the head) to power generic<br />media players.<br /><br />I use this with a Sandisk Sansa Fuze, and it works very well.''')

st.text("")
st.text("")
st.write("""
## Fake Review - Probability
""" )


fraud_st = st.slider('Probability',min_value=None, max_value=None,value=3)
st.write("There is a ", fraud_st, 'percent chance that this is a fake review')


st.success('This is NOT a Fake Review!')

st.text("")
st.text("")
st.text("")


st.write("""
# Next Steps and Applications
""" )

st.write("""
### Search by Date
""" )

st.write("""
### Select a specific date
""" )

st.text("")

d = st.date_input(
     "Select a date",
     datetime.date(2013, 11, 19))
st.write('You selected the date:', d)

st.text("")
st.text("")

st.write("""
### Search by Location
""" )

st.write("""
### Choice of location
""" )

options = st.multiselect(
     'Which country do you want to target?',
     ['India', 'USA', 'France', 'Spain', 'Cuba', 'Peru', 'Argentina', 'Switzerland'],
     ['India'])

st.write('You selected:', options)

st.write("""
### Location of user_id
""" )

india['longitude'] = india['lng']
st.map(india.head(1))

st.write("""
### Search History
""" )

option = st.selectbox(
     'Historical Searches',('34645354', '22496686','52752079') )

st.write('You selected the user_id:', option)


st.write("""
# Thank you!
""" )

clicked = st.button("Group C ")

# st.write("""
# # General Statistics: Benchmark
# """ )
#
#
# st.area_chart(df['fraud_pred'])
#
# col1, col2, col3 = st.columns(3)
#
# col1 = st.metric(label="Average Fraud Reviews", value="9%")
# col2 = st.metric(label="Average Reviews per Week", value="1.44")
# col3 = st.metric(label="Average Similarities", value="0.15")
