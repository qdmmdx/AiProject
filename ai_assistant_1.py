import streamlit as st
import pandas as pd
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
sys_prompt = "你是一个非常厉害的AI助理"

# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

# 展示聊天信息
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message['content'])

# APIKEY配置
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

# 输入框
prompt = st.chat_input("请输入你的问题")
if prompt:
    st.chat_message("user").write(f"用户：{prompt}")
    print("----------> 调用ai大模型，提示词：",prompt)
    # 保存用户输入
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 调用ai大模型
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    print("<--------------大模型返回结果：",response.choices[0].message.content)
    st.chat_message("assistant").write(response.choices[0].message.content)
    # 保存大模型返回结果
    st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})