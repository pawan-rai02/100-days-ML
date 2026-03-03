# 02-Gradient-Descent

Optimization algorithms for training machine learning models.

## Notebooks

- **51-gradient-descent.ipynb** - Introduction to Gradient Descent
- **51-02-gradient-descent.ipynb** - Gradient Descent implementation
- **52-Batch-Gradient-Descent.ipynb** - Batch Gradient Descent (uses all samples)
- **53-stochastic-GD.ipynb** - Stochastic Gradient Descent (uses one sample)

## Gradient Descent Variants

| Variant | Samples per Iteration | Convergence | Speed |
|---------|----------------------|-------------|-------|
| **Batch GD** | All training samples | Smooth, stable | Slow for large datasets |
| **Stochastic GD** | One sample | Noisy, erratic | Fast |
| **Mini-batch GD** | Small batch (e.g., 32, 64) | Balanced | Best of both |

## Key Parameters

- **Learning Rate (α)**: Controls step size
  - Too small → Slow convergence
  - Too large → May overshoot minimum
  
- **Iterations**: Number of passes through data
- **Convergence Threshold**: When to stop training

## Cost Function

**MSE for Linear Regression:**
```
J(θ) = (1/2n) × Σ(hθ(xᵢ) - yᵢ)²
```

**Update Rule:**
```
θⱼ := θⱼ - α × (∂J(θ)/∂θⱼ)
```
