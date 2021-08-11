import numpy as np
import matplotlib
import scipy.special # to use with factorials

x = np.linspace(0.00001,100,1000,True)

matplotlib.rcParams.update({'font.size': 14, 'font.family': 'STIXGeneral', 'mathtext.fontset': 'stix'})
fig, axes = matplotlib.pyplot.subplots(figsize=(10,10))

axes.plot(x, np.ones(1000), 'r-', label="Constant")
axes.plot(x, np.log2(x), 'b:', label=r"$\log_2n$")
axes.plot(x, np.sqrt(x), 'c:', label=r"$\sqrt{n}$")
axes.plot(x, x, "g:", label=r"$n$")
axes.plot(x, x*np.log2(x), "k-", label=r"$n\log_2n$" ) # already numpy executes operations of arrays element-wise unlike MatLab
axes.plot(x, x**2, "m:", label=r"$n^2$")
axes.plot(x, (2*np.ones(1000))**x, "r--", label=r"$2^n$")
axes.plot(x, scipy.special.factorial(x), "b--", label=r"$n!$")
axes.legend(loc=0)
axes.set_xlim([-10,100])
axes.set_ylim([-10,100])
axes.axhline(0, color='black')
axes.axvline(0, color='black')
axes.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
axes.set_xlabel('Input size - n')
axes.set_ylabel('Number of operations - N')
axes.set_title('Common functions used in algorithm analysis')

fig.savefig("fig_1.svg")