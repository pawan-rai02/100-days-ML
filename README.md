# 100 Days of Machine Learning

A comprehensive journey through Machine Learning fundamentals, from data handling to building production-ready ML pipelines and advanced algorithms.

## 📁 Project Structure

```
100-days-ML/
├── Phase-1-Data-Handling-EDA/       # Days 13-22: Data Collection & EDA
│   ├── 01-Data-Collection/
│   └── 02-Exploratory-Data-Analysis/
├── Phase-2-Feature-Engineering/      # Days 24-32: Feature Preparation
│   ├── 01-Feature-Scaling/
│   └── 02-Categorical-Encoding/
├── Phase-3-ML-Pipelines/             # Day 29: Building ML Pipelines
│   ├── 01-Pipeline-Basics/
│   └── 02-Pipeline-Practice/
├── Phase-4-Missing-Values-Outliers/  # Days 35-44: Data Cleaning
│   ├── 01-Missing-Value-Imputation/
│   └── 02-Outlier-Detection/
├── Phase-5-Regression/               # Days 48-56: Regression Algorithms
│   ├── 01-Linear-Regression/
│   ├── 02-Gradient-Descent/
│   └── 03-Regularization/
├── Phase-6-Classification-Ensembles/ # Days 58-66: Classification & Ensembles
│   ├── 01-Logistic-Regression/
│   ├── 02-Decision-Trees/
│   ├── 03-Ensemble-Methods/
│   ├── 04-Random-Forest/
│   └── 05-Boosting/
├── Phase-7-Advanced-Ensembles/       # Day 67+: Gradient Boosting
│   └── 01-Gradient-Boosting/
├── datasets/                          # Raw datasets for practice
├── extras/                            # Additional resources & notes
└── README.md
```

---

## 📚 Learning Phases

### **Phase 1: Data Handling & Exploratory Data Analysis** (Days 13-22)
Learn the fundamentals of working with data, from collection to exploration.

**Topics Covered:**
- Working with CSV files and data loading
- Web scraping techniques
- Understanding data structure and quality
- Univariate and multivariate analysis
- Automated EDA with pandas profiling

📖 [View Phase 1 Details](Phase-1-Data-Handling-EDA/README.md)

---

### **Phase 2: Feature Engineering** (Days 24-32)
Master the art of preparing data for machine learning models.

**Topics Covered:**
- Feature scaling (Standardization & Normalization)
- Power transformations and function transformers
- Ordinal and one-hot encoding
- ColumnTransformer for multiple preprocessing steps
- Binning, binarization, and datetime features

📖 [View Phase 2 Details](Phase-2-Feature-Engineering/README.md)

---

### **Phase 3: ML Pipelines** (Day 29)
Build clean, reproducible, and production-ready ML workflows.

**Topics Covered:**
- Manual preprocessing vs. pipelines
- Building sklearn Pipelines
- ColumnTransformer integration
- Practice with real-world datasets

📖 [View Phase 3 Details](Phase-3-ML-Pipelines/README.md)

---

### **Phase 4: Missing Value Imputation & Outlier Detection** (Days 35-44)
Handle data quality issues for robust models.

**Topics Covered:**
- Complete Case Analysis
- Mean/Median imputation
- Random sample imputation
- Outlier detection using IQR and percentiles
- Outlier capping and treatment

📖 [View Phase 4 Details](Phase-4-Missing-Values-Outliers/README.md)

---

### **Phase 5: Regression** (Days 48-56)
Predict continuous values using regression algorithms.

**Topics Covered:**
- Simple Linear Regression
- Gradient Descent optimization
- Batch and Stochastic Gradient Descent
- Ridge (L2) and Lasso (L1) regularization

📖 [View Phase 5 Details](Phase-5-Regression/README.md)

---

### **Phase 6: Classification & Ensemble Methods** (Days 58-66)
Predict categories and combine models for better accuracy.

