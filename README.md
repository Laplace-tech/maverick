<p align="center">
  <img
    src="https://capsule-render.vercel.app/api?type=waving&color=0:050816,20:09203F,43:087E8B,67:7B2CBF,86:FF4D8D,100:FFB703&height=320&section=header&text=MAVERICK&fontSize=72&fontColor=F5FCFF&fontAlignY=35&animation=twinkling&desc=Charting%20the%20Deep%20Learning%20Frontier%20with%20PyTorch&descSize=19&descAlignY=58"
    width="100%"
    alt="Maverick project header"
  />
</p>

[Dive into Deep Learning](https://d2l.ai/)을 PyTorch로 직접 구현하며 정리한 학습 기록.
각 notebook은 코드를 직접 입력하고 실행하면서 tensor shape, training process, device 동작을 확인하는 방식으로 구성.

## Study progress

| Chapter | Topic | Progress |
|:---:|---|:---:|
| 1 | Introduction | Review later |
| 2 | Preliminaries | 2.1–2.6 done |
| 3 | Linear Neural Networks for Regression | Done |
| 4 | Linear Neural Networks for Classification | 4.1–4.6 done |
| 5 | Multilayer Perceptrons | Done |
| 6 | Builders' Guide | Done |
| 7 | Convolutional Neural Networks | Done |
| **8** | **Modern Convolutional Neural Networks** | **Next** |
| 9 | Recurrent Neural Networks | Planned |
| 10 | Modern Recurrent Neural Networks | Planned |
| 11 | Attention Mechanisms and Transformers | Planned |
| 12 | Optimization Algorithms | Planned |
| 13 | Computational Performance | Planned |
| 14 | Computer Vision | Planned |
| 15 | Natural Language Processing: Pretraining | Planned |
| 16 | Natural Language Processing: Applications | Milestone |
| 17 | Reinforcement Learning | Planned |
| 18 | Gaussian Processes | Planned |
| 19 | Hyperparameter Optimization | Target |
| 20 | Generative Adversarial Networks | Optional |
| 21 | Recommender Systems | Not planned |

## Repository layout

```text
src/
├── ch02_preliminaries/
├── ch03_linear_neural_networks_for_regression/
├── ch04_linear_neural_networks_for_classification/
├── ch05_multilayer_perceptrons/
├── ch06_builders_guide/
└── ch07_convolutional_neural_networks/
```

각 chapter 아래에 section별 directory를 두고, 하나의 notebook에서 하나의 학습 흐름을 다룸.

## Run locally

```bash
cd ~/projects/maverick
code .
```

VS Code에서 다음 kernel을 선택.

```text
Python (maverick .venv)
```

Project interpreter:

```text
/home/anna/projects/maverick/.venv/bin/python
```

Terminal에서 environment를 직접 사용할 때:

```bash
source .venv/bin/activate
python
```
