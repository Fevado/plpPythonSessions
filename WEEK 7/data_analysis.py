# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset

def load_and_explore_data():
    """Load the Iris dataset and perform initial exploration"""
    try:
        # Load the iris dataset
        iris = load_iris()
        
        # Create a DataFrame
        df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        df['species'] = iris.target
        df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
        
        # Display first few rows
        print("First 5 rows of the dataset:")
        print(df.head())
        print("\n")
        
        # Explore structure
        print("Dataset information:")
        print(df.info())
        print("\n")
        
        # Check for missing values
        print("Missing values per column:")
        print(df.isnull().sum())
        print("\n")
        
        # Since there are no missing values in this dataset, we don't need to clean
        # But for demonstration, here's how we would handle missing values:
        # df = df.dropna()  # or df.fillna(value)
        
        return df
    
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return None

# Task 2: Basic Data Analysis

def perform_basic_analysis(df):
    """Perform basic statistical analysis on the dataset"""
    if df is None:
        return
    
    try:
        # Basic statistics
        print("Basic statistics for numerical columns:")
        print(df.describe())
        print("\n")
        
        # Group by species and compute mean
        print("Mean measurements by species:")
        print(df.groupby('species').mean())
        print("\n")
        
        # Additional interesting findings
        print("Additional observations:")
        print("1. Setosa has significantly smaller petal dimensions compared to other species.")
        print("2. Virginica has the largest measurements on average across all features.")
        print("3. Versicolor is intermediate between setosa and virginica in all measurements.")
        
    except Exception as e:
        print(f"An error occurred during analysis: {e}")

# Task 3: Data Visualization

def create_visualizations(df):
    """Create various visualizations of the data"""
    if df is None:
        return
    
    try:
        # Set style for better looking plots
        sns.set(style="whitegrid")
        
        # Create figure with subplots
        plt.figure(figsize=(15, 10))
        
        # 1. Line chart showing trends (using sepal length by index as proxy for time)
        plt.subplot(2, 2, 1)
        df['sepal length (cm)'].plot(kind='line', title='Sepal Length Trend', color='green')
        plt.xlabel('Observation Index')
        plt.ylabel('Sepal Length (cm)')
        
        # 2. Bar chart comparing average petal length per species
        plt.subplot(2, 2, 2)
        df.groupby('species')['petal length (cm)'].mean().plot(kind='bar', color=['red', 'green', 'blue'])
        plt.title('Average Petal Length by Species')
        plt.ylabel('Petal Length (cm)')
        
        # 3. Histogram of sepal width distribution
        plt.subplot(2, 2, 3)
        df['sepal width (cm)'].plot(kind='hist', bins=15, color='purple', alpha=0.7)
        plt.title('Distribution of Sepal Width')
        plt.xlabel('Sepal Width (cm)')
        
        # 4. Scatter plot of sepal length vs petal length
        plt.subplot(2, 2, 4)
        colors = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
        for species, group in df.groupby('species'):
            plt.scatter(group['sepal length (cm)'], group['petal length (cm)'], 
                        color=colors[species], label=species)
        plt.title('Sepal Length vs Petal Length')
        plt.xlabel('Sepal Length (cm)')
        plt.ylabel('Petal Length (cm)')
        plt.legend()
        
        plt.tight_layout()
        plt.show()
        
        # Additional visualization: Pairplot to show all relationships
        print("\nGenerating pairplot (this may take a moment)...")
        sns.pairplot(df, hue='species', palette=colors)
        plt.suptitle('Pairwise Relationships in Iris Dataset', y=1.02)
        plt.show()
        
    except Exception as e:
        print(f"An error occurred during visualization: {e}")

# Main execution
if __name__ == "__main__":
    print("Starting data analysis...\n")
    
    # Task 1
    print("=== TASK 1: LOAD AND EXPLORE DATASET ===")
    iris_df = load_and_explore_data()
    
    # Task 2
    print("\n=== TASK 2: BASIC DATA ANALYSIS ===")
    perform_basic_analysis(iris_df)
    
    # Task 3
    print("\n=== TASK 3: DATA VISUALIZATION ===")
    create_visualizations(iris_df)
    
    print("\nAnalysis complete!")