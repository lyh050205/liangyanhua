# 提升任务仓库

## 仓库结构

```
提升任务/
├── TASK1/                    # 任务1：医学病例实体抽取
├── TASK2/                    # 任务2：心力衰竭死亡率预测模型
├── TASK3/                    # 任务3：医疗大模型新人快速上手指南
├── AI_Chat_Records.md        # AI对话记录汇总
└── README.md
```

## 任务说明

### 任务1：医学病例实体抽取

- **目录**：`TASK1/`
- **核心运行方法**：运行 [task1.ipynb](file:///C:/Users/21041/Desktop/实习/提升任务/TASK1/task1.ipynb)
- **主要提交物**：
  - [case.json](file:///C:/Users/21041/Desktop/实习/提升任务/TASK1/case.json)
  - [case.txt](file:///C:/Users/21041/Desktop/实习/提升任务/TASK1/case.txt)
  - [task1.ipynb](file:///C:/Users/21041/Desktop/实习/提升任务/TASK1/task1.ipynb)

### 任务2：心力衰竭死亡率预测模型

- **目录**：`TASK2/`
- **核心运行方法**：运行 [task2.ipynb](file:///C:/Users/21041/Desktop/实习/提升任务/TASK2/task2.ipynb)
- **主要提交物**：
  - [task2.ipynb](file:///C:/Users/21041/Desktop/实习/提升任务/TASK2/task2.ipynb)
  - [heart_failure_clinical_records_dataset.csv](file:///C:/Users/21041/Desktop/实习/提升任务/TASK2/heart_failure_clinical_records_dataset.csv)
  - [论文PDF](file:///C:/Users/21041/Desktop/实习/提升任务/TASK2/Development%20of%20a%20Machine%20Learning-Based%20Mortality%20Risk%20Prediction%20Model%20Integrating%20Clinical%20Indicators%20for%20Patients%20with%20Heart%20Failure.pdf)

### 任务3：医疗大模型新人快速上手指南

- **目录**：`TASK3/`
- **核心内容**：医疗大模型学习指南，涵盖工具篇、实战篇、进阶篇
- **主要提交物**：
  - [医疗大模型新人快速上手指南.md](file:///C:/Users/21041/Desktop/实习/提升任务/TASK3/医疗大模型新人快速上手指南.md)

## AI对话记录

各任务的AI辅助开发对话记录汇总在 [AI_Chat_Records.md](file:///C:/Users/21041/Desktop/实习/提升任务/AI_Chat_Records.md)，包含：

- 任务一API调用与实现
- 任务二代码编写和论文大纲编写
- 任务二论文润色
- 任务二论文中文翻译
- 任务二生成流程图片
- 任务三学习指南润色

## 运行步骤

```bash
# 安装依赖
pip install -r TASK1/requirements.txt
pip install -r TASK2/requirements.txt

# 运行任务
jupyter notebook TASK1/task1.ipynb
jupyter notebook TASK2/task2.ipynb

```
