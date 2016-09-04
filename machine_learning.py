def split_data(data, prob):
  """split data into fractions[prob, 1 - prob]"""
  results = [], []
  for row in data:
    results[0 if random.random() < prob else 1]. append(row)
  return results 
  
def train_test_split(x, y, test_pct):
    data = zip(x, y)          #pair corresponding values
    train, test = split_data(data, 1 - test_pct)  #split the data set of pairs
    x_train, y_train = zip(*train)       #unzip
    x_test, y_test = zip(*test)
    return x_train, x_test, y_train, y_test


def accuracy(tp, fp, fn, tn): #true positive, false positive, false negative, true negative
  """fraction of correct predictions"""
  correct = tp + tn
  total = tp + fp + fn + tn
  return correct / total
  
def precision(tp, fp, fn, tn):
  """measures how accurate the positive predictions are"""
  return tp / (tp + fp)

def recall(tp, fp, fn, tn):
  """measures fraction of the positives successfully identified"""
  return tp / (tp + fn)

def f1_score(tp, fp, fn, tn):
  """harmonic mean of precision and recall; lies between them"""
  p = precision(tp, fp, fn, tn)
  r = recall(tp, fp, fn, tn)
  return 2 * p * r / (p + r)
