# 03-Ensemble-Methods

Combining multiple models for better predictions.

## Notebooks

- **63-voting-ensemble.ipynb** - Voting Classifier for classification tasks
- **63_voting_regressor.ipynb** - Voting Regressor for regression tasks

## Voting Ensemble

### Hard Voting

- Each classifier votes for a class
- Final prediction = majority vote
- Use when classifiers are confident

### Soft Voting

- Each classifier provides probability estimates
- Final prediction = weighted average of probabilities
- Often outperforms hard voting

## Voting Regressor

- Averages predictions from multiple regressors
- Reduces variance and improves generalization

## Benefits of Ensembles

| Benefit | Description |
|---------|-------------|
| **Reduced Variance** | Averages out individual model errors |
| **Improved Accuracy** | Combines strengths of different models |
| **Robustness** | Less sensitive to noise |
| **Diversity** | Different models capture different patterns |

## Best Practices

1. **Use diverse models** - Different algorithms work better together
2. **Balance ensemble size** - More isn't always better
3. **Consider model weights** - Weight better models higher
4. **Check individual performance** - Ensure all models perform reasonably

## Example Combination

```python
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

voting_clf = VotingClassifier(
    estimators=[
        ('lr', LogisticRegression()),
        ('dt', DecisionTreeClassifier()),
        ('svc', SVC(probability=True))
    ],
    voting='soft'  # or 'hard'
)
```
