import torch


def f(a):
    # a에서 시작해서 b를 만든다.
    b = a * 2

    # b의 크기가 1000 이상이 될 때까지 계속 2배 한다.
    # while문 조건도 tensor 값에 따라 결정된다.
    while b.norm() < 1000:
        b = b * 2

    # b의 부호에 따라 다른 branch를 탄다.
    if b.sum() > 0:
        c = b
    else:
        c = 100 * b

    return c


def check_case(a_value):

    # scalar tensor
    a = torch.tensor(a_value, requires_grad=True)

    # 실제 실행된 경로만 computational graph로 기록된다.
    d = f(a)

    # d는 scalar이므로 backward() 가능
    d.backward()

    # 이 함수는 특정 입력에 대해 d = k * a 꼴이 된다.
    # 그래서 gradient는 k이고, d / a 도 k 다.
    expected_grad = d.detach() / a.detach()

    print(f"\n--- case: a = {a_value} ---")
    print("d: ", d)
    print("a.grad: ", a.grad)
    print("d / a: ", expected_grad)

    assert torch.allclose(a.grad, expected_grad)


def main():

    print("=== 2.5.4 Gradients and Python Control Flow ===")

    # 양수 입력: if b.sum() > 0 branch를 탄다.
    check_case(3.0)

    # 음수 입력: else branch를 탄다.
    check_case(-3.0)


if __name__ == "__main__":
    main()
