import torch

def main():
    x = torch.arange(12, dtype=torch.float32)
    print("x:", x)
    print("shape:", x.shape)
    print("reshape:", x.reshape(3, 4))

    y = torch.ones((3, 4))
    print("x reshaped + y:")
    print(x.reshape(3, 4) + y)

    print("cuda available:", torch.cuda.is_available())
    if torch.cuda.is_available():
        device = torch.device("cuda")
        z = y.to(device)
        print("device:", z.device)

if __name__ == "__main__":
    main()
