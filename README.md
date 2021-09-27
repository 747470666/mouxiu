# 谋秀 - VSWBD科研小站 (Virtual Science Web Base-on Dash)
**本项目目前由<font color='yellow'>汪颖</font>独立开发，目标是为科研工作者提供简单可用的个人网站建设**
> Dash是一个很强大的全栈包（React for Python），整体代码采用Python开发，大大增加了可读性与减少了工程量，在不追求高并发、强交互的要求下是非常合适的开发选择。
## [Open Dash](https://github.com/plotly/dash)
### *Dash is the most downloaded, trusted Python framework for building ML & data science web apps*.
#### 如何使用
在你的`terminal`中, 下载包 `dash`：
```bash
pip install dash
```
在国内，我推荐使用`pip`代理来下载包：
```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple dash
```
如果仍然存在问题，我推荐采用`trust`模式来下载：
```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn dash
```

#### 记住
还需要下载pandas
```bash
pip install pandas
```

## 启动
```bash
python app.py
```

## 目录结构
本项目的初始目录结构及介绍如下
```text
|-- project #项目根目录
    |-- assets #项目使用资源库
        |-- css 样式库
        |-- js 脚本库
        |-- static 静态资源
    |-- src #项目源文件
        |-- components #一些组件库
        |-- pages #所有页面
    |-- tools #常规工具
        |-- router.py #路由配置
    |-- app.py #App入口
    |-- README.md #介绍文档
```