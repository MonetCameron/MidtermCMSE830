import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# Helper function for visualizations
def plot_heatmap(dataframe, title="Heatmap", cmap="YlOrBr"):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(dataframe.isna(), cbar=False, cmap=cmap, yticklabels=False, ax=ax)
    ax.set_title(title)
    return fig

def plot_boxplots(dataframe, columns, title="Boxplots"):
    fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(12, 16))
    axes = axes.flatten()
    for i, col in enumerate(columns):
        sns.boxplot(data=dataframe, x=col, ax=axes[i])
    plt.tight_layout()
    fig.suptitle(title, y=1.02)
    return fig

# Home Page
def home_page():
    st.title("Welcome to Fine Winerary 🍷")
    st.header("The Wine Recommendation System")
    st.write("""
    Welcome to **Fine Winerary**! This app helps you discover the perfect wine for any occasion. 
    We offer personalized recommendations based on what you're looking for. 
    Whether you're pairing a wine with your dinner or simply enjoying a glass, we've got you covered!
    """)
    st.image("IMG_0122.jpeg", caption="Discover the perfect wine", use_column_width=True)

    

# About the Data
def explain_data():
    import streamlit as st

    # Display an image banner
    st.image("glasses-different-wines-placed_961875-161431.jpg", use_column_width=True)

    st.title("Understanding the Data 📊")
    st.write("""
    This project uses the **Wine Quality** dataset from Kaggle. The dataset contains information about various 
    characteristics of red and white wines and their quality ratings. These features offer valuable insights into 
    the wine's chemical composition, taste profiles, and quality assessment.
    """)

      # Add dataset link and description
    st.write("### Dataset Source")
    st.write("""
    The data is sourced from the **[Wine Quality Data Set (Red & White Wine)](https://www.kaggle.com/datasets/ruthgn/wine-quality-data-set-red-white-wine)** on Kaggle.  
    It includes detailed chemical analyses of red and white wines from the Vinho Verde region in Portugal, along with **sensory quality ratings** provided by wine tasters. This dataset is widely used for exploring relationships between chemical properties and wine quality.
    """)

    st.markdown("""
    ## What’s This All About?  
    
    For this project, I wanted to dive deep into the relationship between wine quality ratings and the chemical components that make up wine. Using the Wine Quality dataset, which includes both red and white wines, I explored how the various elements of a wine—like acidity, sugar levels, alcohol content, and others—relate to the wine’s overall quality score.
    
    The main goal was to see if I could identify patterns or trends in the data that could explain the differences in quality. Once I figured out these connections, I created a threshold or set of criteria that could help with wine selection. Think of it as a way to match wines to your exact preferences based on their chemical makeup—whether you’re looking for a wine to pair with a dinner or just something to enjoy.
    
    This survey is where all that work comes together. You’ll answer a few questions about your taste preferences and what you’re eating, and I’ll use the data to recommend wines that are most likely to meet your needs. Whether you prefer something sweet or dry, light or full-bodied, I’ve got you covered with wine suggestions that align with your preferences. It’s all about combining data and flavor to help you make the best choice!
    
    So, let’s dive in and see what wine suits your taste today!  
    """)

    # Load the dataset
    wine_df = pd.read_csv("wine-quality-white-and-red.csv")

    # Dataset overview
    st.write("### Dataset Overview")
    st.dataframe(wine_df.head())
    st.write(f"**Shape of the dataset:** {wine_df.shape}")
    st.write("### Summary Statistics")
    st.write(wine_df.describe())

    # Feature details
    st.write("### Key Features and Insights")
    st.write("""
    Each feature in the dataset represents an important aspect of the wine's composition. Here's a breakdown:
    """)

    feature_details = {
        "Fixed Acidity": """
        - Represents the natural acids in wine after being boiled down.  
        - **Low concentration**: Wine tastes watery and dull.  
        - **High concentration**: Wine tastes sharp and astringent.  
        - Affects the pH level (2.9–3.9).""",
        
        "Volatile Acidity": """
        - Measures gaseous acids (mainly acetic acid) that contribute to aroma and taste.  
        - **Limits**: ≤ 0.98 g/L for reds, ≤ 0.88 g/L for whites and rosés.  
        - **High levels**: Sharp, vinegary aroma and fiery finish.""",
        
        "Citric Acid": """
        - Adds freshness and fruity citrus notes.  
        - Can convert to acetic acid, increasing sharpness over time.""",
        
        "Residual Sugar": """
        - Leftover sugar after fermentation, measured in g/L.  
        - Determines wine sweetness: **Dry** (minimal sugar), **Sweet** (higher residual sugar).  
        - [Learn more about residual sugar in wine](https://winefolly.com/deep-dive/what-is-residual-sugar-in-wine/).""",
        
        "Chlorides": """
        - Represents salt content in wine.  
        - **High levels**: Impart a salty taste, reducing marketability.  
        - Typical range: ≤ 60 mg/L.""",
        
        "Free Sulfur Dioxide (SO₂)": """
        - Functions as an antioxidant and antimicrobial agent.  
        - Measured in parts per million (ppm).""",
        
        "Total Sulfur Dioxide (SO₂)": """
        - Combination of free and bound SO₂.  
        - Helps preserve freshness and fruitiness.""",
        
        "Density": """
        - Linked to alcohol and sugar content.  
        - **Dry wines**: ~0.9 g/cm³.  
        - **Sweet wines**: ~1.03 g/cm³.""",
        
        "pH": """
        - Indicates acidity, ranges from 2.8–4.2.  
        - **Whites**: Typically 3.0–3.5.  
        - **Reds**: Typically 3.3–3.8.  
        - Lower pH improves stability.""",
        
        "Sulphates": """
        - Used to stop fermentation and prevent oxidation.  
        - Protects against color and taste degradation.""",
        
        "Alcohol": """
        - Measured as Alcohol by Volume (ABV).  
        - Varies by climate and grape ripeness:  
          - Colder climates = Lower ABV.  
          - Warmer climates = Higher ABV.""",
        
        "Quality": """
        - Rated 0–10, based on sensory evaluation.  
        - **0**: Very poor.  
        - **10**: Excellent."""
    }

    # Display each feature with its insights
    for feature, details in feature_details.items():
        with st.expander(f"🔍 {feature}"):
            st.write(details)

    # Adding wine classification
    st.write("### Wine Classification")
    st.write("""
    Wines can be categorized by **Type**, **Sweetness**, and **Acidity**:
    
    - **Type**: Red (dark grapes with skins) or White (green grapes or skinless reds).  
    - **Sweetness**: Dry (minimal sugar), Off-Dry (slightly sweet), Sweet (higher sugar).  
    - **Acidity**: High (crisp and refreshing), Medium (balanced flavors), Low (smooth and round).
    """)

    st.write("""
    This information serves as the foundation for preprocessing and analysis steps aimed at creating personalized 
    wine recommendations. Explore how these features influence wine quality, taste profiles, and meal pairings.
    """)


