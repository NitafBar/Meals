import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('Test Meal Sheet - Sheet1.csv')
st.title('Meals Calculator')

# Protein
st.header("Protein")
st.caption("Enter Protein")
protein = st.text_input("calories", value = 0, key = "calories", label_visibility="hidden")
proteinFloat = float(protein)

# Carbohydrates
st.header("Carbohydrates")
st.caption("Enter Carbohydrates")
carbohydrates = st.text_input("protein", value = 0, key = "protein", label_visibility="hidden")
carbohydratesFloat = float(carbohydrates)

# Fat
st.header("Fat")
st.caption("Enter Fat")
fat = st.text_input("carbohydrates", value = 0, key = "carbohydrates", label_visibility="hidden")
fatFloat = float(fat)

# Calories
st.header("Calories")
st.caption("Enter Calories")
calories = st.text_input("fat", value = 0, key = "fat", label_visibility="hidden")
caloriesFloat = float(calories)

macroList = []
mealList = []

if st.button("Calculate"):
	for i in range(len(df.index)):
		for j in range(len(df.columns)):
			macroList.append(df.iloc[i, j])
		if (proteinFloat >= macroList[2] - 10 and proteinFloat <= macroList[2] + 10 and carbohydratesFloat >= macroList[3] - 5 and carbohydratesFloat <= macroList[3] + 5 
			and fatFloat >= macroList[4] - 10 and fatFloat <= macroList[4] + 10 and caloriesFloat >= macroList[5] - 100 and caloriesFloat <= macroList[5] + 100):
			mealList.append(macroList[1])
			st.text(macroList[1] + "\nProtein: " + str(macroList[2]) + " Carbohydrates: " + str(macroList[3]) + " Fat: " + str(macroList[4]) + " Calories: " + str(macroList[5]) + "\n")
		macroList.clear()

# labels = 'Protein', 'Carbohydrates', 'Fat'
# sizes = [macroList[2], macroList[3], macroList[4]]

# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, labels=labels, autopct='%1.1f',
#         shadow=False, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# st.pyplot(fig1)
