# Section A Import Statements
import qiskit
from qiskit import *
from qiskit.tools.visualization import plot_histogram
import matplotlib.pyplot as plt
import random
# Importing standard Qiskit libraries and configuring account
from qiskit import IBMQ
# Loading your IBM Q account(s)
IBMQ.load_account()

# Section B Classical Logic
isoc = 'Heads'
cc = ['Flip', 'Not Flip']
ui1 = input("Choose to 'Flip' or 'Not Flip' the coin. I choose to ")
ci1 = random.choice(cc)
if ci1 == 'Flip':
    isoc = 'Tales'
else:
    isoc = 'Heads'
    
if ui1 == 'Flip' and isoc == 'Heads':
    isoc = 'Tales'
elif ui1 == 'Flip' and isoc == 'Tales':
    isoc = 'Heads'     
else:
    isoc = isoc
ci2 = random.choice(cc)
if ci2 == 'Flip' and isoc=='Heads':
    isoc = 'Tales'
elif ci2=='Flip' and isoc=='Tales':
    isoc = 'Heads'
if isoc == 'Heads':
    i=0
else:
    i=1

# Section C Quantum Logic 
circuit = QuantumCircuit(i+1,i+1)
circuit.h(i)
circuit.x(i)
circuit.h(i)
circuit.measure([i],[i])
# circuit.draw()
provider = IBMQ.get_provider(hub='ibm-q')
device = provider.get_backend('ibmqx2')
result = execute(circuit, backend=backend, shots=1024).result()
counts = result.get_counts()
for i in counts:
    if int(i) !=0:
        print('Congrats, You made it')
    else:
        print('Sorry, the computer won.')
plot_histogram(counts)
