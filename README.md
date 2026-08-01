<p align="center">
  <img
    src="https://capsule-render.vercel.app/api?type=waving&color=0:050816,20:09203F,43:087E8B,67:7B2CBF,86:FF4D8D,100:FFB703&height=320&section=header&text=MAVERICK&fontSize=72&fontColor=F5FCFF&fontAlignY=35&animation=twinkling&desc=Charting%20the%20Deep%20Learning%20Frontier%20with%20PyTorch&descSize=19&descAlignY=58"
    width="100%"
    alt="Maverick project header"
  />
</p>

<div align="center">

### Dive into Deep Learning · Source-faithful PyTorch Practice

직접 입력하고, 실행하고, Tensor shape과 device를 확인하며 쌓아가는 Deep Learning 항해 기록

</div>

## Voyage Map

| Chapter | Topic | Status |
|:---:|---|---|
| 1 | Introduction | Review backlog |
| 2 | Preliminaries | 2.1–2.6 complete · 2.7 deferred |
| 3 | Linear Neural Networks for Regression | Complete |
| 4 | Linear Neural Networks for Classification | 4.1–4.6 complete · 4.7 skipped |
| 5 | Multilayer Perceptrons | Complete |
| 6 | Builders' Guide | Complete |
| 7 | Convolutional Neural Networks | **Complete** |
| 8 | Modern Convolutional Neural Networks | **Next** |
| 9 | Recurrent Neural Networks | Planned |
| 10 | Modern Recurrent Neural Networks | Planned |
| 11 | Attention Mechanisms and Transformers | Planned |
| 12 | Optimization Algorithms | Planned |
| 13 | Computational Performance | Planned |
| 14 | Computer Vision | Planned |
| 15 | Natural Language Processing: Pretraining | Planned |
| 16 | Natural Language Processing: Applications | Required milestone |
| 17 | Reinforcement Learning | Planned |
| 18 | Gaussian Processes | Planned |
| 19 | Hyperparameter Optimization | Target |
| 20 | Generative Adversarial Networks | Optional |
| 21 | Recommender Systems | Excluded |

## Reference notebooks

- [Automatic Differentiation](https://github.com/Laplace-tech/maverick/blob/main/src/ch02_preliminaries/sec2_5_automatic_differentiation/01_a_simple_function.ipynb)
- [Weight Decay](https://github.com/Laplace-tech/maverick/blob/main/src/ch03_linear_neural_networks_for_regression/sec3_7_weight_decay/01_weight_decay_from_scratch.ipynb)

## Launch in VS Code

```bash
cd ~/projects/maverick
code .
```

Notebook 오른쪽 위에서 다음 kernel을 선택한다.

```text
Python (maverick .venv)
```

Project interpreter:

```text
/home/anna/projects/maverick/.venv/bin/python
```

Terminal session이 필요할 때:

```bash
source .venv/bin/activate
python
```

Notebook이 `Python (maverick .venv)` kernel에 연결되어 있다면 cell 실행만을 위해 Terminal에서 별도로 environment를 활성화할 필요는 없다.
