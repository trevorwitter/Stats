def split_data(data, prob):
  """split data into fractions[prob, 1 - prob]"""
  results = [], []
  for row in data:
    results[0 if random.random() < prob else 1]. append(row)
  return results 
  
  
