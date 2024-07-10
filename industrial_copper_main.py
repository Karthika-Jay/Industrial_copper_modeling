import streamlit as st
import pickle
import numpy as np
from datetime import date
import sklearn
from streamlit_option_menu import option_menu
import base64



# Functions
def predict_status(ctry, itmtp, aplcn, wth, prdrf, qtlg, cstlg, tknslg, slgplg, itmdt, itmmn, itmyr, deldtdy, deldtmn, deldtyr):


    #change the datatypes "string" to "int"
    itdd= int(itmdt)
    itdm= int(itmmn)
    itdy= int(itmyr)

    dydd= int(deldtdy)
    dydm= int(deldtmn)
    dydy= int(deldtyr)
    #modelfile of the classification
    with open("C:/Users/lenovo/Desktop/try/industrial_copper_model/Industrial_Class_model_pickle.pkl","rb") as f:
        model_class=pickle.load(f)

    user_data= np.array([[ctry,itmtp,aplcn,wth,prdrf,qtlg,cstlg,tknslg,
                       slgplg,itdd,itdm,itdy,dydd,dydm,dydy]])
    
    y_pred= model_class.predict(user_data)

    if y_pred == 1:
        return 1
    else:
        return 0

def predict_selling_price(ctry, sts, itmtp, aplcn, wth, prdrf, qtlg, cstlg, tknslg, itmdt, itmmn, itmyr, deldtdy, deldtmn, deldtyr):

    #change the datatypes "string" to "int"
    itdd= int(itmdt)
    itdm= int(itmmn)
    itdy= int(itmyr)

    dydd= int(deldtdy)
    dydm= int(deldtmn)
    dydy= int(deldtyr)
    #modelfile of the classification
    with open("C:/Users/lenovo/Desktop/try/industrial_copper_model/Regression_Model_pickle.pkl","rb") as f:
        model_regg=pickle.load(f)

    user_data= np.array([[ctry,sts,itmtp,aplcn,wth,prdrf,qtlg,cstlg,tknslg,
                       itdd,itdm,itdy,dydd,dydm,dydy]])
    
    y_pred= model_regg.predict(user_data)

    ac_y_pred= np.exp(y_pred[0])

    return ac_y_pred


st.set_page_config(layout= "wide")

st.markdown("<div style='background-color:rgb(0, 0, 0);padding:10px;text-align:center;'><h1 style='color:white;'>INDUSTRIAL COPPER MODELING</h1></div>", unsafe_allow_html=True)

st.write(" ")
st.write(" ")
st.write(" ")

# Create tabs for navigation
tabs = ["👋😊Home", "📊ICM Options", "📝Summary"]
selected_tab = st.selectbox(":orange[**SELECT AN OPTION👇**]", tabs)
if selected_tab == "👋😊Home":
        # Load the image and encode it in base64
    with open("C:/Users/lenovo/Desktop/try/industrial_copper_model/fgb16.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    # CSS to set the background image
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpeg;base64,{encoded_string});
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
    """
    <style>
    @keyframes blink {
        0% { opacity: 1; }
        50% { opacity: 0; }
        100% { opacity: 1; }
    }
    .blink {
        animation: blink 1s infinite;
        font-size: 3em; 
        color: white; 
        text-align: center; 
        display: block;
    }
    .container {
        text-align: center; 
    }
    </style>
    <div class='container'>
        <div class='blink'>🙏 WELCOME TO INDUSTRIAL COPPER MODELING</div>
    </div>
    """,
    unsafe_allow_html=True
)
    st.write(" ")
    st.write(" ")
    st.markdown("<div style='background-color:white;padding:10px;text-align:center;'><p style='color:rainbow;'>Introduction and Objectives</p></div>", unsafe_allow_html=True)
    st.markdown("<div style='background-color:rgb(0, 0, 0);padding:10px;text-align:center;'><p style='color:white;'>In the manufacturing domain, specifically within the copper industry, businesses often face challenges related to sales and pricing data. This data is typically less complex but can be affected by skewness and noise, making manual predictions time-consuming and suboptimal. The primary goal of this project is to leverage machine learning techniques to enhance the accuracy and efficiency of predictions related to selling prices and customer lead statuses.</p></div>", unsafe_allow_html=True)

    st.markdown("<div style='background-color:white;padding:10px;text-align:center;'><p style='color:rainbow;'>Why Modeling is Necessary</p></div>", unsafe_allow_html=True)
    st.markdown("<div style='background-color:rgb(0, 0, 0);padding:10px;text-align:center;'><p style='color:white;'>Manual handling of sales and pricing data in the copper industry can lead to inaccuracies due to the presence of noisy and skewed data. These issues can hinder optimal pricing decisions and delay business processes. By developing a machine learning regression model, we can address these challenges effectively. Similarly, capturing and classifying leads efficiently can significantly impact sales outcomes. Hence, a lead classification model is crucial for evaluating and classifying leads based on their likelihood of conversion.</p></div>", unsafe_allow_html=True)

    
            
