#  House Price Prediction System

> A full-stack Machine Learning web application that predicts house prices using real-world data and advanced regression techniques.

---

##  Overview

This project is an end-to-end **Machine Learning system** designed to estimate house prices based on key features such as area, number of bedrooms, and location.

It combines:
-  Data Analysis  
-  Machine Learning  
-  Web Development  
-  Cloud Deployment  

to deliver a complete real-world solution.

---

##  Key Features

✔ Accurate house price prediction using ML  
✔ Clean and interactive UI (Streamlit)  
✔ Real-time prediction via Flask API  
✔ Area vs Price visualization graph   
✔ Fully deployed backend on cloud   
✔ Scalable and modular architecture  

---

##  How It Works

1. User enters property details  
2. Data is sent to Flask API  
3. ML model processes input  
4. Predicted price is returned  
5. UI displays result with graph  

---

##  Tech Stack

| Category        | Technology |
|----------------|-----------|
| Language       | Python  |
| ML Model       | XGBoost Regressor |
| Backend        | Flask |
| Frontend       | Streamlit |
| Visualization  | Matplotlib |
| Deployment     | Render |

---

##  Live Demo

 **Live Application:**  
https://house-price-prediction-vtreja3pj4cryvqpqzchif.streamlit.app/

---

##  Project Structure
House-Price-Prediction
│
├── app.py # Flask API (Backend)
├── app_ui.py # Streamlit UI (Frontend)
├── train.py # Model training script
├── model.pkl # Trained ML model
├── features.pkl # Feature order
├── requirements.txt # Dependencies


---

##  Installation & Setup

###  Clone Repository

```bash
git clone https://github.com/nitinsaini26/house-price-prediction.git
cd house-price-prediction

### Install Dependencies
pip install -r requirements.txt

### Run Frontend 
python -m streamlit run app_ui.py

### Run Backend 
python app.py

```
##  Model Details

- **Algorithm:** XGBoost Regressor  
- **Problem Type:** Regression  
- **Evaluation Metric:** RMSE  

###  Features Used:
- Living Area  
- Number of Bedrooms  
- Number of Bathrooms  
- Grade of the House  
- Built Year  
- Postal Code  

---

##  Sample Output

-  Predicted Price  
-  Area vs Price Graph  

<img width="1395" height="690" alt="Screenshot of House Price Predictor-1" src="https://github.com/user-attachments/assets/79daa3e7-7873-4125-80d0-ffd78e54a189" />
<img width="1323" height="386" alt="Screenshot of HPP (Price)" src="https://github.com/user-attachments/assets/8b02b984-b95a-40fb-8093-7aa615e34083" />
<img width="1333" height="725" alt="Screenshot of HPP(Graph)" src="https://github.com/user-attachments/assets/90c3e90f-a08a-4855-8dca-1e2c090932c4" />


---

##  Deployment

- Backend deployed on cloud using Render  
- API accessible globally via public URL  
- Frontend connected using HTTP requests  

---

##  Challenges Faced

- Handling API connection after deployment  
- Fixing local vs cloud URL issues  
- Ensuring correct feature order for prediction  

---

##  Learning Outcomes

- End-to-end ML project development  
- API creation using Flask  
- UI development using Streamlit  
- Cloud deployment and debugging  
- Real-world problem solving  
