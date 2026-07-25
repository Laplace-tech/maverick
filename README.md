<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:071A2B,25:0B3B60,52:126E82,76:6B5B95,100:B565A7&height=290&section=header&text=MAVERICK&fontSize=68&fontColor=EAFBFF&fontAlignY=38&animation=fadeIn&desc=Dive%20into%20Deep%20Learning%20%C2%B7%20PyTorch%20Study&descSize=20&descAlignY=62" width="100%" alt="Maverick D2L header" />
</p>

<div align="center">

**Dive into Deep Learning PyTorch 실습 기록**

<br />

<img src="https://img.shields.io/badge/Current%20Course-Chapter%203.4-126E82?style=for-the-badge" alt="Current course Chapter 3.4" />
<img src="https://img.shields.io/badge/Target-Transformer-B565A7?style=for-the-badge" alt="Target Transformer" />
<img src="https://img.shields.io/badge/Framework-PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch" />

</div>

<br />

---

## Project

| 항목 | 내용 |
|---|---|
| Textbook | [Dive into Deep Learning](https://d2l.ai/), PyTorch edition |
| Study Range | Chapter 1–11 |
| Current Position | Chapter 3.4 · Linear Regression Implementation from Scratch |
| Goal | Attention과 Transformer를 직접 구현하고 설명할 수 있는 수준 |
| Study Period | 2026.07.23 – 2026.09.07 |
| Environment | Windows 11 · WSL2 Ubuntu · VS Code |
| Repository Style | 소절별 Jupyter Notebook + 누적 복습 테스트 |

<br />

## Environment

<div align="center">

<img src="https://img.shields.io/badge/Python-3.12.3-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.12.3" />
<img src="https://img.shields.io/badge/PyTorch-2.11.0-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch 2.11.0" />
<img src="https://img.shields.io/badge/CUDA-12.8-76B900?style=for-the-badge&logo=nvidia&logoColor=white" alt="CUDA 12.8" />
<img src="https://img.shields.io/badge/D2L-1.0.3-6B5B95?style=for-the-badge" alt="D2L 1.0.3" />
<img src="https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter Notebook" />
<img src="https://img.shields.io/badge/VS%20Code-WSL-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white" alt="VS Code WSL" />

</div>

<br />

## Progress

| Chapter | Course | Status |
|:---:|---|:---:|
| 1 | Introduction | Orientation |
| 2 | Preliminaries | 2.1–2.5 학습 · 2.6 보류 |
| 3 | Linear Neural Networks for Regression | **3.4 진행 중** |
| 4 | Linear Neural Networks for Classification | Planned |
| 5 | Multilayer Perceptrons | Planned |
| 6 | Builders' Guide | Planned |
| 7 | Convolutional Neural Networks | Planned |
| 8 | Modern Convolutional Neural Networks | Planned |
| 9 | Recurrent Neural Networks | Planned |
| 10 | Modern Recurrent Neural Networks | Planned |
| 11 | Attention Mechanisms and Transformers | Target |

<br />

## Contents

### Chapter 2 · Preliminaries

- Data manipulation: tensor 생성, indexing, broadcasting, memory, NumPy 변환
- Data preprocessing: CSV 읽기, 결측값 처리, tensor 변환
- Linear algebra: vector, matrix multiplication, reduction, norm
- Calculus: derivative, partial derivative, gradient, chain rule
- Automatic differentiation: computation graph, nonscalar backward, detach
- Probability and statistics: coin tossing와 probability axioms까지 진행

### Chapter 3 · Linear Neural Networks for Regression

- Linear regression의 model, squared loss, minibatch SGD
- Gaussian noise와 maximum likelihood의 관계
- 선형회귀를 단일층 fully connected network로 해석
- `Module`, `DataModule`, `Trainer`의 역할 분리
- Synthetic regression data와 PyTorch `DataLoader`
- Linear regression from scratch 진행 중

<br />

## Repository Structure

```text
maverick/
├── src/
│   ├── ch02_preliminaries/
│   │   ├── sec2_1_data_manipulation/
│   │   ├── sec2_2_data_preprocessing/
│   │   ├── sec2_3_linear_algebra/
│   │   ├── sec2_4_calculus/
│   │   ├── sec2_5_automatic_differentiation/
│   │   └── sec2_6_probability_and_statistics/
│   └── ch03_linear_neural_networks_for_regression/
│       ├── sec3_1_linear_regression/
│       ├── sec3_2_object_oriented_design_for_implementation/
│       ├── sec3_3_synthetic_regression_data/
│       └── sec3_4_linear_regression_implementation_from_scratch/
├── .gitignore
└── README.md
```

각 실습 노트북은 다음 규칙으로 배치한다.

```text
src/chXX_chapter_name/secX_X_section_name/NN_topic_name.ipynb
```

데이터셋, 모델 weight, notebook checkpoint와 생성 결과물은 Git에서 제외한다.

<br />

## Run in VS Code

브라우저 Jupyter가 아니라 WSL의 VS Code Notebook 환경에서 실행한다.

```bash
cd ~/projects/maverick
code .
```

Notebook 오른쪽 위의 kernel 선택 메뉴에서 다음 kernel을 선택한다.

```text
Python (maverick)
```

또는 프로젝트 interpreter를 직접 선택한다.

```text
/home/anna/projects/maverick/.venv/bin/python
```

터미널에서 Python을 실행할 때는 가상환경을 활성화한다.

```bash
source .venv/bin/activate
python
```

Notebook kernel을 이미 `Python (maverick)`으로 선택했다면, 셀을 실행하기 위해 터미널에서 별도로 가상환경을 활성화할 필요는 없다.

<br />

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:B565A7,24:6B5B95,48:126E82,75:0B3B60,100:071A2B&height=170&section=footer" width="100%" alt="Maverick footer" />
</p>
