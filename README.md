## 一、项目说明

此项目是基于LangGraph开发的文本摘要智能体，因为系统提示词都采用中文编写所以更适合对中文文本进行摘要。若需要适用于不同语言的文本，请自行修改config目录下的提示词脚本。

## 二、流程设计

![image-20250409160445573](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20250409160445573.png)

- 根据原文生成初步的摘要。
- 进入文本润色节点对摘要进行润色，增强摘要的可读性和流畅性。
- 进入文本审查节点对摘要与原文的一致性进行审查

- - 摘要中的信息符合原文，输出结果
  - 摘要中的信息不符合原文，将原文、摘要和摘要中存在的问题都交给文本修改节点进行修改。修改结束以后再进入文本审查节点审查摘要与原文的一致性

## 三、大语言模型

本项目是通过发送请求调用本地部署的大语言模型实现，若采用其它大模型调用方式，请修改util目录下的llm.py文件