# Data Exploration
# Data Exploration (Page 3)
def data_exploration():
    st.title("Data Exploration 🔍")
    st.image("row-glasses-with-wine_186277-5583.jpg", use_column_width=True)
    st.write("""
    Let's explore the data to understand its structure, quality, and distributions.
    This page walks you through the initial data loading, type distribution, and handling of missing values.
    """)

    # Load the modified dataset
    wine_df = pd.read_csv("wine-quality-white-and-red.csv")  # Replace with your actual file path
    wine_df = wine_df.copy(deep=True)

    # Info to get the data types of the columns and label encoder for the type column
    wine_df.info()  # Displaying the data types of columns
    le = LabelEncoder()
    wine_df["encoded_type"] = le.fit_transform(wine_df['type'])

    # Add explanation box for more details on loading data
    if st.checkbox('Click to expand Data Loading and Overview'):
        st.subheader('1. Data Loading and Initial Overview')
        st.write("""
        In this step, I loaded the dataset using pandas' `read_csv()` function. I also defined the target variable 
        (`quality`) and extracted the features (columns excluding `quality`). The dataset contains various characteristics 
        of red and white wines along with their quality scores.
        """)
        st.code("""
wine_df = pd.read_csv("wine-quality-white-and-red.csv")  # Loading the dataset
target = 'quality'  # Target variable
labels = ['Quality-3', 'Quality-4', 'Quality-5', 'Quality-6', 'Quality-7', 'Quality-8']  # Quality labels
features = [i for i in wine_df.columns.values if i not in [target]]  # Feature columns
wine_df = wine_df.copy(deep=True)  # Creating a copy of the dataframe
display(wine_df.head())  # Displaying the first few rows of the data
        """)

    # Check for missing values using a heatmap
    st.write("### Checking for Missing Values")
    st.write("I used a heatmap to visualize any missing values in the dataset. This allows us to see where there might be gaps in the data.")
    if st.checkbox('Click to expand Missing Values Check'):
        st.subheader('2. Heatmap for Missing Values')
        st.write("""
        The heatmap shows missing data (if any) where dark cells indicate the presence of missing values. This step 
        is important as handling missing data correctly ensures the quality and accuracy of our analysis.
        """)
    # Create the heatmap with a different color wave
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(wine_df.isna(), cbar=False, cmap="YlOrBr", yticklabels=False, ax=ax)  # Using 'viridis' colormap
    st.pyplot(fig)

    # Check distribution of wine types
    st.write("### Wine Type Distribution")
    st.write("Now, let's explore the distribution of wine types (Red vs White). This will help to understand how balanced the dataset is.")
    wine_type_counts = wine_df['type'].value_counts()
    st.write(wine_type_counts)

    # Encode wine types and visualize distribution
    le = LabelEncoder()
    wine_df['encoded_type'] = le.fit_transform(wine_df['type'])
    st.write("### Encoded Wine Types (0: Red, 1: White)")
    # Create two columns to display side by side
    col1, col2 = st.columns(2)

    with col1:
        # Display the first few rows
        st.write("First 5 Rows:")
        st.write(wine_df[['type', 'encoded_type']].head())

    with col2:
        # Display the last few rows
        st.write("Last 5 Rows:")
        st.write(wine_df[['type', 'encoded_type']].tail())


    # Add explanation box for more details on encoding and visualization
    if st.checkbox('Click to expand Wine Type Distribution and Encoding'):
        st.subheader('3. Wine Type Encoding and Visualization')
        st.write("""
        I used `LabelEncoder` to encode the categorical `type` column (Red or White) into numerical values (0 for Red, 1 for White).
        This step is crucial for any machine learning tasks, as models work with numeric data. Additionally, I created a pie chart 
        to visualize the distribution of red and white wines in the dataset.
        """)
        st.code("""
le = LabelEncoder()  # Label encoding for the 'type' column
wine_df['encoded_type'] = le.fit_transform(wine_df['type'])  # Encoding the wine type
st.write(wine_df[['type', 'encoded_type']].head())  # Displaying the encoded wine types
        """)

    # Create a pie chart to visualize the distribution of wine types
    st.write("### Wine Type Distribution (Pie Chart)")
    if st.checkbox('Click to expand Pie Chart Visualization'):
        st.subheader('4. Visualizing Wine Type Distribution with a Pie Chart')
        st.write("""
        This pie chart visualizes the proportion of red and white wines in the dataset. It's important to know if the dataset 
        is balanced across wine types. A well-balanced dataset is generally more suitable for training machine learning models.
        """)
        wine_type_counts = wine_df['type'].value_counts()
        
        # Create the pie chart with a figure and axes
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(wine_type_counts, labels=wine_type_counts.index, autopct='%1.1f%%', startangle=90, colors=['#3CB371', '#FF6347'])
        ax.set_title('Wine Type Distribution (Red vs White)')
        
        # Display the plot explicitly by passing the figure object
        st.pyplot(fig)  # Future-proof: Passing the figure object

    st.write("### Key Takeaways from Data Exploration")
    st.write("""
    - The dataset contains both red and white wines, with each wine having various chemical properties and a quality score.
    - I encoded the wine types (Red and White) into numeric values for easier processing in machine learning tasks.
    - The pie chart helped to visualize the distribution of red vs white wines, and the heatmap was useful in checking for missing data.
    """)

     # Save the cleaned dataset as a new CSV file for later use on Page 4
    wine_df.to_csv("cleaned_wine_data.csv", index=False)
    #st.write("The processed dataset has been saved as 'cleaned_wine_data.csv' and will be used in the next section.")
    
    # Optionally, provide a detailed explanation
    with st.expander("Explanation of Data Exploration and Preprocessing"):
        st.write("""
        - **Data Cleaning:** The data was processed by handling missing values and encoding the wine type.""")

