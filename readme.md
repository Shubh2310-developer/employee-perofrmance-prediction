This project involves predicting employee performance using a machine learning model trained on the Employee_Performance dataset. The model utilizes a Random Forest classifier with hyperparameter tuning through Grid Search.

Dataset
The dataset used for training the model is available in the file:
Employee_Performance.xls
Features
The dataset contains the following features, which are used as input parameters for the prediction model:

Age
Type: Integer
Description: The age of the employee.

Gender
Type: Integer (encoded)
Description: Encoded value representing gender (0 for Male, 1 for Female).

Years at Company
Type: Integer
Description: The number of years the employee has been with the company.

Job Role
Type: Integer (encoded)
Description: Encoded value representing the employee's job role.
0: Manager
1: Engineer
2: Sales Representative
3: Data Analyst
4: HR Specialist

Performance Rating
Type: Integer (encoded)
Description: Encoded value representing performance.
0: Low
1: Average
2: Good
3: Excellent

Education Level
Type: Integer (encoded)
Description: Encoded value representing education level.
0: High School
1: Bachelor’s
2: Master’s
3: Doctorate

Salary
Type: Float
Description: The salary of the employee.

Department
Type: Integer (encoded)
Description: Encoded value representing the department.
0: Sales
1: Human Resources
2: Marketing
3: IT

Experience Years
Type: Integer
Description: The total years of experience of the employee.#   E m p l o y e e - p r o j e c t  
 