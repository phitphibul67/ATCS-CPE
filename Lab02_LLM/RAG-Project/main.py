"""
Main RAG program with OpenRouter Integration.

Answer questions using the knowledge base + OpenRouter LLM.
Workflow: Input -> Retrieval -> Context -> LLM Generation -> Output

compile: python main.py
"""

import os
import sys
# นำเข้า OpenAI Client สำหรับต่อเชื่อมกับ OpenRouter
from openai import OpenAI

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import config
from src.retriever import Retriever


# ฟังก์ชันสำหรับส่ง Prompt ให้ LLM ผ่าน OpenRouter
def generate_llm_answer(client: OpenAI, query: str, context_chunks: list) -> str:
    """
    [LLM Generation Stage via OpenRouter]
    """
    context_text = "\n\n".join([f"- {item['answer']}" for item in context_chunks])

    prompt = f"""คุณเป็นผู้ช่วยตอบคำถาม โปรดตอบคำถามต่อไปนี้โดยอ้างอิงจากข้อมูลบริบท (Context) ที่กำหนดให้อย่างถูกต้อง เป็นธรรมชาติ และกระชับ
หากข้อมูลบริบทไม่เกี่ยวข้องหรือไม่อาจตอบคำถามได้ ให้ระบุว่า "ไม่พบข้อมูลที่เกี่ยวข้องในระบบ"

[Context Data]:
{context_text}

[User Question]:
{query}

[Answer]:"""

    model_name = getattr(config, "OPENROUTER_MODEL", "poolside/laguna-s-2.1:free")

    # เรียกใช้ API สไตล์ OpenAI
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "คุณคือ AI ผู้ช่วยตอบคำถาม RAG"},
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message.content


def main():
    if not os.path.exists(config.FAISS_INDEX_FILE):
        print("Vector database not found.")
        print("Please run lab01_extract_text.py -> lab04_create_vector_db.py first.")
        return

    # ดึงค่า API Key จาก config.py
    api_key = getattr(config, "OPENROUTER_API_KEY", os.environ.get("OPENROUTER_API_KEY", ""))

    if not api_key or "วาง_API_KEY" in api_key:
        print("\n❌ Error: กรุณาใส่ OPENROUTER_API_KEY จริงใน config.py ก่อนใช้งานครับ")
        return

    # ตั้งค่า OpenAI Client ให้ชี้ไปที่ OpenRouter Base URL
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    print("--- Complete RAG System (Retrieval + OpenRouter LLM) ---")
    print("--- Enter ('exit', 'quit', or 'q' to quit) ---\n")

    retriever = Retriever(
        model_name=config.EMBEDDING_MODEL_NAME,
        index_path=config.FAISS_INDEX_FILE,
        chunk_store_path=config.CHUNK_STORE_FILE,
    )

    while True:
        # [STAGE 1: INPUT]
        query = input("\nHi Bro! 😎\nAsk me anything: ").strip()

        if query.lower() in ("exit", "quit", "q"):
            print("---- ขอบใจหลายๆ เด้อ !!! ------.")
            break

        if not query:
            continue

        # [STAGE 2: RETRIEVAL]
        results = retriever.retrieve(query, top_k=config.TOP_K)

        if not results:
            print("No relevant answer found in the knowledge base.")
            continue

        print("\n🔍 [Retrieval Phase] ค้นหาเอกสารเรียบร้อยแล้ว...")

        # [STAGE 3 & 4: CONTEXT -> LLM]
        print("🤖 [LLM Generation Phase] กำลังส่งประมวลผลผ่าน OpenRouter...")
        final_answer = generate_llm_answer(client, query, results)

        # [STAGE 5: OUTPUT]
        print("\n=================== AI ANSWER ===================")
        print(final_answer)
        print("=================================================")


if __name__ == "__main__":
    main()