# Data Manipulation (Page 4)
def data_manipulation():
    st.title("Data Manipulation and Preprocessing 🛠️")
    st.image("istockphoto-1196065656-612x612.jpg", use_column_width=True)
    st.write("""
    This page demonstrates the data cleaning and preprocessing pipeline. Each step refines the dataset for better insight into the 
    relationships between wine quality, type, sweetness, and other features. The goal is to create a dataset that enables building 
    thresholds for wine suggestions tailored to individual preferences and meals.
    """)

    # Load dataset
    import numpy as np
    
    wine_df = pd.read_csv("cleaned_wine_data.csv")
    st.write("### Data Preview:")
    st.dataframe(wine_df.head())
    st.write(f"**Initial Shape of the Dataset:** {wine_df.shape}")
    st.write(f"**Number of Quality Levels:** {wine_df['quality'].nunique()}")

    st.expander("What happens here?").write("""
    - We start by loading the cleaned dataset.
    - The `quality` column represents the wine's quality score, ranging from 3 to 8 in this dataset.
    - Maintaining all quality levels is crucial, as they inform the thresholds for sweetness and type classification.
    """)

    # Step 1: Balance Red and White Classes
    st.write("### Step 1: Balancing Red and White Classes")
    st.write("""
    To ensure fair representation, we balance the number of `red` and `white` wine samples using undersampling. 
    This prevents bias towards one type during the analysis.
    """)
    red_count = wine_df[wine_df['type'] == 'red'].shape[0]
    white_undersampled = wine_df[wine_df['type'] == 'white'].sample(n=red_count, random_state=42)
    balanced_df = pd.concat([wine_df[wine_df['type'] == 'red'], white_undersampled]).sample(frac=1, random_state=42).reset_index(drop=True)
    
    st.write("Balanced Dataset Preview (Red and White):")
    st.dataframe(balanced_df.head())
    st.write(f"**Shape After Balancing Types:** {balanced_df.shape}")
    
    # Show the distribution of wine types as a pie chart
    type_counts = balanced_df['type'].value_counts()
    colors = ['red', 'green']
    fig, ax = plt.subplots()
    ax.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=90, colors=colors)
    ax.set_title("Class Distribution for 'type' (Red vs White)")
    st.pyplot(fig)

    st.expander("Why balance red and white wines?").write("""
    - Red and white wines have distinct characteristics. Balancing ensures that both types contribute equally to the analysis.
    - The balance helps build unbiased thresholds for quality and sweetness across wine types.
    """)

    st.write(f"**Number of Unique Quality Classes After Balancing Types:** {balanced_df['quality'].nunique()}")

    # Step 2: Remove Outliers
    st.write("### Step 2: Removing Outliers")
    st.write("""
    Outliers can distort the analysis and thresholds. We use the Interquartile Range (IQR) method to detect and remove outliers 
    from key numeric columns.
    """)

    # # Step 2: Remove Outliers
    # st.write("### Step 2: Removing Outliers")
    balanced_df.drop_duplicates(inplace=True)
    balanced_df.isnull().sum().sort_values()
    balanced_df.shape

    def remove_outliers_thresholdsIQR(dataframe, col_name, th1=0.25, th3=0.75):
        dataframe = dataframe.copy()
        all_outlier_indices = []
    
        for col in col_name:
    
        
            q1 = dataframe[col_name].quantile(th1)
            q3 = dataframe[col_name].quantile(th3)
            iqr = q3 - q1
            upper_limit = q3 + (1.5 * iqr)
            lower_limit = q1 - (1.5 * iqr)
            
            upper_array = np.where(dataframe[col_name] >= upper_limit)[0]
            lower_array = np.where(dataframe[col_name] <= lower_limit)[0]
            
            all_outlier_indices.extend(upper_array)
            all_outlier_indices.extend(lower_array)
            
        all_outlier_indices = list(set(all_outlier_indices))
        
        #resetting the dataframe index before dropping values
        dataframe.reset_index(drop=True, inplace=True)
        
        dataframe.drop(index = all_outlier_indices, inplace=True, errors="ignore")
    
        return dataframe 
 
    check_columns = ["free sulfur dioxide", "alcohol", "citric acid","residual sugar","pH", "sulphates", "fixed acidity", "chlorides", "volatile acidity", "total sulfur dioxide"]
    balanced_df_clean = remove_outliers_thresholdsIQR(balanced_df, check_columns)
    st.write("Dataset After Outlier Removal:")
    st.dataframe(balanced_df_clean.head())
    st.write(f"**Shape of the dataset after outlier removal:** {balanced_df_clean.shape}")
    st.write(f"Number of unique quality classes after outlier removal: {balanced_df_clean['quality'].nunique()}")

    st.expander("Why keep all quality groups?").write("""
    - The quality levels represent different wine standards, guiding the thresholds for sweetness and type.
    - Removing any group may lose critical information for defining taste and meal pairings.
    - However, keeping outliers from smaller quality groups may introduce noise, a trade-off to retain all levels.
    """)

    # Step 3: Balance Quality Classes with SMOTE
    st.write("### Step 3: Balancing Quality Classes with SMOTE")
    st.write("""
    SMOTE (Synthetic Minority Oversampling Technique) generates synthetic samples for underrepresented quality levels, 
    ensuring all classes are equally represented.
    """)

    smote = SMOTE(random_state=42, k_neighbors=2)
    X = balanced_df_clean.drop(columns=['quality', 'type'])
    y = balanced_df_clean['quality']
    X_resampled, y_resampled = smote.fit_resample(X, y)
    wine_balanced = pd.DataFrame(X_resampled, columns=X.columns)
    wine_balanced['quality'] = y_resampled

    st.write("Balanced Dataset Preview (Quality):")
    st.dataframe(wine_balanced.head())
    st.write(f"**Shape After Balancing Quality Classes:** {wine_balanced.shape}")

    col1, col2 = st.columns(2)
    with col1:
        st.write("### Class Distribution Before SMOTE:")
        st.bar_chart(balanced_df_clean['quality'].value_counts())
    with col2:
        st.write("### Class Distribution After SMOTE:")
        st.bar_chart(pd.Series(y_resampled).value_counts())

    st.expander("How does SMOTE work?").write("""
    SMOTE oversamples minority classes by generating synthetic samples along the feature space of nearest neighbors. 
    This avoids simply duplicating existing samples and helps the model generalize better.
    """)

    # Step 4: Feature Engineering
    st.write("### Step 4: Feature Engineering")
    st.write("""
    Transforming skewed numeric columns with log transformations helps normalize the data and reduces the effect of outliers.
    """)

    # Identify numeric columns only
    numeric_cols = wine_balanced.select_dtypes(include=['float64', 'int64']).columns.tolist()

    skewed_cols = [col for col in numeric_cols if wine_balanced[col].skew() > 1]
    for col in skewed_cols:
        wine_balanced[col] = np.log1p(wine_balanced[col])

    st.session_state.wine_balanced = wine_balanced

    st.write("Dataset After Feature Engineering:")
    st.dataframe(wine_balanced.head())
    st.write(f"**Final Shape of the Dataset:** {wine_balanced.shape}")

    st.expander("How do these steps build thresholds?").write("""
    - **Balancing:** Ensures all types and qualities contribute equally to analysis.
    - **Outlier Removal:** Refines the data for accurate threshold definitions.
    - **SMOTE:** Makes quality levels equally represented, crucial for understanding quality-sweetness relationships.
    - **Feature Engineering:** Normalizes the data, making patterns clearer.
    """)

