import torch


def main():
    print("=== 2.5.2 Backward for Non-Scalar Variables ===")

    # x = [0, 1, 2, 3]
    # x에 대한 gradient를 계산하기 위해 requires_grad=True로 둔다.
    x = torch.arange(4.0, requires_grad=True)

    print("\n--- x ---")
    print("x:", x)
    print("x.shape:", x.shape)

    # 1. y = x * x
    # x = [0, 1, 2, 3]
    # y = [0, 1, 4, 9]
    y = x * x

    print("\n--- y = x * x ---")
    print("y:", y)
    print("y.shape:", y.shape)

    # 2. vector y에 대해 y.backward()는 불가능하다.
    error_happened = False

    try:
        y.backward()
    except RuntimeError as error:
        error_happened = True
        print("\n--- expected error ---")
        print(type(error).__name__)
        print(str(error).splitlines()[0])

    assert error_happened is True

    # 3. y.sum()으로 scalar를 만든 뒤 backward()

    # 위에서 실패한 backward 이후, 깔끔하게 재계산
    y = x * x

    # z는 scalar
    # z = y.sum() = x_1^2 + x_2^2 + x_3^2 + x_4^2
    z = y.sum()

    print("\n--- z = y.sum() ---")
    print("z:", z)
    print("z.shape:", z.shape)

    # z는 scalar이므로 backward() 가능
    z.backward()

    # z = x_1^2 + x_2^2 + x_3^2 + x_4^2
    # dz/dx = [2x_1, 2x_2, 2x_3, 2x_4]
    expected_grad = 2 * x.detach()

    print("\n--- gradient ---")
    print("x.grad:", x.grad)
    print("expected 2 * x:", expected_grad)

    assert torch.allclose(x.grad, expected_grad)

    print("\nAll checks passed.")


if __name__ == "__main__":
    main()