elif selected_tab == "📊ICM Options":
    # Load the image and encode it in base64
    with open("C:/Users/lenovo/Desktop/try/industrial_copper_model/image1.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    # CSS to set the background image
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpeg;base64,{encoded_string});
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


    icm_options = ["📈PREDICT STATUS", "📉PREDICT SELLING PRICE"]
    selected_option = st.sidebar.radio("Select an ICM Option:", icm_options)
    
        
    if selected_option == "📈PREDICT STATUS":
            st.markdown("<div style='background-color:white;padding:6px;text-align:center;'><p style='color:blue;font-size:25px;'>🤔PREDICT STATUS : Won🏆 / Lose👎🏼😕</p></div>", unsafe_allow_html=True)
            st.write(" ")

            col1,col2= st.columns(2)

            with col1:
                country= st.number_input(label=":blue[**Enter the Value for COUNTRY** 🔻Min:25.0, 🔺Max:113.0]")
                item_type= st.number_input(label=":blue[**Enter the Value for ITEM TYPE**🔻Min:0.0, 🔺Max:6.0]")
                application= st.number_input(label=":blue[**Enter the Value for APPLICATION**🔻Min:2.0, 🔺Max:87.5]")
                width= st.number_input(label=":blue[**Enter the Value for WIDTH**🔻Min:700.0, 🔺Max:1980.0]")
                product_ref= st.number_input(label=":blue[**Enter the Value for PRODUCT_REF**🔻Min:611728, 🔺Max:1722207579]")
                quantity_tons_log= st.number_input(label=":blue[**Enter the Value for QUANTITY_TONS Log Value🔻Min:-0.322, 🔺Max:6.924**]",format="%0.5f")
                customer_log= st.number_input(label=":blue[**Enter the Value for CUSTOMER Log Value**🔻Min:17.21910, 🔺Max:17.23015**]",format="%0.5f")
                thickness_log= st.number_input(label=":blue[**Enter the Value for THICKNESS Log Value**🔻Min:-1.71479, 🔺Max:3.28154**]",format="%0.5f")
            
            with col2:
                selling_price_log= st.number_input(label=":blue[**Enter the Value for SELLING PRICE Log Value🔻Min:5.97503, 🔺Max:7.39036**]",format="%0.5f")
                item_date_month = st.selectbox(":blue[**Select the Month for ITEM DATE**]", tuple(range(1, 13)), key="item_date_month")
                item_date_year = st.selectbox(":blue[**Select the Year for ITEM DATE**]", ("2020", "2021"), key="item_date_year")
                if item_date_month == 2:
                    if item_date_year in ("2020", "2024"):
                        item_date_day = st.selectbox(":blue[**Select the Day for ITEM DATE**]", tuple(range(1, 30)), key="item_date_day_leap_year")
                    else:
                        item_date_day = st.selectbox(":blue[**Select the Day for ITEM DATE**]", tuple(range(1, 29)), key="item_date_day_non_leap_year")
                else:
                    if item_date_month in (4, 6, 9, 11):
                        item_date_day = st.selectbox(":blue[**Select the Day for ITEM DATE**]", tuple(range(1, 31)), key="item_date_day_30_days")
                    else:
                        item_date_day = st.selectbox(":blue[**Select the Day for ITEM DATE**]", tuple(range(1, 32)), key="item_date_day_31_days")
                
                
                
                delivery_date_month = st.selectbox(":blue[**Select the Month for DELIVERY DATE**]", tuple(range(1, 13)), key="delivery_date_month")
                delivery_date_year = st.selectbox(":blue[**Select the Year for DELIVERY DATE**]", ("2020", "2021", "2022"), key="delivery_date_year")

                if delivery_date_month == 2:
                    if delivery_date_year in ("2020", "2024"):
                        delivery_date_day = st.selectbox(":blue[**Select the Day for DELIVERY DATE**]", tuple(range(1, 30)), key="delivery_date_day_leap_year")
                    else:
                        delivery_date_day = st.selectbox(":blue[**Select the Day for DELIVERY DATE**]", tuple(range(1, 29)), key="delivery_date_day_non_leap_year")
                else:
                    if delivery_date_month in (4, 6, 9, 11):
                        delivery_date_day = st.selectbox(":blue[**Select the Day for DELIVERY DATE**]", tuple(range(1, 31)), key="delivery_date_day_30_days")
                    else:
                        delivery_date_day = st.selectbox(":blue[**Select the Day for DELIVERY DATE**]", tuple(range(1, 32)), key="delivery_date_day_31_days")
                                                
                
            
            button= st.button(":rainbow[**PREDICT THE STATUS**]",use_container_width=True)

            if button:
                status= predict_status(country,item_type,application,width,product_ref,quantity_tons_log,
                                    customer_log,thickness_log,selling_price_log,item_date_day,
                                    item_date_month,item_date_year,delivery_date_day,delivery_date_month,
                                    delivery_date_year)
                
                if status == 1:
                    st.markdown("<style>@keyframes blink {0% {opacity: 1;}50% {opacity: 0;}100% {opacity: 1;}}.blink {animation: blink 1s infinite;}</style><a class='blink'><button style='background-color: #4CAF50; color: white; padding: 20px 40px; text-align: center; display: inline-block; font-size: 20px;'>The Status is WON🏆</button></a>", unsafe_allow_html=True)

                    st.toast('Hooray! WON!', icon='🏆')
                else:
                    
                    st.markdown("<style>@keyframes blink {0% {opacity: 1;}50% {opacity: 0;}100% {opacity: 1;}}.blink {animation: blink 1s infinite;}</style><a class='blink'><button style='background-color: red; color: white; padding: 20px 40px; text-align: center; display: inline-block; font-size: 20px;'>The Status is LOSE👎🏼</button></a>", unsafe_allow_html=True)

                    st.toast('LOSE', icon='👎🏼')

    elif selected_option == "📉PREDICT SELLING PRICE":
            # Load the image and encode it in base64
            with open("C:/Users/lenovo/Desktop/try/industrial_copper_model/fgb19.jpg", "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()

            # CSS to set the background image
            st.markdown(
                f"""
                <style>
                .stApp {{
                    background-image: url(data:image/jpeg;base64,{encoded_string});
                    background-size: cover;
                    background-position: center;
                }}
                </style>
                """,
                unsafe_allow_html=True
            )

        # Display the background image
            st.markdown("<div style='background-color:white;padding:6px;text-align:center;'><p style='color:navy;font-size:25px;'>PREDICT SELLING PRICE💰</p></div>", unsafe_allow_html=True)

            st.write(" ")

            col1,col2= st.columns(2)

            with col1:
                country= st.number_input(label=":red[**Enter the Value for COUNTRY**🔻Min:25.0, 🔺Max:113.0]")
                status= st.number_input(label=":red[**Enter the Value for STATUS**🔻Min:0.0, 🔺Max:8.0]")
                item_type= st.number_input(label=":red[**Enter the Value for ITEM TYPE**🔻Min:0.0, 🔺Max:6.0]")
                application= st.number_input(label=":red[**Enter the Value for APPLICATION**🔻Min:2.0, 🔺Max:87.5]")
                width= st.number_input(label=":red[**Enter the Value for WIDTH**🔻Min:700.0, 🔺Max:1980.0]")
                product_ref= st.number_input(label=":red[**Enter the Value for PRODUCT_REF**🔻Min:611728, 🔺Max:1722207579**]")
                quantity_tons_log= st.number_input(label=":red[**Enter the Value for QUANTITY_TONS Log Value🔻Min:-0.3223343801166147, 🔺Max:6.924734324081348**]",format="%0.3f")
                customer_log= st.number_input(label=":red[**Enter the Value for CUSTOMER Log Value🔻Min:17.21910565821408, 🔺Max:17.230155364880137**]",format="%0.3f")
                
            
            with col2:
                thickness_log= st.number_input(label=":red[**Enter the Value for THICKNESS Log Value🔻Min:-1.7147984280919266, 🔺Max:3.281543137578373**]",format="%0.3f")
                item_date_month = st.selectbox(":red[**Select the Month for ITEM DATE**]", tuple(range(1, 13)), key="item_date_month")
                item_date_year = st.selectbox(":red[**Select the Year for ITEM DATE**]", ("2020", "2021"), key="item_date_year")
                if item_date_month == 2:
                    if item_date_year in ("2020", "2024"):
                        item_date_day = st.selectbox(":red[**Select the Day for ITEM DATE**]", tuple(range(1, 30)), key="item_date_day_leap_year")
                    else:
                        item_date_day = st.selectbox(":red[**Select the Day for ITEM DATE**]", tuple(range(1, 29)), key="item_date_day_non_leap_year")
                else:
                    if item_date_month in (4, 6, 9, 11):
                        item_date_day = st.selectbox(":red[**Select the Day for ITEM DATE**]", tuple(range(1, 31)), key="item_date_day_30_days")
                    else:
                        item_date_day = st.selectbox(":red[**Select the Day for ITEM DATE**]", tuple(range(1, 32)), key="item_date_day_31_days")
                
                delivery_date_month = st.selectbox(":red[**Select the Month for DELIVERY DATE**]", tuple(range(1, 13)), key="delivery_date_month")
                delivery_date_year = st.selectbox(":red[**Select the Year for DELIVERY DATE**]", ("2020", "2021", "2022"), key="delivery_date_year")

                if delivery_date_month == 2:
                    if delivery_date_year in ("2020", "2024"):
                        delivery_date_day = st.selectbox(":red[**Select the Day for DELIVERY DATE**]", tuple(range(1, 30)), key="delivery_date_day_leap_year")
                    else:
                        delivery_date_day = st.selectbox(":red[**Select the Day for DELIVERY DATE**]", tuple(range(1, 29)), key="delivery_date_day_non_leap_year")
                else:
                    if delivery_date_month in (4, 6, 9, 11):
                        delivery_date_day = st.selectbox(":red[**Select the Day for DELIVERY DATE**]", tuple(range(1, 31)), key="delivery_date_day_30_days")
                    else:
                        delivery_date_day = st.selectbox(":red[**Select the Day for DELIVERY DATE**]", tuple(range(1, 32)), key="delivery_date_day_31_days")
                                                
                

            button= st.button(":rainbow[**PREDICT THE SELLING PRICE**]",use_container_width=True)

            if button:
                price= predict_selling_price(country,status,item_type,application,width,product_ref,quantity_tons_log,
                                    customer_log,thickness_log,item_date_day,
                                    item_date_month,item_date_year,delivery_date_day,delivery_date_month,
                                    delivery_date_year)
                
                st.markdown(f"""
                        <style>
                        @keyframes blink {{
                            0% {{ opacity: 1; }}
                            50% {{ opacity: 0; }}
                            100% {{ opacity: 1; }}
                        }}
                        .blink {{
                            animation: blink 1s infinite;
                            background-color: blue;
                            color: white;
                            padding: 20px 40px;
                            text-align: center;
                            display: inline-block;
                            font-size: 30px;
                        }}
                        </style>
                        <div class="blink">The Selling Price is: {price:.2f}</div>
                    """, unsafe_allow_html=True)
elif selected_tab == "📝Summary":
    # Load the image and encode it in base64
    with open("C:/Users/lenovo/Desktop/try/industrial_copper_model/fgb18.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    # CSS to set the background image
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpeg;base64,{encoded_string});
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div style='background-color:white;padding:6px;text-align:center;'><p style='color:blue;font-size:30px;'>✍SUMMARY OF THE PROJECT</p></div>", unsafe_allow_html=True)
    st.write(" ")
    st.write(" ")
    st.write(" ")


    st.markdown('<div style="background-color:white;padding:6px;text-align:left;"><p style="color:black;font-size:15px;">This project, "Industrial Copper Modeling," aims to harness the power of machine learning to improve sales and pricing predictions in the copper industry. We will address data challenges such as skewness and noise through advanced preprocessing techniques and build robust regression and classification models. By implementing a user-friendly Streamlit application, we will enable users to make real-time predictions about selling prices and lead statuses, thereby enhancing decision-making and operational efficiency.</p></div>', unsafe_allow_html=True)
    st.markdown('''<div style="background-color:white;padding:6px;text-align:left;"><p style="color:black;font-size:20px;">
                
🔹Python scripting and data preprocessing.

🔹Exploratory Data Analysis (EDA) using libraries like Seaborn.
                
🔹Developing regression and classification models using Scikit-learn.
                
🔹Creating interactive web applications with Streamlit.</p></div>''', unsafe_allow_html=True)
    
    st.markdown('''<div style="background-color:white;padding:6px;text-align:left;"><p style="color:black;font-size:15px;">
                
📌Data Overview
                
The dataset includes various features such as transaction IDs, dates, quantities, customer information, item specifications, and pricing details. Key columns include:

🔹selling_price: Target variable for regression.
                
🔹status: Target variable for classification (WON/LOST).
 </p></div>''', unsafe_allow_html=True)

    st.markdown('''<div style="background-color:white;padding:6px;text-align:left;"><p style="color:black;font-size:15px;">               
📌Project Approach
                
1. Data Understanding and Preprocessing:

🔹Identify variable types and distributions.
                
🔹Handle missing values, outliers, and skewness.
                
🔹Encode categorical variables appropriately.
                
2. Exploratory Data Analysis (EDA):

🔹Visualize data distributions and relationships.
                
3. Feature Engineering:

🔹Create informative features and eliminate redundant ones.
                
4.Model Building and Evaluation:

🔹Train and evaluate regression and classification models.
                
🔹Optimize models using cross-validation and grid search.
                
5.Streamlit Application Development:

🔹Create an interactive interface for predictions.
            </p></div>''', unsafe_allow_html=True)


    st.markdown(
    """
    <style>
    @keyframes blink {
        0% { opacity: 1; }
        50% { opacity: 0; }
        100% { opacity: 1; }
    }
    .blink {
        animation: blink 1s infinite;
        font-size: 3em; 
        color: white; 
        text-align: center; 
        display: block;
    }
    .container {
        text-align: center; 
    }
    </style>
    <div class='container'>
        <div class='blink'>👋😊 END</div>
    </div>
    """,
    unsafe_allow_html=True
)
    st.balloons()
