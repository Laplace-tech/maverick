# Maverick

[Dive into Deep Learning](https://d2l.ai/)의 PyTorch 실습 코드를 공부하고 기록하는 프로젝트입니다.

## 시작하기

의존성 설치:

```bash
uv sync
```

환경 확인:

```bash
uv run python scripts/verify_environment.py
```

Jupyter 실행:

```bash
uv run jupyter lab
```

실습 코드는 `notebooks/`에, 일반 Python 코드는 `src/`에 저장합니다.
데이터셋과 모델 가중치는 Git에 포함하지 않습니다.
