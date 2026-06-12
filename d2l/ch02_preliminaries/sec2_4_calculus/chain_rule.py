import torch


def main():

    print("=== chain rule ===")

    # 1. Single-variable chain rule

    x = torch.tensor(2.0, requires_grad=True)

    u = x**2
    y = 3 * u + 1

    # y는 scalar이므로 backward()로 dy/dx를 계산할 수 있다.
    y.backward()

    # 수학적으로 직접 계산한 gradient
    manual_grad = 3 * 2 * x.detach()

    print("\n--- single-variable chain rule ---")
    print("x.detach().item() -> x: ", x.detach().item())
    print("u.detach().item() -> u = x^2: ", u.detach().item())
    print("y.detach().item() -> y = 3u + 1: ", y.detach().item())
    print("x.grad.item() -> x.grad: ", x.grad.item())
    print("manual_grad.item() -> manual dy/dx:", manual_grad.item())



    # 2. Multivariate chain rule
    
    # u = Bx + b
    # y = ||u||^2
    # y = u1^2 + u2^2 + u3^2
    B = torch.tensor(
        [
            [1.0, 2.0],
            [3.0, 4.0],
            [5.0, 6.0],
        ]
    )
    b = torch.tensor([0.5, -0.5, 1.0])
    x = torch.tensor([1.0, -1.0], requires_grad=True)
    u = B @ x + b
    y = (u**2).sum()

    # autograd가 chain rule을 이용해 dy/dx를 계산한다.
    y.backward()

    # dy/du = 2u
    # du/dx = B    
    # du/dx * dy/du = B.T @ (2u)
    manual_grad = B.T @ (2 * u.detach())
    
    print("\n--- multivariate chain rule ---")
    print("B shape:", B.shape)
    print("x shape:", x.shape)
    print("u shape:", u.shape)
    print("y shape:", y.shape)
    print("\nB:")
    print(B)
    print("\nx:", x.detach())
    print("b:", b)
    print("u = Bx + b:", u.detach())
    print("y = ||u||^2:", y.detach().item())
    print("\nx.grad:", x.grad)
    print("manual dy/dx:", manual_grad)
    

if __name__ == "__main__":
    main()
