# Phase 5: Regression

**Days 48-56** | Predicting Continuous Values

---

## 📋 Overview

This phase covers regression algorithms, from Simple Linear Regression to advanced optimization techniques like Gradient Descent and regularization methods.

---

## 📂 Folder Structure

```
Phase-5-Regression/
├── 01-Linear-Regression/
│   ├── 48-simple-linear-reg.ipynb
│   └── 48-SLR-02.ipynb
├── 02-Gradient-Descent/
│   ├── 51-gradient-descent.ipynb
│   ├── 51-02-gradient-descent.ipynb
│   ├── 52-Batch-Gradient-Descent.ipynb
│   └── 53-stochastic-GD.ipynb
├── 03-Regularization/
│   ├── 55-ridge-regression.ipynb
│   └── 56-lasso-regression.ipynb
└── README.md
```

---

## 📚 Notebooks

### **01-Linear-Regression/**
| Notebook | Description |
|----------|-------------|
| `48-simple-linear-reg.ipynb` | Introduction to Simple Linear Regression |
| `48-SLR-02.ipynb` | SLR implementation practice |

### **02-Gradient-Descent/**
| Notebook | Description |
|----------|-------------|
| `51-gradient-descent.ipynb` | Understanding Gradient Descent algorithm |
| `51-02-gradient-descent.ipynb` | Gradient Descent implementation |
| `52-Batch-Gradient-Descent.ipynb` | Batch Gradient Descent optimization |
| `53-stochastic-GD.ipynb` | Stochastic Gradient Descent (SGD) |

### **03-Regularization/**
| Notebook | Description |
|----------|-------------|
| `55-ridge-regression.ipynb` | L2 Regularization (Ridge Regression) |
| `56-lasso-regression.ipynb` | L1 Regularization (Lasso Regression) |

---

## 🎯 Learning Objectives

By the end of this phase, you will be able to:
- ✅ Understand Simple Linear Regression
- ✅ Implement regression from scratch
- ✅ Understand cost functions and optimization
- ✅ Implement Gradient Descent algorithm
- ✅ Compare Batch vs. Stochastic Gradient Descent
- ✅ Understand overfitting and regularization
- ✅ Apply Ridge (L2) and Lasso (L1) regularization
- ✅ Choose appropriate regularization techniques

---

## 🔑 Key Concepts

### Simple Linear Regression

**Equation:** `y = mx + c` or `y = β₀ + β₁x`

- **m (β₁)**: Slope/Coefficient
- **c (β₀)**: Intercept/Bias

### Cost Function

**Mean Squared Error (MSE):**
```
MSE = (1/n) × Σ(yᵢ - ŷᵢ)²
```

### Gradient Descent

**Update Rule:**
```
θⱼ := θⱼ - α × (∂MSE/∂θⱼ)
```

| Variant | Description | Pros | Cons |
|---------|-------------|------|------|
| **Batch GD** | Uses all samples per iteration | Stable convergence | Slow for large datasets |
| **Stochastic GD** | Uses one sample per iteration | Fast, escapes local minima | Noisy convergence |
| **Mini-batch GD** | Uses small batch of samples | Balance of both | Requires tuning batch size |

### Regularization

| Type | Penalty | Formula | Use Case |
|------|---------|---------|----------|
| **Ridge (L2)** | Sum of squared coefficients | λ × Σβⱼ² | Reduces coefficient values |
| **Lasso (L1)** | Sum of absolute coefficients | λ × Σ\|βⱼ\| | Feature selection (sparse solutions) |

---

## 🛠️ Key Formulas

### Gradient Descent Parameters

- **Learning Rate (α)**: Step size for each iteration
- **Iterations**: Number of updates to coefficients
- **Convergence**: When cost function stops decreasing significantly

### Regularization Trade-off

- **High λ**: Underfitting (high bias)
- **Low λ**: Overfitting (high variance)
- **Optimal λ**: Balance between bias and variance

---

## 💡 Tips

1. Always scale features before applying regularization
2. Start with a small learning rate for Gradient Descent
3. Use learning curves to diagnose bias/variance
4. Lasso can perform feature selection by zeroing coefficients
5. Monitor cost function during training to ensure convergence

---

## 📊 Comparison: Ridge vs. Lasso

| Aspect | Ridge | Lasso |
|--------|-------|-------|
| **Penalty** | L2 (squared) | L1 (absolute) |
| **Feature Selection** | No | Yes |
| **When to Use** | Many small effects | Few important features |
| **Solution** | Closed form | Iterative optimization |

---

**Previous Phase:** [Phase 4 - Missing Values & Outliers](../Phase-4-Missing-Values-Outliers/README.md)  
**Next Phase:** [Phase 6 - Classification & Ensembles](../Phase-6-Classification-Ensembles/README.md)
