import torch


def main():
    
    x = torch.arange(12, dtype=torch.float32)
    X_view = x.reshape(3, 4)
    X_view[:2, :] = 12
    
    print("x after modifying X_view = ")
    print("x:", x)
    print("X_view: \n", X_view)
    
    # unary elementwise operation: f: R -> R
    # 각 원소 x_i에 대해 exp(x_i)를 계산한다.
    
    print("torch.exp(x) = ")
    print(torch.exp(X_view))
    
    # binary elementwise opeations: f: R X R -> R
    # 같은 위치의 원소끼리 연산한다.
    a = torch.tensor([1, 2, 4, 8])
    b = torch.tensor([2, 2, 2, 2])
    
    print("\na + b =", a + b)
    print("a - b =", a - b)
    print("a * b =", a * b)
    print("a / b =", a / b)
    print("a ** b =", a ** b) 
    
    # matrix tensors: X, Y ∈ R^(3x4)
    X = torch.arange(12, dtype=torch.float32).reshape(3, 4)
    Y = torch.tensor([
        [2.0, 1, 4, 3],
        [1, 2, 3, 4],
        [4, 3, 2, 1],
    ])
    
    print("\nX = ")
    print(X)
    
    print("\nY = ")
    print(Y)
    
    # dim = 0: 행 방향으로 이어 붙인다.
    # R^(3x4) + R^(3x4) -> R^(6x4)
    cat_dim0 = torch.cat((X, Y), dim=0)
    print("\ntorch.cat((X, Y), dim=0) = ")
    print(cat_dim0)
    
    # dim=1: 열 방향으로 이어 붙인다.
    # R^(3x4) + R^(3x4) -> R^(3x8)
    cat_dim1 = torch.cat((X, Y), dim=1)
    print("\ntorch.cat((X, Y), dim=1) = ")
    print(cat_dim1)
    
    # elementwise comparision
    # 각 위치의 원소가 같으면 True, 다르면 False
    print("\n X == Y =")
    print(X == Y)
    
    # sum: 모든 원소르 더해서 scalar tensor를 만든다.
    print("\nX.sum() = ")
    print(X.sum())
    
if __name__ == "__main__":
    main()