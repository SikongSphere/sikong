[**中文**](./README.md) | [**English**](./README_en.md)

# 司空：基于中文建筑行业知识的LLaMA微调大模型

### SiKong：Tuning LLaMA Model With Chinese Architecture Instructions



1.  创建`conda`虚拟环境
```shell
conda create -n sikong python=3.9
conda activate sikong
```
2.  安装`LMflow`仓库
```shell
./install_repo.sh
```
3.  启动服务
```shell
./run_app.sh
```
启动服务后，可以打开`127.0.0.1:6006`查看聊天界面

<img src="assets/SikongSphere-Logo.png" alt="SikongSphere" style="zoom:40%;" />



[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](https://github.com/SCIR-HI/Huatuo-Llama-Med-Chinese/blob/main/LICENSE) ![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)

本项目开源了经过中文建筑学指令精调/指令微调（Instruct-tuning）的LLaMA-7B模型。我们通过采集建筑行业数据集，对LLaMA进行了指令微调，提高了LLaMA在建筑领域的问答效果。

目前我们只开放针对基础建筑行业知识的模型参数。在未来，我们计划添加更多领域的建筑专业数据集（中式古建筑、建筑行业规范和标准、外国古建筑、建筑结构等），针对不同建筑领域和建筑类型训练模型。

## 1. 更新日志



## 2. A Quick Start



## 3. 模型下载



## 4. Infer



## 5. 数据集构建



## 6. Finetune



## 7.训练细节



### 7.1. 计算资源需求



### 7.2. 实验过程



## 8. 模型效果对比

| 测试输入 | Llama输出 | Alpaca输出 | SiKong司空输出 |
| :------- | :-------- | :--------- | :------------- |
|          |           |            |                |
|          |           |            |                |
|          |           |            |                |



## 9. 常见问题

1. Q：

   A：

2. Q：

   A：

3. Q：

   A：

4. Q：

   A：

5. Q：

   A：

## 10. 项目参与者

本项目由司空学社的刘钧文、梁超完成。

## 11. Star History



## 12. 致谢

- 感谢王非先生对本项目的资金支持。

## 13. 免责声明

本项目相关资源仅供学术研究之用，严禁用于商业用途。使用涉及第三方代码的部分时，请严格遵循相应的开源协议。模型生成的内容受模型计算、随机性和量化精度损失等因素影响，本项目无法对其准确性作出保证。本项目数据集绝大部分由模型生成，即使符合某些建筑学事实，也不能被用作实际建筑设计的依据。对于模型输出的任何内容，本项目不承担任何法律责任，亦不对因使用相关资源和输出结果而可能产生的任何损失承担责任。

## 14. Citation

如果你使用了本项目的数据或者代码，请声明引用



## 15. 合作单位



