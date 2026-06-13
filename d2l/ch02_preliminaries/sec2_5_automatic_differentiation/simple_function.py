import torch


def main():

    print("=== automatic differentiation: a simple function ===")

    # 처음에는 gradient 추적이 꺼져 있다.
    x = torch.arange(4.0)

    print("\n=== initial tensor ===")
    print("x: ", x)
    print("x.shape: ", x.shape)
    print("x.dtype: ", x.dtype)
    print("x.requires_grad: ", x.requires_grad)
    print("x.grad: ", x.grad)

    # x에 대한 연산을 autograd가 추적하도록 설정한다.
    # 이제 x가 포함된 계산 그래프가 기록된다.
    x.requires_grad_(True)

    print("\n=== after requires_grad(True) ===")
    print("x.requires_grad: ", x.requires_grad)
    print("x.grad: ", x.grad)

    # 1. y = 2 * x^T x
    # torch.dot(x, x) = x^T x = sum_i x_i^2
    # y = 2 * x^T x
    y = 2 * torch.dot(x, x)

    print("\n=== y = 2 * torch.dot(x, x) ===")
    print("y: ", y)
    print("y.shape: ", y.shape)

    # y는 scalar이므로 backward()를 바로 호출할 수 있다.
    # dy/dx가 계산되어 x.grad에 저장된다.
    y.backward()

    # 수학적으로 y = 2x^T x 이므로 gradient는 4x다.
    expected_grad = 4 * x.detach()

    print("\n=== gradient of y = 2 * x^T x ===")
    print("x.grad: ", x.grad)
    print("expected 4 * x: ", expected_grad)
    print("x.grad == 4 * x: ", x.grad == 4 * x)

    # ========================
    # 2. Gradient buffer reset
    # ========================

    # PyTorch는 gradient를 자동으로 초기화하지 않는다.
    # 새 backward를 하기 전에 기존 gradient를 0으로 만든다.
    x.grad.zero_()

    print("\n=== after x.grad.zero_() ===")
    print("x.grad: ", x.grad)

    # ==============
    # 3. y = sum(x)
    # ==============

    # y = x_1 + x_2 + x_3 + x_4
    # 각 x_i에 대한 미분값은 모두 1이다.
    y = x.sum()
    
    print("\n=== y.sum() ===")
    print("y: ", y)
    print("y.shape: ", y.shape)

    y.backward()
    
    expected_grad = torch.ones_like(x)
    
    print("\n=== gradient of y = x.sum() ===")
    print("x.grad: ", x.grad)
    print("expected ones: ", expected_grad)
    
    print(f"x.grad.shape: {x.grad.shape}, x.shape: {x.shape}")


if __name__ == "__main__":
    main()