#EDA: PAGE 5
def exploratory_data_analysis():
    st.title("Exploratory Data Analysis 📊")
    st.image("images.jpg", use_column_width=True)
    st.write("""
    After cleaning and balancing the data, we can now dive into its characteristics through visualizations. 
    This helps uncover patterns and correlations vital for building predictive models.
    """)

    # Check if 'wine_balanced' is available in the session state
    if 'wine_balanced' in st.session_state:
        wine_balanced = st.session_state.wine_balanced

        # Correlation Heatmap
        st.write("### Correlation Heatmap:")
        numerical_features = wine_balanced.select_dtypes(include=["number"]).columns  # Exclude non-numerical columns
        plt.figure(figsize=(12, 8))
        sns.heatmap(
            wine_balanced[numerical_features].corr(),
            annot=True,
            cmap="coolwarm",
            fmt=".2f",
            vmin=-1,
            vmax=1,
            center=0
        )
        st.pyplot(plt)

        # # Pairplot for feature relationships
        # st.write("### Pairplot of Features by Quality:")
        # pairplot_fig = sns.pairplot(wine_balanced, hue="quality", diag_kind="kde", height=2.5)
        # st.pyplot(pairplot_fig.fig)

        # Quality Distribution
        # st.write("### Quality Distribution (Balanced Data):")
        # quality_counts = wine_balanced["quality"].value_counts()
        # st.bar_chart(quality_counts)

        with st.expander("What does this tell us?"):
            st.write("""
            - **Feature Correlations:** The heatmap identifies highly correlated features, guiding feature selection for models.
            """)

       # Wine Classification based on thresholds (Dry, Off-Dry, Sweet, Dessert)
        # Apply the classification function to the dataset if it’s not already done
        if 'wine_type' not in wine_balanced.columns:
            wine_balanced['wine_type'] = wine_balanced.apply(classify_wine, axis=1)
        
        st.write("### Transition to Key Features Used for Thresholds")

        st.write("""
        Now that we’ve explored the dataset as a whole, let’s zoom in on the specific features that will help us define the thresholds for wine classification. 
        The key features—**Residual Sugar** and **Alcohol Content**—are critical in determining the type of wine, such as dry, sweet, or dessert wines. 
        We'll focus on their distributions and relationships with each wine type.
        """)

        # Plot boxplots side by side for Alcohol Content and Residual Sugar by Wine Type
        st.write("### Boxplots: Alcohol Content and Residual Sugar by Wine Type")
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 6))

        # Alcohol Content by Wine Type
        sns.boxplot(x='wine_type', y='alcohol', data=wine_balanced, ax=ax1)
        ax1.set_title('Alcohol Content by Wine Type')
        ax1.set_xlabel('Wine Type')
        ax1.set_ylabel('Alcohol Content (%)')

        # Residual Sugar by Wine Type
        sns.boxplot(x='wine_type', y='residual sugar', data=wine_balanced, ax=ax2)
        ax2.set_title('Residual Sugar by Wine Type')
        ax2.set_xlabel('Wine Type')
        ax2.set_ylabel('Residual Sugar (g/L)')

        # Display both boxplots side by side
        plt.tight_layout()
        st.pyplot(fig)

        # Scatter Plot: Alcohol Content vs Residual Sugar colored by Wine Type
        st.write("### Scatter Plot: Alcohol Content vs Residual Sugar, Colored by Wine Type")
        plt.figure(figsize=(12, 6))
        sns.scatterplot(x='alcohol', y='residual sugar', hue='wine_type', data=wine_balanced, palette='Set3', s=100, alpha=0.7)
        plt.title('Wine Types Classified by Alcohol Content and Residual Sugar')
        plt.xlabel('Alcohol Content (%)')
        plt.ylabel('Residual Sugar (g/L)')
        plt.legend(title='Wine Type')
        st.pyplot(plt)

    else:
        st.write("No data found, please go back and load the dataset.")

