import streamlit as st
import pandas as pd 
import plotly.express as px
#import matplotlib.pylot as plt
import math 

def home_page():
    st.title("Welcome to Fine Winerary - the Wine Selection App")
    st.header("This app helps you find the perfect wine to pass the time.")
    st.subheader("Use the navigation menu to access the survey and get personalized recommendations.")

# Define the survey page function
def survey_page():
    import streamlit as st
    import pandas as pd 
    import plotly.express as px
    #import matplotlib.pylot as plt
    import math 

    st.title("Wine Selection Survey")
    
    wine_red_white = pd.read_csv("wine-quality-white-and-red.csv")
    #st.write(wine_red_white)
    #st.dataframe(wine_data)
    
    # st.write("Are you looking for wine for a dinner pairing or for enjoying?")
    # left, right = st.columns(2)
    # if left.button("Pairing", use_container_width=True):
    #     left.markdown("You clicked the pairing button.")
    # if right.button("Enjoying", use_container_width=True):
    #     right.markdown("You clicked the enjoying button.")
    import streamlit as st
    
    # User selection for the wine purpose
    purpose = st.radio(
        "Are you looking for wine for a dinner pairing or for enjoying?",
        [":rainbow[Enjoying]", "***Dinner Pairing***"],
        index=None,
        key="wine_purpose"  # Unique key for this radio
    )
    
    st.write("You selected:", purpose)
    
    if purpose == "***Dinner Pairing***":
        # User selection for dinner
        dinner = st.radio(
            "What are you having for dinner tonight? Steak, chicken, seafood?",
            ["Red meat", "Poultry", "Seafood"],
            index=None,
            key="dinner_selection"  # Unique key for this radio
        )
        
        st.write("You selected:", dinner)
        
        if dinner == "Seafood":
            seafood_type = st.radio(
                "What kind of seafood are you having?",
                ["Fish", "Shellfish"],
                index=None,
            )
            st.write("You selected:", seafood_type)
        
        # User selection for taste preference
        taste = st.radio(
            "Do you prefer sweet or bitter?",
            ["Sweet", "Bitter"],
            index=None,
            key="taste_preference"  # Unique key for this radio
        )
        
        st.write("You selected:", taste)
        
        # Check if the conditions are met
        
    #### Red Meat Options #####
        if purpose == "***Dinner Pairing***" and dinner == "Red Meat" and taste == "Sweet":
            st.title("Sweet Dry Wines") #looking for lower acidity
    
            # Create individual masks for dry wines
            mask_fixed_acidity_dry = (wine_red_white["fixed acidity"] >= 4.0) & (wine_red_white["fixed acidity"] <= 8)
            mask_volatile_acidity_dry = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] <= 0.7)
            mask_citric_acid_dry = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 0.5)
            mask_residual_sugar_dry = (wine_red_white["residual sugar"] >= 0.1) & (wine_red_white["residual sugar"] <= 5)
            mask_chlorides_dry = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
            mask_free_sulfur_dioxide_dry = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 50)
            mask_total_sulfur_dioxide_dry = (wine_red_white["total sulfur dioxide"] >= 70) & (wine_red_white["total sulfur dioxide"] <= 200)
            mask_density_dry = (wine_red_white["density"] >= 0.99) & (wine_red_white["density"] <= 1.05)
            mask_pH_dry = (wine_red_white["pH"] >= 3.2) & (wine_red_white["pH"] <= 3.6)
            mask_sulphates_dry = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
            mask_alcohol_dry = (wine_red_white["alcohol"] >= 11.0) & (wine_red_white["alcohol"] <= 14.0)
            
            # Create individual masks for sweet wines
            mask_fixed_acidity_sweet = (wine_red_white["fixed acidity"] >= 5.0) & (wine_red_white["fixed acidity"] <= 10)
            mask_volatile_acidity_sweet = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] < 1.2)
            mask_citric_acid_sweet = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 1.0)
            mask_residual_sugar_sweet = (wine_red_white["residual sugar"] >= 0.030) & (wine_red_white["residual sugar"] <= 0.150)
            mask_chlorides_sweet = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
            mask_free_sulfur_dioxide_sweet = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 70)
            mask_total_sulfur_dioxide_sweet = (wine_red_white["total sulfur dioxide"] >= 100) & (wine_red_white["total sulfur dioxide"] <= 300)
            mask_density_sweet = (wine_red_white["density"] >= 1.05) & (wine_red_white["density"] <= 1.15)
            mask_pH_sweet = (wine_red_white["pH"] >= 3.00) & (wine_red_white["pH"] <= 3.50)
            mask_sulphates_sweet = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
            mask_alcohol_sweet = (wine_red_white["alcohol"] >= 12.0) & (wine_red_white["alcohol"] <= 20.0)
        
            combined_mask = (
                (mask_fixed_acidity_dry | mask_fixed_acidity_sweet) &
                (mask_volatile_acidity_dry | mask_volatile_acidity_sweet) &
                (mask_citric_acid_dry | mask_citric_acid_sweet) &
                (mask_residual_sugar_dry | mask_residual_sugar_sweet) &
                (mask_chlorides_dry | mask_chlorides_sweet) &
                (mask_free_sulfur_dioxide_dry | mask_free_sulfur_dioxide_sweet) &
                (mask_total_sulfur_dioxide_dry | mask_total_sulfur_dioxide_sweet) &
                (mask_density_dry | mask_density_sweet) &
                (mask_pH_dry | mask_pH_sweet) &
                (mask_sulphates_dry | mask_sulphates_sweet) &
                (mask_alcohol_dry | mask_alcohol_sweet)
                )
        
            # Create the final DataFrame for dry and sweet wines
            sweet_n_dry = wine_red_white[combined_mask]
            
            # if dry_sweet_wines_df1.empty:
            #     st.write("No wines match your criteria.")
            # else: 
            # Display the result
            st.write(sweet_n_dry)
            
    
            fig = px.scatter(
            dry_sweet_wines_df1,
            x='alcohol',  # X-axis variable
            y='residual sugar',  # Y-axis variable
            color='quality',  # Color by quality (or any other categorical variable)
            hover_data=['fixed acidity', 'volatile acidity'],  # Additional data to show on hover
            title='Dry & Sweet Wines: Alcohol vs. Residual Sugar',
            labels={'alcohol': 'Alcohol Content (%)', 'residual sugar': 'Residual Sugar (g/dm³)'}
            )
            
            # Display the plot in the Streamlit app
            st.plotly_chart(fig)
        
        elif purpose == "***Dinner Pairing***" and dinner == "Red meat" and taste == "Bitter":
            st.title("Dry Wines")
            
            # Create individual masks for dry wines
            mask_fixed_acidity = (wine_red_white["fixed acidity"] >= 4.0) & (wine_red_white["fixed acidity"] <= 8)
            mask_volatile_acidity = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] <= 0.7)
            mask_citric_acid = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 0.5)
            mask_residual_sugar = (wine_red_white["residual sugar"] >= 0.1) & (wine_red_white["residual sugar"] <= 5)
            mask_chlorides = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
            mask_free_sulfur_dioxide = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 50)
            mask_total_sulfur_dioxide = (wine_red_white["total sulfur dioxide"] >= 70) & (wine_red_white["total sulfur dioxide"] <= 200)
            mask_density = (wine_red_white["density"] >= 0.99) & (wine_red_white["density"] <= 1.05)
            mask_pH = (wine_red_white["pH"] >= 3.2) & (wine_red_white["pH"] <= 3.6)
            mask_sulphates = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
            mask_alcohol = (wine_red_white["alcohol"] >= 11.0) & (wine_red_white["alcohol"] <= 14.0)
        
            # Combine all masks into one
            combined_mask = (mask_fixed_acidity &
                             mask_volatile_acidity &
                             mask_citric_acid &
                             mask_residual_sugar &
                             mask_chlorides &
                             mask_free_sulfur_dioxide &
                             mask_total_sulfur_dioxide &
                             mask_density &
                             mask_pH &
                             mask_sulphates &
                             mask_alcohol)
        
            # Create the final DataFrame for dry wines
            dry_wines_df = wine_red_white[combined_mask]
        
            # Display the result
            st.write(dry_wines_df)
    
            fig = px.scatter(
            dry_wines_df,
            x='alcohol',  # X-axis variable
            y='residual sugar',  # Y-axis variable
            color='quality',  # Color by quality (or any other categorical variable)
            hover_data=['fixed acidity', 'volatile acidity'],  # Additional data to show on hover
            title='Dry & Sweet Wines: Alcohol vs. Residual Sugar',
            labels={'alcohol': 'Alcohol Content (%)', 'residual sugar': 'Residual Sugar (g/dm³)'}
            )
            
            # Display the plot in the Streamlit app
            st.plotly_chart(fig)
    
            
    #### Poultry Outputs #######        
        elif purpose == "***Dinner Pairing***" and dinner == "Poultry" and taste == "Sweet":
            st.title("Sweet Dry Wines")
        
            # Create individual masks for dry wines
            mask_fixed_acidity_dry = (wine_red_white["fixed acidity"] >= 4.0) & (wine_red_white["fixed acidity"] <= 8)
            mask_volatile_acidity_dry = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] <= 0.7)
            mask_citric_acid_dry = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 0.5)
            mask_residual_sugar_dry = (wine_red_white["residual sugar"] >= 0.1) & (wine_red_white["residual sugar"] <= 5)
            mask_chlorides_dry = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
            mask_free_sulfur_dioxide_dry = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 50)
            mask_total_sulfur_dioxide_dry = (wine_red_white["total sulfur dioxide"] >= 70) & (wine_red_white["total sulfur dioxide"] <= 200)
            mask_density_dry = (wine_red_white["density"] >= 0.99) & (wine_red_white["density"] <= 1.05)
            mask_pH_dry = (wine_red_white["pH"] >= 3.2) & (wine_red_white["pH"] <= 3.6)
            mask_sulphates_dry = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
            mask_alcohol_dry = (wine_red_white["alcohol"] >= 11.0) & (wine_red_white["alcohol"] <= 14.0)
            
            # Create individual masks for sweet wines
            mask_fixed_acidity_sweet = (wine_red_white["fixed acidity"] >= 5.0) & (wine_red_white["fixed acidity"] <= 10)
            mask_volatile_acidity_sweet = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] < 1.2)
            mask_citric_acid_sweet = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 1.0)
            mask_residual_sugar_sweet = (wine_red_white["residual sugar"] >= 0.030) & (wine_red_white["residual sugar"] <= 0.150)
            mask_chlorides_sweet = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
            mask_free_sulfur_dioxide_sweet = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 70)
            mask_total_sulfur_dioxide_sweet = (wine_red_white["total sulfur dioxide"] >= 100) & (wine_red_white["total sulfur dioxide"] <= 300)
            mask_density_sweet = (wine_red_white["density"] >= 1.05) & (wine_red_white["density"] <= 1.15)
            mask_pH_sweet = (wine_red_white["pH"] >= 3.00) & (wine_red_white["pH"] <= 3.50)
            mask_sulphates_sweet = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
            mask_alcohol_sweet = (wine_red_white["alcohol"] >= 12.0) & (wine_red_white["alcohol"] <= 20.0)
        
            combined_mask = (
            (mask_fixed_acidity_dry | mask_fixed_acidity_sweet) &
            (mask_volatile_acidity_dry | mask_volatile_acidity_sweet) &
            (mask_citric_acid_dry | mask_citric_acid_sweet) &
            (mask_residual_sugar_dry | mask_residual_sugar_sweet) &
            (mask_chlorides_dry | mask_chlorides_sweet) &
            (mask_free_sulfur_dioxide_dry | mask_free_sulfur_dioxide_sweet) &
            (mask_total_sulfur_dioxide_dry | mask_total_sulfur_dioxide_sweet) &
            (mask_density_dry | mask_density_sweet) &
            (mask_pH_dry | mask_pH_sweet) &
            (mask_sulphates_dry | mask_sulphates_sweet) &
            (mask_alcohol_dry | mask_alcohol_sweet)
            )
        
            # Create the final DataFrame for dry and sweet wines
            dry_sweet_wines_df = wine_red_white[combined_mask]
            dry_sweet_wines_df = wine_red_white[combined_mask & (wine_red_white["quality"] > 5.0)]
            
            # Display the result
            st.write(dry_sweet_wines_df)
    
            fig = px.scatter(
            dry_sweet_wines_df,
            x='alcohol',  # X-axis variable
            y='residual sugar',  # Y-axis variable
            color='quality',  # Color by quality (or any other categorical variable)
            hover_data=['fixed acidity', 'volatile acidity'],  # Additional data to show on hover
            title='Dry Sweet Wines: Alcohol vs. Residual Sugar',
            labels={'alcohol': 'Alcohol Content (%)', 'residual sugar': 'Residual Sugar (g/dm³)'}
            )
            
            # Display the plot in the Streamlit app
            st.plotly_chart(fig)    
    
        elif purpose == "***Dinner Pairing***" and dinner == "Poultry" and taste == "Bitter":
            st.title("Dry Wines")
            
            # Create individual masks for dry wines
            mask_fixed_acidity = (wine_red_white["fixed acidity"] >= 4.0) & (wine_red_white["fixed acidity"] <= 8)
            mask_volatile_acidity = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] <= 0.7)
            mask_citric_acid = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 0.5)
            mask_residual_sugar = (wine_red_white["residual sugar"] >= 0.1) & (wine_red_white["residual sugar"] <= 5)
            mask_chlorides = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
            mask_free_sulfur_dioxide = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 50)
            mask_total_sulfur_dioxide = (wine_red_white["total sulfur dioxide"] >= 70) & (wine_red_white["total sulfur dioxide"] <= 200)
            mask_density = (wine_red_white["density"] >= 0.99) & (wine_red_white["density"] <= 1.05)
            mask_pH = (wine_red_white["pH"] >= 3.2) & (wine_red_white["pH"] <= 3.6)
            mask_sulphates = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
            mask_alcohol = (wine_red_white["alcohol"] >= 11.0) & (wine_red_white["alcohol"] <= 14.0)
        
            # Combine all masks into one
            combined_mask = (mask_fixed_acidity &
                             mask_volatile_acidity &
                             mask_citric_acid &
                             mask_residual_sugar &
                             mask_chlorides &
                             mask_free_sulfur_dioxide &
                             mask_total_sulfur_dioxide &
                             mask_density &
                             mask_pH &
                             mask_sulphates &
                             mask_alcohol)
        
            # Create the final DataFrame for dry wines
            dry_wines_df = wine_red_white[combined_mask]
            dry_wines_df = wine_red_white[combined_mask & (wine_red_white["quality"] > 5.0)]
        
            # Display the result
            st.write(dry_wines_df)
    
            fig = px.scatter(
            dry_wines_df,
            x='alcohol',  # X-axis variable
            y='residual sugar',  # Y-axis variable
            color='quality',  # Color by quality (or any other categorical variable)
            hover_data=['fixed acidity', 'volatile acidity'],  # Additional data to show on hover
            title='High Quality Dry Wines: Alcohol vs. Residual Sugar',
            labels={'alcohol': 'Alcohol Content (%)', 'residual sugar': 'Residual Sugar (g/dm³)'}
            )
            
            # Display the plot in the Streamlit app
            st.plotly_chart(fig)
    
    #### Seafood Outputs ########
        elif purpose == "***Dinner Pairing***" and dinner == "Seafood" and seafood_type == "Fish" and taste == "Sweet":
            st.title("Sweet Dry Wines")
            
            # Create individual masks for dry wines
            mask_fixed_acidity_dry = (wine_red_white["fixed acidity"] >= 4.0) & (wine_red_white["fixed acidity"] <= 8)
            mask_volatile_acidity_dry = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] <= 0.7)
            mask_citric_acid_dry = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 0.5)
            mask_residual_sugar_dry = (wine_red_white["residual sugar"] >= 0.1) & (wine_red_white["residual sugar"] <= 5)
            mask_chlorides_dry = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
            mask_free_sulfur_dioxide_dry = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 50)
            mask_total_sulfur_dioxide_dry = (wine_red_white["total sulfur dioxide"] >= 70) & (wine_red_white["total sulfur dioxide"] <= 200)
            mask_density_dry = (wine_red_white["density"] >= 0.99) & (wine_red_white["density"] <= 1.05)
            mask_pH_dry = (wine_red_white["pH"] >= 3.2) & (wine_red_white["pH"] <= 3.6)
            mask_sulphates_dry = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
            mask_alcohol_dry = (wine_red_white["alcohol"] >= 11.0) & (wine_red_white["alcohol"] <= 14.0)
            
            # Create individual masks for sweet wines
            mask_fixed_acidity_sweet = (wine_red_white["fixed acidity"] >= 5.0) & (wine_red_white["fixed acidity"] <= 10)
            mask_volatile_acidity_sweet = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] < 1.2)
            mask_citric_acid_sweet = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 1.0)
            mask_residual_sugar_sweet = (wine_red_white["residual sugar"] >= 0.030) & (wine_red_white["residual sugar"] <= 0.150)
            mask_chlorides_sweet = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
            mask_free_sulfur_dioxide_sweet = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 70)
            mask_total_sulfur_dioxide_sweet = (wine_red_white["total sulfur dioxide"] >= 100) & (wine_red_white["total sulfur dioxide"] <= 300)
            mask_density_sweet = (wine_red_white["density"] >= 1.05) & (wine_red_white["density"] <= 1.15)
            mask_pH_sweet = (wine_red_white["pH"] >= 3.00) & (wine_red_white["pH"] <= 3.50)
            mask_sulphates_sweet = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
            mask_alcohol_sweet = (wine_red_white["alcohol"] >= 12.0) & (wine_red_white["alcohol"] <= 20.0)
        
            combined_mask = (
            (mask_fixed_acidity_dry | mask_fixed_acidity_sweet) &
            (mask_volatile_acidity_dry | mask_volatile_acidity_sweet) &
            (mask_citric_acid_dry | mask_citric_acid_sweet) &
            (mask_residual_sugar_dry | mask_residual_sugar_sweet) &
            (mask_chlorides_dry | mask_chlorides_sweet) &
            (mask_free_sulfur_dioxide_dry | mask_free_sulfur_dioxide_sweet) &
            (mask_total_sulfur_dioxide_dry | mask_total_sulfur_dioxide_sweet) &
            (mask_density_dry | mask_density_sweet) &
            (mask_pH_dry | mask_pH_sweet) &
            (mask_sulphates_dry | mask_sulphates_sweet) &
            (mask_alcohol_dry | mask_alcohol_sweet)
            )
        
            # Create the final DataFrame for dry and sweet wines
            dry_sweet_wines_df = wine_red_white[combined_mask]
            dry_sweet_wines_df = wine_red_white[combined_mask & (wine_red_white["quality"] > 5.0) & (wine_red_white["alcohol"] >= 12.0)]
            
            # Display the result
            st.write(dry_sweet_wines_df)
    
            fig = px.scatter(
            dry_sweet_wines_df,
            x='alcohol',  # X-axis variable
            y='residual sugar',  # Y-axis variable
            color='quality',  # Color by quality (or any other categorical variable)
            hover_data=['fixed acidity', 'volatile acidity'],  # Additional data to show on hover
            title='High Quality Dry Wines: Alcohol vs. Residual Sugar',
            labels={'alcohol': 'Alcohol Content (%)', 'residual sugar': 'Residual Sugar (g/dm³)'}
            )
            
            # Display the plot in the Streamlit app
            st.plotly_chart(fig)
    
    
        elif purpose == "***Dinner Pairing***" and dinner == "Seafood" and seafood_type == "Fish" and taste == "Bitter":
            st.title("Dry Wines")
            
            # Create individual masks for dry wines
            mask_fixed_acidity = (wine_red_white["fixed acidity"] >= 4.0) & (wine_red_white["fixed acidity"] <= 8)
            mask_volatile_acidity = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] <= 0.7)
            mask_citric_acid = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 0.5)
            mask_residual_sugar = (wine_red_white["residual sugar"] >= 0.1) & (wine_red_white["residual sugar"] <= 5)
            mask_chlorides = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
            mask_free_sulfur_dioxide = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 50)
            mask_total_sulfur_dioxide = (wine_red_white["total sulfur dioxide"] >= 70) & (wine_red_white["total sulfur dioxide"] <= 200)
            mask_density = (wine_red_white["density"] >= 0.99) & (wine_red_white["density"] <= 1.05)
            mask_pH = (wine_red_white["pH"] >= 3.2) & (wine_red_white["pH"] <= 3.6)
            mask_sulphates = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
            mask_alcohol = (wine_red_white["alcohol"] >= 11.0) & (wine_red_white["alcohol"] <= 14.0)
        
            # Combine all masks into one
            combined_mask = (mask_fixed_acidity &
                             mask_volatile_acidity &
                             mask_citric_acid &
                             mask_residual_sugar &
                             mask_chlorides &
                             mask_free_sulfur_dioxide &
                             mask_total_sulfur_dioxide &
                             mask_density &
                             mask_pH &
                             mask_sulphates &
                             mask_alcohol)
        
            # Create the final DataFrame for dry wines
            dry_wines_df = wine_red_white[combined_mask]
            dry_wines_df = wine_red_white[combined_mask & (wine_red_white["quality"] > 5.0) & (wine_red_white["alcohol"] > 12.0)]
        
            # Display the result
            st.write(dry_wines_df)
    
            fig = px.scatter(
            dry_wines_df,
            x='alcohol',  # X-axis variable
            y='residual sugar',  # Y-axis variable
            color='quality',  # Color by quality (or any other categorical variable)
            hover_data=['fixed acidity', 'volatile acidity'],  # Additional data to show on hover
            title='High Quality Dry Wines: Alcohol vs. Residual Sugar',
            labels={'alcohol': 'Alcohol Content (%)', 'residual sugar': 'Residual Sugar (g/dm³)'}
            )
            
            # Display the plot in the Streamlit app
            st.plotly_chart(fig)
    
        elif purpose == "***Dinner Pairing***" and dinner == "Seafood" and seafood_type == "Shellfish" and taste == "Bitter":
            st.title("Dry Wines")
            
            # Create individual masks for dry wines
            mask_fixed_acidity = (wine_red_white["fixed acidity"] >= 4.0) & (wine_red_white["fixed acidity"] <= 8)
            mask_volatile_acidity = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] <= 0.7)
            mask_citric_acid = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 0.5)
            mask_residual_sugar = (wine_red_white["residual sugar"] >= 0.1) & (wine_red_white["residual sugar"] <= 5)
            mask_chlorides = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
            mask_free_sulfur_dioxide = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 50)
            mask_total_sulfur_dioxide = (wine_red_white["total sulfur dioxide"] >= 70) & (wine_red_white["total sulfur dioxide"] <= 200)
            mask_density = (wine_red_white["density"] >= 0.99) & (wine_red_white["density"] <= 1.05)
            mask_pH = (wine_red_white["pH"] >= 3.2) & (wine_red_white["pH"] <= 3.6)
            mask_sulphates = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
            mask_alcohol = (wine_red_white["alcohol"] >= 11.0) & (wine_red_white["alcohol"] <= 14.0)
        
            # Combine all masks into one
            combined_mask = (mask_fixed_acidity &
                             mask_volatile_acidity &
                             mask_citric_acid &
                             mask_residual_sugar &
                             mask_chlorides &
                             mask_free_sulfur_dioxide &
                             mask_total_sulfur_dioxide &
                             mask_density &
                             mask_pH &
                             mask_sulphates &
                             mask_alcohol)
        
            # Create the final DataFrame for dry wines
            dry_wines_df = wine_red_white[combined_mask]
            dry_wines_df = wine_red_white[combined_mask & (wine_red_white["quality"] > 5.0)]
        
            # Display the result
            st.write(dry_wines_df)
    
            fig = px.scatter(
            dry_wines_df,
            x='alcohol',  # X-axis variable
            y='residual sugar',  # Y-axis variable
            color='quality',  # Color by quality (or any other categorical variable)
            hover_data=['fixed acidity', 'volatile acidity'],  # Additional data to show on hover
            title='High Quality Dry Wines: Alcohol vs. Residual Sugar',
            labels={'alcohol': 'Alcohol Content (%)', 'residual sugar': 'Residual Sugar (g/dm³)'}
            )
            
            # Display the plot in the Streamlit app
            st.plotly_chart(fig)
    
        elif purpose == "***Dinner Pairing***" and dinner == "Seafood" and seafood_type == "Shellfish" and taste == "Bitter":
            st.title("Light Bodied Dry Wines")
            
            # Create individual masks for dry wines
            mask_fixed_acidity = (wine_red_white["fixed acidity"] >= 4.0) & (wine_red_white["fixed acidity"] <= 8)
            mask_volatile_acidity = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] <= 0.7)
            mask_citric_acid = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 0.5)
            mask_residual_sugar = (wine_red_white["residual sugar"] >= 0.1) & (wine_red_white["residual sugar"] <= 5)
            mask_chlorides = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
            mask_free_sulfur_dioxide = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 50)
            mask_total_sulfur_dioxide = (wine_red_white["total sulfur dioxide"] >= 70) & (wine_red_white["total sulfur dioxide"] <= 200)
            mask_density = (wine_red_white["density"] >= 0.99) & (wine_red_white["density"] <= 1.05)
            mask_pH = (wine_red_white["pH"] >= 3.2) & (wine_red_white["pH"] <= 3.6)
            mask_sulphates = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
            mask_alcohol = (wine_red_white["alcohol"] >= 11.0) & (wine_red_white["alcohol"] <= 14.0)
        
            # Combine all masks into one
            combined_mask = (mask_fixed_acidity &
                             mask_volatile_acidity &
                             mask_citric_acid &
                             mask_residual_sugar &
                             mask_chlorides &
                             mask_free_sulfur_dioxide &
                             mask_total_sulfur_dioxide &
                             mask_density &
                             mask_pH &
                             mask_sulphates &
                             mask_alcohol)
        
            # Create the final DataFrame for dry wines
            dry_wines_df = wine_red_white[combined_mask]
            dry_wines_df = wine_red_white[combined_mask & (wine_red_white["quality"] > 5.0), (wine_red_white["density"] == 0.99)]
        
            # Display the result
            st.write(dry_wines_df)
    
            fig = px.scatter(
            dry_wines_df,
            x='alcohol',  # X-axis variable
            y='residual sugar',  # Y-axis variable
            color='quality',  # Color by quality (or any other categorical variable)
            hover_data=['fixed acidity', 'volatile acidity'],  # Additional data to show on hover
            title='High Quality Dry Wines: Alcohol vs. Residual Sugar',
            labels={'alcohol': 'Alcohol Content (%)', 'residual sugar': 'Residual Sugar (g/dm³)'}
            )
            
            # Display the plot in the Streamlit app
            st.plotly_chart(fig)
    
        elif purpose == "***Dinner Pairing***" and dinner == "Seafood" and seafood_type == "Shellfish" and taste == "Sweet":
            st.title("Mild Wines")
            
            # Create individual masks for dry wines
            mask_fixed_acidity_dry = (wine_red_white["fixed acidity"] >= 4.0) & (wine_red_white["fixed acidity"] <= 8)
            mask_volatile_acidity_dry = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] <= 0.7)
            mask_citric_acid_dry = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 0.5)
            mask_residual_sugar_dry = (wine_red_white["residual sugar"] >= 0.1) & (wine_red_white["residual sugar"] <= 5)
            mask_chlorides_dry = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
            mask_free_sulfur_dioxide_dry = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 50)
            mask_total_sulfur_dioxide_dry = (wine_red_white["total sulfur dioxide"] >= 70) & (wine_red_white["total sulfur dioxide"] <= 200)
            mask_density_dry = (wine_red_white["density"] >= 0.99) & (wine_red_white["density"] <= 1.05)
            mask_pH_dry = (wine_red_white["pH"] >= 3.2) & (wine_red_white["pH"] <= 3.6)
            mask_sulphates_dry = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
            mask_alcohol_dry = (wine_red_white["alcohol"] >= 11.0) & (wine_red_white["alcohol"] <= 14.0)
            
            # Create individual masks for sweet wines
            mask_fixed_acidity_sweet = (wine_red_white["fixed acidity"] >= 5.0) & (wine_red_white["fixed acidity"] <= 10)
            mask_volatile_acidity_sweet = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] < 1.2)
            mask_citric_acid_sweet = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 1.0)
            mask_residual_sugar_sweet = (wine_red_white["residual sugar"] >= 0.030) & (wine_red_white["residual sugar"] <= 0.150)
            mask_chlorides_sweet = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
            mask_free_sulfur_dioxide_sweet = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 70)
            mask_total_sulfur_dioxide_sweet = (wine_red_white["total sulfur dioxide"] >= 100) & (wine_red_white["total sulfur dioxide"] <= 300)
            mask_density_sweet = (wine_red_white["density"] >= 1.05) & (wine_red_white["density"] <= 1.15)
            mask_pH_sweet = (wine_red_white["pH"] >= 3.00) & (wine_red_white["pH"] <= 3.50)
            mask_sulphates_sweet = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
            mask_alcohol_sweet = (wine_red_white["alcohol"] >= 12.0) & (wine_red_white["alcohol"] <= 20.0)
        
            combined_mask = (
            (mask_fixed_acidity_dry | mask_fixed_acidity_sweet) &
            (mask_volatile_acidity_dry | mask_volatile_acidity_sweet) &
            (mask_citric_acid_dry | mask_citric_acid_sweet) &
            (mask_residual_sugar_dry | mask_residual_sugar_sweet) &
            (mask_chlorides_dry | mask_chlorides_sweet) &
            (mask_free_sulfur_dioxide_dry | mask_free_sulfur_dioxide_sweet) &
            (mask_total_sulfur_dioxide_dry | mask_total_sulfur_dioxide_sweet) &
            (mask_density_dry | mask_density_sweet) &
            (mask_pH_dry | mask_pH_sweet) &
            (mask_sulphates_dry | mask_sulphates_sweet) &
            (mask_alcohol_dry | mask_alcohol_sweet)
            )
        
            # Create the final DataFrame for dry and sweet wines
            dry_sweet_wines_df = wine_red_white[combined_mask]
            dry_sweet_wines_df = wine_red_white[combined_mask & 
                                (wine_red_white["quality"] > 5.0) & 
                                (wine_red_white["alcohol"] >= 12.0) & 
                                (wine_red_white["citric acid"] >= 0.4)]
            
            # Display the result
            st.write(dry_sweet_wines_df)
    
            fig = px.scatter(
            dry_sweet_wines_df,
            x='alcohol',  # X-axis variable
            y='residual sugar',  # Y-axis variable
            color='quality',  # Color by quality (or any other categorical variable)
            hover_data=['fixed acidity', 'volatile acidity'],  # Additional data to show on hover
            title='High Quality Mild Wines: Alcohol vs. Residual Sugar',
            labels={'alcohol': 'Alcohol Content (%)', 'residual sugar': 'Residual Sugar (g/dm³)'}
            )
            
            # Display the plot in the Streamlit app
            st.plotly_chart(fig)
    ##################################################################################################
    elif purpose == ":rainbow[Enjoying]":
        # User selection for taste preference
        taste = st.radio(
            "Are you looking for a more sweet or salty wine?",
            ["Sweet", "Bitter"],
            index=None,
            key="taste_preference"  # Unique key for this radio
        )
        
        st.write("You selected:", taste)
    
        # User selection for alcohol consumption
        alchy = st.radio(
            "Are you looking for a higher or lower ABV?",
            ["High (> 10%)", "Lower"],
            index=None,
            key="alchy_preference"  # Unique key for this radio
        )
        
        st.write("You selected:", alchy)
    
        # Check if the conditions are met
        if purpose == ":rainbow[Enjoying]" and taste == "Bitter" and alchy == "High (> 10%)":
            st.title("Off-Dry Sweet Wines")
    
    
            # Create individual masks for off-dry wines
            mask_fixed_acidity_off_dry = (wine_red_white["fixed acidity"] >= 4.0) & (wine_red_white["fixed acidity"] <= 8)
            mask_volatile_acidity_off_dry = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] <= 0.8)
            mask_citric_acid_off_dry = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 0.5)
            mask_residual_sugar_off_dry = (wine_red_white["residual sugar"] >= 5) & (wine_red_white["residual sugar"] <= 30)
            mask_chlorides_off_dry = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
            mask_free_sulfur_dioxide_off_dry = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 60)
            mask_total_sulfur_dioxide_off_dry = (wine_red_white["total sulfur dioxide"] >= 70) & (wine_red_white["total sulfur dioxide"] <= 250)
            mask_density_off_dry = (wine_red_white["density"] >= 1.00) & (wine_red_white["density"] <= 1.07)
            mask_pH_off_dry = (wine_red_white["pH"] >= 3.2) & (wine_red_white["pH"] <= 3.5)
            mask_sulphates_off_dry = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
            mask_alcohol_off_dry = (wine_red_white["alcohol"] >= 11.0) & (wine_red_white["alcohol"] <= 14.5)
            
            # Create individual masks for sweet wines
            mask_fixed_acidity_sweet = (wine_red_white["fixed acidity"] >= 5.0) & (wine_red_white["fixed acidity"] <= 10)
            mask_volatile_acidity_sweet = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] < 1.2)
            mask_citric_acid_sweet = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 1.0)
            mask_residual_sugar_sweet = (wine_red_white["residual sugar"] >= 0.030) & (wine_red_white["residual sugar"] <= 0.150)
            mask_chlorides_sweet = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
            mask_free_sulfur_dioxide_sweet = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 70)
            mask_total_sulfur_dioxide_sweet = (wine_red_white["total sulfur dioxide"] >= 100) & (wine_red_white["total sulfur dioxide"] <= 300)
            mask_density_sweet = (wine_red_white["density"] >= 1.05) & (wine_red_white["density"] <= 1.15)  # Added density mask for sweet wines
            mask_pH_sweet = (wine_red_white["pH"] >= 3.00) & (wine_red_white["pH"] <= 3.50)
            mask_sulphates_sweet = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
            mask_alcohol_sweet = (wine_red_white["alcohol"] >= 12.0) & (wine_red_white["alcohol"] <= 20.0)
            
            # Combine masks for off-dry and sweet wines using logical OR
            combined_mask = (
                mask_fixed_acidity_off_dry | mask_fixed_acidity_sweet &
                mask_volatile_acidity_off_dry | mask_volatile_acidity_sweet &
                mask_citric_acid_off_dry | mask_citric_acid_sweet &
                mask_residual_sugar_off_dry | mask_residual_sugar_sweet &
                mask_chlorides_off_dry | mask_chlorides_sweet &
                mask_free_sulfur_dioxide_off_dry | mask_free_sulfur_dioxide_sweet &
                mask_total_sulfur_dioxide_off_dry | mask_total_sulfur_dioxide_sweet &
                mask_density_off_dry | mask_density_sweet &  # Include density masks
                mask_pH_off_dry | mask_pH_sweet &
                mask_sulphates_off_dry | mask_sulphates_sweet &
                mask_alcohol_off_dry | mask_alcohol_sweet
            )
            
            # Create the final DataFrame for off-dry and sweet wines
            offdry_sweet_wines_df = wine_red_white[combined_mask & (wine_red_white["alcohol"] > 10.0)]
            
            # Display the result
            st.write(offdry_sweet_wines_df)
    
            fig = px.scatter(
            offdry_sweet_wines_df,
            x='alcohol',  # X-axis variable
            y='residual sugar',  # Y-axis variable
            color='quality',  # Color by quality (or any other categorical variable)
            hover_data=['fixed acidity', 'volatile acidity'],  # Additional data to show on hover
            title='Dry & Sweet Wines: Alcohol vs. Residual Sugar',
            labels={'alcohol': 'Alcohol Content (%)', 'residual sugar': 'Residual Sugar (g/dm³)'}
            )
            
            # Display the plot in the Streamlit app
            st.plotly_chart(fig)
    
        elif purpose == ":rainbow[Enjoying]" and taste == "Bitter" and alchy == "Lower":
            st.title("Off-Dry Sweet Wines")
    
            # Create individual masks for off-dry wines
            mask_fixed_acidity_off_dry = (wine_red_white["fixed acidity"] >= 4.0) & (wine_red_white["fixed acidity"] <= 8)
            mask_volatile_acidity_off_dry = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] <= 0.8)
            mask_citric_acid_off_dry = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 0.5)
            mask_residual_sugar_off_dry = (wine_red_white["residual sugar"] >= 5) & (wine_red_white["residual sugar"] <= 30)
            mask_chlorides_off_dry = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
            mask_free_sulfur_dioxide_off_dry = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 60)
            mask_total_sulfur_dioxide_off_dry = (wine_red_white["total sulfur dioxide"] >= 70) & (wine_red_white["total sulfur dioxide"] <= 250)
            mask_density_off_dry = (wine_red_white["density"] >= 1.00) & (wine_red_white["density"] <= 1.07)
            mask_pH_off_dry = (wine_red_white["pH"] >= 3.2) & (wine_red_white["pH"] <= 3.5)
            mask_sulphates_off_dry = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
            mask_alcohol_off_dry = (wine_red_white["alcohol"] >= 11.0) & (wine_red_white["alcohol"] <= 14.5)
            
            # Create individual masks for sweet wines
            mask_fixed_acidity_sweet = (wine_red_white["fixed acidity"] >= 5.0) & (wine_red_white["fixed acidity"] <= 10)
            mask_volatile_acidity_sweet = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] < 1.2)
            mask_citric_acid_sweet = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 1.0)
            mask_residual_sugar_sweet = (wine_red_white["residual sugar"] >= 0.030) & (wine_red_white["residual sugar"] <= 0.150)
            mask_chlorides_sweet = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
            mask_free_sulfur_dioxide_sweet = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 70)
            mask_total_sulfur_dioxide_sweet = (wine_red_white["total sulfur dioxide"] >= 100) & (wine_red_white["total sulfur dioxide"] <= 300)
            mask_density_sweet = (wine_red_white["density"] >= 1.05) & (wine_red_white["density"] <= 1.15)  # Added density mask for sweet wines
            mask_pH_sweet = (wine_red_white["pH"] >= 3.00) & (wine_red_white["pH"] <= 3.50)
            mask_sulphates_sweet = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
            mask_alcohol_sweet = (wine_red_white["alcohol"] >= 12.0) & (wine_red_white["alcohol"] <= 20.0)
    
            # Combine masks for off-dry and sweet wines using logical OR
            combined_mask = (
                mask_fixed_acidity_off_dry | mask_fixed_acidity_sweet &
                mask_volatile_acidity_off_dry | mask_volatile_acidity_sweet &
                mask_citric_acid_off_dry | mask_citric_acid_sweet &
                mask_residual_sugar_off_dry | mask_residual_sugar_sweet &
                mask_chlorides_off_dry | mask_chlorides_sweet &
                mask_free_sulfur_dioxide_off_dry | mask_free_sulfur_dioxide_sweet &
                mask_total_sulfur_dioxide_off_dry | mask_total_sulfur_dioxide_sweet &
                mask_density_off_dry | mask_density_sweet &  # Include density masks
                mask_pH_off_dry | mask_pH_sweet &
                mask_sulphates_off_dry | mask_sulphates_sweet &
                mask_alcohol_off_dry | mask_alcohol_sweet
            )
    
        
            # Create the final DataFrame for off-dry and sweet wines
            offdry_sweet_wines_df2 = wine_red_white[combined_mask & (wine_red_white["alcohol"] < 10.0)]
                
                # Display the result
            st.write(offdry_sweet_wines_df2)
    
            fig = px.scatter(
            offdry_sweet_wines_df2,
            x='alcohol',  # X-axis variable
            y='residual sugar',  # Y-axis variable
            color='quality',  # Color by quality (or any other categorical variable)
            hover_data=['fixed acidity', 'volatile acidity'],  # Additional data to show on hover
            title='Dry & Sweet Wines: Alcohol vs. Residual Sugar',
            labels={'alcohol': 'Alcohol Content (%)', 'residual sugar': 'Residual Sugar (g/dm³)'}
            )
            
            # Display the plot in the Streamlit app
            st.plotly_chart(fig)
    
        elif purpose == ":rainbow[Enjoying]" and taste == "Sweet" and alchy == "Lower":
            st.title("Off-Dry Sweet Wines")
    
            # Create individual masks for off-dry wines
            mask_fixed_acidity_off_dry = (wine_red_white["fixed acidity"] >= 4.0) & (wine_red_white["fixed acidity"] <= 8)
            mask_volatile_acidity_off_dry = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] <= 0.8)
            mask_citric_acid_off_dry = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 0.5)
            mask_residual_sugar_off_dry = (wine_red_white["residual sugar"] >= 5) & (wine_red_white["residual sugar"] <= 30)
            mask_chlorides_off_dry = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
            mask_free_sulfur_dioxide_off_dry = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 60)
            mask_total_sulfur_dioxide_off_dry = (wine_red_white["total sulfur dioxide"] >= 70) & (wine_red_white["total sulfur dioxide"] <= 250)
            mask_density_off_dry = (wine_red_white["density"] >= 1.00) & (wine_red_white["density"] <= 1.07)
            mask_pH_off_dry = (wine_red_white["pH"] >= 3.2) & (wine_red_white["pH"] <= 3.5)
            mask_sulphates_off_dry = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
            mask_alcohol_off_dry = (wine_red_white["alcohol"] >= 11.0) & (wine_red_white["alcohol"] <= 14.5)
            
            # Create individual masks for sweet wines
            mask_fixed_acidity_sweet = (wine_red_white["fixed acidity"] >= 5.0) & (wine_red_white["fixed acidity"] <= 10)
            mask_volatile_acidity_sweet = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] < 1.2)
            mask_citric_acid_sweet = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 1.0)
            mask_residual_sugar_sweet = (wine_red_white["residual sugar"] >= 0.030) & (wine_red_white["residual sugar"] <= 0.150)
            mask_chlorides_sweet = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
            mask_free_sulfur_dioxide_sweet = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 70)
            mask_total_sulfur_dioxide_sweet = (wine_red_white["total sulfur dioxide"] >= 100) & (wine_red_white["total sulfur dioxide"] <= 300)
            mask_density_sweet = (wine_red_white["density"] >= 1.05) & (wine_red_white["density"] <= 1.15)  # Added density mask for sweet wines
            mask_pH_sweet = (wine_red_white["pH"] >= 3.00) & (wine_red_white["pH"] <= 3.50)
            mask_sulphates_sweet = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
            mask_alcohol_sweet = (wine_red_white["alcohol"] >= 12.0) & (wine_red_white["alcohol"] <= 20.0)
    
            # Combine masks for off-dry and sweet wines using logical OR
            combined_mask = (
                mask_fixed_acidity_off_dry | mask_fixed_acidity_sweet &
                mask_volatile_acidity_off_dry | mask_volatile_acidity_sweet &
                mask_citric_acid_off_dry | mask_citric_acid_sweet &
                mask_residual_sugar_off_dry | mask_residual_sugar_sweet &
                mask_chlorides_off_dry | mask_chlorides_sweet &
                mask_free_sulfur_dioxide_off_dry | mask_free_sulfur_dioxide_sweet &
                mask_total_sulfur_dioxide_off_dry | mask_total_sulfur_dioxide_sweet &
                mask_density_off_dry | mask_density_sweet &  # Include density masks
                mask_pH_off_dry | mask_pH_sweet &
                mask_sulphates_off_dry | mask_sulphates_sweet &
                mask_alcohol_off_dry | mask_alcohol_sweet
            )
    
        
            # Create the final DataFrame for off-dry and sweet wines
            offdry_sweet_wines_df2 = wine_red_white[combined_mask & (wine_red_white["alcohol"] < 10.0)]
            offdry_sweet_wines_df2 = wine_red_white[combined_mask & (wine_red_white["quality"] > 5.0)]
                
                # Display the result
            st.write(offdry_sweet_wines_df2)
    
            fig = px.scatter(
            offdry_sweet_wines_df2,
            x='alcohol',  # X-axis variable
            y='residual sugar',  # Y-axis variable
            color='quality',  # Color by quality (or any other categorical variable)
            hover_data=['fixed acidity', 'volatile acidity'],  # Additional data to show on hover
            title='Off-Dry Sweet Wines: Alcohol vs. Residual Sugar',
            labels={'alcohol': 'Alcohol Content (%)', 'residual sugar': 'Residual Sugar (g/dm³)'}
            )
            
            # Display the plot in the Streamlit app
            st.plotly_chart(fig)
    
        elif purpose == ":rainbow[Enjoying]" and taste == "Sweet" and alchy == "High (> 10%)":
            st.title("Off-Dry Sweet Wines")
    
    
            # Create individual masks for off-dry wines
            mask_fixed_acidity_off_dry = (wine_red_white["fixed acidity"] >= 4.0) & (wine_red_white["fixed acidity"] <= 8)
            mask_volatile_acidity_off_dry = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] <= 0.8)
            mask_citric_acid_off_dry = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 0.5)
            mask_residual_sugar_off_dry = (wine_red_white["residual sugar"] >= 5) & (wine_red_white["residual sugar"] <= 30)
            mask_chlorides_off_dry = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
            mask_free_sulfur_dioxide_off_dry = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 60)
            mask_total_sulfur_dioxide_off_dry = (wine_red_white["total sulfur dioxide"] >= 70) & (wine_red_white["total sulfur dioxide"] <= 250)
            mask_density_off_dry = (wine_red_white["density"] >= 1.00) & (wine_red_white["density"] <= 1.07)
            mask_pH_off_dry = (wine_red_white["pH"] >= 3.2) & (wine_red_white["pH"] <= 3.5)
            mask_sulphates_off_dry = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
            mask_alcohol_off_dry = (wine_red_white["alcohol"] >= 11.0) & (wine_red_white["alcohol"] <= 14.5)
            
            # Create individual masks for sweet wines
            mask_fixed_acidity_sweet = (wine_red_white["fixed acidity"] >= 5.0) & (wine_red_white["fixed acidity"] <= 10)
            mask_volatile_acidity_sweet = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] < 1.2)
            mask_citric_acid_sweet = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 1.0)
            mask_residual_sugar_sweet = (wine_red_white["residual sugar"] >= 0.030) & (wine_red_white["residual sugar"] <= 0.150)
            mask_chlorides_sweet = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
            mask_free_sulfur_dioxide_sweet = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 70)
            mask_total_sulfur_dioxide_sweet = (wine_red_white["total sulfur dioxide"] >= 100) & (wine_red_white["total sulfur dioxide"] <= 300)
            mask_density_sweet = (wine_red_white["density"] >= 1.05) & (wine_red_white["density"] <= 1.15)  # Added density mask for sweet wines
            mask_pH_sweet = (wine_red_white["pH"] >= 3.00) & (wine_red_white["pH"] <= 3.50)
            mask_sulphates_sweet = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
            mask_alcohol_sweet = (wine_red_white["alcohol"] >= 12.0) & (wine_red_white["alcohol"] <= 20.0)
            
            # Combine masks for off-dry and sweet wines using logical OR
            combined_mask = (
                mask_fixed_acidity_off_dry | mask_fixed_acidity_sweet &
                mask_volatile_acidity_off_dry | mask_volatile_acidity_sweet &
                mask_citric_acid_off_dry | mask_citric_acid_sweet &
                mask_residual_sugar_off_dry | mask_residual_sugar_sweet &
                mask_chlorides_off_dry | mask_chlorides_sweet &
                mask_free_sulfur_dioxide_off_dry | mask_free_sulfur_dioxide_sweet &
                mask_total_sulfur_dioxide_off_dry | mask_total_sulfur_dioxide_sweet &
                mask_density_off_dry | mask_density_sweet &  # Include density masks
                mask_pH_off_dry | mask_pH_sweet &
                mask_sulphates_off_dry | mask_sulphates_sweet &
                mask_alcohol_off_dry | mask_alcohol_sweet
            )
            
            # Create the final DataFrame for off-dry and sweet wines
            offdry_sweet_wines_df = wine_red_white[combined_mask & (wine_red_white["alcohol"] > 10.0)]
            
            # Display the result
            st.write(offdry_sweet_wines_df)
    
            fig = px.scatter(
            offdry_sweet_wines_df,
            x='alcohol',  # X-axis variable
            y='residual sugar',  # Y-axis variable
            color='quality',  # Color by quality (or any other categorical variable)
            hover_data=['fixed acidity', 'volatile acidity'],  # Additional data to show on hover
            title='Dry & Sweet Wines: Alcohol vs. Residual Sugar',
            labels={'alcohol': 'Alcohol Content (%)', 'residual sugar': 'Residual Sugar (g/dm³)'}
            )
            
            # Display the plot in the Streamlit app
            st.plotly_chart(fig)

