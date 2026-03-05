# 02-Decision-Trees

Non-linear models that make decisions based on feature values.

## Notebook

- **61-decision-trees-over-under-fitting.ipynb** - Decision Trees and the bias-variance tradeoff

## Tree Structure

```
Root Node (entire dataset)
    ├── Internal Node (decision based on feature)
    │   ├── Leaf Node (final prediction)
    │   └── Internal Node
    │       └── Leaf Node
    └── Leaf Node
```

## Splitting Criteria

| Criterion | Description | Use Case |
|-----------|-------------|----------|
| **Gini Impurity** | Measures probability of incorrect classification | Classification (default) |
| **Entropy** | Measures disorder/uncertainty | Classification |
| **MSE** | Mean Squared Error reduction | Regression |

## Controlling Overfitting

| Parameter | Description | Effect |
|-----------|-------------|--------|
| **max_depth** | Maximum tree depth | Prevents deep trees |
| **min_samples_split** | Min samples to split a node | Prevents small splits |
| **min_samples_leaf** | Min samples in leaf nodes | Smooths predictions |
| **max_features** | Features to consider for split | Adds randomness |

## Bias-Variance Tradeoff

- **Shallow trees**: High bias, low variance (underfitting)
- **Deep trees**: Low bias, high variance (overfitting)
- **Optimal depth**: Balance between both
