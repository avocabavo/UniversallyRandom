
import math
from matplotlib import pyplot as plt
from scipy import stats

dpi= 25
stdevs= 4
fin= 2 * dpi * stdevs + 1

xs= []
for i in range(fin):
  xs.append(i/dpi-stdevs)

def analyze(targets):
  datasets= {}
  for best_of in targets:
    ds= {'data': [best_of * stats.norm.cdf(x) ** (best_of - 1) * stats.norm.pdf(x) for x in xs]}
    datasets[best_of]= ds
    print('analyzing what happens when you take the best of {} random normal shots'.format(best_of))
    ds['mean']= sum([xs[i]*ds['data'][i] for i in range(fin)]) / dpi
    print('mean: ' + str(ds['mean']))
    ds['variance']= sum([(xs[i] - ds['mean'])**2 * ds['data'][i] for i in range(fin)]) / dpi
    ds['stdev']= ds['variance'] ** 0.5
    print('stdev: ' + str(ds['stdev']))
    ds['skewness']= sum([((xs[i] - ds['mean']) / ds['stdev']) ** 3 * ds['data'][i] for i in range(fin)]) / dpi
    print('skewness: ' + str(ds['skewness']))
    ds['kurtosis']= sum([((xs[i] - ds['mean']) / ds['stdev']) ** 4 * ds['data'][i] for i in range(fin)]) / dpi
    print('kurtosis: ' + str(ds['kurtosis']))
  return datasets

if __name__=='__main__':
  targets= list(range(1, 11))
  datasets= analyze(targets)

  fig, plots= plt.subplots(1, 2)
  for best_of in targets:
    plots[0].plot(xs, datasets[best_of]['data'])
  plots[1].plot(targets, [datasets[best_of]['mean'] for best_of in targets])
  plots[1].plot(targets, [math.log(best_of)/math.log(3) for best_of in targets])
  plt.show()
