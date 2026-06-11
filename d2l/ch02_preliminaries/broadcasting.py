import torch

def main():
    
    # a ∈ R^(3×1), b ∈ R^(1×2)
    a = torch.arange(3).reshape(3, 1)
    b = torch.arange(2).reshape(1, 2)
    
    print("a =")
    print(a)
    print("a.shape =", a.shape)

    print("\nb =")
    print(b)
    print("b.shape =", b.shape)
    
    # broadcasting:
    # a: (3, 1) -> (3, 2)
    # b: (1, 2) -> (3 ,2)
    print("\na + b = ")
    print(a + b)
    
    
if __name__ == "__main__":
    main()