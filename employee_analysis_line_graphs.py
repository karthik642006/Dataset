
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("employee_performance_productivity_dataset.csv")

# Set figure size
plt.figure(figsize=(15, 10))

# Line Plot 1: Monthly Hours Worked vs Projects Completed
plt.subplot(2, 2, 1)
plt.plot(df['Employee_ID'], df['Monthly_Hours_Worked'], label='Monthly Hours', marker='o')
plt.plot(df['Employee_ID'], df['Projects_Completed'], label='Projects Completed', marker='s')
plt.xticks(rotation=90)
plt.title('Monthly Hours vs Projects Completed')
plt.xlabel('Employee ID')
plt.ylabel('Value')
plt.legend()

# Line Plot 2: Performance Score over Employees
plt.subplot(2, 2, 2)
plt.plot(df['Employee_ID'], df['Performance_Score'], color='green', marker='^')
plt.xticks(rotation=90)
plt.title('Performance Score per Employee')
plt.xlabel('Employee ID')
plt.ylabel('Performance Score')

# Line Plot 3: Salary vs Experience Years
plt.subplot(2, 2, 3)
plt.plot(df['Employee_ID'], df['Salary (INR/month)'], label='Salary', color='orange', marker='D')
plt.plot(df['Employee_ID'], df['Experience_Years'], label='Experience Years', color='blue', marker='x')
plt.xticks(rotation=90)
plt.title('Salary vs Experience')
plt.xlabel('Employee ID')
plt.ylabel('Value')
plt.legend()

# Line Plot 4: Remote Work Ratio vs Job Satisfaction
plt.subplot(2, 2, 4)
plt.plot(df['Employee_ID'], df['Remote_Work_Ratio (%)'], label='Remote Work Ratio', marker='o')
plt.plot(df['Employee_ID'], df['Job_Satisfaction'], label='Job Satisfaction', marker='s')
plt.xticks(rotation=90)
plt.title('Remote Work vs Satisfaction')
plt.xlabel('Employee ID')
plt.ylabel('Value')
plt.legend()

# Adjust layout and show plots
plt.tight_layout()
plt.show()
