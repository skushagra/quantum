# For a n-bit input it results a n-bit 0 output. 
# Regardless of the n-bit input it will return a n-bit 0 output.
import qiskit
from qiskit import *
import matplotlib
i = input()
circuit = QuantumCircuit(len(i), len(i))
for j in range(0,len(i)):
    circuit.h(i)
for j in range(0,len(i)):
    circuit.x(0)
    circuit.x(len(i))
for j in range(1,len(i)-1,2):
    circuit.cx(i,i+1)
for j in range(0,len(i)):
    circuit.h(i)
circuit.draw(output='mpl')
