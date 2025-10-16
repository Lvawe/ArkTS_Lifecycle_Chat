# ArkTS Lifecycle Chat (使用开源模型对 ArkTS 生命周期分析)

这是一个面向鸿蒙（ArkTS）原生项目的工具，使用大模型自动提取并分析 ArkTS 中的所有生命周期函数。项目目标包括但不限于组件（Component）、页面（Page）以及其他自定义或框架层面的生命周期函数。

## 项目简介

ArkTS Lifecycle Chat 是一个专门面向鸿蒙应用开发者的智能辅助工具。它可以帮助开发者：

- 扫描代码并识别 ArkTS 的生命周期钩子（组件、页面及其他）
- 使用大模型对生命周期函数进行语义提取与说明（例如触发时机、参数说明、典型用法）
- 生成可读的生命周期文档或报告，便于开发者理解与迁移

## 功能特点

- 🚀 智能代码分析
- 🔄 自动化处理
- 🛠️ 开发辅助工具

## 适用场景

- 代码审查与文档生成
- ArkTS 项目迁移与兼容性分析
- 教学与团队协作（快速掌握生命周期调用时序）

## 开始使用

### 环境要求

- Python 3.9+
- 配置 ARK_API_KEY 环境变量

### 安装

```bash
git clone https://github.com/[your-username]/arkts-assistant.git
cd arkts-assistant
```

### 使用方法

```bash
python arkts_chat.py --file your_arkts_file.ts
```

## 配置说明

在使用之前，请确保设置了必要的环境变量：

```bash
export ARK_API_KEY="your_api_key_here"
```

## 贡献指南

欢迎提交 Issue 和 Pull Request 来帮助改进这个项目。

## 许可证

MIT License
