# 01-Logistic-Regression

Classification algorithms for predicting categorical outcomes.

## Notebooks

- **58-logistic-regression-perceptron-trick.ipynb** - Logistic Regression with perceptron trick
- **60_softmax_regression.ipynb** - Softmax Regression for multi-class classification

## Key Concepts

### Sigmoid Function (Binary Classification)

```
σ(z) = 1 / (1 + e⁻ᶻ)
```

- Maps any real value to (0, 1)
- Used for binary classification
- Decision boundary at 0.5

### Softmax Function (Multi-class Classification)

```
σ(z)ᵢ = eᶻⁱ / Σⱼeᶻʲ
```

- Generalizes sigmoid to multiple classes
- Outputs probability distribution
- Sum of all class probabilities = 1

## Cost Function

**Log Loss (Binary Cross-Entropy):**
```
Cost = -[y×log(ŷ) + (1-y)×log(1-ŷ)]
```

## Decision Boundary

- **Default threshold**: 0.5
- Can be adjusted based on business requirements
- Trade-off between precision and recall
