import torch

def main():
    x = torch.arange(4.0)
    x.requires_grad_(True)

    y = 2 * torch.dot(x, x)
    y.backward()

    print("x:", x)
    print("y:", y.item())
    print("x.grad:", x.grad)
    print("expected grad:", 4 * x)

if __name__ == "__main__":
    main()
