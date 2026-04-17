# 100 Days of Machine Learning

A comprehensive journey through Machine Learning fundamentals, from data handling to building production-ready ML pipelines and advanced algorithms.

## 📁 Project Structure

```
100-days-ML/
├── Phase-1-Data-Handling-EDA/          # days 13-22: Data Collection & EDA
│   ├── 01-Data-Collection/
│   │   ├── 15-working-with-csv.ipynb
│   │   └── 18-Web-Scrapping.ipynb
│   ├── 02-Exploratory-Data-Analysis/
│   │   ├── 19-understanding-data.ipynb
│   │   ├── 20-eda-univariate.ipynb
│   │   ├── 21-eda-multivariate.ipynb
│   │   └── 22-pandas-profiling.ipynb
│   └── 03-Practice/
│       ├── 13-end-to-end-placement.ipynb
│       └── 13-practice.ipynb
├── Phase-2-Feature-Engineering/         # Days 24-45: Feature Preparation
│   ├── 01-Feature-Scaling/
│   │   ├── 24-feature-scaling.ipynb
│   │   ├── 24-feature-scaling-practice.ipynb
│   │   ├── 25-featureScale-normalization.ipynb
│   │   ├── 30_function_transformer.ipynb
│   │   └── 31-power-transformer.ipynb
│   ├── 02-Categorical-Encoding/
│   │   ├── 26-ordinal-encoding.ipynb
│   │   ├── 27-one-hot-encoding.ipynb
│   │   └── 28-column-transform.ipynb
│   └── 03-Feature-Construction/
│       ├── 32-binning-binarization.ipynb
│       ├── 34_dateTime.ipynb
│       └── 45-feature-construction.ipynb
├── Phase-3-ML-Pipelines/                # Day 29: Building ML Pipelines
│   ├── 01-Pipeline-Basics/
│   │   ├── 29-without-pipeline.ipynb
│   │   └── 29-02-with-pipeline.ipynb
│   └── 02-Pipeline-Practice/
│       ├── 29-03-practice-pipeline.ipynb
│       └── 29-04-practice-pipeline.ipynb
├── Phase-4-Missing-Values-Outliers/     # Days 35-44: Data Cleaning
│   ├── 01-Missing-Value-Imputation/
│   │   ├── 35-missing-values-CCA.ipynb
│   │   ├── 36-mean-median-imputation.ipynb
│   │   └── 38-random-simple-imputation.ipynb
│   └── 02-Outlier-Detection/
│       ├── 42-outlier-detection-removal.ipynb
│       ├── 43-outlier-IQR-capping.ipynb
│       └── 44-outlier-percentile.ipynb
├── Phase-5-Regression/                  # Days 48-56: Regression Algorithms
│   ├── 01-Linear-Regression/
│   │   ├── 48-simple-linear-reg.ipynb
│   │   └── 48-SLR-02.ipynb
│   ├── 02-Gradient-Descent/
│   │   ├── 51-gradient-descent.ipynb
│   │   ├── 51-02-gradient-descent.ipynb
│   │   ├── 52-Batch-Gradient-Descent.ipynb
│   │   └── 53-stochastic-GD.ipynb
│   └── 03-Regularization/
│       ├── 55-ridge-regression.ipynb
│       └── 56-lasso-regression.ipynb
├── Phase-6-Classification-Ensembles/    # Days 58-66: Classification & Ensembles
│   ├── 01-Logistic-Regression/
│   │   ├── 58-logistic-regression-perceptron-trick.ipynb
│   │   └── 60_softmax_regression.ipynb
│   ├── 02-Decision-Trees/
│   │   └── 61-decision-trees-over-under-fitting.ipynb
│   ├── 03-Ensemble-Methods/
│   │   ├── 63-voting-ensemble.ipynb
│   │   ├── 63_voting_regressor.ipynb
│   │   ├── 64_bagging_ensemble.ipynb
│   │   └── 65_bagging.ipynb
│   ├── 04-Random-Forest/
│   │   ├── 66-01-random-forest-demo.ipynb
│   │   ├── 66-02-random-forest-demo.ipynb
│   │   ├── 66-03-bagging-vs-randomForest.ipynb
│   │   ├── 66-04-code-example-rf.ipynb
│   │   ├── 66-05-oob-score-demo.ipynb
│   │   └── 66-06-feature-importance-rf-dt.ipynb
│   └── 05-Boosting/
│       └── 66-adaboost-demo.ipynb
├── Phase-7-Advanced-Ensembles/          # Days 67-68: Advanced Boosting
│   ├── 01-Gradient-Boosting/
│   │   ├── 67-01-gradient-boost.ipynb
│   │   └── 67-02-gradient-boost-maths-demo.ipynb
│   └── 02-XGBoost/
│       └── 68-01-XGBoost-test.ipynb
├── Phase-8-Unsupervised/                 # Days 70+: Unsupervised Learning
│   ├── 01-K-Means/
│   │   ├── 70-k-means.ipynb
│   │   ├── _71_kMeans.py
│   │   └── 71-app.py
│   └── 02-Naive-Bayes/
├── datasets/                             # Raw datasets for practice
│   └── heart.csv
├── extras/                               # Additional resources & notes
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

### **Phase 2: Feature Engineering** (Days 24-45)
Master the art of preparing data for machine learning models.

**Topics Covered:**
- Feature scaling (Standardization & Normalization)
- Power transformations and function transformers
- Ordinal and one-hot encoding
- ColumnTransformer for multiple preprocessing steps
- Binning, binarization, and datetime features
- Feature construction

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

### **Phase 7: Advanced Ensembles** (Days 67-68)
Master advanced boosting techniques used in competitions and production.

**Topics Covered:**
- Gradient Boosting algorithm
- Mathematical foundations of gradient boosting
- XGBoost testing and implementation

📖 [View Phase 7 Details](Phase-7-Advanced-Ensembles/README.md)

---

### **Phase 8: Unsupervised Learning** (Days 70+)
Implement unsupervised learning algorithms.

**Topics Covered:**
- K-Means clustering algorithm (from scratch)
- Elbow method for optimal clusters
- Streamlit app for interactive demo
- Naive Bayes classification

📖 [View Phase 8 Details](Phase-8-Unsupervised/)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Jupyter Notebook / JupyterLab
- Required libraries (see below)

### Installation

```bash
# Navigate to the repository
cd 100-days-ML

