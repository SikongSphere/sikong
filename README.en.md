[**中文**](./README.md) | [**English**](./README.en.md)

# SiKong：Tuning LLaMA and Alpaca Model With Chinese Architecture Instructions



<div>
<a href="https://imgse.com/i/pCUwnJg"><img src="https://s1.ax1x.com/2023/06/26/pCUwnJg.png" alt="pCUwnJg.png" border="0" /></a>
</div>



[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](LICENSE) ![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)
<a href='https://gitee.com/sikongsphere/sikong/stargazers'><img src='https://gitee.com/sikongsphere/sikong/badge/star.svg?theme=dark' alt='star'></img></a>
<a href='https://github.com/sikongsphere/sikong/stargazers'><img src="https://img.shields.io/github/stars/sikongphere/sikong.svg?style=social&label=Stars"></img></a>
This project has open sourced the LLaMA-7B model that has been fine-tuned/instruct-tuned in Chinese architecture. By collecting  basic information form the construction industry and construct the datasets, we fine-tuned the instructions of LLaMA and improved the Q&A effect of LLaMA in the field of construction in Chinese.

Currently we only open model parameters for basic construction industry knowledge. In the future, we plan to add architectural professional datasets in more fields (Chinese ancient buildings, construction industry codes and standards, foreign ancient buildings, architectural structures, etc.) to train models for different architectural fields and building types.

## 1. Update Log

