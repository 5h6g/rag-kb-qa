# rag-kb-qa
## 当前状态
已完成：文档切分 → 向量生成 → ChromaDB 存储 → 相似度检索 → 本地模型生成，全链路跑通。
未完成：还没有评测集和准确率数据（计划 11 月第二周补齐 Top-1/3/5 命中率基线）。

## 设计取舍
- 为什么用本地 Ollama 而不是云端 API：零成本、可离线开发、无网络依赖
- 为什么用 nomic-embed-text 而不是聊天模型做向量：聊天模型不输出 embedding 向量
- 遇到的坑：langchain-community 新版移除 ChatOllama，需改用 langchain-ollama 独立包
- 遇到的坑：HuggingFace 不可达，embedding 改走 OllamaEmbeddings

## 下一步
1. 去框架化实现一版纯 Python 检索链路，验证对每一环的理解
2. 标注 25 题评测集，建立命中率基线
3. 对比固定长度 / 按标题层级 / 递归三种切分策略的命中率差异
