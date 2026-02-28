# ai-tanchishe

## 项目概述
贪吃蛇（Snake）游戏，基于 Python 和 pygame，实现于 uv 虚拟环境下。

## 安装方式

1. 安装 Python 3.12 及 uv（建议使用 uv 管理虚拟环境）。
2. 使用以下命令初始化虚拟环境并安装依赖：
```shell
uv venv .venv
uv pip install pygame
```
3. 启动游戏
```shell
.venv/Scripts/python.exe snake.py
```

## 使用方法
方向键控制移动，吃到红色食物即可得分，撞墙或撞到自己则游戏结束。窗口左上角显示当前得分。

## pip 安装指引
后续提供 pip 安装包，敬请关注。
当前使用源码运行，如需打包请见下方【打包发布说明】。

## 项目结构
- snake.py 主体游戏程序
- test_snake.py 自动化测试/单元测试
- README.md 项目信息、说明
- .venv uv 虚拟环境目录

## 代码规范
- 遵循 PEP8 代码风格
- 严格分层，逻辑清晰
- 命名清晰、注释完备

## 开发/打包说明
如需 pip 安装请先运行如下命令打包：
```
uv pip install build
python -m build
```
将生成的 dist/ 目录发布至第三方 pip 仓库（如 PyPI）

---
有任何建议或问题请在 GitHub Issues 中反馈。