- Web Demo Experience Address: [sikong](http://region-9.seetacloud.com:33955/)


## 2. A Quick Start

- Locally clone the `sikong` project repository

```shell
# github repository
git clone https://github.com/SikongSphere/sikong.git

# gitee repository
git clone https://gitee.com/sikongsphere/sikong.git
```

- Create a virtual environment and install third-party libraries.

Please make sure `conda` is installed and available locally, and create an environment according to the following command

```shell
conda env create -f environment.yaml
conda activate sikong
```

- Download the architectural doman language large model `sikong` hosted on `huggingface`, and place it in the `model` folder.

<div align="center">
<a href="https://imgse.com/i/pCUMD1S"><img src="https://s1.ax1x.com/2023/06/26/pCUMD1S.png" alt="pCUMD1S.png" border="0" height="100"/></a>
</div>



Fine-tuned models：

 - [sikong-llama-7b-chinese](https://huggingface.co/SikongSphere/sikong-llama-7b-chinese/tree/main)
 - [sikong-alpaca-7b-chinese](https://huggingface.co/SikongSphere/sikong-alpaca-7b-chinese/tree/main)

```shell
cd model

# Make sure you have git-lfs installed (https://git-lfs.com)
git lfs install
git clone https://huggingface.co/SikongSphere/sikong-llama-7b-chinese

# if you want to clone without large files – just their pointers
# prepend your git clone with the following env var:
GIT_LFS_SKIP_SMUDGE=1
```

- Start the chat interface:

```shell
./scripts/run_app.sh
```

After starting the service, you can open `127.0.0.1:6006` to view the chat interface. If you want to replace the model, you can change the path of the model in `run_app.sh`。


## 5. Dataset Construction

The required format for the input data of the `sikong` architectural domain large model is as follows：

```json
{
    "type": "text2text",
    "instance": [
        {
            "input": "建筑艺术创作中的核心问题是什么？",
            "output": "建筑的空间与实体，是对立统一的两个方面，抓住它并认真地去剖析，运用一定的构图技法把它解决好，则是建筑艺术创作中非常重要的核心问题。"
        }
    ]
}
```

In order to facilitate users to enter data and convert it to the target `json` format, we provide a format conversion script, which is located at `scripts/data_preprocess/csv2json.py`, the specific usage is:

```python
python scripts/data_preprocess csv2json.py --csv data/example.csv --json data/example.json
```

It should be noted that after converting `json` data, you need to use `script/add_end_mark.py ` to add stop words to it。

## 6. Finetune

If the user needs to fine-tune the model, the following command can be used：

```shell
./scripts/run_finetune.sh
```

Specific parameters can be changed in the `run_finetune.sh` file to meet specific needs.

## 7. Training Details

<a href="https://imgse.com/i/pCUMmwR"><img src="https://s1.ax1x.com/2023/06/26/pCUMmwR.png" alt="pCUMmwR.png" border="0" /></a>


### 7.1. Computing Resource Requirements

`sikong` training resources:

 - `GPU`: `A100-PCIE-40GB` * 4卡
 - `CPU`: `40 vCPU Intel Xeon Processor (Skylake, IBRS)`
 - `Memory` 288GB


### 7.2. Experiment Procedure



## 8. Comparison of model effects

In order to demonstrate the capabilities of the Sikong language large model, we present the following sets of tests.

### 8.1 Question 1

- 测试输入：
  - **请介绍一下变形缝的概念。**
- Llama输出：
  - 变形缝是一种可以改变形状的缝。
- Alpaca输出：
  - 变形缝是一种特殊的缝合技术，它可以将两个物体结合在一起，而不需要使用任何粘合剂。
- ChatGLM输出：
  - 变形缝通常由混凝土或砖石等建筑材料制成，其目的是在地震或自然灾害时，使岩石形成隔离缝，防止相邻的岩石受到更大的破坏。
- SiKong司空输出：
  - 变形缝是指将建筑物垂直分开的预留缝。由于温度变化、地基不均匀沉降和地震因素的影响，易使建筑物发生裂缝或破坏，故在设计时应事先将房屋划分成若干个独立的部分，使各部分能自由地变化。

### 8.2 Question 2

- Input：
  - **图书馆中书架之间以及书架与墙体之间通道的最小宽度是多少？**
- Llama Output：
  - 1.5m
- Alpaca Output：
  - 书架之间通道的最小宽度是0.5厘米，书架与墙体之间通道的最小宽度是0.5厘米。
- ChatGLM Output：
  - 图书馆中书架之间以及书架与墙体之间通道的最小宽度取决于不同国家和地区的法规和规定。一般来说，图书馆的书架通道应该保证书籍的流通和检索，因此最小宽度应该能够容纳一个人的步行距离。
- SiKong Output：
  - 按照《图书馆建筑设计规范》（JGJ 38-2015）中规定，图书馆中书架之间以及书架与墙体之间通道的最小宽度按通道类型划分为以下几种情况： 
    1. 主通道中，开架的常用书架间隔不小于1.5m，闭架的常用书架间隔不小于1.2m，不常用书架间隔不小于1m；
    2. 次通道中，开架的常用书架间隔不小于1.1m，闭架的常用书架间隔不小于0.75m，不常用书架间隔不小于0.6m；
    3. 档头走道（即靠墙走道）中，开架的常用书架间隔不小于0.7m，闭架的常用书架间隔不小于0.6m，不常用书架间隔不小于0.6m；
    4. 行道中，开架的常用书架间隔不小于1m，闭架的常用书架间隔不小于0.75m，不常用书架间隔不小于0.6m。

### 8.3 Question 3

- Input：
  - **在中国建筑设计防火规范中，重要公共建筑是什么?**
- Llama Output：
  - “重要公共建筑”指在中国建造的具有特殊社会功能、影响面广、对社会和经济发展有显著作用的建筑。
- Alpaca Output：
  - 在中国建筑设计防火规范中，重要公共建筑是指一类公共建筑，包括医院、学校、博物馆、图书馆、商场、政治机关、金融机构等，这些建筑的使用功能复杂，人员密集，且具有较高的火灾危险。
- ChatGLM Output：
  - 在中国建筑设计防火规范中，重要公共建筑是指一类公共建筑，包括医院、学校、博物馆、图书馆、商场、政治机关、金融机构等，这些建筑的使用功能复杂，人员密集，且具有较高的火灾危险。
- SiKong Output：
  - 在《建筑设计防火规范》中，重要公共建筑是指发生火灾可能造成重大人员伤亡、财产损失和严重社会影响的公共建筑。


## 9. Common Problem

1. Q：Why does the model ask and answer itself after the input?

   A：If this happens, please add `##` to the end of the input sentence and enter it again.

2. Q：Why is it called SiKong

   A：Because Sikong is an official position in ancient China, it is mainly responsible for the country's urban construction and water conservancy project construction, which is also the origin of the name of Sikong Academy. This large model adopts the title of Sikong, in fact, it hopes to inherit the tradition of the Chinese construction industry.

3. Q：

   A：

4. Q：

   A：

5. Q：

   A：

## 10. Project Participants

This project was completed by Liu Junwen, Liang Chao and Sun Yiwei of Sikong Academy.

## 11. Star History

[![Star History Chart](https://api.star-history.com/svg?repos=SikongSphere/sikong&type=Date)](https://star-history.com/#SikongSphere/sikong&Date)



## 12. Thanking

- Thanks to Mr. Wang Fei for his financial support for this project.
- This project uses the warehouses of [LMFlow](https://github.com/OptimalScale/LMFlow.git) and [Chinese-LLaMA-Alpaca](https://github.com/ymcui/Chinese-LLaMA-Alpaca.git) , thanks!

<div class="imgGroup" align="center">
  <a href="https://imgse.com/i/pCU0dN8"><img src="https://s1.ax1x.com/2023/06/26/pCU0dN8.png" alt="pCU0dN8.png" border="0" width="300"/></a>
  <a href="https://imgse.com/i/pCU0w4S"><img src="https://s1.ax1x.com/2023/06/26/pCU0w4S.png" alt="pCU0w4S.png" border="0" width="300"/></a>
</div>      

## 13. Disclaimer

The resources related to this project are for academic research only, and commercial use is strictly prohibited. When using parts involving third-party code, please strictly follow the corresponding open source agreement. The content generated by the model is affected by factors such as model calculation, randomness, and loss of quantification accuracy. This project cannot guarantee its accuracy. Most of the data set of this project is generated by the model, even if it conforms to some architectural facts, it cannot be used as the basis for the actual architectural design. This project does not assume any legal responsibility for any content output by the model, nor is it liable for any losses that may arise from the use of relevant resources and output results.

## 14. Citation

If you use the data or code of this project, please declare the reference



## 15. Cooperation Units

<a href="https://imgse.com/i/pCUMem9"><img src="https://s1.ax1x.com/2023/06/26/pCUMem9.png" alt="pCUMem9.png" border="0" width="230" height="70"/></a>