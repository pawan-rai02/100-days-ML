# 01-Feature-Scaling

Notebooks covering feature scaling techniques for numerical data.

## Notebooks

- **24-feature-scaling.ipynb** - Introduction to feature scaling with StandardScaler
- **24-feature-scaling-practice.ipynb** - Hands-on practice with breast cancer dataset
- **25-featureScale-normalization.ipynb** - Min-Max normalization technique

## Techniques Covered

| Technique | Class | Range |
|-----------|-------|-------|
| Standardization | `StandardScaler` | No fixed range |
| Normalization | `MinMaxScaler` | [0, 1] |

## When to Use

- **Standardization**: Most ML algorithms, especially distance-based (KNN, SVM, K-Means)
- **Normalization**: Neural networks, image processing, when bounds are important
