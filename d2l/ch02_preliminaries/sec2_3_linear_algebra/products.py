import torch


def main():

    print("=== Dot Product === ")

    # x, y ∈ R^3
    x = torch.arange(3, dtype=torch.float32)
    y = torch.ones(3, dtype=torch.float32)

    print("x = ", x)
    print("y = ", y)

    # dot product
    print("\ntorch.dot(x, y) = ", torch.dot(x, y))
    print("torch.sum(x * y) = ", torch.sum(x * y))

    print("\n=== Matrix-Vector product ===")

    # A ∈ R^(2x3), x ∈ R^3
    A = torch.arange(6, dtype=torch.float32).reshape(2, 3)

    print("A = ")
    print(A)
    print("x = ", x)
    print("A.shape = ", A.shape)
    print("x.shape = ", x.shape)

    # Ax ∈ R^2
    print("\ntorch.mv(A, x) = ")
    print(torch.mv(A, x))

    print("\nA @ x =")
    print(A @ x)

    print("\n=== Matrix-Matrix Multiplication ===")

    # A ∈ R^(2x3), B ∈ R^(3x4)
    B = torch.ones(3, 4)

    print("B = ")
    print(B)
    print("B.shape = ", B.shape)

    # AB ∈ R^(2x4)
    print("\ntorch.mm(A, B) = ")
    print(torch.mm(A, B))

    print("\nA @ B = ")
    print(A @ B)

    print("=== Vector Norms ===")

    # u = [3, -4]
    u = torch.tensor([3.0, -4.0])

    print("u = ", u)

    # L2 norm: sqrt(3^2 + (-4)^2) = 5
    print("\nL2 norm:")
    print(torch.norm(u))

    # L1 norm: |3| + |-4| = 7
    print("\nL1 norm:")
    print(torch.norm(u))

    # Frobenius norm: 행렬 원소 전체를 벡터처럼 보고 L2 norm 계산
    M = torch.ones((4, 9))

    print("\nM.shape = ", M.shape)
    print("torch.norm(M) = ", torch.norm(M))


if __name__ == "__main__":
    main()
