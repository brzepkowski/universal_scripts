import numpy as np
from math import sqrt
import sys

def spin_model(J, L, D):
    print("J: ", J)
    print("L: ", L)
    print("D: ", D)
    # Two particles with spin S = 1/2

    # S = 1/2
    # I = np.array([[1, 0], [0, 1]])
    # Sx = 0.5 * np.array([[0, 1], [1, 0]])
    # Sy = 0.5 * np.array([[0, -1j], [1j, 0]])
    # Sz = 0.5 * np.array([[1, 0], [0, -1]])

    # S = 3/2
    I = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
    Sx = 0.5 * np.array([[0, sqrt(3), 0, 0], [sqrt(3), 0, 2, 0], [0, 2, 0, sqrt(3)], [0, 0, sqrt(3), 0]])
    Sy = (1 / (2*1j)) * np.array([[0, sqrt(3), 0, 0], [-sqrt(3), 0, 2, 0], [0, -2, 0, sqrt(3)], [0, 0, -sqrt(3), 0]])
    Sz = 0.5 * np.array([[3/2, 0, 0, 0], [0, 1/2, 0, 0], [0, 0, -1/2, 0], [0, 0, 0, -3/2]])

    Sx2 = Sx**2
    Sy2 = Sy**2
    Sz2 = Sz**2

    H = np.zeros([np.shape(I)[0]**2, np.shape(I)[1]**2], dtype=np.complex)

    H -= J * np.matmul(np.kron(Sx, I),np.kron(I, Sx))
    H -= J * np.matmul(np.kron(Sy, I), np.kron(I, Sy))
    H -= J * np.matmul(np.kron(Sz, I), np.kron(I, Sz))

    H -= L * np.matmul(np.kron(Sz, I), np.kron(I, Sz))

    H -= D * np.kron(Sz2, I)
    H -= D * np.kron(I, Sz2)

    # print("H:")
    # print(H)

    eigenvals, eigenvecs = np.linalg.eig(H)
    print("eigenvals: ", eigenvals)
    groundstate_index = 0
    min_energy = np.inf
    for i in range(len(eigenvals)):
        if eigenvals[i] < min_energy:
            min_energy = eigenvals[i]
            groundstate_index = i
    print("groundstate_index: ", groundstate_index)
    psi_groundstate = np.array(eigenvecs)[:, groundstate_index]
    # print("eigenvecs: ")
    # print(eigenvecs)
    # print("psi_groundstate: ", psi_groundstate)



    print("#"*10 + " Sx^2 " + "#"*10)
    Sx2_I = np.kron(Sx2, I)
    I_Sx2 = np.kron(I, Sx2)
    Sx2_Sx2 = np.matmul(Sx2_I, I_Sx2)
    expected_value = np.matmul(np.matmul(np.conj(psi_groundstate.T), Sx2_Sx2), psi_groundstate)
    print("Sx2_Sx2: ", expected_value)

    expected_value = np.matmul(np.matmul(np.conj(psi_groundstate.T), Sx2_I), psi_groundstate)
    print("Sx2_I: ", expected_value)

    expected_value = np.matmul(np.matmul(np.conj(psi_groundstate.T), I_Sx2), psi_groundstate)
    print("I_Sx2: ", expected_value)


    print("#"*10 + " Sx " + "#"*10)
    Sx_I = np.kron(Sx, I)
    I_Sx = np.kron(I, Sx)
    Sx_Sx = np.matmul(Sx_I, I_Sx)
    expected_value = np.matmul(np.matmul(np.conj(psi_groundstate.T), Sx_Sx), psi_groundstate)
    print("Sx_Sx: ", expected_value)

    expected_value = np.matmul(np.matmul(np.conj(psi_groundstate.T), Sx_I), psi_groundstate)
    print("Sx_I: ", expected_value)

    expected_value = np.matmul(np.matmul(np.conj(psi_groundstate.T), I_Sx), psi_groundstate)
    print("I_Sx: ", expected_value)



    print("#"*10 + " Sy^2 " + "#"*10)
    Sy2_I = np.kron(Sy2, I)
    I_Sy2 = np.kron(I, Sy2)
    Sy2_Sy2 = np.matmul(Sy2_I, I_Sy2)
    expected_value = np.matmul(np.matmul(np.conj(psi_groundstate.T), Sy2_Sy2), psi_groundstate)
    print("Sy2_Sy2: ", expected_value)

    expected_value = np.matmul(np.matmul(np.conj(psi_groundstate.T), Sy2_I), psi_groundstate)
    print("Sy2_I: ", expected_value)

    expected_value = np.matmul(np.matmul(np.conj(psi_groundstate.T), I_Sy2), psi_groundstate)
    print("I_Sy2: ", expected_value)


    print("#"*10 + " Sy " + "#"*10)
    Sy_I = np.kron(Sy, I)
    I_Sy = np.kron(I, Sy)
    Sy_Sy = np.matmul(Sy_I, I_Sy)
    expected_value = np.matmul(np.matmul(np.conj(psi_groundstate.T), Sy_Sy), psi_groundstate)
    print("Sy_Sy: ", expected_value)

    expected_value = np.matmul(np.matmul(np.conj(psi_groundstate.T), Sy_I), psi_groundstate)
    print("Sy_I: ", expected_value)

    expected_value = np.matmul(np.matmul(np.conj(psi_groundstate.T), I_Sy), psi_groundstate)
    print("I_Sy: ", expected_value)



    print("#"*10 + " Sz^2 " + "#"*10)
    Sz2_I = np.kron(Sz2, I)
    I_Sz2 = np.kron(I, Sz2)
    Sz2_Sz2 = np.matmul(Sz2_I, I_Sz2)
    expected_value = np.matmul(np.matmul(np.conj(psi_groundstate.T), Sz2_Sz2), psi_groundstate)
    print("Sz2_Sz2: ", expected_value)

    expected_value = np.matmul(np.matmul(np.conj(psi_groundstate.T), Sz2_I), psi_groundstate)
    print("Sz2_I: ", expected_value)

    expected_value = np.matmul(np.matmul(np.conj(psi_groundstate.T), I_Sz2), psi_groundstate)
    print("I_Sz2: ", expected_value)


    print("#"*10 + " Sz " + "#"*10)
    Sz_I = np.kron(Sz, I)
    I_Sz = np.kron(I, Sz)
    Sz_Sz = np.matmul(Sz_I, I_Sz)
    expected_value = np.matmul(np.matmul(np.conj(psi_groundstate.T), Sz_Sz), psi_groundstate)
    print("Sz_Sz: ", expected_value)

    expected_value = np.matmul(np.matmul(np.conj(psi_groundstate.T), Sz_I), psi_groundstate)
    print("Sz_I: ", expected_value)

    expected_value = np.matmul(np.matmul(np.conj(psi_groundstate.T), I_Sz), psi_groundstate)
    print("I_Sz: ", expected_value)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Wrong number of parameters! Provide them in the following fashion:")
        print("- J,")
        print("- L,")
        print("- D.")
        sys.exit()
    else:
        J = float(sys.argv[1])
        L = float(sys.argv[2])
        D = float(sys.argv[3])
        spin_model(J, L, D)
