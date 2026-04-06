# # import streamlit as st
# # import requests

# # st.title("🏠 House Price Prediction")

# # st.write("Enter values:")

# # # create inputs
# # features = []

# # for i in range(22):
# #     val = st.number_input(f"Feature {i+1}", value=0.0)
# #     features.append(val)

# # # button
# # if st.button("Predict"):
# #     try:
# #         response = requests.post(
# #             "http://127.0.0.1:5000/predict",
# #             json={"features": features}
# #         )

# #         data = response.json()

# #         if "predicted_price" in data:
# #             st.success(f"Predicted Price: ₹ {data['predicted_price']:.2f}")
# #         else:
# #             st.error(data)

# #     except Exception as e:
# #         st.error(f"Error: {e}")


# import streamlit as st
# import requests

# st.title("🏠 House Price Prediction App")

# st.write("Fill house details:")

# # Real inputs (example mapping)
# living_area = st.number_input("Living Area")
# bedrooms = st.number_input("Bedrooms")
# bathrooms = st.number_input("Bathrooms")
# floors = st.number_input("Number of Floors")
# waterfront = st.number_input("Waterfront (0/1)")
# views = st.number_input("Number of Views")
# condition = st.number_input("Condition (1-5)")
# grade = st.number_input("Grade")
# basement_area = st.number_input("Basement Area")
# built_year = st.number_input("Built Year")
# renovation_year = st.number_input("Renovation Year")
# postal_code = st.number_input("Postal Code")
# latitude = st.number_input("Latitude")
# longitude = st.number_input("Longitude")
# living_area_renov = st.number_input("Living Area Renovated")
# lot_area_renov = st.number_input("Lot Area Renovated")
# schools = st.number_input("Nearby Schools")
# distance_airport = st.number_input("Distance from Airport")

# # Fill remaining dummy values if needed
# features = [
#     living_area, bedrooms, bathrooms, floors, waterfront, views,
#     condition, grade, basement_area, built_year, renovation_year,
#     postal_code, latitude, longitude, living_area_renov,
#     lot_area_renov, schools, distance_airport
# ]

# # ⚠️ Ensure total = 22
# while len(features) < 22:
#     features.append(0)

# # Predict
# if st.button("Predict Price"):
#     try:
#         response = requests.post(
#             "http://127.0.0.1:5000/predict",
#             json={"features": features}
#         )

#         result = response.json()

#         st.success(f"💰 Predicted Price: ₹ {result['predicted_price']:.2f}")

#     except Exception as e:
#         st.error(f"Error: {e}")



# import streamlit as st
# import requests

# st.title("🏠 House Price Predictor")

# living_area = st.number_input("Living Area")
# bedrooms = st.number_input("Bedrooms")
# bathrooms = st.number_input("Bathrooms")
# grade = st.number_input("Grade")
# built_year = st.number_input("Built Year")
# postal_code = st.number_input("Postal Code")

# if st.button("Predict Price"):
#     data = {
#         "living area": living_area,
#         "bedrooms": bedrooms,
#         "bathrooms": bathrooms,
#         "grade": grade,
#         "built year": built_year,
#         "postal code": postal_code
#     }

#     response = requests.post(
#         "http://127.0.0.1:5000/predict",
#         json=data
#     )

#     result = response.json()

#     if "predicted_price" in result:
#         st.success(f"💰 Price: ₹ {result['predicted_price']:.2f}")
#     else:
#         st.error(result)

#  code with new ui 

# import streamlit as st
# import requests

# # Page config
# st.set_page_config(
#     page_title="House Price Predictor",
#     page_icon="🏠",
#     layout="centered"
# )

# # Custom CSS for styling
# st.markdown("""
#     <style>
#     body {
#         background-color: #0f172a;
#     }
#     .main {
#         background-color: #0f172a;
#         color: white;
#     }
#     .stTextInput, .stNumberInput, .stSelectbox {
#         background-color: #1e293b;
#         border-radius: 10px;
#         padding: 5px;
#     }
#     .stButton>button {
#         background-color: #22c55e;
#         color: white;
#         border-radius: 10px;
#         height: 50px;
#         width: 100%;
#         font-size: 18px;
#         font-weight: bold;
#     }
#     .stButton>button:hover {
#         background-color: #16a34a;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Title Section
# st.markdown("<h1 style='text-align: center;'>🏠 House Price Predictor</h1>", unsafe_allow_html=True)
# st.markdown("<p style='text-align: center; color: gray;'>Enter property details to estimate price</p>", unsafe_allow_html=True)

# # Card-like layout
# with st.container():
#     st.markdown("### 📋 Property Details")

#     col1, col2 = st.columns(2)

#     with col1:
#         living_area = st.number_input("Living Area (sq ft)", help="Enter total living area")
#         bedrooms = st.number_input("Bedrooms")
#         bathrooms = st.number_input("Bathrooms")

#     with col2:
#         grade = st.slider("House Grade", 1, 13)
#         built_year = st.number_input("Built Year")
#         postal_code = st.number_input("Postal Code")

# # Unit conversion
# st.markdown("### 🔄 Area Unit")
# unit = st.selectbox("Select Unit", ["Square Feet", "Gaj", "Square Meter"])

# if unit == "Gaj":
#     living_area = living_area * 9
# elif unit == "Square Meter":
#     living_area = living_area * 10.764

# # Predict Button
# if st.button("💰 Predict Price"):
#     data = {
#         "living area": living_area,
#         "number of bedrooms": bedrooms,
#         "number of bathrooms": bathrooms,
#         "grade of the house": grade,
#         "Built Year": built_year,
#         "Postal Code": postal_code
#     }

