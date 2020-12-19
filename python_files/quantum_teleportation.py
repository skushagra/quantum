## Block 1
import qiskit
from qiskit import *
circuit = QuantumCircuit(3,3)
circuit.x(0)
circuit.barrier()
circuit.draw()
from qiskit.tools.visualization import plot_histogram
## Block 2
circuit.h(1)
circuit.cx(1,2)
circuit.draw()
## Block 3
circuit.cx(2,1)
circuit.h(0)
circuit.draw()
## Block 4
circuit.barrier()
circuit.measure([0,1],[0,1])
circuit.draw()
## Block 5
circuit.barrier()
circuit.cx(1,2)
circuit.cz(0,2)
circuit.draw()
## Block 5
circuit.measure(2,2)
circuit.draw()
## Block 6
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend =simulator, shots = 1024).result()
counts = result.get_counts()
plot_histogram(counts)
## Block 7
print(counts)