# Main function to control the app flow
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Survey"])

    if page == "Home":
        home_page()
    elif page == "Survey":
        survey_page()

# Run the app
if __name__ == "__main__":
    main()

    # # Create individual masks for off-dry wines
    # mask_fixed_acidity_off_dry = (wine_red_white["fixed acidity"] >= 4.0) & (wine_red_white["fixed acidity"] <= 8)
    # mask_volatile_acidity_off_dry = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] <= 0.8)
    # mask_citric_acid_off_dry = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 0.5)
    # mask_residual_sugar_off_dry = (wine_red_white["residual sugar"] >= 5) & (wine_red_white["residual sugar"] <= 30)
    # mask_chlorides_off_dry = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
    # mask_free_sulfur_dioxide_off_dry = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 60)
    # mask_total_sulfur_dioxide_off_dry = (wine_red_white["total sulfur dioxide"] >= 70) & (wine_red_white["total sulfur dioxide"] <= 250)
    # mask_density_off_dry = (wine_red_white["density"] >= 1.00) & (wine_red_white["density"] <= 1.07)
    # mask_pH_off_dry = (wine_red_white["pH"] >= 3.2) & (wine_red_white["pH"] <= 3.5)
    # mask_sulphates_off_dry = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
    # mask_alcohol_off_dry = (wine_red_white["alcohol"] >= 11.0) & (wine_red_white["alcohol"] <= 14.5)
    
    # # Create individual masks for sweet wines
    # mask_fixed_acidity_sweet = (wine_red_white["fixed acidity"] >= 5.0) & (wine_red_white["fixed acidity"] <= 10)
    # mask_volatile_acidity_sweet = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] < 1.2)
    # mask_citric_acid_sweet = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 1.0)
    # mask_residual_sugar_sweet = (wine_red_white["residual sugar"] >= 0.030) & (wine_red_white["residual sugar"] <= 0.150)
    # mask_chlorides_sweet = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
    # mask_free_sulfur_dioxide_sweet = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 70)
    # mask_total_sulfur_dioxide_sweet = (wine_red_white["total sulfur dioxide"] >= 100) & (wine_red_white["total sulfur dioxide"] <= 300)
    # mask_pH_sweet = (wine_red_white["pH"] >= 3.00) & (wine_red_white["pH"] <= 3.50)
    # mask_sulphates_sweet = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
    # mask_alcohol_sweet = (wine_red_white["alcohol"] >= 12.0) & (wine_red_white["alcohol"] <= 20.0)
    
    # # Combine masks for off-dry and sweet wines using logical OR
    # combined_mask = (
    #     mask_fixed_acidity_off_dry | mask_fixed_acidity_sweet &
    #     mask_volatile_acidity_off_dry | mask_volatile_acidity_sweet &
    #     mask_citric_acid_off_dry | mask_citric_acid_sweet &
    #     mask_residual_sugar_off_dry | mask_residual_sugar_sweet &
    #     mask_chlorides_off_dry | mask_chlorides_sweet &
    #     mask_free_sulfur_dioxide_off_dry | mask_free_sulfur_dioxide_sweet &
    #     mask_total_sulfur_dioxide_off_dry | mask_total_sulfur_dioxide_sweet &
    #     mask_density_off_dry | mask_density_sweet &  # Optional, adjust as needed
    #     mask_pH_off_dry | mask_pH_sweet &
    #     mask_sulphates_off_dry | mask_sulphates_sweet &
    #     mask_alcohol_off_dry | mask_alcohol_sweet
    # )
    
    # # Create the final DataFrame for off-dry and sweet wines
    # dry_sweet_wines_df = wine_red_white[combined_mask]
    
    # # Display the result
    # st.write(dry_sweet_wines_df)

