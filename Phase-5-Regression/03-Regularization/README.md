# 03-Regularization

Techniques to prevent overfitting in regression models.

## Notebooks

- **55-ridge-regression.ipynb** - Ridge Regression (L2 Regularization)
- **56-lasso-regression.ipynb** - Lasso Regression (L1 Regularization)

## Regularization Techniques

### Ridge Regression (L2)

**Cost Function:**
```
J(θ) = MSE(θ) + λ × Σθⱼ²
```

- Shrinks coefficients toward zero
- Never sets coefficients exactly to zero
- Good when many features have small effects

### Lasso Regression (L1)

**Cost Function:**
```
J(θ) = MSE(θ) + λ × Σ|θⱼ|
```

- Can set coefficients exactly to zero
- Performs automatic feature selection
- Good when only a few features are important

## Hyperparameter: λ (alpha)

| λ Value | Effect |
|---------|--------|
| **λ = 0** | No regularization (standard linear regression) |
| **λ too small** | May overfit |
| **λ too large** | May underfit |
| **λ optimal** | Good generalization |

## Comparison

| Aspect | Ridge | Lasso |
|--------|-------|-------|
| **Penalty Type** | L2 (squared) | L1 (absolute) |
| **Feature Selection** | No | Yes |
| **Solution** | Analytical | Numerical optimization |
| **When to Use** | Many small effects | Few important features |
