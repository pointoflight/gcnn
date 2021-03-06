import matplotlib.pyplot as plt
plt.switch_backend('agg')
import math


def plotSamples(datapoints, marker, label='', title=''):
	"""
	Given a vector of datapoints plots a 2-D graph with x-axis as epoch
	"""
	plt.plot(range(1, len(datapoints)+1), datapoints, marker, label=label)
	plt.title(title)
	plt.legend()
	
def plotMultiGraph(train_datapoints, val_datapoints, label1='sd', label2='sdfs', path='', name='train_val_err_vs_epoch', titles=[]):
	"""
	Given two epochs*n_p size matrix, generates n_p plots for each property.
	X-axis is epoch, Y-axis is mae
	
	"""
	data_shape = train_datapoints.shape
	# n_p is only valid if the number of properties are more than 1
	if len(data_shape) > 1:
		n_p = data_shape[1]
	else:
		n_p = 1
		train_datapoints = train_datapoints.reshape(-1,1)
		val_datapoints = val_datapoints.reshape(-1,1)
	num_columns = 2
	num_rows = math.ceil(n_p/num_columns)

	plt.figure()
	for i in range(n_p):
		# collect the valid datapoints in a vector
		train_values = train_datapoints[:,i]
		val_values = val_datapoints[:,i]
		plt.subplot(num_rows, num_columns, i+1)
		plotSamples(train_values, 'g-', label1, titles[i])
		plotSamples(val_values, 'r-.', label2, titles[i])
	plt.savefig(path + name + '.png')


def plotGraph(train_datapoints, val_datapoints, path='', name='train_val_err_avg_vs_epoch', label1='sdfsdf', label2='fff', title=''):
	"""
	Given two lists of length [epochs], plots them in one graph
	"""
	plt.figure()
	plotSamples(train_datapoints, 'g-', label=label1)
	plotSamples(val_datapoints, 'r-.', label=label2)
	plt.savefig(path + name + '.png')
