# Employee-perofrmance-prediction
# Employee Performance Prediction

This project aims to predict employee performance using machine learning models based on various employee attributes such as age, department, job role, work experience, and satisfaction scores.

## 📊 Dataset

The dataset used in this project is an Excel file containing employee details. It includes features like:

- Age, Gender, Education Background
- Department, Job Role, Business Travel Frequency
- Work-Life Balance, Training Times Last Year
- Attrition Status, Performance Rating

Data Source: [GitHub - Employee_Performance.xls](https://github.com/Shubh2310-developer/employee-perofrmance-prediction/raw/main/Employee_Performance.xls)

## 🧪 Technologies and Libraries

- Python
- pandas, seaborn, matplotlib
- scikit-learn (LabelEncoder, StandardScaler, GridSearchCV, etc.)
- pickle (for model serialization)

## ⚙️ Workflow

1. **Data Loading and Cleaning**
   - Read the dataset from a remote GitHub URL.
   - Handle categorical variables using Label Encoding.
   - Normalize features using StandardScaler.

2. **Exploratory Data Analysis (EDA)**
   - Visualizations using seaborn and matplotlib.
   - Check correlation between features.

3. **Model Building**
   - Train-test split of the dataset.
   - Use machine learning classifiers (like Random Forest, SVM, or others).
   - Hyperparameter tuning using GridSearchCV.

4. **Evaluation**
   - Accuracy score
   - Confusion matrix
   - Classification report

5. **Model Saving**
   - Save the trained model using `pickle` for future use.

## 📈 Performance Metrics

The model is evaluated on standard metrics like:
- Accuracy
- Precision, Recall, F1-Score
- Confusion Matrix

## 🚀 How to Run

1. Clone this repository
2. Install required libraries:
   ```bash
   pip install pandas seaborn matplotlib scikit-learn xlrd
Run the Jupyter Notebook:
jupyter notebook MLMODEL.ipynb
