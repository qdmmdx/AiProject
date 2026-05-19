import streamlit as st
import pandas as pd

# 页面配置项

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# 大标题
st.title("大标题")
st.header("一级标题")
st.subheader("二级标题")

# 段落
st.write("在你的GitHub仓库设置中（Settings -> Secrets and variables -> Actions），添加名为LLM_API_KEY的密钥，值就是你使用的AI模型的API Key")

# 图片
# st.image("path")

# 音频
# st.audio("path")

# 视频
# st.vedio("path")

# logo
# st.logo("path")

# 表格
confusion_matrix = pd.DataFrame(
    {
        "Predicted Cat": [85, 3, 2, 1],
        "Predicted Dog": [2, 78, 4, 0],
        "Predicted Bird": [1, 5, 72, 3],
        "Predicted Fish": [0, 2, 1, 89],
    },
    index=["Actual Cat", "Actual Dog", "Actual Bird", "Actual Fish"],
)
st.table(confusion_matrix)

# 输入框
title = st.text_input("输入姓名")
st.write(f"姓名是{title}" )
# 密码输入框
pwd = st.text_input("输入密码",type="password")
st.write(f"密码是{pwd}" )

# 按钮
genre = st.radio(
    "请输入您的性别",
    ["男","女"],
)
st.write(f"您的性别为{genre}" )