###############
# st.write("What are you having for dinner tonight? Steak, chicken, seafood?")
# left, middle, right = st.columns(3)
# if left.button("Steak", use_container_width=True):
#     left.markdown("You are having steak for dinner.")
# if middle.button("Chicken", use_container_width=True):
#     middle.markdown("You are having chicken for dinner.")
# if right.button("Seafood", use_container_width=True):
#     right.markdown("You are having seafood for dinner.")

# st.write("Are you looking for more a more sweet or salty wine?")
# left, right = st.columns(2)
# if left.button("Sweet", use_container_width=True):
#     left.markdown("You are looking for a sweeter wine.")
# if right.button("Salty", use_container_width=True):
    # right.markdown("You are looking for a salty.")
    
# st.button("Reset", type="primary")
# a = st.write("Are you looking for wine for a dinner pairing or for enjoying?")
# if st.button("pairing"):
#     st.write("What are you having for dinner tonight? Steak, chicken, seafood?")
# if st.button("enjoying"):
#     st.write(("Are you looking for more a more sweet or salty wine?")
# else:
#     st.text_input("what is your max price you are looking to spend per bottle?")

#########################################################################################################

### PLOTS - MASKED DATA BY SWEETNESS #####

# st.title("Dessert Wines")
# # Create individual masks
# mask_fixed_acidity = (wine_red_white["fixed acidity"] >= 5.0) & (wine_red_white["fixed acidity"] <= 10)
# mask_volatile_acidity = (wine_red_white["volatile acidity"] >= 0.5) & (wine_red_white["volatile acidity"] < 1.5)
# mask_citric_acid = (wine_red_white["citric acid"] >= 0.5) & (wine_red_white["citric acid"] <= 1.0)
# #mask_residual_sugar = (wine_red_white["residual sugar"] >= 45) & (wine_red_white["residual sugar"] <= 300)
# mask_chlorides = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
# mask_free_sulfur_dioxide = (wine_red_white["free sulfur dioxide"] >= 30) & (wine_red_white["free sulfur dioxide"] <= 150)
# mask_total_sulfur_dioxide = (wine_red_white["total sulfur dioxide"] >= 100) & (wine_red_white["total sulfur dioxide"] <= 300)
# #mask_density = (wine_red_white["density"] >= 1.05) & (wine_red_white["density"] <= 1.15)
# mask_pH = (wine_red_white["pH"] >= 3.00) & (wine_red_white["pH"] <= 4.00)
# mask_sulphates = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
# #mask_alcohol = (wine_red_white["alcohol"] >= 15.0) & (wine_red_white["alcohol"] <= 20.0)