#     try:
#         response = requests.post(
#             "http://127.0.0.1:5000/predict",
#             json=data
#         )

#         result = response.json()

#         if "predicted_price" in result:
#             st.markdown(f"""
#                 <div style="
#                     background-color:#1e293b;
#                     padding:20px;
#                     border-radius:15px;
#                     text-align:center;
#                     margin-top:20px;">
#                     <h2 style="color:#22c55e;">💰 Estimated Price</h2>
#                     <h1>₹ {result['predicted_price']:,.0f}</h1>
#                 </div>
#             """, unsafe_allow_html=True)
#         else:
#             st.error(result)

#     except Exception as e:
#         st.error(f"Error: {e}")

# /new ui with loading animation

# import streamlit as st
# import requests
# import time
# import matplotlib.pyplot as plt

# # Page config
# st.set_page_config(page_title="House Price Predictor", layout="centered")

# st.title("🏠 House Price Predictor")
# st.markdown("### Enter Property Details")

# # Inputs
# col1, col2 = st.columns(2)

# with col1:
#     living_area = st.number_input("Living Area (sq ft)")
#     bedrooms = st.number_input("Bedrooms")
#     bathrooms = st.number_input("Bathrooms")

# with col2:
#     grade = st.slider("House Grade", 1, 13)
#     built_year = st.number_input("Built Year")
#     postal_code = st.number_input("Postal Code")

# # Unit conversion
# unit = st.selectbox("Area Unit", ["Square Feet", "Gaj", "Square Meter"])

# if unit == "Gaj":
#     living_area = living_area * 9
# elif unit == "Square Meter":
#     living_area = living_area * 10.764

# # Predict
# if st.button("💰 Predict Price"):

#     with st.spinner("🔄 Predicting price... Please wait"):
#         time.sleep(2)  # fake loading effect

#         data = {
#             "living area": living_area,
#             "number of bedrooms": bedrooms,
#             "number of bathrooms": bathrooms,
#             "grade of the house": grade,
#             "Built Year": built_year,
#             "Postal Code": postal_code
#         }

#         try:
#             response = requests.post(
#                 "http://127.0.0.1:5000/predict",
#                 json=data
#             )

#             result = response.json()

#             if "predicted_price" in result:
#                 price = result['predicted_price']

#                 # Show result
#                 st.success(f"💰 Estimated Price: ₹ {price:,.0f}")

#                 # 📊 GRAPH: Price vs Area
#                 st.markdown("### 📊 Price vs Living Area")

#                 areas = [500, 1000, 1500, 2000, 2500]
#                 prices = []

#                 for a in areas:
#                     temp_data = data.copy()
#                     temp_data["living area"] = a

#                     res = requests.post(
#                         "http://127.0.0.1:5000/predict",
#                         json=temp_data
#                     ).json()

#                     prices.append(res["predicted_price"])

#                 # Plot graph
#                 fig, ax = plt.subplots()
#                 ax.plot(areas, prices, marker='o')
#                 ax.set_xlabel("Living Area (sq ft)")
#                 ax.set_ylabel("Predicted Price")
#                 ax.set_title("Price vs Area Trend")

#                 st.pyplot(fig)

#             else:
#                 st.error(result)

#         except Exception as e:
#             st.error(f"Error: {e}")

import streamlit as st
import requests
import time
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="House Price Predictor", layout="centered")

# Header
st.markdown("""
    <h1 style='text-align:center;'>🏠 House Price Predictor</h1>
    <p style='text-align:center; color:gray;'>Smart ML-based property valuation</p>
""", unsafe_allow_html=True)

# Input Section
st.markdown("### 📋 Property Details")

col1, col2 = st.columns(2)

with col1:
    living_area = st.number_input("Living Area (sq ft)")
    bedrooms = st.number_input("Bedrooms")
    bathrooms = st.number_input("Bathrooms")

with col2:
    grade = st.slider("House Grade", 1, 13)
    built_year = st.number_input("Built Year")
    postal_code = st.number_input("Postal Code")

# Predict button
if st.button("💰 Predict Price"):

    with st.spinner("🔄 Predicting..."):
        time.sleep(1.5)

        data = {
            "living area": living_area,
            "number of bedrooms": bedrooms,
            "number of bathrooms": bathrooms,
            "grade of the house": grade,
            "Built Year": built_year,
            "Postal Code": postal_code
        }

        try:
            response = requests.post(
                "http://127.0.0.1:5000/predict",
                json=data
            )

            result = response.json()

            if "predicted_price" in result:
                price = result["predicted_price"]

                # 🔥 BIG PRICE CARD
                st.markdown(f"""
                    <div style="
                        background: linear-gradient(135deg, #22c55e, #16a34a);
                        padding:30px;
                        border-radius:20px;
                        text-align:center;
                        margin-top:20px;
                        color:white;">
                        <h2>Estimated Price</h2>
                        <h1 style="font-size:48px;">₹ {price:,.0f}</h1>
                    </div>
                """, unsafe_allow_html=True)

                # 📊 SMALL GRAPH
                st.markdown("### 📊 Price Trend (Area vs Price)")

                areas = [500, 1000, 1500, 2000, 2500]
                prices = []

                for a in areas:
                    temp = data.copy()
                    temp["living area"] = a

                    res = requests.post(
                        "http://127.0.0.1:5000/predict",
                        json=temp
                    ).json()

                    prices.append(res["predicted_price"])

                fig, ax = plt.subplots(figsize=(5,3))
                ax.plot(areas, prices, marker='o')
                ax.set_xlabel("Area (sq ft)")
                ax.set_ylabel("Price")

                st.pyplot(fig)

            else:
                st.error(result)

        except Exception as e:
            st.error(f"Error: {e}")