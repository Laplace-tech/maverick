import torch


def main():
    
    # x ∈ R^12: 1차원 텐서, 즉 벡터
    x = torch.arange(12, dtype=torch.float32)

    print("x =", x)
    print("x.numel() =", x.numel())
    print("x.shape =", x.shape)

    # X ∈ R^(3x4): 같은 원소 12개를 3행 4열로 해석
    X = x.reshape(3, 4)
    
    print("\nX = ")
    print(X)
    print("X.shape = ", X.shape)

    # reshape는 값을 바꾸지 않고 배치 구조만 바꾼다.
    print("\nx[3] = ", x[3])    
    print("X[0, 3] = ", X[0, 3])
    
    # -1은 해당 차원을 자동 계산하라는 의미
    print("\nx.reshape(-1, 4) =")
    print(x.reshape(-1, 4))
    
    print("\nx.reshape(3, -1) =")
    print(x.reshape(3, -1))
    
    # 3차 텐서: shape = (2, 3, 4), 원소 수 = 2x3x4
    zeros = torch.zeros((2, 3, 4))
    ones = torch.ones((2, 3, 4))
    
    print("\nzeros = ")
    print(zeros)
    print("zeros.shape = ", zeros.shape)
    print("zeros.numel() = ", zeros.numel())

    print("\nones = ")
    print(ones)
    
    # 각 원소를 표준정규분포 N(0, 1)에서 샘플링
    random_tensor = torch.randn(3, 4)
    
    print("\nrandom_tensor = ")
    print(random_tensor)
    
    A = torch.tensor([
        [2, 1, 4, 3],
        [1, 2, 3, 4],
        [5, 4, 3, 1]
    ])
    print("\nA = ")
    print(A)
    print("A.shape = ", A.shape)
    
    assert x.numel() == 12
    assert X.shape == torch.Size([3, 4])
    assert x[3] == X[0, 3]
    assert zeros.numel() == 24
    assert A.shape == torch.Size([3, 4])
    
    print("\nAll checks passed.")


if __name__ == "__main__":
    main()