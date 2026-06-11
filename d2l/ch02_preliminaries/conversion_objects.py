from numpy import float32
import torch

def main():
    
    X = torch.arange(12, dtype=torch.float32).reshape(3, 4)

    # CPU tensor와 NumPy ndarray는 메모리를 공유한다.
    A = X.numpy()
    B = torch.from_numpy(A)
    
    print("type(A) = ", type(A))
    print("type(B) = ", type(B))
    
    print("\nA before change:")
    print(A)
    
    A[0, 0] = -999
    
    print("\nA after A[0, 0] = -999:")
    print(A)
    
    print("\nX also changed because memory is shared:")
    print(X)
    
    
    # size-1 tensor -> Python scalar
    scalar_tensor = torch.tensor([3.5])
    
    print("\nscalar_tensor =", scalar_tensor)
    print("scalar_tensor.item() =", scalar_tensor.item())
    print("float(scalar_tensor) =", float(scalar_tensor))
    print("int(scalar_tensor) =", int(scalar_tensor))
    
    
if __name__ == "__main__":
    main()