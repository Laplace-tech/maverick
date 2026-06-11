from pathlib import Path

import pandas as pd
import torch


def main():

    # - Path(__file__): 현재 실행 중인 파이썬 스크립트 파일의 위치를 가져옴
    # - .resolve() 해당 파일의 위치를 컴퓨터의 절대 경로로 변환
    # - .parents[2]: 현재 파일 위치에서 상위 폴더로 3단계 거슬로 올라감
    # .parents[0]: /home/anna/projects/maverick/d2l/ch02_preliminaries/sec2_2_data_preprocessing
    # .parents[1]: /home/anna/projects/maverick/d2l/ch02_preliminaries
    # .parents[2]: /home/anna/projects/maverick/d2l

    # d2l/data/house_tiny.csv 생성

    # data_dir = /home/anna/projects/maverick/d2l/data
    data_dir = Path(__file__).resolve().parents[2] / "data"
    data_dir.mkdir(exist_ok=True)  # data라는 폴더가 이미 존재하더라도 OK

    # data_file = /home/anna/projects/maverick/d2l/data/house_tiny.csv
    data_file = data_dir / "house_tiny.csv"

    data_file.write_text(
        """NumRooms,RoofType,Price
NA,NA,127500
2,NA,106000
4,Slate,178100
NA,NA,140000""",
        encoding="utf-8",
    )

    # CSV -> pandas DataFrame
    data = pd.read_csv(data_file)

    print("Original data:")
    print(data)

    # inputs: feature matrix의 source
    # targets: 예측해야 할 target vector의 source
    inputs = data.iloc[:, 0:2]
    targets = data.iloc[:, 2]

    print("\nInputs before preprocessing:")
    print(inputs)

    print("\nTargets:")
    print(targets)

    # 범주형/문자열 변수 RoofType을 one-hot encoding
    # NaN도 하나의 category로 처리
    inputs = pd.get_dummies(inputs, dummy_na=True)

    print("Inputs after get_dummies:")
    print(inputs)

    # 수치형 결측값 NumRooms의 NaN을 평균값으로 대체
    inputs = inputs.fillna(inputs.mean())

    print("\nInputs after fillna(mean):")
    print(inputs)

    # DataFrame -> NumPy -> Tensor
    # X ∈ R^(4×3), y ∈ R^4
    X = torch.tensor(inputs.to_numpy(dtype=float))
    y = torch.tensor(targets.to_numpy(dtype=float))

    print("\nX tensor:")
    print(X)
    print("X.shape = ", X.shape)

    print("\ny tensor:")
    print(y)
    print("y.shape = ", y.shape)


if __name__ == "__main__":
    main()
