def split_data(data, prob):
  """split data into fractions[prob, 1 - prob]"""
  results = [], []
  for row in data:
    results[0 if random.random() < prob else 1]. append(row)
  return results 
  
def train_test_split(x, y, test_pct):
    data = zip(x, y)          #pair corresponding values
    train, test = split_data(data, 1 - test_pct)  #split the data set of pairs
    x_train, y_train = zipi(*train)       #unzip
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
  
