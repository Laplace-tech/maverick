from unicodedata import numeric

import torch


def f(x: torch.Tensor) -> torch.Tensor:
    # f(x) = 3x^2 - 4x
    return 3 * x**2 - 4 * x


def f_prime(x: torch.Tensor) -> torch.Tensor:
    # f'(x) = d/dx [3x^2 - 4x] = 6x - 4
    return 6 * x - 4


def main():

    print("=== derivatives ===")

    # scalar tensor
    # dtype=torch.float64를 쓰는 이유는 작은 h로 나눌 때 수치 오차를 줄이기 위해서다.
    x = torch.tensor(1.0, dtype=torch.float64)

    print("Numerical derivative by limit approximation")

    # h = 10^-1, 10^-2, ..., 10^-5
    # h가 0에 가까워질 수록 [f(x+h)-f(x)]/h 가 f'(x)에 가까워진다.
    for h in 10.0 ** torch.arange(-1, -10, -1, dtype=torch.float64):
        numerical_derivative = (f(x + h) - f(x)) / h
        print(
            f"h={h.item():.5f}, numerical derivative={numerical_derivative.item():.5f}"
        )

    # 정확한 도함수 값
    exact_derivative = f_prime(x)

    print()
    print(f"f(1) = {f(x).item():.5f}")
    print(f"f'(1) = {exact_derivative.item():.5f}")

    # shape 확인
    # scalar tensor의 shape은 torch.Size([])다.
    print("\nx.shape: ", x.shape)
    print("f(x).shape: ", f(x).shape)
    print("exact_derivative.shape: ", exact_derivative.shape)

    h = torch.tensor(1e-5, dtype=torch.float64)
    approx_derivative = (f(x + h) - f(x)) / h

    print("\napprox_derivatrive: ", approx_derivative)

    assert torch.isclose(
        approx_derivative,
        torch.tensor(2.0, dtype=torch.float64),
        atol=1e-4,
    )


if __name__ == "__main__":
    main()
