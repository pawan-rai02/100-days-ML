# Phase 3: ML Pipelines

**Day 29** | Building Production-Ready Machine Learning Workflows

---

## 📋 Overview

This phase focuses on building clean, reproducible, and production-ready machine learning pipelines. You'll learn why pipelines are essential and how to implement them using scikit-learn's `Pipeline` and `ColumnTransformer`.

---

## 📂 Folder Structure

```
Phase-3-ML-Pipelines/
├── 01-Pipeline-Basics/
│   ├── 29-without-pipeline.ipynb
│   └── 29-02-with-pipeline.ipynb
├── 02-Pipeline-Practice/
│   ├── 29-03-practice-pipeline.ipynb
│   └── 29-04-practice-pipeline.ipynb
└── README.md
```

---

## 📚 Notebooks

### **01-Pipeline-Basics/**
| Notebook | Description | Dataset |
|----------|-------------|---------|
| `29-without-pipeline.ipynb` | Manual step-by-step preprocessing (comparison) | Titanic |
| `29-02-with-pipeline.ipynb` | Building complete ML pipelines with sklearn | Titanic |

### **02-Pipeline-Practice/**
| Notebook | Description | Dataset |
|----------|-------------|---------|
| `29-03-practice-pipeline.ipynb` | Pipeline implementation with telecom churn data | Telecom Churn |
| `29-04-practice-pipeline.ipynb` | Pipeline implementation with loan default data | Loan Default |

---

## 🎯 Learning Objectives

By the end of this phase, you will be able to:
- ✅ Understand the benefits of using ML pipelines
- ✅ Compare manual preprocessing vs. pipeline approach
- ✅ Build sklearn Pipeline with multiple steps
- ✅ Integrate ColumnTransformer within pipelines
- ✅ Handle numerical and categorical features separately
- ✅ Apply imputation, scaling, and encoding in a single pipeline
- ✅ Work with `handle_unknown` parameter for categorical features
- ✅ Create reproducible ML workflows

---

## 🔑 Key Concepts

### What is a Pipeline?

A pipeline chains multiple preprocessing steps and a model together into a single estimator.

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression())
])
```

### Benefits of Pipelines

| Benefit | Description |
|---------|-------------|
| **Clean Code** | No repetitive code, organized workflow |
| **No Data Leakage** | Ensures proper train/test separation |
| **Reproducibility** | Same transformations every time |
| **Easy Deployment** | Save and load entire workflow as one object |
| **Cross-Validation** | Works seamlessly with `cross_val_score` |

---

## 🛠️ Pipeline Components

### Typical Pipeline Structure

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier

# Preprocessing for numerical features
numerical_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', MinMaxScaler())
])

# Preprocessing for categorical features
categorical_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

# Combine with ColumnTransformer
preprocessor = ColumnTransformer([
    ('num', numerical_pipeline, numerical_columns),
    ('cat', categorical_pipeline, categorical_columns)
])

# Full pipeline with model
full_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', DecisionTreeClassifier())
])
```

---

## 📊 Practice Datasets

### Telecom Churn Dataset
- **Features:** 11 columns (gender, age, city, plan, tenure, monthly_bill, etc.)
- **Target:** churn (Yes/No)
- **Challenge:** Missing values and dirty categories

### Loan Default Dataset
- **Features:** 11 columns (gender, age, education, job_type, income, loan_amount, etc.)
- **Target:** default (Yes/No)
- **Challenge:** Mixed data types with missing values

---

## 💡 Tips

1. **Always use pipelines** for production code
2. Set `handle_unknown='ignore'` for robust categorical encoding
3. Name your pipeline steps for easy access and debugging
4. Use `pipeline.named_steps.step_name` to access specific components
5. Save entire pipeline with `joblib.dump()` for deployment

---

## 🚀 Deployment Example

```python
import joblib

# Save the trained pipeline
joblib.dump(full_pipeline, 'model_pipeline.pkl')

# Load and use for predictions
loaded_model = joblib.load('model_pipeline.pkl')
predictions = loaded_model.predict(new_data)
```

---

## 📈 Comparison: With vs. Without Pipeline

| Aspect | Without Pipeline | With Pipeline |
|--------|-----------------|---------------|
| Code Length | 50+ lines | ~20 lines |
| Data Leakage Risk | High | None |
| Reproducibility | Manual tracking | Automatic |
| Deployment | Multiple objects | Single object |
| Cross-Validation | Complex | Simple |

---

## 🎓 Summary

You've now completed the foundational ML learning path! You can:
1. Collect and explore data (Phase 1)
2. Engineer features effectively (Phase 2)
3. Build production-ready pipelines (Phase 3)

**Next Steps:** Continue with advanced ML algorithms, model tuning, and deployment!

---

**Previous Phase:** [Phase 2 - Feature Engineering](../Phase-2-Feature-Engineering/README.md)  
**Main README:** [Back to Overview](../README.md)
