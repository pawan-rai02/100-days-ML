# Phase 7: Advanced Ensembles

**Days 67+** | Gradient Boosting and Advanced Ensemble Methods

---

## 📋 Overview

This phase covers advanced ensemble methods, focusing on Gradient Boosting algorithms. These powerful techniques build models sequentially to minimize errors, forming the basis of many winning solutions in machine learning competitions.

---

## 📂 Folder Structure

```
Phase-7-Advanced-Ensembles/
├── 01-Gradient-Boosting/
│   ├── 67-01-gradient-boost.ipynb
│   └── 67-02-gradient-boost-maths-demo.ipynb
└── README.md
```

---

## 📚 Notebooks

### **01-Gradient-Boosting/**

| Notebook | Description |
|----------|-------------|
| `67-01-gradient-boost.ipynb` | Introduction to Gradient Boosting algorithm |
| `67-02-gradient-boost-maths-demo.ipynb` | Mathematical foundations of Gradient Boosting |

---

## 🎯 Learning Objectives

By the end of this phase, you will be able to:
- ✅ Understand Gradient Boosting fundamentals
- ✅ Explain the gradient descent approach to boosting
- ✅ Implement Gradient Boosting classifiers and regressors
- ✅ Understand the mathematics behind gradient boosting
- ✅ Compare AdaBoost, Gradient Boosting, and other ensemble methods

---

## 🔑 Key Concepts

### Gradient Boosting

**How it works:**
1. Start with initial prediction (mean for regression, log-odds for classification)
2. Calculate residuals (negative gradients of loss function)
3. Fit a tree to the residuals
4. Update predictions: add tree predictions × learning rate
5. Repeat for n estimators

**Key Differences from AdaBoost:**
| Aspect | AdaBoost | Gradient Boosting |
|--------|----------|-------------------|
| **Weight Update** | Sample weights | Fits to residuals |
| **Loss Function** | Exponential | Any differentiable loss |
| **Flexibility** | Limited | High (custom loss functions) |

### Loss Functions

**Regression:**
- **Squared Error**: Standard least squares
- **Absolute Error**: Robust to outliers
- **Huber**: Combination of both

**Classification:**
- **Deviance**: Logistic regression loss
- **Exponential**: Same as AdaBoost

---

## 🛠️ Key Libraries

```python
from sklearn.ensemble import GradientBoostingClassifier, GradientBoostingRegressor
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
```

---

## 💡 Tips

1. **Learning Rate**: Start with 0.1, reduce for better generalization
2. **N Estimators**: Use early stopping to find optimal number
3. **Max Depth**: Keep trees shallow (3-5 levels) to prevent overfitting
4. **Subsample**: Use < 1.0 for stochastic gradient boosting
5. **Feature Scaling**: Not required for tree-based methods

---

## 📊 Hyperparameters

| Hyperparameter | Description | Typical Values |
|----------------|-------------|----------------|
| `n_estimators` | Number of boosting stages | 100, 200, 500 |
| `learning_rate` | Shrinks contribution of each tree | 0.01, 0.1, 0.2 |
| `max_depth` | Maximum depth of trees | 3, 5, 7 |
| `min_samples_split` | Min samples to split internal node | 2, 5, 10 |
| `min_samples_leaf` | Min samples at leaf node | 1, 2, 4 |
| `subsample` | Fraction of samples for each tree | 0.8, 1.0 |
| `loss` | Loss function to optimize | 'deviance', 'exponential' |

---

## 🎯 Advantages & Disadvantages

### Advantages
- ✅ Highly accurate predictions
- ✅ Flexible (custom loss functions)
- ✅ Handles mixed data types well
- ✅ No feature scaling required
- ✅ Provides feature importance

### Disadvantages
- ❌ Requires careful tuning
- ❌ Can overfit easily
- ❌ Slower to train than Random Forest
- ❌ More hyperparameters to tune

---

## 📈 Ensemble Methods Comparison

| Method | Parallelizable | Bias | Variance | Speed |
|--------|---------------|------|----------|-------|
| **Random Forest** | Yes | Low | Very Low | Fast |
| **AdaBoost** | No | Very Low | Medium | Medium |
| **Gradient Boosting** | No | Very Low | Low | Slow |

---

## 🔗 Related Topics

- **Previous**: [Phase 6 - Classification & Ensembles](../Phase-6-Classification-Ensembles/README.md)
- **Next**: Neural Networks and Deep Learning

---

**Main README:** [Back to Overview](../README.md)
