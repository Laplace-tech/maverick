<p align="center">
  <img
    src="https://capsule-render.vercel.app/api?type=waving&color=0:050816,20:09203F,43:087E8B,67:7B2CBF,86:FF4D8D,100:FFB703&height=300&section=header&text=MAVERICK&fontSize=72&fontColor=F5FCFF&fontAlignY=35&animation=twinkling&desc=Charting%20the%20Deep%20Learning%20Frontier%20with%20PyTorch&descSize=19&descAlignY=58"
    width="100%"
    alt="Maverick project header"
  />
</p>

<div align="center">

<a href="https://d2l.ai/">
  <img
    src="./assets/d2l-cover.jpg"
    width="250"
    alt="Dive into Deep Learning book cover"
  />
</a>

### Dive into Deep Learning · Source-faithful PyTorch Practice

교재의 수식과 알고리즘을 PyTorch notebook으로 직접 구현하고,
Tensor shape, data flow, training behavior를 실행하며 검증한 학습 기록.

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![Notebooks](https://img.shields.io/badge/Notebooks-159-087E8B)
![Progress](https://img.shields.io/badge/Chapters_1--11-Done-7B2CBF)

</div>

## About

Maverick은 [Dive into Deep Learning](https://d2l.ai/)의 수식과 알고리즘을
PyTorch로 직접 구현한 학습 기록이다. From-scratch와 framework implementation을
비교하고, Tensor shape와 training result를 notebook에 검증·보존한다.

## Selected implementations

| Topic | Notebook | Focus |
|---|---|---|
| Automatic Differentiation | [A Simple Function](src/ch02_preliminaries/sec2_5_automatic_differentiation/01_a_simple_function.ipynb) | Computation graph와 gradient |
| Linear Regression | [Concise Linear Regression](src/ch03_linear_neural_networks_for_regression/sec3_5_concise_implementation_of_linear_regression/01_concise_linear_regression.ipynb) | Model, loss, optimizer, training loop |
| Softmax & Cross-Entropy | [Softmax Revisited](src/ch04_linear_neural_networks_for_classification/sec4_5_concise_softmax_regression/02_softmax_revisited.ipynb) | Stable probability와 loss computation |
| Multilayer Perceptron | [MLP from Scratch](src/ch05_multilayer_perceptrons/sec5_2_implementation_of_multilayer_perceptrons/01_mlp_from_scratch.ipynb) | Hidden Layer와 nonlinear activation |
| Regularization | [Dropout from Scratch](src/ch05_multilayer_perceptrons/sec5_6_dropout/01_dropout_from_scratch.ipynb) | Training과 inference behavior |
| Convolutional Network | [LeNet](src/ch07_convolutional_neural_networks/sec7_6_lenet/01_lenet_architecture.ipynb) | CNN architecture와 feature hierarchy |
| Residual Learning | [ResNet](src/ch08_modern_convolutional_neural_networks/sec8_6_residual_networks_resnet_and_resnext/02_resnet_model.ipynb) | Residual Block과 deep network training |
| Recurrent Network | [Character-Level RNN](src/ch09_recurrent_neural_networks/sec9_5_recurrent_neural_network_implementation_from_scratch/04_training.ipynb) | Sequence modeling과 generation |
| Transformer | [Training and Attention](src/ch11_attention_mechanisms_and_transformers/sec11_7_the_transformer_architecture/05_transformer_training_and_attention.ipynb) | Encoder–Decoder, causal mask, attention map |
| Vision Transformer | [Vision Transformer](src/ch11_attention_mechanisms_and_transformers/sec11_8_transformers_for_vision/03_vision_transformer.ipynb) | Patch Embedding, ViT Block, image classification |

## Voyage log

| Chapter | Topic | Progress |
|:---:|---|:---:|
| 1 | Introduction | **Done** |
| 2 | Preliminaries | **Done** |
| 3 | Linear Neural Networks for Regression | **Done** |
| 4 | Linear Neural Networks for Classification | **Done** |
| 5 | Multilayer Perceptrons | **Done** |
| 6 | Builders' Guide | **Done** |
| 7 | Convolutional Neural Networks | **Done** |
| 8 | Modern Convolutional Neural Networks | **Done** |
| 9 | Recurrent Neural Networks | **Done** |
| 10 | Modern Recurrent Neural Networks | **Done** |
| 11 | Attention Mechanisms and Transformers | **Done** |
| **12** | **Optimization Algorithms** | **Next** |
| 13 | Computational Performance | Planned |
| 14 | Computer Vision | Planned |
| 15 | Natural Language Processing: Pretraining | Planned |
| 16 | Natural Language Processing: Applications | Milestone |
| 17 | Reinforcement Learning | Planned |
| 18 | Gaussian Processes | Planned |
| 19 | Hyperparameter Optimization | Target |
| 20 | Generative Adversarial Networks | Optional |
| 21 | Recommender Systems | Not planned |

## Repository map

```text
src/
├── ch02_preliminaries/                              38 notebooks
├── ch03_linear_neural_networks_for_regression/      17 notebooks
├── ch04_linear_neural_networks_for_classification/  11 notebooks
├── ch05_multilayer_perceptrons/                      7 notebooks
├── ch06_builders_guide/                             15 notebooks
├── ch07_convolutional_neural_networks/               9 notebooks
├── ch08_modern_convolutional_neural_networks/       15 notebooks
├── ch09_recurrent_neural_networks/                  12 notebooks
├── ch10_modern_recurrent_neural_networks/           14 notebooks
└── ch11_attention_mechanisms_and_transformers/      21 notebooks
```

각 chapter 아래에 section별 directory를 두고, 하나의 notebook에서 하나의
학습 흐름을 다룬다.

## Run locally

```bash
git clone https://github.com/Laplace-tech/maverick.git
cd maverick
code .
```

VS Code에서 다음 interpreter와 kernel을 선택한다.

```text
Interpreter: .venv/bin/python
Kernel:      Python (maverick)
```

Terminal에서 environment를 직접 사용할 때:

```bash
source .venv/bin/activate
python
```

<p align="center">
  <sub>Study archive based on <a href="https://d2l.ai/">Dive into Deep Learning</a>.</sub>
</p>
