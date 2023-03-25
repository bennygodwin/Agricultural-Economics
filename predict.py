import streamlit as st
import pandas as pd
import numpy as np
import pickle
import numpy as np

label_encoder_year = pickle.load(open("label_encoder_year.pickle", "rb"))
label_encoder_state = pickle.load(open("label_encoder_state.pickle", "rb"))
label_encoder_dis = pickle.load(open("label_encoder_dis.pickle", "rb"))

label_encoder_year1 = pickle.load(open("label_encoder_year1.pickle", "rb"))
label_encoder_state1 = pickle.load(open("label_encoder_state1.pickle", "rb"))

model1 = pickle.load(open("model1.pickle", "rb"))
model2 = pickle.load(open("model2.pickle", "rb"))
model3 = pickle.load(open("model3.pickle", "rb"))

def predmodel1():
    districts = ('Chittoor', 'East Godavari', 'Guntur', 'Krishna', 'Kurnool',
       'Srikakulam', 'West Godavari', 'Cachar', 'Darrang', 'Dibrugarh',
       'Goalpara', 'Karbi Anglong', 'Lakhimpur', 'Nagaon', 'Sibsagar',
       'Bhagalpur', 'Darbhanga', 'Gaya', 'Muzaffarpur', 'Patna',
       'Saharsa', 'Saran', 'Bastar', 'Bilaspur', 'Durg', 'Raigarh',
       'Raipur', 'Surguja', 'Ahmedabad', 'Amreli', 'Banaskantha',
       'Bhavnagar', 'Dangs', 'Jamnagar', 'Kheda', 'Kutch', 'Mehsana',
       'Panchmahal', 'Rajkot', 'Sabarkantha', 'Surat', 'Surendranagar',
       'Valsad', 'Ambala', 'Gurgaon', 'Jind', 'Karnal', 'Rohtak',
       'Chamba', 'Kangra', 'Kinnaur', 'Kullu', 'Mandi', 'Sirmaur',
       'Solan', 'Dhanbad', 'Hazaribagh', 'Palamau', 'Ranchi', 'Belgaum',
       'Bellary', 'Bidar', 'Chitradurga', 'Dharwad', 'Hassan', 'Kolar',
       'Mandya', 'Mysore', 'Raichur', 'Tumkur', 'Kannur', 'Kollam',
       'Kottayam', 'Kozhikode', 'Malappuram', 'Palakkad',
       'Thiruvananthapuram', 'Thrissur', 'Balaghat', 'Betul', 'Bhind',
       'Chhatarpur', 'Chhindwara', 'Damoh', 'Datia', 'Dewas', 'Dhar',
       'Guna', 'Gwalior', 'Hoshangabad', 'Indore', 'Jabalpur', 'Jhabua',
       'Mandla', 'Mandsaur', 'Morena', 'Narsinghpur', 'Panna', 'Raisen',
       'Rajgarh', 'Ratlam', 'Rewa', 'Sagar', 'Satna', 'Sehore', 'Shahdol',
       'Shajapur', 'Shivpuri', 'Sidhi', 'Tikamgarh', 'Ujjain', 'Vidisha',
       'Ahmednagar', 'Akola', 'Aurangabad', 'Beed', 'Bhandara',
       'Buldhana', 'Chandrapur', 'Dhule', 'Jalgaon', 'Kolhapur', 'Nagpur',
       'Nanded', 'Nasik', 'Osmanabad', 'Parbhani', 'Pune', 'Raigad',
       'Ratnagiri', 'Sangli', 'Satara', 'Solapur', 'Thane', 'Wardha',
       'Balasore', 'Bolangir', 'Cuttack', 'Dhenkanal', 'Ganjam',
       'Kalahandi', 'Keonjhar', 'Koraput', 'Puri', 'Sambalpur',
       'Sundargarh', 'Amritsar', 'Gurdaspur', 'Hoshiarpur', 'Jalandhar',
       'Kapurthala', 'Ludhiana', 'Patiala', 'Sangrur', 'Ajmer', 'Alwar',
       'Banswara', 'Barmer', 'Bharatpur', 'Bhilwara', 'Bikaner', 'Bundi',
       'Chittorgarh', 'Churu', 'Dungarpur', 'Jaipur', 'Jaisalmer',
       'Jalore', 'Jhalawar', 'Jhunjhunu', 'Jodhpur', 'Kota', 'Nagaur',
       'Pali', 'Sikar', 'Sirohi', 'Tonk', 'Udaipur', 'Agra', 'Aligarh',
       'Allahabad', 'Azamgarh', 'Bahraich', 'Ballia', 'Banda',
       'Barabanki', 'Bareilly', 'Basti', 'Bijnor', 'Deoria', 'Etah',
       'Etawah', 'Faizabad', 'Farrukhabad', 'Fatehpur', 'Ghazipur',
       'Gonda', 'Gorakhpur', 'Hamirpur', 'Hardoi', 'Jalaun', 'Jaunpur',
       'Jhansi', 'Kheri', 'Lucknow', 'Mainpuri', 'Mathura', 'Meerut',
       'Moradabad', 'Muzaffarnagar', 'Pilibhit', 'Pratapgarh', 'Rampur',
       'Saharanpur', 'Shahjahanpur', 'Sitapur', 'Sultanpur', 'Unnao',
       'Varanasi', 'Chamoli', 'Dehradun', 'Nainital', 'Bankura',
       'Birbhum', 'Burdwan', 'Cooch Behar', 'Darjeeling', 'Hooghly',
       'Howrah', 'Jalpaiguri', 'Malda', 'Murshidabad', 'Nadia', 'Purulia',
       'Adilabad', 'Hyderabad', 'Karimnagar', 'Khammam', 'Medak',
       'Nalgonda', 'Nizamabad', 'Warangal')
    years = (2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017)
    district = st.selectbox("District",districts)
    district_le = label_encoder_dis.transform([district])
    year = st.selectbox("Year",years)
    year_le = label_encoder_year.transform([year])
    rainfall = st.number_input("Enter Rainfall(mm): ")
    area = st.number_input("Enter Total Area (1000 ha) for Agriculture: ")

    ok = st.button("Predict Total Crop Production")
    if ok:
        production = model1.predict([[year_le,district_le,rainfall,area]])
        st.write("The Estimated Crop Production (1000 tons) is ",production[0])


