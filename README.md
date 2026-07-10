# 提升任务仓库

## 仓库结构

```
提升任务/
├── TASK1/                    # 任务1：医学病例实体抽取
│   ├── .ipynb_checkpoints/   # Jupyter Notebook 检查点（自动生成）
│   ├── A case of portal vein recanalization and symptomatic heart failure.pdf  # 原始病例PDF
│   ├── case.txt              # PDF文本提取结果
│   ├── case.json             # 医学实体抽取结果（JSON格式）
│   ├── requirements.txt      # Python依赖
│   ├── task1.ipynb           # 核心代码（Jupyter Notebook）
│   └── task1 .py             # Notebook导出文件
│
├── TASK2/                    # 任务2：心力衰竭死亡率预测模型
│   ├── Task2_latex/          # 论文LaTeX源文件
│   │   ├── Development of a Machine Learning-Based Mortality Risk Prediction Model Integrating Clinical Indicators for Patients with Heart Failure.tex
│   │   ├── references.bib
│   │   └── *.png (图片文件)
│   ├── Development of a Machine Learning-Based Mortality Risk Prediction Model Integrating Clinical Indicators for Patients with Heart Failure.pdf  # 生成的论文PDF
│   ├── heart_failure_clinical_records_dataset.csv  # 数据集
│   ├── requirements.txt      # Python依赖
│   └── task2.ipynb           # 核心代码（Jupyter Notebook）
│
└── README.md                 # 本文件
```

## 任务说明

### 任务1：医学病例实体抽取

- **目录**：`TASK1/`
- **任务描述**：从PDF病例文献中提取文本，并使用Qwen大语言模型进行医学实体抽取，输出标准化JSON格式
- **核心运行方法**：
  ```bash
  cd TASK1
  pip install -r requirements.txt
  jupyter notebook task1.ipynb
  ```
- **主要提交物**：
  - [case.json](file:///C:/Users/21041/Desktop/实习/提升任务/TASK1/case.json) - 医学实体抽取结果
  - [case.txt](file:///C:/Users/21041/Desktop/实习/提升任务/TASK1/case.txt) - PDF文本提取结果
  - [task1.ipynb](file:///C:/Users/21041/Desktop/实习/提升任务/TASK1/task1.ipynb) - 源代码

### 任务2：心力衰竭死亡率预测模型

- **目录**：`TASK2/`
- **任务描述**：基于临床指标数据集，开发机器学习死亡率风险预测模型，包含数据预处理、因子分析、相关性分析等
- **核心运行方法**：
  ```bash
  cd TASK2
  pip install -r requirements.txt
  jupyter notebook task2.ipynb
  ```
- **主要提交物**：
  - [task2.ipynb](file:///C:/Users/21041/Desktop/实习/提升任务/TASK2/task2.ipynb) - 源代码
  - [heart_failure_clinical_records_dataset.csv](file:///C:/Users/21041/Desktop/实习/提升任务/TASK2/heart_failure_clinical_records_dataset.csv) - 数据集
  - [Development of a Machine Learning-Based Mortality Risk Prediction Model Integrating Clinical Indicators for Patients with Heart Failure.pdf](file:///C:/Users/21041/Desktop/实习/提升任务/TASK2/Development%20of%20a%20Machine%20Learning-Based%20Mortality%20Risk%20Prediction%20Model%20Integrating%20Clinical%20Indicators%20for%20Patients%20with%20Heart%20Failure.pdf) - 研究报告

### 任务3

- **目录**：未创建（当前仓库中不存在）
- **说明**：仓库中暂未包含任务3的相关文件

## 环境要求

- Python 3.13+
- Jupyter Notebook
- 各任务的依赖见对应目录的 `requirements.txt`

## 运行步骤

1. 克隆或下载仓库
2. 进入对应任务目录
3. 安装依赖：`pip install -r requirements.txt`
4. 运行 Jupyter Notebook：`jupyter notebook taskX.ipynb`（X为任务编号）
5. 按顺序执行 Notebook 中的代码单元
