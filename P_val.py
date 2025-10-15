import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np
import scipy
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv("full_data.csv")


# Note: the larger the ChiSq value, the greater the probability that there is a significance difference.
# In other words, the greater the probability of accepting the alternative hypothesis (See below)

# H_0: the dataset follows the distribution (depending on distribution that have the lowest ChiSq value)
# H_1: the dataset does not follow the distribution
print("")
print("Null hypothesis: The data follows the distribution.")
print("Alternative hypothesis: The data does not follow the distribution.")
print("")

# P-value can be calculated using chi2.cdf('chi-sq value', 'degree of freedom')
# The degree of freedom is the length of the dataset minus 1


pval = 1 - stats.chi2.cdf(results['chi_square'].iat[0],(len(data)-1))
print("p-val:",pval)

print("")
# Conclusion:
# if p-value is greater than the significance level, then the null hypothesis cannot be rejected
# if pvalue is lower than the significance level, then reject the null hypothesis and take the alternative hypothesis H_1
if 0.05 < pval <= 1:
    print("Conclusion: The p-value is greater than the significance level, thus the data follows the distribution.")
elif pval > 1:
    print("Error, p-value greater than 1 can't occur")
else:
    print("Conclusion: The p-value is lower than the significance level, thus the data does not follow the distribution.")