# # Combine all masks into one
# combined_mask = (mask_fixed_acidity &
#                  mask_volatile_acidity &
#                  mask_citric_acid &
#   #               mask_residual_sugar &
#                  mask_chlorides &
#                  mask_free_sulfur_dioxide &
#                  mask_total_sulfur_dioxide &
#   #               mask_density &
#                  mask_pH &
#                  mask_sulphates)
#    #              mask_alcohol)

# # Create the final DataFrame for dessert wines
# dessert_wines_df = wine_red_white[combined_mask]

# # Display the result
# st.write(dessert_wines_df)
# #########################################################################################################

# st.title("Sweet Wines")
# # Create individual masks for sweet wines
# mask_fixed_acidity = (wine_red_white["fixed acidity"] >= 5.0) & (wine_red_white["fixed acidity"] <= 10)
# mask_volatile_acidity = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] < 1.2)
# mask_citric_acid = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 1.0)
# mask_residual_sugar = (wine_red_white["residual sugar"] >= .030) & (wine_red_white["residual sugar"] <= .150)
# mask_chlorides = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
# mask_free_sulfur_dioxide = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 70)
# mask_total_sulfur_dioxide = (wine_red_white["total sulfur dioxide"] >= 100) & (wine_red_white["total sulfur dioxide"] <= 300)
# #mask_density = (wine_red_white["density"] >= 1.05) & (wine_red_white["density"] <= 1.15)
# mask_pH = (wine_red_white["pH"] >= 3.00) & (wine_red_white["pH"] <= 3.50)
# mask_sulphates = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
# mask_alcohol = (wine_red_white["alcohol"] >= 12.0) & (wine_red_white["alcohol"] <= 20.0)

