import streamlit as st
from openai import OpenAI
import os

# 页面配置项

st.set_page_config(
    page_title="AI助手",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

# 大标题
st.title("AI助手")

# 系统提示词
sys_prompt = """
    你叫 %s。
    规则：
        1. 每次只回复一条消息
        2. 匹配用户的语言
    性格：
        - %s
    你必须严格遵守上述规则来回复用户

"""

# 初始化聊天信息 昵称 性格
if "messages" not in st.session_state:
    st.session_state.messages = []

if "nick_name" not in st.session_state:
    st.session_state.nick_name = "AI助手"

if "nature" not in st.session_state:
    st.session_state.nature = "非常专业"

# 展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message['content'])

# APIKEY配置
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

# 侧边栏
# with -- streamlit的上下文管理器
with st.sidebar:
    st.subheader("助手信息")
    # 昵称输入框
    nick_name = st.text_input("名称",placeholder="请输入名称",value=st.session_state.nick_name)
    st.session_state.nick_name = nick_name
    # 性格输入框
    nature = st.text_area("性格",placeholder="请输入性格",value=st.session_state.nature)
    st.session_state.nature = nature



# 输入框
prompt = st.chat_input("请输入你的问题")
if prompt:
    st.chat_message("user").write(f"用户：{prompt}")
    print("----------> 调用ai大模型，提示词：",prompt)
    # 保存用户输入
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 调用ai大模型
    print([
            {"role": "system", "content": sys_prompt},
            *st.session_state.messages])

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": sys_prompt % (st.session_state.nick_name,st.session_state.nature)},
            *st.session_state.messages],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )
    # 非流式输出
    # print("<--------------大模型返回结果：",response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)
    # # 保存大模型返回结果
    # st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})


    # 流式输出
    response_message = st.empty() # 创建一个空消息, 用于保存大模型返回结果
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
