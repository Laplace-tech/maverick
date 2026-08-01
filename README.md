# Maverick

PyTorch로 *Dive into Deep Learning*을 공부하며 작성한 실습 notebook 모음입니다.
원문의 algorithm과 학습 흐름을 유지하되, tensor shape과 중간 결과를 직접 확인할 수 있도록 구성했습니다.

## Current status

| Item | Status |
|---|---|
| Completed | Chapter 3–7 |
| Current checkpoint | Chapter 7 · Convolutional Neural Networks |
| Next | Chapter 8 · Modern Convolutional Neural Networks |
| Target | Chapter 19 · Hyperparameter Optimization |
| Notebooks | 97 |
| Environment | Python 3.12 · PyTorch · VS Code/WSL2 · RTX 3060 Ti 8GB |

Chapter 4는 Section 4.1–4.6을 완료하고 Section 4.7을 건너뛰었습니다.

Chapter 5의 Kaggle House Prices 실습 public score는 `0.41188`입니다.

## Progress

| Chapter | Topic | Status |
|:---:|---|---|
| 2 | Preliminaries | 2.1–2.6 complete · 2.7 deferred |
| 3 | Linear Neural Networks for Regression | Complete |
| 4 | Linear Neural Networks for Classification | 4.1–4.6 complete · 4.7 skipped |
| 5 | Multilayer Perceptrons | Complete |
| 6 | Builders' Guide | Complete |
| 7 | Convolutional Neural Networks | Complete |
| 8 | Modern Convolutional Neural Networks | Next |
| 9–20 | Advanced topics | Planned |
| 21 | Recommender Systems | Excluded |

## Covered topics

- Tensor operation, linear algebra, calculus와 automatic differentiation
- Linear regression, minibatch SGD, generalization과 weight decay
- Linear classification, softmax와 cross-entropy
- MLP, activation function, initialization과 dropout
- K-Fold cross-validation과 Kaggle House Prices submission
- Custom module, parameter management, serialization과 GPU execution
- 2D cross-correlation, padding, stride, multiple channels와 pooling
- LeNet architecture와 Fashion-MNIST GPU training

Kaggle House Prices public score는 `0.41188`, LeNet validation accuracy는 `73.39%`입니다.

## Repository structure

```text
src/
├── ch02_preliminaries/
├── ch03_linear_neural_networks_for_regression/
├── ch04_linear_neural_networks_for_classification/
├── ch05_multilayer_perceptrons/
├── ch06_builders_guide/
└── ch07_convolutional_neural_networks/
    ├── sec7_2_convolutions_for_images/
    ├── sec7_3_padding_and_stride/
    ├── sec7_4_multiple_input_and_multiple_output_channels/
    ├── sec7_5_pooling/
    └── sec7_6_lenet/

references/d2l/
├── CHAT_TUTOR_MANUAL.md
├── CODE_STYLE.md
├── STUDY_CHECKPOINT.md
└── source/
```

Notebook 경로는 다음 형식을 사용합니다.

```text
src/chXX_chapter_name/secX_X_section_name/NN_topic_name.ipynb
```

## Selected notebooks

| Topic | Notebook |
|---|---|
| Automatic Differentiation | [A Simple Function](src/ch02_preliminaries/sec2_5_automatic_differentiation/01_a_simple_function.ipynb) |
| Linear Regression | [Concise Linear Regression](src/ch03_linear_neural_networks_for_regression/sec3_5_concise_implementation_of_linear_regression/01_concise_linear_regression.ipynb) |
| Weight Decay | [Weight Decay from Scratch](src/ch03_linear_neural_networks_for_regression/sec3_7_weight_decay/01_weight_decay_from_scratch.ipynb) |
| Linear Classification | [Softmax Regression Training](src/ch04_linear_neural_networks_for_classification/sec4_5_concise_softmax_regression/03_training.ipynb) |
| Softmax and Cross-Entropy | [Softmax Revisited](src/ch04_linear_neural_networks_for_classification/sec4_5_concise_softmax_regression/02_softmax_revisited.ipynb) |
| MLP | [MLP from Scratch](src/ch05_multilayer_perceptrons/sec5_2_implementation_of_multilayer_perceptrons/01_mlp_from_scratch.ipynb) |
| Dropout | [Dropout from Scratch](src/ch05_multilayer_perceptrons/sec5_6_dropout/01_dropout_from_scratch.ipynb) |
| K-Fold Cross-Validation | [Kaggle House Price Prediction](src/ch05_multilayer_perceptrons/sec5_7_predicting_house_prices_on_kaggle/01_kaggle_house_price_prediction.ipynb) |
| LeNet | [LeNet Architecture and Training](src/ch07_convolutional_neural_networks/sec7_6_lenet/01_lenet_architecture.ipynb) |

## Study conventions

- 원문의 algorithm, class hierarchy, data helper와 lesson flow를 유지합니다.
- 각 실습에서 tensor shape과 중요한 intermediate value를 확인합니다.
- Notebook의 lesson cell은 직접 입력하고 실행합니다.
- Exercises는 별도로 필요할 때 진행합니다.

## Running notebooks

```bash
cd ~/projects/maverick
source .venv/bin/activate
jupyter lab
```

VS Code에서는 `.venv/bin/python` 또는 `Python (maverick .venv)` kernel을 선택합니다.