def premodel2():
    states = (
        'Andhra Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Gujarat',
       'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala',
       'Madhya Pradesh', 'Maharashtra', 'Punjab', 'Rajasthan',
       'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Telangana'
    )
    state = st.selectbox("State",states)
    state_le = label_encoder_state1.transform([state])
    years = (2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017)
    year = st.selectbox("Year",years)
    year_le = label_encoder_year1.transform([year])
    rainfall = st.number_input("Enter Rainfall(mm): ")
    area = st.number_input("Enter Total Area (1000 ha) for Agriculture: ")

    ok = st.button("Predict Total Crop Production")

    if ok:
        production = model2.predict([year_le,state_le,rainfall,area])
        st.write("The Estimated Crop Production (1000 tons) is ",production)

def premodel3():
    states = (
        'Andhra Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Gujarat',
       'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala',
       'Madhya Pradesh', 'Maharashtra', 'Punjab', 'Rajasthan',
       'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Telangana'
    )
    state = st.selectbox("State",states)
    state_le = label_encoder_state1.transform([state])
    years = (2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017)
    year = st.selectbox("Year",years)
    year_le = label_encoder_year1.transform([year])
    rainfall = st.number_input("Enter Rainfall(mm): ")
    area = st.number_input("Enter Total Area (1000 ha) for Agriculture: ")
    production = st.number_input("Enter Total Production (1000 tons): ")

    ok = st.button("Predict Average State GDP")

    if ok:
        gdp = model3.predict([year_le,state_le,rainfall,area,production])
        st.write("The Estimated GDP for the State",state," is ",gdp, "LAKH INR")



def show_predict_page():
    st.title("Analytics on Indian Agriculture with Economy")

    st.write("""### Developed By Benny Godwin J Davidson""")

    models = (
        "Predict Total Crop Production District Wise",
        "Predict Total Production State Wise",
        "Predict Economy"
    )

    model = st.selectbox("What You Want to Predict? ",models)

    if model == "Predict Total Crop Production District Wise":
        predmodel1()
    elif model == "Predict Total Production State Wise":
        premodel2()
    else:
        premodel3()




