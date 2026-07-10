{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "534179f4-ffd2-4272-9a1e-fe3d90d49d42",
   "metadata": {},
   "outputs": [],
   "source": [
    "#!pip install pdfplumber"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "27fe3f63-730c-4a22-be2e-4d4b7e45e944",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pdfplumber"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "7c76bfe6-a68b-4db4-af54-6aff913b226f",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# PDF路径\n",
    "pdf_path =r'A case of portal vein recanalization and symptomatic heart failure.pdf'\n",
    "\n",
    "# 保存全部文本\n",
    "all_text = \"\"\n",
    "\n",
    "# 打开PDF\n",
    "with pdfplumber.open(pdf_path) as pdf:\n",
    "\n",
    "    # 遍历每一页\n",
    "    for page in pdf.pages:\n",
    "\n",
    "        # 提取文本\n",
    "        text = page.extract_text()\n",
    "\n",
    "        # 如果页面存在文本\n",
    "        if text:\n",
    "            all_text += text + \"\\n\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "a175391d-154e-4165-81dc-09071ef402a6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 保存为txt\n",
    "with open(\"case.txt\", \"w\", encoding=\"utf-8\") as f:\n",
    "    f.write(all_text)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "98576451-802d-4b4e-a1a6-31d7825c9f2d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#!pip install openai"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "ad8546aa-32f3-4b9b-8980-ffaa9a4684bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "from openai import OpenAI\n",
    "import json\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "c17765ef-2827-4318-9d9d-154666659094",
   "metadata": {},
   "outputs": [],
   "source": [
    "# ===========================\n",
    "# 1. 配置 API\n",
    "# ===========================\n",
    "client = OpenAI(\n",
    "    api_key=\"sk-ws-H.EMIMPXM.W8bQ.MEQCIHIyiVflY-tLMRdJ_D1797ONJV08r2b2Q1LFmXKb4vKIAiBeC-ZaUbQO8goF_SmJr7l4THFy9aqRCccHzcCJPgd7ig\",\n",
    "    base_url=\"https://ws-vqnlz5zj6z0rlkyr.cn-beijing.maas.aliyuncs.com/compatible-mode/v1\"\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "225bb1c9-12da-4821-9daf-ef24ba1dd2c1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# ===========================\n",
    "# 2. 读取病例文本\n",
    "# ===========================\n",
    "with open(\"case.txt\", \"r\", encoding=\"utf-8\") as f:\n",
    "    case_text = f.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "86972843-7f6d-400f-a2ea-7ed104989c59",
   "metadata": {},
   "outputs": [],
   "source": [
    "# ===========================\n",
    "# 3. 构造 Prompt\n",
    "# ===========================\n",
    "prompt = f\"\"\"\n",
    "你是一名医学自然语言处理专家，熟悉电子病历、临床病例以及医学实体识别。\n",
    "\n",
    "你的任务是从病例中抽取医学实体。\n",
    "\n",
    "要求：\n",
    "1. 所有信息必须来源于原文。\n",
    "2. 不允许推测。\n",
    "3. 保留医学术语。\n",
    "4. 没有的信息填写 \"\" 或 []。\n",
    "5. 输出合法标准化的 JSON。\n",
    "\n",
    "请抽取：\n",
    "1.患者基本信息\n",
    "2.主要症状\n",
    "3.现病史（提炼为关键病史列表）\n",
    "4.既往史（提炼为关键病史列表）\n",
    "5.诊断结果（提炼为诊断名称列表）\n",
    "6.治疗方案（仅包含医疗操作/干预手段，不含药物名称）\n",
    "7.使用药物（仅列出药品通用名）\n",
    "\n",
    "输出格式：\n",
    "\n",
    "{{\n",
    "  \"patient_information\":{{\n",
    "      \"gender\":\"\",\n",
    "      \"age\":\"\",\n",
    "      \"height\":\"\",\n",
    "      \"weight\":\"\"\n",
    "  }},\n",
    "  \"chief_complaint\":\"\",\n",
    "  \"major_symptoms\":[],\n",
    "  \"present_illness\":[],\n",
    "  \"past_history\":[],\n",
    "  \"diagnosis\":[],\n",
    "  \"treatment\":[],\n",
    "  \"medications\":[]\n",
    "}}\n",
    "\n",
    "\n",
    "病例：\n",
    "\n",
    "{case_text}\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "4d74b828-1c2f-4e3f-aa5a-748b8e1fc7c6",
   "metadata": {},
   "outputs": [],
   "source": [
    "# ===========================\n",
    "# 4. 调用 Qwen API\n",
    "# ===========================\n",
    "response = client.chat.completions.create(\n",
    "    model=\"qwen-plus\",\n",
    "    messages=[\n",
    "        {\n",
    "            \"role\": \"user\",\n",
    "            \"content\": prompt\n",
    "        }\n",
    "    ],\n",
    "    temperature=0\n",
    ")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "7ce71d6d-da9a-447d-8cea-29c3a96d60d0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# ===========================\n",
    "# 5. 获取返回结果\n",
    "# ===========================\n",
    "result = response.choices[0].message.content\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "398fa84c-cc8c-44f9-a1f4-88f5c8f2bf84",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "医学实体抽取完成，结果已保存到 case.json\n"
     ]
    }
   ],
   "source": [
    "# ===========================\n",
    "# 6. 解析 JSON\n",
    "# ===========================\n",
    "try:\n",
    "    result_json = json.loads(result)\n",
    "\n",
    "    with open(\"case.json\", \"w\", encoding=\"utf-8\") as f:\n",
    "        json.dump(result_json, f, ensure_ascii=False, indent=4)\n",
    "\n",
    "    print(\"医学实体抽取完成，结果已保存到 case.json\")\n",
    "\n",
    "except json.JSONDecodeError:\n",
    "    print(\"模型返回内容不是合法 JSON，请检查 Prompt 或模型输出。\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bc5fd5a7-0035-4546-8f6c-b55e86cd289b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b3d9dbe3-9fd7-44cb-9fb6-6a311a54b868",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2c0e8f0a-6ad1-4c12-a191-9e3f3341da45",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ab01a35f-d278-4db3-b1f1-10bd8cbfab99",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9dc1a833-62e4-4b2f-849f-a7c5ba94f6a5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
