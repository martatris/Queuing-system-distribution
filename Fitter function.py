import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np
import scipy
import warnings
from fitter import Fitter, get_common_distributions, get_distributions
warnings.filterwarnings("ignore")

#data = pd.read_csv("/Users/tristonmarta/Desktop/VUW/2023/Trimester 1/DATA474/Project/Report 3/full_data.csv")
data = pd.read_csv("full_data.csv")

from fitter import Fitter, get_common_distributions, get_distributions

data.info()
# saving the values in a variable
systemVa = data.iloc[:,3]
f = Fitter(systemVa, distributions=['gamma',
                                    'norm',
                                    'beta',
                                    'erlang',
                                    'lognorm'])
f.fit()
print(f.summary())
print("")
print(f.get_best(method = 'sumsquare_error'))

print(get_distributions())















