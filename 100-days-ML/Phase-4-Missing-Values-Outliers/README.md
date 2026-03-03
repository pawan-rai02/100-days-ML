# Phase 4: Missing Value Imputation & Outlier Detection

**Days 35-44** | Data Cleaning and Quality

---

## 📋 Overview

This phase covers two critical aspects of data preprocessing: handling missing values and detecting/treating outliers. These steps are essential for building robust machine learning models.

---

## 📂 Folder Structure

```
Phase-4-Missing-Values-Outliers/
├── 01-Missing-Value-Imputation/
│   ├── 35-missing-values-CCA.ipynb
│   ├── 36-mean-median-imputation.ipynb
│   └── 38-random-simple-imputation.ipynb
├── 02-Outlier-Detection/
│   ├── 42-outlier-detection-removal.ipynb
│   ├── 43-outlier-IQR-capping.ipynb
│   └── 44-outlier-percentile.ipynb
└── README.md
```

---

## 📚 Notebooks

### **01-Missing-Value-Imputation/**
| Notebook | Description |
|----------|-------------|
| `35-missing-values-CCA.ipynb` | Complete Case Analysis (dropping missing values) |
| `36-mean-median-imputation.ipynb` | Imputation using mean and median values |
| `38-random-simple-imputation.ipynb` | Random sample and SimpleImputer techniques |

### **02-Outlier-Detection/**
| Notebook | Description |
|----------|-------------|
| `42-outlier-detection-removal.ipynb` | Detecting and removing outliers |
| `43-outlier-IQR-capping.ipynb` | IQR-based outlier capping/winsorization |
| `44-outlier-percentile.ipynb` | Percentile-based outlier treatment |

---

## 🎯 Learning Objectives

By the end of this phase, you will be able to:
- ✅ Identify different types of missing data (MCAR, MAR, NMAR)
- ✅ Apply Complete Case Analysis
- ✅ Use mean/median imputation
- ✅ Implement random sample imputation
- ✅ Detect outliers using statistical methods
- ✅ Apply IQR-based capping (winsorization)
- ✅ Use percentile-based outlier treatment

---

## 🔑 Key Concepts

### Missing Data Mechanisms

| Type | Description | Treatment |
|------|-------------|-----------|
| **MCAR** | Missing Completely At Random | Any imputation method |
| **MAR** | Missing At Random | Model-based imputation |
| **NMAR** | Not Missing At Random | Requires domain knowledge |

### Imputation Methods

| Method | Pros | Cons |
|--------|------|------|
| **Complete Case Analysis** | Simple, no bias introduced | Loss of data |
| **Mean/Median Imputation** | Preserves sample size | Reduces variance, distorts correlations |
| **Random Sample Imputation** | Preserves distribution | Requires sufficient data |

### Outlier Detection Methods

| Method | Description | Use Case |
|--------|-------------|----------|
| **IQR Method** | Q1 - 1.5×IQR, Q3 + 1.5×IQR | Skewed distributions |
| **Percentile Method** | Cap at specific percentiles (e.g., 1st, 99th) | Any distribution |
| **Z-Score** | Values beyond ±3 standard deviations | Normal distributions |

---

## 💡 Tips

1. Always analyze the pattern of missingness before choosing a method
2. IQR method is robust for skewed distributions
3. Consider domain knowledge when treating outliers
4. Document all imputation decisions for reproducibility

---

**Previous Phase:** [Phase 2 - Feature Engineering](../Phase-2-Feature-Engineering/README.md)  
**Next Phase:** [Phase 5 - Regression](../Phase-5-Regression/README.md)
