# 🏥 Insurance Premium Prediction App

This project is a full-stack machine learning web app to predict insurance premiums.

- ✅ **Backend:** FastAPI for serving the model (`ajayk01/insurance-premium-backend`)
- ✅ **Frontend:** Streamlit for user interaction (`ajayk01/insurance-premium-frontend`)
- ✅ **Dockerized:** Runs both services in isolated containers that communicate over a shared network.

---

## 📂 Project Structure

```
├── Backend
│   ├── app.py
│   ├── config
│   │   └── city_tier.py
│   ├── Dockerfile
│   ├── Model
│   │   ├── model.pkl
│   │   └── predict.py
│   ├── requirements.txt
│   └── schema
│       ├── prediction_response.py
│       └── user_input.py
├── docker-compose.yml
├── extras
│   ├── insurance.csv
│   └── serve_ml_with_fastAPI.ipynb
├── Frontend
│   ├── Dockerfile
│   ├── frontend.py
│   └── requirements.txt
└── README.md
```

---

### Clone the repository & Run

```bash
git clone https://github.com/Ajay1812/insurance-preimum-predictor.git
cd insurance-preimum-predictor
docker-compose up
```
