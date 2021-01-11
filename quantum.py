def circ(a,b):
    from qiskit import QuantumCircuit
    c= QuantumCircuit(a,b)
    return c
def plot(pt,counts):
    import qiskit
    from qiskit import *
    if pt == 'hist':
        from qiskit.tools.visualization import plot_histogram
        plot_histogram(counts)
    if pt == 'bloch_mv':
        from qiskit.tools.visualization import plot_bloch_multivector
        plot_bloch_multivector(counts)
def qreg(a):
    q  = QuantumRegister(a)
    return q
def creg(a):
    c = ClassicalRegister(a)
    return c
def circ():
    def exe(c, b, s):
        return execute(c, backend=b, shots=s).result()
