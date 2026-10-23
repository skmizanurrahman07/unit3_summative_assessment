# Linear Regression Findings Report

## 1. Overview

A multiple linear regression model was used to predict healthcare insurance
charges from the following five predictors:

- `Age`
- `BMI`
- `Smoker_num`
- `Children`
- `Region_num`

The model was trained using an 80/20 train-test split with
`random_state=42`. The results below are the performance and parameter
estimates reported for the test set.

## 2. Model results

| Measure | Result |
|---|---:|
| Intercept | -11,090.44 |
| Test-set R² score | 0.8068 |
| Variance explained | 80.68% |

The R² score of **0.8068** indicates that the model explains approximately
**80.68% of the variation in insurance charges** in the test data. The
remaining 19.32% is not explained by this model and may reflect non-linear
relationships, omitted variables, interactions, outliers, or random
variation.

## 3. Coefficient interpretation

The coefficients are aligned with the feature order used in the notebook:
`Age`, `BMI`, `Smoker_num`, `Children`, and `Region_num`.

| Predictor | Coefficient | Interpretation, holding other predictors constant |
|---|---:|---|
| Age | 248.88 | A one-unit increase in age is associated with an estimated increase of **248.88 charge units**. |
| BMI | 312.19 | A one-unit increase in BMI is associated with an estimated increase of **312.19 charge units**. |
| Smoker_num | 23,041.77 | A one-unit increase in the smoker indicator is associated with an estimated increase of **23,041.77 charge units**. This is the largest positive coefficient. |
| Children | 534.15 | An additional child is associated with an estimated increase of **534.15 charge units**. |
| Region_num | -236.34 | A one-unit increase in the numeric region code is associated with an estimated decrease of **236.34 charge units**. |

The coefficient for `Smoker_num` is substantially larger than the other
coefficients. This suggests that smoking status is the strongest linear
predictor of insurance charges in this model, consistent with the wider
analysis indicating that smokers tend to have considerably higher charges.

The positive coefficients for age, BMI, and number of children suggest that
increases in these variables are associated with higher predicted charges
when the other predictors remain unchanged.

The negative `Region_num` coefficient should be interpreted cautiously.
Region is represented by a numeric code, so the coefficient describes a
change between successive codes rather than a meaningful increase in
geographic region. If the regions are categorical, one-hot encoding would
usually provide a more appropriate interpretation.

## 4. Regression equation

Using the reported coefficients, the fitted model can be represented as:

```text
Predicted Charges =
    -11,090.44
    + (248.88 × Age)
    + (312.19 × BMI)
    + (23,041.77 × Smoker_num)
    + (534.15 × Children)
    - (236.34 × Region_num)
```

The intercept is the predicted charge when every predictor is zero. Because
an age of zero, a BMI of zero, and the encoded values used here may not
represent realistic policyholders, the intercept is primarily a mathematical
component of the regression equation rather than a practical customer
scenario.

## 5. Business implications

1. **Smoking status is the dominant linear driver.** The large positive
   coefficient indicates that smoker status has a major relationship with
   insurance charges.
2. **Age and BMI are meaningful cost indicators.** Both have positive
   coefficients, suggesting that older customers and customers with higher
   BMI tend to have higher estimated charges.
3. **Dependants have a comparatively smaller effect.** The children
   coefficient is positive but much smaller than the smoking coefficient.
4. **Geographic effects require careful encoding.** The region result should
   not be treated as an ordered geographic scale unless the numeric coding
   has a genuine ordinal meaning.
5. **The model is useful but not complete.** Explaining 80.68% of test-set
   variance indicates a reasonably strong baseline, but approximately
   one-fifth of the variation remains unexplained.

## 6. Limitations and recommended next steps

- The coefficients describe associations, not causal effects.
- Numeric encoding of categorical variables can create misleading linear
  interpretations, particularly for `Region_num`.
- The model assumes linear relationships and additive effects. Interactions,
  especially between smoking status and BMI or age, may be important.
- R² should be considered alongside MAE and RMSE before the model is used for
  operational decisions.
- Compare this baseline with the notebook's tree-based models, which can
  represent non-linear patterns and interactions more effectively.
- Validate the findings with cross-validation and inspect residuals for
  systematic errors and unequal variance.

## 7. Conclusion

The linear regression model provides a strong, interpretable baseline for
predicting healthcare insurance charges, achieving a test-set R² of
**0.8068**. Smoking status is the clearest cost driver in the fitted model,
while age, BMI, and number of children show positive associations with
charges. The results support the project hypothesis that these customer
characteristics influence insurance costs, while also showing why
categorical encoding, non-linearity, and model validation should be
considered before applying the findings to real-world pricing or healthcare
decisions.
