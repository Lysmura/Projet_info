from Outils.cartoplot import CartoPlot

cp = CartoPlot()

d = {}
d['Betagni'] = 1
fig = cp.plot_reg_map(data=d)
fig.show()
fig.savefig('regions.test.jpg')

# d = {}
# for i in range(1, 96):
#     d[str(i)] = i
# del(d['69'])
# d['69D'] = 69
# d['69M'] = 69
# d['2A'] = 20
# d['2B'] = 20.5
# fig = cp.plot_dep_map(data=d, x_lim=(-6, 10), y_lim=(41, 52))
# fig.show()
# fig.savefig('departements.test.jpg')