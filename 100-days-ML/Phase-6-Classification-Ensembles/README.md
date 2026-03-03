# Phase 6: Classification & Ensemble Methods

**Days 58-63** | Predicting Categories and Combining Models

---

## 📋 Overview

This phase introduces classification algorithms and ensemble methods. You'll learn Logistic Regression for binary classification, Decision Trees for non-linear problems, and ensemble techniques that combine multiple models for better predictions.

---

## 📂 Folder Structure

```
Phase-6-Classification-Ensembles/
├── 01-Logistic-Regression/
│   ├── 58-logistic-regression-perceptron-trick.ipynb
│   └── 60_softmax_regression.ipynb
├── 02-Decision-Trees/
│   └── 61-decision-trees-over-under-fitting.ipynb
├── 03-Ensemble-Methods/
│   ├── 63-voting-ensemble.ipynb
│   └── 63_voting_regressor.ipynb
└── README.md
```

---

## 📚 Notebooks

### **01-Logistic-Regression/**
| Notebook | Description |
|----------|-------------|
| `58-logistic-regression-perceptron-trick.ipynb` | Logistic Regression with perceptron trick |
| `60_softmax_regression.ipynb` | Softmax Regression for multi-class classification |

### **02-Decision-Trees/**
| Notebook | Description |
|----------|-------------|
| `61-decision-trees-over-under-fitting.ipynb` | Decision Trees and bias-variance tradeoff |

### **03-Ensemble-Methods/**
| Notebook | Description |
|----------|-------------|
| `63-voting-ensemble.ipynb` | Voting classifiers for classification |
| `63_voting_regressor.ipynb` | Voting regressor for regression problems |

---

## 🎯 Learning Objectives

By the end of this phase, you will be able to:
- ✅ Understand Logistic Regression for binary classification
- ✅ Implement the perceptron trick
- ✅ Apply Softmax Regression for multi-class problems
- ✅ Build and interpret Decision Trees
- ✅ Understand overfitting and underfitting in trees
- ✅ Implement Voting Classifiers and Regressors
- ✅ Combine multiple models for better predictions

---

## 🔑 Key Concepts

### Logistic Regression

**Sigmoid Function:**
```
σ(z) = 1 / (1 + e⁻ᶻ)
```

- Outputs probability between 0 and 1
- Decision threshold typically at 0.5
- Uses log loss (binary cross-entropy) as cost function

### Softmax Regression

**Softmax Function:**
```
σ(z)ᵢ = eᶻⁱ / Σⱼeᶻʲ
```

- Generalization of logistic regression for multi-class
- Outputs probability distribution over classes

### Decision Trees

| Component | Description |
|-----------|-------------|
| **Root Node** | Top node representing entire dataset |
| **Internal Node** | Decision point based on feature |
| **Leaf Node** | Final prediction |
| **Splitting** | Dividing data based on feature values |

**Splitting Criteria:**
- **Gini Impurity**: Measures node purity
- **Information Gain**: Reduction in entropy
- **Variance Reduction**: For regression trees

### Ensemble Methods

| Method | Description | Use Case |
|--------|-------------|----------|
| **Voting Classifier** | Combines predictions from multiple classifiers | Classification |
| **Voting Regressor** | Averages predictions from multiple regressors | Regression |
| **Hard Voting** | Majority vote | Discrete predictions |
| **Soft Voting** | Weighted average of probabilities | Probabilistic predictions |

---

## 🎯 Bias-Variance Tradeoff

### Decision Trees

| Tree Depth | Bias | Variance | Result |
|------------|------|----------|--------|
| **Too Shallow** | High | Low | Underfitting |
| **Too Deep** | Low | High | Overfitting |
| **Optimal** | Balanced | Balanced | Good generalization |

### Controlling Overfitting

- **Max Depth**: Limit tree depth
- **Min Samples Split**: Minimum samples required to split
- **Min Samples Leaf**: Minimum samples in leaf nodes
- **Max Features**: Limit features considered for splitting

---

## 🛠️ Key Libraries

```python
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import VotingClassifier, VotingRegressor
from sklearn.model_selection import train_test_split
```

---

## 💡 Tips

1. Scale features for Logistic Regression (not required for trees)
2. Use class_weight='balanced' for imbalanced datasets
3. Visualize decision trees for interpretability
4. Combine diverse models in voting ensembles
5. Soft voting often outperforms hard voting

---

## 📊 Model Comparison

| Algorithm | Linearity | Feature Scaling | Interpretability | Speed |
|-----------|-----------|-----------------|------------------|-------|
| **Logistic Regression** | Linear | Required | High | Fast |
| **Decision Trees** | Non-linear | Not required | Medium | Fast |
| **Voting Ensemble** | Either | Depends | Low | Medium |

---

## 🎓 Summary

You've now completed 6 phases of Machine Learning:

1. ✅ **Phase 1**: Data Handling & EDA
2. ✅ **Phase 2**: Feature Engineering
3. ✅ **Phase 3**: ML Pipelines
4. ✅ **Phase 4**: Missing Values & Outliers
5. ✅ **Phase 5**: Regression
6. ✅ **Phase 6**: Classification & Ensembles

**Next Steps:** Explore advanced topics like Random Forests, Gradient Boosting, Neural Networks, and Deep Learning!

---

**Previous Phase:** [Phase 5 - Regression](../Phase-5-Regression/README.md)  
**Main README:** [Back to Overview](../README.md)
