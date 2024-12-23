## Data Analysis Report - User Behavior, Cooking Preferences, and Order Trends.

### Project Overview ###

This project analyzes user behavior, cooking preferences, and order trends datasets. The primary goal is to uncover insights about user demographics, popular dishes, and spending patterns to guide marketing strategies and improve customer engagement.

### Datasets Used ###

a) UserDetails - Contains demographic data, favorite meals, and order history.

b) CookingSessions - Logs cooking session details, including ratings and durations.

c) OrderDetails - Tracks order details, including status, amounts, and ratings.

### Analysis Objectives ###

- Clean and merge the datasets to create a comprehensive view of user behavior.

- Identify popular dishes based on order frequency.

- Analyze the relationship between cooking sessions and user orders.

- Explore demographic factors (age, location) influencing user preferences.

- Visualize trends to support business recommendations.

### EDA and Data Preprocessing ###
<details>
 <summary>using Python</summary>
	
 ```python
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

```
</details>

### Key Findings ###

- #### Popular Dishes:
![alt text](https://github.com/Subham1702/Data-Analytics-Upliance-AI-/blob/main/Popular%20dishes.png)
   - 'Spaghetti' and 'Caesar Salad' account for 25% and 18.75% of total orders, respectively.

   - Combined, these two dishes make up 43.75% of all orders, highlighting user preferences.

- #### Order Timing:
![alt text](https://github.com/Subham1702/Data-Analytics-Upliance-AI-/blob/main/Order%20Timing.png)
   - 50% of orders are placed during evening hours (dinner), while 31.25% occur during daytime (lunch).

   - Morning orders account for only 18.75%, indicating lower breakfast engagement.

- #### Demographic Insights:
![alt text](https://github.com/Subham1702/Data-Analytics-Upliance-AI-/blob/main/Demography%20(Age).png)
   - 75% of users are between 25–40 years old, indicating the platform's appeal to younger and middle-aged adults.

   - Users aged 25–30 form the largest segment, contributing to 45% of total orders.

- #### Spending Patterns:
![alt text](https://github.com/Subham1702/Data-Analytics-Upliance-AI-/blob/main/Spending.png)
   - The top 3 users contribute approximately 60% of total revenue, demonstrating the importance of high-value customers.

   The average spending per user is $25.50, with high-spenders averaging $35.00.

- #### Correlation Analysis:
![alt text](https://github.com/Subham1702/Data-Analytics-Upliance-AI-/blob/main/Correlation.png)
   - Session ratings and order ratings show a positive correlation of 0.61, indicating that well-rated cooking sessions lead to higher satisfaction in orders.

   - Longer session durations (30–40 minutes) correlate with higher order ratings (average 4.7).

### Technologies Used ###

- Python Libraries: Pandas, Matplotlib.

- Data Handling: Data cleaning, transformation, and merging.

- Visualization: Charts and graphs to present insights.

### Recommendations ###

- Promote Popular Dishes - Highlight 'Spaghetti' and 'Caesar Salad' in marketing campaigns.

- Target Peak Hours - Launch promotional offers during lunch and dinner hours to boost sales.

- Personalized Engagement - Leverage cooking session data to recommend dishes aligned with user preferences.

- Focus on Demographics - Optimize campaigns targeting users aged 25–40.

- Loyalty Programs - Introduce incentives for high-spending users to improve retention.

### Future Improvements ###

- Expand analysis to include time-series trends for seasonal demand.

- Incorporate machine learning models to predict user preferences.

- Automate reporting dashboards for real-time insights.