# # Combine all masks into one
# combined_mask = (mask_fixed_acidity &
#                  mask_volatile_acidity &
#                  mask_citric_acid &
#                #  mask_residual_sugar &
#                  mask_chlorides &
#                  mask_free_sulfur_dioxide &
#                  mask_total_sulfur_dioxide &
#                 # mask_density &
#                  mask_pH &
#                  mask_sulphates &
#                  mask_alcohol)

# # Create the final DataFrame for sweet wines
# sweet_wines_df = wine_red_white[combined_mask]

# # Display the result
# st.write(sweet_wines_df)
# #########################################################################################################

# st.title("Dry Wines")
# # Create individual masks for dry wines
# mask_fixed_acidity = (wine_red_white["fixed acidity"] >= 4.0) & (wine_red_white["fixed acidity"] <= 8)
# mask_volatile_acidity = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] <= 0.7)
# mask_citric_acid = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 0.5)
# mask_residual_sugar = (wine_red_white["residual sugar"] >= 0.1) & (wine_red_white["residual sugar"] <= 5)
# mask_chlorides = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
# mask_free_sulfur_dioxide = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 50)
# mask_total_sulfur_dioxide = (wine_red_white["total sulfur dioxide"] >= 70) & (wine_red_white["total sulfur dioxide"] <= 200)
# mask_density = (wine_red_white["density"] >= 0.99) & (wine_red_white["density"] <= 1.05)
# mask_pH = (wine_red_white["pH"] >= 3.2) & (wine_red_white["pH"] <= 3.6)
# mask_sulphates = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
# mask_alcohol = (wine_red_white["alcohol"] >= 11.0) & (wine_red_white["alcohol"] <= 14.0)

