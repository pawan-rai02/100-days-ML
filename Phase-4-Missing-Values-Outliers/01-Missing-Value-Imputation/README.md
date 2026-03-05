# 01-Missing-Value-Imputation

Techniques for handling missing data in datasets.

## Notebooks

- **35-missing-values-CCA.ipynb** - Complete Case Analysis (removing rows with missing values)
- **36-mean-median-imputation.ipynb** - Imputation using statistical measures
- **38-random-simple-imputation.ipynb** - Random sample and sklearn SimpleImputer

## Methods Covered

| Method | Description | When to Use |
|--------|-------------|-------------|
| **Complete Case Analysis** | Remove rows with missing values | <5% missing, MCAR |
| **Mean Imputation** | Replace with mean value | Numeric, normal distribution |
| **Median Imputation** | Replace with median value | Numeric, skewed distribution |
| **Random Sample** | Replace with random observed value | Preserves distribution |
