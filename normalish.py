
import math
from matplotlib import pyplot as plt
from scipy import stats

dpi= 25
stdevs= 4
fin= 2 * dpi * stdevs + 1

if __name__=='__main__':
  xs= []
  for i in range(fin):
    xs.append(i/dpi-stdevs)

  datasets= {}
  for best_of in [1, 2]:
    ds= [best_of * stats.norm.cdf(x) ** (best_of - 1) * stats.norm.pdf(x) for x in xs]
    datasets[best_of]= ds
    print('analyzing what happens when you take the best of {} random normal shots'.format(best_of))
    mean= sum([xs[i]*ds[i] for i in range(fin)]) / dpi
    print('mean: ' + str(mean))
    variance= sum([(xs[i] - mean)**2 * ds[i] for i in range(fin)]) / dpi
    stdev= variance ** 0.5
    print('stdev: ' + str(stdev))
    skewness= sum([((xs[i] - mean) / stdev) ** 3 * ds[i] for i in range(fin)]) / dpi
    print('skewness: ' + str(skewness))
    kurtosis= sum([((xs[i] - mean) / stdev) ** 4 * ds[i] for i in range(fin)]) / dpi
    print('kurtosis: ' + str(kurtosis))



  p= plt.subplot()
  for key in datasets.keys():
    p.plot(xs, datasets[key])
  plt.show()
