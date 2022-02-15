import pandas as pd
from numpy import mean
from numpy import std
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.ensemble import GradientBoostingClassifier

"""GradientBoosting classifier for loan default data"""

data = pd.read_csv("/Users/stephaniekim/downloads/TrainingData.csv")

print(data)
