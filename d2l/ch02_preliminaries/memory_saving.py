import torch

def main():
    
    print("\n === 2.1.5 Saving Memory ===")
    
    X = torch.arange(12, dtype=torch.float32).reshape(3, 4)
    Y = torch.tensor([
        [2.0, 1, 4, 3],
        [1, 2, 3, 4],
        [4, 3, 2, 1],
    ])

    print("X =")
    print(X)

    print("\nY =")
    print(Y)
    
    # Y = Y + X는 새 텐서를 만들고 Y가 그 새 객체를 가리키게 한다.
    # -> 메모리 낭비
    before = id(Y)
    Y = Y + X
    print("\nid(Y) changed after Y = Y + X:", id(Y) == before)
    
    # in-place (1st) 
    # Z[:] = ... 는 이미 할당된 Z의 메모리에 값을 덮어쓴다.
    Z = torch.zeros_like(Y)
    before = id(Z)
    Z[:] = X + Y
    
    print("\nid(Z) preserved after Z[:] = X + Y:", id(Z) == before)
    
    # in-place (2nd) 
    # X += Y는 in-place update다.
    before = id(X)
    X += Y
    
    print("\nid(X) preserved after X += Y:", id(X) == before)
    
    print("\nX after in-place update =")
    print(X)
    

    
if __name__ == "__main__":
    main()