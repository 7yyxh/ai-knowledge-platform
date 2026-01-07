import dotenv
from langchain_openai import ChatOpenAI
from langchain_community.llms.tongyi import Tongyi
import os

dotenv.load_dotenv()  #加载当前目录下的 .env 文件

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")
os.environ['DASHSCOPE_API_KEY'] = os.getenv("DASHSCOPE_API_KEY")

llm = Tongyi(
    api_key= os.environ['DASHSCOPE_API_KEY'] ,
    model="qwen-plus"
)

def chat_with_llm(query: str) -> str:
    prompt = f"请简要回答：{query}"
    return llm.invoke(prompt)
