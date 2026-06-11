import torch


def main():

    print("=== Scalars ===")

    # scalar: 0차 텐서, 원소 하나
    x = torch.tensor(3.0)
    y = torch.tensor(2.0)

    print("x + y =", x + y)
    print("x * y =", x * y)
    print("x / y =", x / y)
    print("x ** y =", x**y)

    print("\n=== Vectors ===")

    # vector: 1차 텐서, x ∈ R^3
    v = torch.arange(3)

    print("v = ", v)
    print("v[2] = ", v[2])
    print("len(v) = ", len(v))
    print("v.shape = ", v.shape)

    # matrix: 2차 텐서, A x ∈ R^(3x2)
    A = torch.arange(6).reshape(3, 2)

    print("A =")
    print(A)
    print("A.shape = ", A.shape)

    # transpose A x ∈ R^(3x2) -> A.T x ∈ R^(2x3)
    print("\nA.T = ")
    print(A.T)
    print("A.T.shape = ", A.T.shape)

    # symmetric matrix: A == A.T
    S = torch.tensor([
        [1, 2, 3],
        [2, 0, 4],
        [3, 4, 5],
    ])
    
    print("\nS =")
    print(S)

    print("\nS == S.T =")
    print(S == S.T)
    

if __name__ == "__main__":
    main()