# Install required packages
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
pip install ydata-profiling playwright beautifulsoup4 requests
pip install xgboost streamlit
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
| Heart Disease | Phase 8 | Heart disease prediction |

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
- ✅ Construct new features from existing data

### Machine Learning
- ✅ Build and evaluate regression models
- ✅ Implement classification algorithms
- ✅ Understand and apply regularization
- ✅ Create ensemble models (Bagging, Random Forest, Boosting)
- ✅ Deploy production-ready ML pipelines
- ✅ Implement clustering algorithms from scratch

---

## 📝 Course Progress

| Phase | Status | Notebooks/Files |
|-------|--------|-----------------|
| Phase 1 - Data Handling & EDA | ✅ Complete | 6 notebooks |
| Phase 2 - Feature Engineering | ✅ Complete | 8 notebooks |
| Phase 3 - ML Pipelines | ✅ Complete | 4 notebooks |
| Phase 4 - Missing Values & Outliers | ✅ Complete | 6 notebooks |
| Phase 5 - Regression | ✅ Complete | 8 notebooks |
| Phase 6 - Classification & Ensembles | ✅ Complete | 11 notebooks |
| Phase 7 - Advanced Ensembles | ✅ Complete | 3 notebooks |
| Phase 8 - Unsupervised Learning | 🚧 In Progress | 1 notebook + 2 Python scripts |

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

| Phase 7 | Phase 8 |
|---------|---------|
| [Advanced Ensembles](Phase-7-Advanced-Ensembles/README.md) | [Unsupervised](Phase-8-Unsupervised/) |

---

**Happy Learning! 🚀**

*Last Updated: April 2026*
