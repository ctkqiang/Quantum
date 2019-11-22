from blueqat import vqe
from blueqat.pauli import qubo_bit as qubit

the_supposed_simulation = -3*qubit(0) - 3*qubit(1) - 3*qubit(2) - 3*qubit(3) -3*qubit(4) +  2*qubit(0)*qubit(1)+2*qubit(0)*qubit(2)+2*qubit(0)*qubit(3)+2*qubit(0)*qubit(4)+2*qubit(1)*qubit(2)+2*qubit(1)*qubit(3)+2*qubit(1)*qubit(4)+2*qubit(2)*qubit(3)+2*qubit(2)*qubit(4)+2*qubit(3)*qubit(4)
print(the_supposed_simulation)
steps = 2
result = vqe.Vqe(vqe.QaoaAnsatz(the_supposed_simulation, steps)).run()
print(result.most_common(12))