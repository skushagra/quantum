import qiskit
from qiskit import *
from qiskit.tools.visualization import plot_histogram
secretnumber = input("Enter Secret number")
circuit = QuantumCircuit(len(secretnumber)+1, len(secretnumber))
circuit.h(range(len(secretnumber)))
circuit.x(len(secretnumber))
circuit.h(len(secretnumber))
circuit.barrier()
for ii,yesno in enumerate(reversed(secretnumber)):
    if yesno == "1":
        circuit.cx(ii,len(secretnumber))
circuit.barrier()
circuit.h(range(len(secretnumber)))
circuit.barrier()
circuit.measure(range(len(secretnumber)), range(len(secretnumber)))
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend= simulator, shots=1).result()
counts = result.get_counts()
print(counts)
plot_histogram(counts)
