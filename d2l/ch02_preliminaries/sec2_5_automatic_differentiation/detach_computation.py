import torch


def main():

    print("=== 2.5.3 Detaching Computation ===")

    # x = [0, 1, 2, 3]
    x = torch.arange(4.0, requires_grad=True)

    print("\n--- x ---")
    print("x: ", x)

    # 1. y = x * x
    # y는 x로부터 만들어졌으므로 Computational graph에 연결되어 있다.
    y = x * x

    print("\n--- y = x * x ---")
    print("y: ", y)
    print("y.requires_grad: ", y.requires_grad)

    # 2. u = y.detach()
    # u는 y와 값은 같지만, y가 x로부터 만들어졌다는 기록은 끊긴다.
    u = y.detach()

    print("\n--- u = y.detach() ---")
    print("u: ", u)
    print("u.requires_grad: ", u.requires_grad)

    # 3. z = u * x
    # u는 상수 취급된다.
    # 따라서 z = u * x 의 gradient는 u다.
    z = u * x

    print("\n--- z = u * x ---")
    print("z: ", z)
    print("z.sum(): ", z.sum())

    z.sum().backward()

    print("\n--- gradient with detach ---")
    print("x.grad: ", x.grad)
    print("expected u: ", u)

    assert torch.allclose(x.grad, u)



    # 4. 비교: detach를 안 쓰면 z = x^3이 된다.
    x.grad.zero_()
    
    y = x * x
    z_no_detach = y * x
    
    z_no_detach.sum().backward()
    
    expected_grad = 3 * x.detach() * x.detach()
    
    print("\n---gradient without detach ---")
    print("x.grad: ", x.grad)
    print("expected 3 * x^2: ", expected_grad)
    
    assert torch.allclose(x.grad, expected_grad)
    


if __name__ == "__main__":
    main()
