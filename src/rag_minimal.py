import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

# ============ 配置 ============
DOCS_DIR = "docs"
CHROMA_DIR = "./chroma_db"
MODEL_NAME = "qwen3:4b"

# ============ 第一步：加载并切分文档 ============
def build_knowledge_base():
    print("[1/4] 加载文档并切分...")
    
    texts = []
    for fname in sorted(os.listdir(DOCS_DIR)):
        if fname.endswith(".txt"):
            with open(os.path.join(DOCS_DIR, fname), "r", encoding="utf-8") as f:
                texts.append(f.read())
    raw_text = "\n\n".join(texts)
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50,
        separators=["\n\n", "\n", "。", "，", ""]
    )
    chunks = splitter.split_text(raw_text)
    total = sum((len(x)for x in chunks[0:3]))
    print(total)
    print(len(chunks))
    print(chunks[0])
    print(len(chunks[0]))
    print(chunks[1])
    print(f"    → 切分出 {len(chunks)} 个 chunk")
    
    print("[2/4] 生成向量并构建知识库...")
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = Chroma.from_texts(chunks, embeddings, persist_directory=CHROMA_DIR)
    print(f"    → 知识库已保存到 {CHROMA_DIR}")
    
    return vectorstore

# ============ 第二步：检索 + 生成 ============
def ask_rag(vectorstore, question):
    print(f"\n[问题] {question}")
    
    # 检索最相关的 2 个文档块
    docs = vectorstore.similarity_search(question, k=2)
    context = "\n\n".join([d.page_content for d in docs])
    
    print(f"[检索到 {len(docs)} 个相关片段]")
    for i, d in enumerate(docs, 1):
        print(f"  片段{i}: {d.page_content[:80]}...")
    
    # 拼接 prompt
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""你是一个专业的知识问答助手。请严格根据以下上下文回答用户问题。如果上下文中没有相关信息，请明确说明"知识库中没有相关信息"。

上下文：
{context}

问题：{question}

回答："""
    )
    
    # 调用本地模型
    print("\n[生成中] ", end="", flush=True)
    llm = ChatOllama(model=MODEL_NAME, temperature=0.3)
    response = llm.invoke(prompt.format(context=context, question=question))
    
    # 提取纯文本答案
    answer = response.content if hasattr(response, 'content') else str(response)
    print(f"\n[回答] {answer}")
    
    return answer

# ============ 主流程 ============
if __name__ == "__main__":
    if os.path.exists(CHROMA_DIR) and len(os.listdir(CHROMA_DIR)) > 0:
        print("[+] 检测到已有知识库，直接加载\n")
        embeddings = OllamaEmbeddings(model="nomic-embed-text")
        vectorstore = Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings)
    else:
        vectorstore = build_knowledge_base()
    
    questions = [
        "Java程序设计课考核占比是多少？",
        "RAG 相比直接让大模型回答有什么优势？",
        "RAG 适合用在哪些场景？",
        "我室友的生日是多少？",
        "前端开发期末考试各题型占比？",
        "易混淆点有几条？",
        "模拟卡片hover代码是什么？",
        "阴影分为几个？",
        "transform有几个常用方法？",
    ]
    
    for q in questions:
        ask_rag(vectorstore, q)
        print("-" * 60)
