# Assignment Information
print("Data 51100- Spring 2020")
print("Alec Peterson")
print("Programming Assignment #4")

# Import pandas
import pandas as pd

# Grab data from file specified
data = pd.read_csv("cars.csv")

# Grab specific data for probability
ma_data = data[['make', 'aspiration']]

# Calculate the probability for both aspiration and make
make_data = (ma_data['make'].value_counts() / ma_data['make'].count() * 100).round(2)
aspiration_data = (ma_data['aspiration'].value_counts() / ma_data['aspiration'].count() * 100)

# Creating the DataFrame for probabilities of make
make_df = pd.DataFrame({'make': make_data.index.unique(), 'make_prob': make_data.values})

# Loop to print conditional probability
for make in ma_data['make'].unique():
    for aspiration in ma_data['aspiration'].unique():
        make_frame = ma_data[ma_data['make'] == make]
        make_count = make_frame.shape[0]
        both_frame = make_frame[make_frame['aspiration'] == aspiration]
        both_count = both_frame.shape[0]
        if both_count != 0:
            print("Prob(aspiration=" + aspiration + "|make=" + make + ")" + " = " + str(round(100 * both_count / make_count, 2)) + "%")
        else:
            print("Prob(aspiration=" + aspiration + "|make=" + make + ")" + " = " + str(0) + "%")
print("\n")

# Loop to print probability for each make
for make in ma_data['make'].unique():
    print("Prob(make=" + make + ") = " + str(round(data['make'].value_counts().loc[make] / data['make'].value_counts().sum() * 100, 2)) + "%")