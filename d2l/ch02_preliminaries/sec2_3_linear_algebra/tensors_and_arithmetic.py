import torch


def main():

    print("=== Higher-order Tensors ===")

    # 3차 텐서: T ∈ R^(2x3x4)
    T = torch.arange(24).reshape(2, 3, 4)

    print("T = ")
    print(T)
    print("T.shape = ", T.shape)

    print("\n=== Elementwise Arithmetic ===")

    # A, B ∈ R^(2x3)
    A = torch.arange(6, dtype=torch.float32).reshape(3, 2)
    B = A.clone()

    print("A = ")
    print(A)

    print("\nB = ")
    print(B)

    # elementwise addition: shape 유지
    print("\nA + B = ")
    print(A + B)

    # Hadamard product: 같은 위치의 원소끼리 곱
    print("\nA * B = ")
    print(A * B)

    print("\n=== Scalar and Tensor ===")

    a = 2
    X = torch.arange(24).reshape(2, 3, 4)

    print("a + X = ")
    print(a + X)

    print("\n(a * X).shape = ", (a * X).shape)


if __name__ == "__main__":
    main()
