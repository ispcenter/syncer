#0 imports
import os

#1 classes

class Computer:
  '''Any comp at network'''

  def __init__(self, netName,):
    self.netName = netName
    self.path = r'{}'.format(netName)

class Stend(Computer):
	'''Origin stend'''

	def __init__(self, netName):
		




server = Computer(r'Saukip')
stend1 = Computer(r'Arm_1')

#2 launch and work
os.chdir(stend1.path)
cwd = os.getcwd()
print(cwd)
print(os.listdir(cwd))