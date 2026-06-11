from matplotlib import axis
import torch


def main():

    print("=== Reduction ===")

    # vector: 1차 텐서, x ∈ R^3
    x = torch.arange(3, dtype=torch.float32)

    print("x = ", x)
    print("x.sum() = ", x.sum())

    # matrix: 2차 텐서, A ∈ R^(2x3)
    A = torch.arange(6, dtype=torch.float32).reshape(2, 3)

    print("\nA = ")
    print(A)
    print("A.shape = ", A.shape)

    # 모든 axis를 줄여 scalar 생성
    print("\nA.sum() = ", A.sum())

    # axis=0: 행 방향으로 누적해서 행 axis 제거
    print("\nA.sum(axis=0) = ")
    print(A.sum(axis=0))
    print("shape = ", A.sum(axis=0).shape)

    # axis=1: 열 방향으로 누적해서 column axis 제거
    print("\nA.sum(axis=1) = ")
    print(A.sum(axis=1))
    print("shape = ", A.sum(axis=1).shape)

    print("\nA.sum(axis=[0, 1]) == A.sum()")
    print(A.sum(axis=[0, 1]) == A.sum())

    print("\nA.mean() = ", A.mean())
    print("A.sum() / A.numel() = ", A.sum() / A.numel())

    print(A)

    # 행 방향으로 누적 후 평균
    print("\nA.mean(axis=0) = ")
    print(A.mean(axis=0))

    print("\nA.sum(axis=0) / A.shape[0] = ")
    print(A.sum(axis=0) / A.shape[0])

    # keepdims=True: axis 수 유지 (자기 행의 합 구하기)
    sum_A = A.sum(axis=1, keepdims=True)

    print("\nsum_A = ")
    print(sum_A)
    print("sum_A.shape = ", sum_A.shape)

    # broadcasting으로 각 행을 자기 행의 합으로 나눔
    print("\nA / sum_A = ")
    print(A / sum_A)

    # cumsum은 축을 줄이지 않는다.
    print("\nA.cumsum(axis=0) = ")
    print(A.cumsum(axis=0))


if __name__ == "__main__":
    main()
