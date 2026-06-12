from pathlib import Path

import torch
from matplotlib import pyplot as plt


def f(x: torch.Tensor) -> torch.Tensor:
    # f(x) = 3x^2 - 4x
    return 3 * x**2 - 4 * x


def main():

    print("=== visualization ===")

    # 0 이상 3 미만까지 0.1 간격으로 점을 만든다.
    x = torch.arange(0, 3, 0.1)

    # 함수값 f(x)를 계산한다.
    y = f(x)

    # x = 1 에서의 접선
    tangent = 2 * x - 3

    # 값 확인
    # f(1) = -1
    # 접선도 x=1에서 f(x)와 같은 값 -1을 가져야 한다.
    x_one = torch.tensor(1.0)
    f_at_one = f(x_one)
    tangent_at_one = 2 * x_one - 3

    assert torch.isclose(f_at_one, torch.tensor(-1.0))
    assert torch.isclose(tangent_at_one, torch.tensor(-1.0))

    # 그래프 생성
    plt.figure(figsize=(5, 3.5))

    # 원래 함수 그래프
    plt.plot(x, y, label="f(x) = 3x^2 - 4x")

    # x = 1에서의 접선
    plt.plot(x, tangent, "--", label="Tangent line at x=1")

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()

    # 그래프를 파일로 저장한다.
    output_dir = Path("d2l/assets")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / "calculus_tangent_line.png"
    plt.savefig(output_path, dpi=160, bbox_inches="tight")
    plt.close()

    print(f"\nx shape: {x.shape}")
    print(f"y shape: {y.shape}")
    print(f"tangent shape: {tangent.shape}")
    print("\nx.ndim: ", x.ndim)
    print("y.ndim: ", y.ndim)
    print("tangent.ndim: ", tangent.ndim)
    print(f"\nf(1): {f_at_one.item():.5f}")
    print(f"tangent at x=1: {tangent_at_one.item():.5f}")
    print(f"Saved figure to: {output_path}")


if __name__ == "__main__":
    main()
