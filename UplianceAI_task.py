import pandas as pd
import matplotlib.pyplot as plt

# Loading of the dataset
file_path = r"C:\Users\mital\Videos\Profile details\UplianceAI DA-intern\Data Analyst Intern Assignment - Excel.xlsx"
user_details = pd.read_excel(file_path, sheet_name='UserDetails.csv')
cooking_sessions = pd.read_excel(file_path, sheet_name='CookingSessions.csv')
order_details = pd.read_excel(file_path, sheet_name='OrderDetails.csv')

# Cleaning of data
order_details.isna().sum()
order_details['Rating'].fillna(order_details['Rating'].mean(), inplace=True)

# Renaming the columns to avoid conflicts
cooking_sessions = cooking_sessions.rename(columns={'Dish Name': 'Session Dish Name', 'Meal Type': 'Session Meal Type'})
order_details = order_details.rename(columns={'Dish Name': 'Order Dish Name', 'Meal Type': 'Order Meal Type'})

# Merging of datasets
merged_data = pd.merge(cooking_sessions, order_details, on='Session ID', how='inner')
merged_data = pd.merge(merged_data, user_details, on='User ID', how='inner')

                        ### Charts/Visuals ###
# Popular Dishes Analysis
popular_dishes = merged_data['Order Dish Name'].value_counts()
plt.figure(figsize=(10, 6))
popular_dishes.plot(kind='bar')
plt.title('Top Ordered Dishes')
plt.xlabel('Dish Name')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Orders by Time of Day
time_of_day_orders = merged_data['Time of Day'].value_counts()
plt.figure(figsize=(8, 5))
time_of_day_orders.plot(kind='bar')
plt.title('Orders by Time of Day')
plt.xlabel('Time of Day')
plt.ylabel('Number of Orders')
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Age Distribution
plt.figure(figsize=(8, 5))
merged_data['Age'].plot(kind='hist', bins=5, edgecolor='black')
plt.title('Age Distribution of Users')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Spending Trends
spending_per_user = merged_data.groupby('User Name')['Amount (USD)'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
spending_per_user.plot(kind='bar')
plt.title('Total Spending Per User')
plt.xlabel('User Name')
plt.ylabel('Total Amount (USD)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Correlation Analysis
correlation_matrix = merged_data[['Session Rating', 'Rating', 'Duration (mins)', 'Amount (USD)']].corr()
print(correlation_matrix)
