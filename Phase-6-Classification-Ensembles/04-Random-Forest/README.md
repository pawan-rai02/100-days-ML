# 04-Random-Forest

**Day 66** | Ensemble Learning with Random Forests

---

## 📋 Overview

This section introduces Random Forests, a powerful ensemble learning method that combines multiple decision trees to create a more robust and accurate model. You'll learn about bagging, feature randomness, out-of-bag scoring, and feature importance.

---

## 📂 Notebooks

| Notebook | Description |
|----------|-------------|
| `66-01-random-forest-demo.ipynb` | Introduction to Random Forest Classifier |
| `66-02-random-forest-demo.ipynb` | Random Forest implementation examples |
| `66-03-bagging-vs-randomForest.ipynb` | Comparing Bagging and Random Forest approaches |
| `66-04-code-example-rf.ipynb` | Practical code examples with Random Forest |
| `66-05-oob-score-demo.ipynb` | Understanding Out-of-Bag (OOB) scoring |
| `66-06-feature-importance-rf-dt.ipynb` | Feature importance comparison: Random Forest vs Decision Trees |

---

## 🎯 Learning Objectives

By the end of this section, you will be able to:
- ✅ Understand the Random Forest algorithm
- ✅ Explain the difference between Bagging and Random Forest
- ✅ Implement Random Forest classifiers and regressors
- ✅ Use Out-of-Bag (OOB) score for model validation
- ✅ Extract and interpret feature importance
- ✅ Tune Random Forest hyperparameters

---

## 🔑 Key Concepts

### Random Forest Algorithm

**How it works:**
1. **Bootstrap Sampling**: Create multiple subsets of data with replacement
2. **Feature Randomness**: At each split, consider only a random subset of features
3. **Tree Building**: Build a decision tree on each bootstrap sample
4. **Aggregation**: Combine predictions from all trees (voting for classification, averaging for regression)

### Bagging vs Random Forest

| Aspect | Bagging | Random Forest |
|--------|---------|---------------|
| **Data Sampling** | Bootstrap samples | Bootstrap samples |
| **Feature Selection** | All features considered | Random subset of features |
| **Tree Correlation** | Higher | Lower (more diverse) |
| **Variance Reduction** | Good | Better |

### Out-of-Bag (OOB) Score

- **Definition**: Error rate calculated on samples NOT used in training each tree
- **Purpose**: Internal validation without needing a separate validation set
- **Benefit**: Efficient use of data, especially with small datasets

**OOB Score Formula:**
```
OOB Score = 1 - (Number of OOB errors / Total OOB samples)
```

### Feature Importance

**How it's calculated:**
- **Gini Importance**: Total reduction in Gini impurity across all trees
- **Permutation Importance**: Decrease in model accuracy when feature values are shuffled

**Benefits:**
- Identifies most predictive features
- Helps with feature selection
- Provides model interpretability

---

## 🛠️ Key Libraries

```python
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
```

---

## 💡 Tips

1. **Number of Trees**: More trees generally improve performance but increase computation time
2. **Max Features**: 
   - Classification: `sqrt(n_features)` is a good default
   - Regression: `n_features // 3` is a good starting point
3. **Max Depth**: Control overfitting by limiting tree depth
4. **OOB Score**: Enable with `oob_score=True` for internal validation
5. **Feature Importance**: Use `.feature_importances_` attribute to extract importance scores
6. **Random State**: Set for reproducibility

---

## 📊 Hyperparameters

| Hyperparameter | Description | Typical Values |
|----------------|-------------|----------------|
| `n_estimators` | Number of trees in the forest | 100, 200, 500 |
| `max_features` | Number of features to consider at each split | 'sqrt', 'log2', int |
| `max_depth` | Maximum depth of each tree | None, 10, 20, 30 |
| `min_samples_split` | Minimum samples required to split a node | 2, 5, 10 |
| `min_samples_leaf` | Minimum samples required at leaf node | 1, 2, 4 |
| `bootstrap` | Whether to use bootstrap samples | True, False |
| `oob_score` | Whether to use OOB samples for validation | True, False |

---

## 🎯 Advantages & Disadvantages

### Advantages
- ✅ Reduces overfitting compared to single decision trees
- ✅ Works well with high-dimensional data
- ✅ Provides feature importance measures
- ✅ Handles missing values well
- ✅ Robust to outliers
- ✅ No need for feature scaling

### Disadvantages
- ❌ Slower to train and predict compared to single trees
- ❌ Less interpretable than individual decision trees
- ❌ Can overfit on noisy datasets
- ❌ Requires more memory

---

## 🔗 Related Topics

- **Previous**: [Ensemble Methods](../03-Ensemble-Methods/README.md)
- **Next**: [Gradient Boosting](../../Phase-7-Advanced-Topics/README.md) *(if available)*

---

**Phase README:** [Back to Phase 6](../README.md)