# # Combine all masks into one
# combined_mask = (mask_fixed_acidity &
#                  mask_volatile_acidity &
#                  mask_citric_acid &
#                  mask_residual_sugar &
#                  mask_chlorides &
#                  mask_free_sulfur_dioxide &
#                  mask_total_sulfur_dioxide &
#                  mask_density &
#                  mask_pH &
#                  mask_sulphates &
#                  mask_alcohol)

# # Create the final DataFrame for dry wines
# dry_wines_df = wine_red_white[combined_mask]

# # Display the result
# st.write(dry_wines_df)

# #########################################################################################################

# st.title("Off-Dry Wines")
# # Create individual masks for off-dry wines
# mask_fixed_acidity = (wine_red_white["fixed acidity"] >= 4.0) & (wine_red_white["fixed acidity"] <= 8)
# mask_volatile_acidity = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] <= 0.8)
# mask_citric_acid = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 0.5)
# mask_residual_sugar = (wine_red_white["residual sugar"] >= 5) & (wine_red_white["residual sugar"] <= 30)
# mask_chlorides = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
# mask_free_sulfur_dioxide = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 60)
# mask_total_sulfur_dioxide = (wine_red_white["total sulfur dioxide"] >= 70) & (wine_red_white["total sulfur dioxide"] <= 250)
# mask_density = (wine_red_white["density"] >= 1.00) & (wine_red_white["density"] <= 1.07)
# mask_pH = (wine_red_white["pH"] >= 3.2) & (wine_red_white["pH"] <= 3.5)
# mask_sulphates = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
# mask_alcohol = (wine_red_white["alcohol"] >= 11.0) & (wine_red_white["alcohol"] <= 14.5)

