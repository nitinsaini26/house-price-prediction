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
                "https://house-price-api-8k09.onrender.com/predict",
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

                    # res = requests.post(
                    #     "http://127.0.0.1:5000/predict",
                    #     json=temp
                    # ).json()
                    res = requests.post(
                        "https://house-price-api-8k09.onrender.com/predict",
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
