import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the models from the .pkl file
with open('model.pkl', 'rb') as file:
    loaded_models = pickle.load(file)

# Access a specific model (e.g., Random Forest)
rf_model = loaded_models['random_forest']  # Change this to the model you want to use

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect all 9 features from the form
        age = int(request.form['age'])
        gender = int(request.form['gender'])
        years_at_company = int(request.form['years_at_company'])
        job_role = int(request.form['job_role'])  # Example encoded value
        performance_rating = int(request.form['performance_rating'])  # Example encoded value
        education_level = int(request.form['education_level'])  # Example encoded value
        salary = float(request.form['salary'])  # Example value
        department = int(request.form['department'])  # Example encoded value
        experience_years = int(request.form['experience_years'])  # Example value

        # Prepare input data for prediction
        input_data = [[age, gender, years_at_company, job_role, performance_rating,
                       education_level, salary, department, experience_years]]  
        
        # Make prediction using the selected model
        prediction = rf_model.predict(input_data)[0]  # Get the first prediction result

        return render_template('result.html', prediction=prediction)
    
    except Exception as e:
        return str(e)  # Display error message for debugging

if __name__ == '__main__':
    app.run(debug=True)