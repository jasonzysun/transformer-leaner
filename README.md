# transformer-leaner
Transformer 学习记录

## 环境搭建

本项目推荐使用 Anaconda 来管理 Python 环境。请按照以下步骤创建并激活一个新的 Conda 环境：

### 1. 创建并激活 Conda 环境

在终端（或 Anaconda Prompt）中运行以下命令（此示例使用 Python 3.9，可根据需要调整版本）：

```bash
conda create --name transformer-env python=3.9
conda activate transformer-env
```

### 2. 安装所需依赖库
使用 Conda 安装部分库
例如，安装 PyTorch（包含 torchvision、torchaudio 以及 cudatoolkit）：

```bash
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
```

使用 pip 安装其他库
安装 HuggingFace 的 transformers、numpy、matplotlib 和 jupyter：

```bash
pip install transformers numpy matplotlib jupyter
```

### 3. 记录依赖环境
为了方便以后复现环境，建议将当前环境依赖记录下来。你可以选择以下两种方式之一：

使用 Conda 导出环境配置：
```bash
conda env export > environment.yml
```
使用 pip freeze 导出依赖列表：
```bash
pip freeze > requirements.txt
```