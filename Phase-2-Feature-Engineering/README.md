# Phase 2: Feature Engineering

**Days 24-28** | Preparing Data for Machine Learning

---

## 📋 Overview

Feature engineering is the process of transforming raw data into features that better represent the underlying problem to the predictive models. This phase covers two critical aspects: **Feature Scaling** and **Categorical Encoding**.

---

## 📂 Folder Structure

```
Phase-2-Feature-Engineering/
├── 01-Feature-Scaling/
│   ├── 24-feature-scaling.ipynb
│   ├── 24-feature-scaling-practice.ipynb
│   └── 25-featureScale-normalization.ipynb
├── 02-Categorical-Encoding/
│   ├── 26-ordinal-encoding.ipynb
│   ├── 27-one-hot-encoding.ipynb
│   └── 28-column-transform.ipynb
└── README.md
```

---

## 📚 Notebooks

### **01-Feature-Scaling/**
| Notebook | Description | Dataset |
|----------|-------------|---------|
| `24-feature-scaling.ipynb` | Introduction to feature scaling concepts | Social Network Ads |
| `24-feature-scaling-practice.ipynb` | Hands-on practice with scaling | Breast Cancer |
| `25-featureScale-normalization.ipynb` | Min-Max normalization technique | Wine Quality |

### **02-Categorical-Encoding/**
| Notebook | Description | Dataset |
|----------|-------------|---------|
| `26-ordinal-encoding.ipynb` | Encoding ordered categorical variables | Review Data |
| `27-one-hot-encoding.ipynb` | Encoding nominal categorical variables | Car Selling Price |
| `28-column-transform.ipynb` | Applying multiple transformations | Cold/Fever Data |

---

## 🎯 Learning Objectives

By the end of this phase, you will be able to:
- ✅ Understand why feature scaling is necessary
- ✅ Apply Standardization (Z-score normalization)
- ✅ Apply Normalization (Min-Max scaling)
- ✅ Choose between standardization and normalization
- ✅ Encode ordinal categorical variables
- ✅ Encode nominal categorical variables
- ✅ Use ColumnTransformer for multiple preprocessing steps
- ✅ Handle missing values during transformation

---

## 🔑 Key Concepts

### Feature Scaling

| Technique | Formula | Range | Use Case |
|-----------|---------|-------|----------|
| **Standardization** | z = (x - μ) / σ | No fixed range | Most algorithms, especially distance-based |
| **Normalization** | z = (x - min) / (max - min) | [0, 1] | Neural networks, image processing |

### Categorical Encoding

| Technique | Description | When to Use |
|-----------|-------------|-------------|
| **Ordinal Encoding** | Assigns integer values based on order | Ordered categories (e.g., Low, Medium, High) |
| **One-Hot Encoding** | Creates binary columns for each category | Nominal categories (e.g., Red, Blue, Green) |
| **ColumnTransformer** | Applies different transformations to different columns | Mixed data types preprocessing |

---

## 🛠️ Key Libraries

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
```

---

## 💡 Tips

1. **Always split before scaling** to avoid data leakage
2. Use `fit_transform()` on training data, `transform()` on test data
3. Choose encoding based on the nature of your categorical variable
4. ColumnTransformer keeps your preprocessing pipeline clean and organized
5. Practice with different datasets to understand when to use which technique

---

## 📊 Common Pitfalls

| Mistake | Solution |
|---------|----------|
| Scaling before train-test split | Split first, then scale |
| Using one-hot on ordinal data | Use ordinal encoding instead |
| Using ordinal on nominal data | Use one-hot encoding instead |
| Fitting scaler on test data | Only transform test data |

---

**Previous Phase:** [Phase 1 - Data Handling & EDA](../Phase-1-Data-Handling-EDA/README.md)  
**Next Phase:** [Phase 3 - ML Pipelines](../Phase-3-ML-Pipelines/README.md)
