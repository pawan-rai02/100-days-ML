# 05-Boosting

**Day 66** | Adaptive Boosting (AdaBoost)

---

## 📋 Overview

This section introduces Boosting methods, specifically AdaBoost (Adaptive Boosting). Unlike bagging and random forests that build trees independently, boosting builds trees sequentially, with each tree learning from the mistakes of its predecessors.

---

## 📂 Notebooks

| Notebook | Description |
|----------|-------------|
| `66-adaboost-demo.ipynb` | Introduction to AdaBoost algorithm and implementation |

---

## 🎯 Learning Objectives

By the end of this section, you will be able to:
- ✅ Understand the Boosting paradigm vs Bagging
- ✅ Explain how AdaBoost works
- ✅ Implement AdaBoost classifiers
- ✅ Understand the concept of weighted samples
- ✅ Tune AdaBoost hyperparameters

---

## 🔑 Key Concepts

### Boosting vs Bagging

| Aspect | Bagging | Boosting |
|--------|---------|----------|
| **Tree Building** | Parallel (independent) | Sequential (dependent) |
| **Sample Weight** | Equal weight | Updated based on errors |
| **Goal** | Reduce variance | Reduce bias |
| **Overfitting** | Less prone | More prone if too many estimators |

### AdaBoost Algorithm

**How it works:**
1. Start with equal weights for all samples
2. Train a weak learner (typically decision stump)
3. Calculate weighted error rate
4. Calculate learner importance (alpha)
5. Update sample weights: increase for misclassified, decrease for correctly classified
6. Repeat for n estimators
7. Final prediction: weighted vote of all learners

**Key Formulas:**
```
Learner Weight (α) = ½ × ln((1 - error) / error)

Sample Weight Update: w_new = w_old × exp(-α × y × ŷ)
```

---

## 🛠️ Key Libraries

```python
from sklearn.ensemble import AdaBoostClassifier, AdaBoostRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
```

---

## 💡 Tips

1. **Weak Learners**: AdaBoost works best with simple models (decision stumps)
2. **Learning Rate**: Lower learning rate requires more estimators but can improve generalization
3. **Outliers**: AdaBoost is sensitive to outliers (they get high weights)
4. **Feature Scaling**: Not required for tree-based boosting
5. **N Estimators**: Start with 50-100, increase if underfitting

---

## 📊 Hyperparameters

| Hyperparameter | Description | Typical Values |
|----------------|-------------|----------------|
| `n_estimators` | Number of weak learners | 50, 100, 200 |
| `learning_rate` | Shrinks contribution of each learner | 0.1, 0.5, 1.0 |
| `algorithm` | Boosting algorithm | 'SAMME', 'SAMME.R' |
| `base_estimator` | Weak learner to use | DecisionTreeClassifier(max_depth=1) |

---

## 🎯 Advantages & Disadvantages

### Advantages
- ✅ Simple to implement
- ✅ Works with various types of weak learners
- ✅ Less prone to overfitting (with proper n_estimators)
- ✅ Good for binary classification

### Disadvantages
- ❌ Sensitive to noisy data and outliers
- ❌ Can overfit with too many estimators
- ❌ Slower to train than bagging
- ❌ Less effective on multi-class problems

---

## 🔗 Related Topics

- **Previous**: [Random Forest](../04-Random-Forest/README.md)
- **Next**: [Gradient Boosting](../../Phase-7-Advanced-Ensembles/README.md)

---

**Phase README:** [Back to Phase 6](../README.md)
