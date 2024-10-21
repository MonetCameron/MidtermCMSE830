import streamlit as st
import pandas as pd 
import plotly.express as px
import matplotlib.pylot as plt
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
            st.subheader("This app provides a list of wines that best compliment your needs based on the combinations of chemical components that compose the body of the wine.")
    
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
            st.write("Below is a plot showing the Alcohol vs. Residual Sugar content of each wine presented in the above list, if you hover over a point it will show the fixed and volatile acidity as well as the quality score. The quality score ranges from 0 to 10, with 10 being the most highly rated.")
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