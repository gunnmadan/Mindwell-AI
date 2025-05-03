# Artifical-Intelligence

🧠 MindWell: Enhancing Therapeutic Intervention Through Technology

MindWell is a personalized AI-powered health platform designed to bridge the gap between traditional therapy and modern digital health solutions. This project integrates wearable data, machine learning models, and fuzzy logic systems to assess mental health risks and deliver tailored recommendations. By analyzing heart rate, sleep quality, and physical activity, MindWell provides actionable insights to promote psychological well-being.

---

## Features

- **Real-time Risk Scoring:** Evaluate individual risk levels using four ML models: Logistic Regression, Random Forest, SVM, and XGBoost.
- **Fuzzy Logic Integration:** A fuzzy scoring engine helps capture nuanced relationships among features.
- **Visual Dashboards:** Interactive graphs to explore trends in heart rate, sleep, and stress levels.
- **Health Alerts:** Automatically flags users with high stress, low sleep, or elevated heart rate.
- **Recommendations:** Personalized health tips based on user profile and risk classification.
- **Streamlit App:** Clean, modular web interface organized across different pages.

---

## Project Structure

```
.
├── app.py                       # Main Streamlit application
├── clean_dataset_labeled.csv   # Processed and labeled dataset
├── fuzzy_scoring.py            # Fuzzy logic model
├── models/                     # Jupyter Notebooks for each model
│   ├── logistic_regression.ipynb
│   ├── random_forest.ipynb
│   ├── svm.ipynb
│   └── xgboost.ipynb
├── pages/                      # Streamlit pages
│   ├── home.py
│   ├── visuals.py
│   ├── alerts.py
│   └── recommendations.py
├── utils/
│   └── risk_analysis.py        # Logic for calculating and categorizing risk
└── README.md
```

---

## Dataset

This project uses two main datasets:

1. **Sleep Health and Lifestyle Dataset (Kaggle)**  
   Includes attributes like sleep duration, stress levels, sleep disorders, and heart rate.

2. **Fitbit User Data**  
   Derived from multiple CSV files (daily activity, heart rate, and sleep data), cleaned and merged to form a unified dataset with over 25 features.

**Merged Dataset Columns Include:**  
- Activity metrics (Steps, Distance, Calories)  
- Sleep metrics (Minutes Asleep, Time in Bed, Sleep Efficiency)  
- Heart metrics (AverageHeartRate)  
- Custom labels (Risk Score, Risk Category)

---

## Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/mindwell.git
cd mindwell
```

2. **Create and activate a virtual environment**
```bash
python3 -m venv env
source env/bin/activate  # for macOS/Linux
env\Scripts\activate   # for Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```
Or manually:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost streamlit
```

---

## Running the Application

Launch the Streamlit dashboard with:

```bash
streamlit run app.py
```

- A browser window will open at `http://localhost:8501`
- Navigate between Home, Visualizations, Alerts, and Recommendations using the sidebar

---

## Model Performance Summary

| Model              | Accuracy | Macro F1 Score | Key Insight                                  |
|-------------------|----------|----------------|----------------------------------------------|
| Logistic Regression | 98.19%   | 0.94           | Balanced and interpretable model             |
| Random Forest      | 98.19%   | 0.94           | Equally strong, less prone to overfitting    |
| SVM                | 90.91%   | 0.48           | Failed to generalize across minority class   |
| XGBoost            | 98.13%   | 0.94           | Effective even with imbalanced classes       |

---

## Visualizations

- **Scatter Plot:** Relationship between stress and sleep duration
- **Bar Chart:** Sleep disorder distribution
- **Boxplots:** Variation in sleep efficiency and heart rate
- **Histogram:** Risk score spread
- **ROC Curve:** Classifier performance comparison

---

## Streamlit Pages Overview

- `Home`: Mood check-in + dataset overview
- `Visualizations`: Plots to explore sleep and stress trends
- `Alerts`: Real-time health warnings
- `Recommendations`: Personalized wellness advice with risk breakdown

---

## Future Enhancements

- Integrate with real-time wearable APIs (Fitbit, Apple Health)
- Include additional psychological attributes (mood logs, screen time)
- Improve fuzzy membership tuning using domain expertise
- Expand classification labels (e.g., Severe Risk, Improving)

---

## Author

**Madan**, Department of Computer Science, Georgia State University  
📧 gmadan1@student.gsu.edu

---

## License

MIT License – use freely for academic and educational purposes.