**Topics Covered:**
- Logistic Regression and Softmax Regression
- Decision Trees and bias-variance tradeoff
- Voting Classifiers and Regressors
- Bagging ensemble methods
- Random Forest algorithm and feature importance
- Out-of-Bag (OOB) scoring
- AdaBoost boosting algorithm

📖 [View Phase 6 Details](Phase-6-Classification-Ensembles/README.md)

---

### **Phase 7: Advanced Ensembles** (Day 67+)
Master advanced boosting techniques used in competitions and production.

**Topics Covered:**
- Gradient Boosting algorithm
- Mathematical foundations of gradient boosting
- Gradient Boosting for classification and regression

📖 [View Phase 7 Details](Phase-7-Advanced-Ensembles/README.md)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Jupyter Notebook / JupyterLab
- Required libraries (see below)

### Installation

```bash
# Navigate to the repository
cd 100-days-ML/100-days-ML

# Install required packages
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
pip install ydata-profiling playwright beautifulsoup4 requests
```

### Running Notebooks

1. Navigate to any phase folder
2. Open the `.ipynb` file in Jupyter Notebook or VS Code
3. Run cells sequentially to follow along

---

## 📊 Datasets Used

| Dataset | Phase | Description |
|---------|-------|-------------|
| Placement Data | Phase 1 | Student placement predictions |
| Fraud Detection | Phase 1 | Transaction fraud classification |
| Titanic | Phase 1, 3 | Passenger survival data |
| Telecom Churn | Phase 3 | Customer churn prediction |
| Loan Default | Phase 3 | Loan default prediction |
| Social Network Ads | Phase 2 | Ad purchase predictions |
| Wine Quality | Phase 2 | Wine chemical properties |
| Car Selling Price | Phase 2 | Vehicle pricing data |

*See [datasets/README.md](datasets/README.md) for complete list*

---

## 🎯 Learning Outcomes

By completing this course, you will:

### Data Skills
- ✅ Collect and load data from various sources
- ✅ Perform comprehensive exploratory data analysis
- ✅ Identify and handle missing values
- ✅ Detect and treat outliers

### Feature Engineering
- ✅ Apply feature scaling techniques
- ✅ Encode categorical variables appropriately
- ✅ Build preprocessing pipelines

### Machine Learning
- ✅ Build and evaluate regression models
- ✅ Implement classification algorithms
- ✅ Understand and apply regularization
- ✅ Create ensemble models
- ✅ Deploy production-ready ML pipelines

---

## 📝 Course Progress

| Phase | Status | Notebooks |
|-------|--------|-----------|
| Phase 1 - Data Handling & EDA | ✅ Complete | 8 notebooks |
| Phase 2 - Feature Engineering | ✅ Complete | 9 notebooks |
| Phase 3 - ML Pipelines | ✅ Complete | 4 notebooks |
| Phase 4 - Missing Values & Outliers | ✅ Complete | 6 notebooks |
| Phase 5 - Regression | ✅ Complete | 8 notebooks |
| Phase 6 - Classification & Ensembles | ✅ Complete | 16 notebooks |
| Phase 7 - Advanced Ensembles | ✅ Complete | 2 notebooks |

---

## 📖 Additional Resources

- [Scikit-Learn Documentation](https://scikit-learn.org/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [Towards Data Science](https://towardsdatascience.com/)

---

## 📂 Quick Navigation

| Phase 1 | Phase 2 | Phase 3 |
|---------|---------|---------|
| [Data Handling](Phase-1-Data-Handling-EDA/README.md) | [Feature Engineering](Phase-2-Feature-Engineering/README.md) | [ML Pipelines](Phase-3-ML-Pipelines/README.md) |

| Phase 4 | Phase 5 | Phase 6 |
|---------|---------|---------|
| [Missing Values & Outliers](Phase-4-Missing-Values-Outliers/README.md) | [Regression](Phase-5-Regression/README.md) | [Classification & Ensembles](Phase-6-Classification-Ensembles/README.md) |

| Phase 7 |
|---------|
| [Advanced Ensembles](Phase-7-Advanced-Ensembles/README.md) |

---

**Happy Learning! 🚀**

*Last Updated: April 2026*
