# Student Depression

[中文文档](./README_CN.md)

Student Depression Dataset Analysis

- [dataset](https://www.kaggle.com/datasets/hopesb/student-depression-dataset/data)

## Setup

```bash
conda create -n dm python=3.10
conda activate dm
pip install -r requirements.txt

# Download Dataset
bash download-dataset.sh
```

## TODO

- **Exploratory Data Analysis (EDA)** <br>
    Start by exploring the dataset to understand its structure, distribution, and relationships:
    - **Descriptive Statistics**: Calculate means, medians, standard deviations, and proportions for numeric and categorical columns.
    - **Visualization**:
        - Histograms for distributions (e.g., Age, Sleep Duration, CGPA).
	    - Bar charts for categorical data (e.g., Gender, City, Degree).
	    - Boxplots to analyze CGPA, Sleep Duration, etc., across categorical variables.
	    - Correlation matrix to identify relationships between numeric variables like CGPA, Sleep Duration, and pressures.
    - **Missing Values Analysis**: Check for and handle missing or inconsistent data

- **Clustering** ✅ <br>
    Use clustering to identify patterns or groups within the dataset:
	- **K-Means or Hierarchical Clustering**: Group individuals based on variables like Academic Pressure, Work Pressure, Sleep Duration, and Financial Stress.
	- **Principal Component Analysis (PCA)**: Reduce dimensionality for visualization of clusters.


- **Classification and Prediction** ✅ <br>
    Develop models to predict key outcomes:
	- **Depression Prediction**: Use features like Sleep Duration, Dietary Habits, Financial Stress, and Family History of Mental Illness to predict depression.
	- **Suicidal Thoughts Prediction**: Analyze the likelihood of suicidal thoughts based on Work Pressure, Academic Pressure, Financial Stress, etc
    **Algorithm**: Decison Tree

- **Association Rule Mining** ✅ <br>
    Explore patterns among categorical variables:
	- Use Apriori or FP-Growth algorithms to find relationships like:
        - “Individuals with high academic pressure and low sleep duration are more likely to report depression.”
        - “People with family history of mental illness and dietary habits rated poorly tend to experience suicidal thoughts.”