# # Combine all masks into one
# combined_mask = (mask_fixed_acidity &
#                  mask_volatile_acidity &
#                  mask_citric_acid &
#                 # mask_residual_sugar &
#                  mask_chlorides &
#                  mask_free_sulfur_dioxide &
#                  mask_total_sulfur_dioxide &
#                 # mask_density &
#                  mask_pH &
#                  mask_sulphates &
#                  mask_alcohol)

# # Create the final DataFrame for off-dry wines
# off_dry_wines_df = wine_red_white[combined_mask]

# # Display the result
# st.write(off_dry_wines_df)
# #########################################################################################################

# import streamlit as st

# # User selection for the wine purpose
# genre = st.radio(
#     "Are you looking for wine for a dinner pairing or for enjoying?",
#     [":rainbow[Enjoying]", "***Dinner Pairing***"],
#     index=None,
# )

# st.write("You selected:", genre)

# # User selection for dinner
# dinner = st.radio(
#     "What are you having for dinner tonight? Steak, chicken, seafood?",
#     ["Red meat", "Poultry", "Seafood"],
#     index=None,
# )

# st.write("You selected:", dinner)

# # User selection for taste preference
# taste = st.radio(
#     "Are you looking for a more sweet or salty wine?",
#     ["Sweet", "Salty"],
#     index=None,
# )