# Classification function (Ensure you have this function defined somewhere)
def classify_wine(row):
    if row['residual sugar'] > 5.65 and row['alcohol'] >= 12.5:
        return 'Dessert'
    elif 2 <= row['residual sugar'] <= 5.65 and 11.6 < row['alcohol'] < 12.5:
        return 'Sweet'
    elif 2 <= row['residual sugar'] <= 5.65 and 9.9 < row['alcohol'] <= 11.6:
        return 'Off-Dry'
    elif row['residual sugar'] <= 2 and row['alcohol'] <= 9.9:
        return 'Dry'
    else:
        return 'Other'  # For edge cases
    

# Predictive Modeling
def predictive_modeling():
    st.title("Predictive Modeling 🤖")
    st.image("Red-Wine-Rosacea-the-sunday-edit-1.jpg", use_column_width=True)
    
    if 'wine_balanced' in st.session_state:
        wine_balanced = st.session_state.wine_balanced

        # Label Encoding for 'quality' column (if it's categorical)
        label_encoder = LabelEncoder()
        wine_balanced['quality_encoded'] = label_encoder.fit_transform(wine_balanced['quality'])
        wine_balanced['wine_encoded'] = label_encoder.fit_transform(wine_balanced['wine_type'])
        #st.dataframe(wine_balanced)

        # Select only numeric columns for features (X)
        numeric_columns = wine_balanced.select_dtypes(include=["number"]).columns
        X = wine_balanced[numeric_columns].drop(columns=['quality_encoded', 'quality'])  # Drop 'quality_encoded'
        y = wine_balanced['quality_encoded']  # Use the encoded 'quality' as the target variable

        # Train-Test Split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        # Random Forest Model
        rf_model = RandomForestClassifier(random_state=42)
        rf_model.fit(X_train, y_train)
        st.write("### Random Forest Model Accuracy")
        st.write(rf_model.score(X_test, y_test))  # Show the accuracy

        # Logistic Regression Model
        lr_model = LogisticRegression(max_iter=10000, random_state=42)
        lr_model.fit(X_train, y_train)
        st.write("### Logistic Regression Model Accuracy")
        st.write(lr_model.score(X_test, y_test))  # Show the accuracy

        # K-Means Clustering and PCA (for Visualization)
        pca = PCA(n_components=2)
        pca_components = pca.fit_transform(X)  # Perform PCA to reduce to 2 components
        
        # KMeans clustering
        kmeans = KMeans(n_clusters=3, random_state=42)
        kmeans.fit(pca_components)  # Fit KMeans on the PCA components

        # Plot KMeans Clusters with labels
        st.write("### KMeans Clustering (2 Principal Components):")
        plt.figure(figsize=(8, 6))
        scatter = plt.scatter(pca_components[:, 0], pca_components[:, 1], c=kmeans.labels_, cmap='viridis', alpha=0.6)
        
        # Add cluster labels
        centers = kmeans.cluster_centers_
        for i, center in enumerate(centers):
            plt.text(center[0], center[1], f"Cluster {i+1}", color='red', fontsize=12, ha='center', va='center')
        
        plt.title("KMeans Clustering in PCA Space")
        plt.xlabel("Principal Component 1")
        plt.ylabel("Principal Component 2")
        plt.colorbar(label="Cluster Label")
        st.pyplot(plt)

        # User-Friendly Explanation
        st.write("""
        **KMeans Clustering** groups the data into distinct clusters based on their similarities in the feature space. 
        The plot shows the data points reduced to two principal components using **PCA (Principal Component Analysis)**, 
        which allows us to visualize high-dimensional data in two dimensions.
        
        - The colors represent different clusters identified by K-Means.
        - Each cluster represents a group of wines that share similar characteristics.
        - The red labels on the plot indicate the centroids of each cluster, representing the center of the group.

        This technique helps to identify underlying patterns in the data, such as grouping wines based on similar features 
        (e.g., alcohol content, residual sugar) that may not be immediately obvious.
        """)
        
    else:
        st.write("No data found, please go back and load the dataset.")

