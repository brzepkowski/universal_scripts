import numpy as np
import sys

def spin_1_2(J, L, D):
    print("J: ", J)
    print("L: ", L)
    print("D: ", D)
    # Two particles with spin S = 1/2

    I = np.array([[1, 0], [0, 1]])
    Sx = 0.5 * np.array([[0, 1], [1, 0]])
    Sy = 0.5 * np.array([[0, -1j], [1j, 0]])
    Sz = 0.5 * np.array([[1, 0], [0, -1]])
    Sz2 = Sz**2

    H = np.zeros([4, 4], dtype=np.complex)
    print("[0] H:")
    print(H)
    H -= J * (np.kron(Sx, I)*np.kron(I, Sx))
    print("[1] H:")
    print(H)
    H -= J * (np.kron(Sy, I)*np.kron(I, Sy))
    print("[2] H:")
    print(H)
    H -= J * (np.kron(Sz, I)*np.kron(I, Sz))
    print("[3] H:")
    print(H)

    H -= L * (np.kron(Sz, I)*np.kron(I, Sz))
    print("[4] H:")
    print(H)

    H -= D * np.kron(Sz2, I)
    H -= D * np.kron(I, Sz2)



    eigenvals, eigenvecs = np.linalg.eig(H)
    print("eigenvals: ", eigenvals)


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
        spin_1_2(J, L, D)