# st.write("You selected:", taste)

# # Check if the conditions are met
# if (genre == "***Dinner Pairing***" and dinner == "Red meat" and taste == "Salty"):
#     st.title("Dry Wines")
    
#     # Create individual masks for dry wines
#     mask_fixed_acidity = (wine_red_white["fixed acidity"] >= 4.0) & (wine_red_white["fixed acidity"] <= 8)
#     mask_volatile_acidity = (wine_red_white["volatile acidity"] >= 0.3) & (wine_red_white["volatile acidity"] <= 0.7)
#     mask_citric_acid = (wine_red_white["citric acid"] >= 0.1) & (wine_red_white["citric acid"] <= 0.5)
#     mask_residual_sugar = (wine_red_white["residual sugar"] >= 0.1) & (wine_red_white["residual sugar"] <= 5)
#     mask_chlorides = (wine_red_white["chlorides"] >= 0.01) & (wine_red_white["chlorides"] < 0.1)
#     mask_free_sulfur_dioxide = (wine_red_white["free sulfur dioxide"] >= 20) & (wine_red_white["free sulfur dioxide"] <= 50)
#     mask_total_sulfur_dioxide = (wine_red_white["total sulfur dioxide"] >= 70) & (wine_red_white["total sulfur dioxide"] <= 200)
#     mask_density = (wine_red_white["density"] >= 0.99) & (wine_red_white["density"] <= 1.05)
#     mask_pH = (wine_red_white["pH"] >= 3.2) & (wine_red_white["pH"] <= 3.6)
#     mask_sulphates = (wine_red_white["sulphates"] >= 0.1) & (wine_red_white["sulphates"] <= 0.5)
#     mask_alcohol = (wine_red_white["alcohol"] >= 11.0) & (wine_red_white["alcohol"] <= 14.0)

#     # Combine all masks into one
#     combined_mask = (mask_fixed_acidity &
#                      mask_volatile_acidity &
#                      mask_citric_acid &
#                      mask_residual_sugar &
#                      mask_chlorides &
#                      mask_free_sulfur_dioxide &
#                      mask_total_sulfur_dioxide &
#                      mask_density &
#                      mask_pH &
#                      mask_sulphates &
#                      mask_alcohol)

#     # Create the final DataFrame for dry wines
#     dry_wines_df = wine_red_white[combined_mask]

#     # Display the result
#     st.write(dry_wines_df)
    
# #else genre == "***Dinner Pairing***" and dinner == "Poultry" and taste == "Salty":

# # st.write("Are you looking for wine for a dinner pairing or for enjoying?")
# # left, right = st.columns(2)
# # if left.button("Pairing", use_container_width=True):
# #     left.markdown("You clicked the pairing button.")
# # if right.button("Enjoying", use_container_width=True):
# #     right.markdown("You clicked the enjoying button.")

# # st.write("What are you having for dinner tonight? Steak, chicken, seafood?")
# # left, middle, right = st.columns(3)
# # if left.button("Steak", use_container_width=True):
# #     left.markdown("You are having steak for dinner.")
# # if middle.button("Chicken", use_container_width=True):
# #     middle.markdown("You are having chicken for dinner.")
# # if right.button("Seafood", use_container_width=True):
# #     right.markdown("You are having seafood for dinner.")

# # st.write("Are you looking for more a more sweet or salty wine?")
# # left, right = st.columns(2)
# # if left.button("Sweet", use_container_width=True):
# #     left.markdown("You are looking for a sweeter wine.")
# # if right.button("Salty", use_container_width=True):
# #     right.markdown("You are looking for a salty.")
    
# # if (a = "pairing")
# #     a1 = st.text_input("What are you having for dinner tonight? Steak, chicken, seafood?")
# # else: 
# #     a2 = st.text_input("Are you looking for more a more sweet or salty wine?")


# #st.write(f"You are leaning more towards: {a2}")
# #st.slider("How much are you wanting to spend on a bottle?", 0, 120)
# # b = st.text_input("What are you having for dinner tonight?")
# # c = st.text_input("Do you lean more towards sweet or salty?")

# # st.bar_chart(wine_data)