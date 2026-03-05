# 02-Categorical-Encoding

Notebooks covering encoding techniques for categorical variables.

## Notebooks

- **26-ordinal-encoding.ipynb** - Encoding ordered categorical variables
- **27-one-hot-encoding.ipynb** - Encoding nominal categorical variables
- **28-column-transform.ipynb** - Applying multiple transformations with ColumnTransformer

## Techniques Covered

| Technique | Class | Use Case |
|-----------|-------|----------|
| Ordinal Encoding | `OrdinalEncoder` | Ordered categories (bad < poor < average < good < excellent) |
| One-Hot Encoding | `pd.get_dummies()` / `OneHotEncoder` | Nominal categories (red, blue, green) |
| ColumnTransformer | `ColumnTransformer` | Mixed preprocessing on different column types |

## Key Considerations

- Use **Ordinal Encoding** when categories have a natural order
- Use **One-Hot Encoding** when categories are nominal (no order)
- Set `handle_unknown='ignore'` to handle new categories in test data
- Use **ColumnTransformer** to apply different transformations to different columns in one step