wine_red_white = pd.read_csv("cleaned_wine_data.csv")

# Define the wine classification based on threshold model
def classify_wine(row):
    # Dessert Wine: High residual sugar and high alcohol
    if row['residual sugar'] > 5.65 and row['alcohol'] >= 12.5:
        return 'Dessert'
    
    # Sweet Wine: Moderate residual sugar and moderate to higher alcohol
    elif 2 <= row['residual sugar'] <= 5.65 and 11.6 < row['alcohol'] < 12.5:
        return 'Sweet'
    
    # Off-Dry Wine: Moderate residual sugar and moderate alcohol
    elif 2 <= row['residual sugar'] <= 5.65 and 9.9 < row['alcohol'] <= 11.6:
        return 'Off-Dry'
    
    # Dry Wine: Low residual sugar and low alcohol
    elif row['residual sugar'] <= 2 and row['alcohol'] <= 9.9:
        return 'Dry'
    
    else:
        return 'Other'  # For edge cases

# Apply the classification function to the dataset
wine_red_white['wine_type'] = wine_red_white.apply(classify_wine, axis=1)

# Survey Page
def survey_page():

    st.title("Wine Selection Survey🍷")

    # User selection for the wine purpose
    purpose = st.radio(
        "Are you looking for wine for a dinner pairing or for enjoying?",
        ["Enjoying", "Dinner Pairing"]
    )
    st.write("You selected:", purpose)

    # Taste preference for "Enjoying" purpose
    if purpose == "Enjoying":
        taste = st.radio(
            "Do you prefer sweet or bitter?",
            ["Sweet", "Bitter"]
        )
        st.write("You selected:", taste)
    
    # Meal and taste preferences for "Dinner Pairing" purpose
    if purpose == "Dinner Pairing":
        # User selection for dinner
        dinner = st.radio(
            "What are you having for dinner tonight? Steak, chicken, seafood?",
            ["Red meat", "Poultry", "Seafood"]
        )
        st.write("You selected:", dinner)
        
        # User selection for taste preference
        taste = st.radio(
            "Do you prefer sweet or bitter?",
            ["Sweet", "Bitter"]
        )
        st.write("You selected:", taste)

    # Get the user's preferred wine characteristics
    st.write("""
        The wines listed above match your preferences based on the residual sugar level and alcohol percentage you selected.
        - **Residual Sugar** indicates the amount of sugar left after fermentation.
        - **Alcohol** percentage is the level of alcohol in the wine.
        - **Type** indicates whether the wine is red or white.
        - **Quality** is a score based on wine characteristics.
        """)
    # Residual Sugar Scale Explanation
    st.write("""
        ### Residual Sugar Scale:
        - **0-1 g/L**: Bone Dry
        - **1-4 g/L**: Dry
        - **4-8 g/L**: Off-Dry
        - **8-20 g/L**: Sweet
        - **20+ g/L**: Very Sweet
        """)
        
    # Quality Score Explanation
    st.write("""
        ### Quality Score Scale:
        - **0 to 4**: Low quality
        - **5 to 7**: Average quality
        - **8 to 10**: High quality
        The quality score is based on a variety of factors, including acidity, sugar levels, alcohol content, and other chemical properties.
        """)

    st.write("### Enter your preferred wine characteristics:")

    # Dynamic slider based on taste preference (Sweet or Bitter)
    if taste == "Sweet":
        min_residual_sugar = st.slider("Select minimum residual sugar level:", 8.0, 20.0, 8.0)
        max_residual_sugar = st.slider("Select maximum residual sugar level:", 8.0, 20.0, 20.0)
    else:
        min_residual_sugar = st.slider("Select minimum residual sugar level:", 0.0, 10.0, 0.0)
        max_residual_sugar = st.slider("Select maximum residual sugar level:", 0.0, 10.0, 10.0)

    # Alcohol sliders
    min_alcohol = st.slider("Select minimum alcohol percentage:", 8.0, 20.0, 8.0)
    max_alcohol = st.slider("Select maximum alcohol percentage:", 8.0, 20.0, 20.0)

    # Quality Score Slider
    min_quality = st.slider("Select minimum quality score:", 0, 10, 0)
    max_quality = st.slider("Select maximum quality score:", 0, 10, 10)

    # Filter wines based on user inputs
    filtered_wines = wine_red_white[
        (wine_red_white['residual sugar'] >= min_residual_sugar) &
        (wine_red_white['residual sugar'] <= max_residual_sugar) &
        (wine_red_white['alcohol'] >= min_alcohol) &
        (wine_red_white['alcohol'] <= max_alcohol) &
        (wine_red_white['quality'] >= min_quality) &
        (wine_red_white['quality'] <= max_quality) &
        (wine_red_white['wine_type'] != 'Other')  # Exclude "Other" wine types
    ]

    # Adjust wine selection based on the meal type
    if purpose == "Dinner Pairing":
        if dinner == "Red meat":
            # Prioritize red wines for red meat
            filtered_wines = filtered_wines[filtered_wines['type'] == 'red']
        elif dinner == "Seafood":
            # Prioritize white wines for seafood
            filtered_wines = filtered_wines[filtered_wines['type'] == 'white']
        # No filter is needed for "Poultry" as it will show both red and white wines by default

    # Show the filtered wines based on the thresholds
    st.write("### Wines that fit your criteria:")
    if filtered_wines.empty:
        st.write("No wines match your criteria.")
    else:
        # Display relevant columns
        filtered_wines_display = filtered_wines[['residual sugar', 'alcohol', 'type', 'quality', 'wine_type']]
        st.dataframe(filtered_wines_display)

        st.write("**Off-dry falls between bone dry and dry**")

        st.image("wine-sweetness-chart-red-wines-2.jpeg", caption="Red Wines Reference Chart", use_column_width=True)
        st.image("wine-sweetness-chart-white-wines.jpeg", caption="White Wines Reference Chart", use_column_width=True)

        # # A graph for better visualization
        # fig = px.scatter(
        #     filtered_wines,
        #     x='alcohol',  # X-axis variable
        #     y='residual sugar',  # Y-axis variable
        #     color='quality',  # Color by quality score
        #     title='Alcohol vs Residual Sugar Content of Wines',
        #     labels={'alcohol': 'Alcohol Content (%)', 'residual sugar': 'Residual Sugar (g/dm³)'},
        #     color_continuous_scale='Viridis'  # You can use other color scales like 'Blues', 'Inferno', etc.
        # )
        # st.plotly_chart(fig)


# Main Function
def main():
    pages = {
        "Home": home_page,
        "About the Data": explain_data,
        "Data Exploration": data_exploration,
        "Data Manipulation": data_manipulation,
        "Exploratory Data Analysis": exploratory_data_analysis,
        "Predictive Modeling": predictive_modeling,
        "Survey": survey_page,
    }
    page = st.sidebar.selectbox("Navigation", list(pages.keys()))
    pages[page]()

if __name__ == "__main__":
    main()
