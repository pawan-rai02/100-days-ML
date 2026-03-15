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
│   ├── 63_voting_regressor.ipynb
│   ├── 64_bagging_ensemble.ipynb
│   └── 65_bagging.ipynb
├── 04-Random-Forest/
│   ├── 66-01-random-forest-demo.ipynb
│   ├── 66-02-random-forest-demo.ipynb
│   ├── 66-03-bagging-vs-randomForest.ipynb
│   ├── 66-04-code-example-rf.ipynb
│   ├── 66-05-oob-score-demo.ipynb
│   └── 66-06-feature-importance-rf-dt.ipynb
├── 05-Boosting/
│   └── 66-adaboost-demo.ipynb
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
| `64_bagging_ensemble.ipynb` | Bagging ensemble method introduction |
| `65_bagging.ipynb` | Bagging implementation examples |

### **04-Random-Forest/**
| Notebook | Description |
|----------|-------------|
| `66-01-random-forest-demo.ipynb` | Introduction to Random Forest Classifier |
| `66-02-random-forest-demo.ipynb` | Random Forest implementation examples |
| `66-03-bagging-vs-randomForest.ipynb` | Comparing Bagging and Random Forest |
| `66-04-code-example-rf.ipynb` | Practical code examples with Random Forest |
| `66-05-oob-score-demo.ipynb` | Understanding Out-of-Bag (OOB) scoring |
| `66-06-feature-importance-rf-dt.ipynb` | Feature importance: RF vs Decision Trees |

### **05-Boosting/**
| Notebook | Description |
|----------|-------------|
| `66-adaboost-demo.ipynb` | Introduction to AdaBoost algorithm |

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
- ✅ Understand and implement Bagging ensembles
- ✅ Master Random Forest algorithm and its applications
- ✅ Use Out-of-Bag (OOB) scoring for validation
- ✅ Extract and interpret feature importance from Random Forests
- ✅ Understand Boosting paradigm and implement AdaBoost

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
| **Bagging** | Bootstrap aggregating to reduce variance | Classification & Regression |
| **Random Forest** | Bagging with random feature selection | Classification & Regression |
| **Boosting (AdaBoost)** | Sequential learning from mistakes | Classification & Regression |

### Random Forest

**Algorithm Steps:**
1. Create bootstrap samples from training data
2. Build decision tree on each sample
3. At each split, consider random subset of features
4. Aggregate predictions from all trees

**Key Advantages:**
- Reduces overfitting compared to single trees
- Provides feature importance measures
- Robust to outliers and noise
- No feature scaling required

### Boosting (AdaBoost)

**Algorithm Steps:**
1. Assign equal weights to all samples
2. Train weak learner, calculate weighted error
3. Calculate learner importance (alpha)
4. Increase weights for misclassified samples
5. Repeat for n estimators
6. Combine learners with weighted voting

**Key Advantages:**
- Reduces bias effectively
- Works with weak learners
- Automatic feature selection
- Less prone to overfitting (with proper tuning)

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
from sklearn.ensemble import (VotingClassifier, VotingRegressor, 
                              BaggingClassifier, BaggingRegressor,
                              RandomForestClassifier, RandomForestRegressor,
                              AdaBoostClassifier, AdaBoostRegressor)
from sklearn.model_selection import train_test_split
```

---

## 💡 Tips

1. Scale features for Logistic Regression (not required for trees)
2. Use class_weight='balanced' for imbalanced datasets
3. Visualize decision trees for interpretability
4. Combine diverse models in voting ensembles
5. Soft voting often outperforms hard voting
6. Random Forest: use `sqrt(n_features)` for classification, `n_features // 3` for regression
7. Enable OOB score in Random Forest for internal validation (`oob_score=True`)
8. Use feature importance for feature selection insights
9. AdaBoost: use simple weak learners (decision stumps, max_depth=1)
10. AdaBoost: sensitive to outliers - clean data first

---

## 📊 Model Comparison

| Algorithm | Linearity | Feature Scaling | Interpretability | Speed |
|-----------|-----------|-----------------|------------------|-------|
| **Logistic Regression** | Linear | Required | High | Fast |
| **Decision Trees** | Non-linear | Not required | Medium | Fast |
| **Voting Ensemble** | Either | Depends | Low | Medium |
| **Bagging** | Non-linear | Not required | Low | Medium |
| **Random Forest** | Non-linear | Not required | Low-Medium | Medium |
| **AdaBoost** | Non-linear | Not required | Low-Medium | Medium |

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
