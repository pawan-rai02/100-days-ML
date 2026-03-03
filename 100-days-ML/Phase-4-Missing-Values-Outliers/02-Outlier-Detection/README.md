# 02-Outlier-Detection

Techniques for detecting and treating outliers in data.

## Notebooks

- **42-outlier-detection-removal.ipynb** - Identifying and removing outliers
- **43-outlier-IQR-capping.ipynb** - Interquartile Range (IQR) based capping/winsorization
- **44-outlier-percentile.ipynb** - Percentile-based outlier treatment

## Methods Covered

| Method | Formula | Use Case |
|--------|---------|----------|
| **IQR Method** | Lower: Q1 - 1.5×IQR, Upper: Q3 + 1.5×IQR | Skewed distributions |
| **Percentile Capping** | Cap at 1st and 99th percentile | Any distribution |
| **Z-Score** | Values beyond ±3 standard deviations | Normal distributions |

## Treatment Options

1. **Removal** - Delete outlier rows (if errors)
2. **Capping/Winsorization** - Cap at threshold values
3. **Transformation** - Apply log/sqrt to reduce impact
4. **Binning** - Group into bins to minimize effect
