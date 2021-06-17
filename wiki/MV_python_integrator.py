# -*- coding: utf-8 -*-


import sys
from py4j.java_gateway import JavaGateway, GatewayParameters, CallbackServerParameters

#Here you should replace 'model_file_name' with the name of the .py file containing your model (without .py)
import model_file_name

class SimulationWrapper(object):

	# constructor for Python
	def __init__(self, model):
		self.model = model

	# code to let multivesta initialize the simulator for a new simulation
	# that is, re-initialize the model to its initial state, and set the
	# new random seed
	def setSimulatorForNewSimulation(self, random_seed):
		self.model.setSimulatorForNewSimulation(random_seed)	
			#Here you should replace 'setSimulatorForNewSimulation(random_seed)' 
			# with a method of your model to 
			#- set the new nuovo random seed
			#- reset the status of the model to the initial one
			#

	# code to let multivesta ask the simulator to perform a step of simulation
	def performOneStepOfSimulation(self):
		self.model.one_step()
		#Here you should replace 'one_step()' with
		# your method to perform a step of simulation 

	# code to let multivesta ask the simulator to perform a
	# "whole simulation"
	# (i.e., until a stopping condition is found by the simulator)
	def performWholeSimulation(self):
		print('Not supported\n')

	# code to let multivesta ask the simulator the current simulated time
	def getTime(self):
		return float(self.model.getTime())
		#Here you should replace 'getTime()' with
		# your method to get the current simulation time 
		# (or number of simulation step)


	# code to let multivesta ask the simulator to return the value of the
	# specified observation in the current state of the simulation
	def rval(self, observation):
		return float(self.model.eval(observation))
		#Here you should replace 'eval(observation)' with
		# your method to evaluate an observation in the 
		# current simulation step 

	class Java:
		implements = ['vesta.python.IPythonSimulatorWrapper']


if __name__ == '__main__':
	porta = int(sys.argv[1])
	callback_porta = int(sys.argv[2])
	print('Python engine: expecting connection with java on port: '+str(porta)+' and callback connection on port '+str(callback_porta))
	gateway = JavaGateway(start_callback_server=True,gateway_parameters=GatewayParameters(port=porta),callback_server_parameters=CallbackServerParameters(port=callback_porta))
	
	#Here you should put any initialization code you need to create an instance of
	#your model_file_name class
	
	model=model_file_name.Model(put here your parameters)
	gateway.entry_point.playWithState(SimulationWrapper(model))