import torch

# X[i]      -> axis 0에서 i번째 항목
# X[i, j]   -> i번째 행, j번째 열의 scalar
# X[a:b]    -> a 이상 b 미만 범위
# X[:2, :]  -> 앞의 두 행, 모든 열 

def main():
    
    x= torch.arange(12, dtype=torch.float32)
    X = x.reshape(3, 4)
    
    print("Original X = ")
    print(X)
    
    # X[-1]: axis 0 기준 마지막 행
    print("\nX[-1] = ")
    print(X[-1])
    
    # X[1:3]: axis 0 기준 1번 행부터 3번 행 직전까지
    # 즉, 두 번째 행과 세 번째 행
    print("\nX[1:3] =")
    print(X[1:3])
    
    # X[1, 2]: 1번 행, 2번 열의 scalar 원소
    # 행렬 관점에서는 X_{1, 2}
    print("\nBefore assignment, X[1, 2] = ", X[1, 2])
    
    X[1, 2] = 99
    print("\nAfter X[1, 2] = 99:", X[1, 2])
    print(X)
    
    # [:2, :]는 행 방향으로 0번, 1번 행 선택
    # 열 방향으로는 모든 열 선택
    X[:2, :] = 100
    print("\nAfter X[:2, :] = 10:")
    print(X)
    

    
if __name__ == "__main__":
    main()