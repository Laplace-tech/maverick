from importlib.metadata import requires

import torch

# Derivative는 변수 하나짜리 함수의 순간 변화율
# Partial derivative는 다변수 함수에서 특정 변수 하나만 움직였을 때의 변화율
#
# 딥러닝으로 연결하면
# - loss = f(parameters)
# - gradient = 각 parameter를 바꾸면 loss가 얼마나 변하는지 모아둔 값


def scalar_function(x: torch.Tensor) -> torch.Tensor:
    # f(x1, x2) = x1^2 + 2x1x2 + 3x2^2
    # 입력은 vector지만 출력은 scalar다
    x1 = x[0]
    x2 = x[1]
    return x1**2 + 2 * x1 * x2 + 3 * x2**2


def main():

    print("=== partial derivatives and gradients ===")

    # x= [x1, x2]
    # requires_grad=True는 이 tensor에 대한 gradient를 추적하겠다는 뜻이다.
    x = torch.tensor([1.0, 2.0], requires_grad=True)
    y = scalar_function(x)

    # y는 scalar이므로 backward()를 호출하면 x에 대한 gradient가 계산된다.
    y.backward()

    # 직접 계산:
    # f(x1, x2) = x1^2 + 2x1x2 + 3x2^2
    # ∂f/∂x1 = 2x1 + 2x2
    # ∂f/∂x2 = 2x1 + 6x2
    expected_grad = torch.tensor(
        [
            2 * x.detach()[0] + 2 * x.detach()[1],
            2 * x.detach()[0] + 6 * x.detach()[1],
        ]
    )

    print("--- scalar function ---")
    print("x.detach(): ", x.detach())
    print("y.item(): ", y.item())
    print("x.grad: ", x.grad)
    print("expected grad: ", expected_grad)

    print("\nx.shape: ", x.shape)
    print("y.shape: ", y.shape)
    print("x.grad.shape: ", x.shape)
    print(f"x.grad: {x.grad}, expected_grad: {expected_grad}")

    print("\n=== Gradient of ||x||^2 ===")

    # 새 gradient 계산를 위해 tensor를 새로 만든다.
    v = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
    print("v: ", v)

    # y = v1^2 + v2^2 + v3^2 = ||v||^2
    squared_norm = (v**2).sum()

    # Gradient 게산
    squared_norm.backward()

    # ∇ ||v||^2 = 2v
    expected_v_grad = 2 * v.detach()

    print("\n---gradient of squared norm ---")
    print("v.detach(): ", v.detach())
    print("||v||^2 squared_norm: ", squared_norm.item())
    print(f"v.grad.shape: {v.grad.shape}, v.shape: {v.shape}")
    print(f"v.grad: {v.grad}, expected_v_grad: {expected_v_grad}")

    print("=== Gradient of Frobenius norm ||X||_F^2 ===")

    X = torch.tensor(
        [
            [1.0, 2.0],
            [3.0, 4.0],
        ],
        requires_grad=True,
    )

    # y = sum of all squared entries = ||X||_F^2
    frobenius_squared = (X**2).sum()

    # Gradient 계산
    frobenius_squared.backward()

    # ∇ ||X||_F^2 = 2X
    expected_X_grad = 2 * X.detach()

    print("\n--- gradient of Frobenius norm squared ---")
    print("X:")
    print(X.detach())

    print("||X||_F^2:", frobenius_squared.item())

    print("X.grad:")
    print(X.grad)

    print("expected grad:")
    print(expected_X_grad)

    print("\nX.shape: ", X.shape)
    print("frobenius_squared.shape: ", frobenius_squared.shape)
    print(f"X.grad.shape: {X.grad.shape}, X.shape: {X.shape}")
    print(f"X.grad: \n{X.grad}, \nexpected_X_grad: \n{expected_X_grad}")


if __name__ == "__main__":
    main()
