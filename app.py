# 環境変数からAPIキーを取得
from dotenv import load_dotenv
load_dotenv()

#タイトル
import streamlit as st
st.title("提出課題: 簡単なWebアプリ")

#機能の説明
st.write("##### 動作モード1: 医学の専門家")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで医学的な視点からのアドバイスを得ることができます。")
st.write("##### 動作モード2: 幼児教育の専門家")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで幼児教育の専門家の視点からアドバイスを得ることができます。")

#ラジオボタンの作成
selected_item = st.radio(
    "動作モードを選択してください。",
    ["医学の専門家", "幼児教育の専門家"]
)

#区切り線
st.divider()

#ラジオボタンの選択に応じて、入力フォームを表示
if selected_item == "医学の専門家":
    input_message = st.text_input(label="健康に関する質問を入力してください。")
else:
    input_message = st.text_input(label="子どもの教育に関する質問を入力してください。")

#区切り線
if st.button("実行"):
    st.divider()

    if selected_item == "医学の専門家":
        # OpenAI APIを使用して、医学的なアドバイスを取得
        if input_message:
            from langchain.chat_models import ChatOpenAI
            from langchain.schema import SystemMessage, HumanMessage

            llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

            messages = [
                SystemMessage(content="あなたは健康に関するアドバイザーです。医学の専門的な観点からアドバイスを提供してください。"),
                HumanMessage(content=input_message),
            ]

            result = llm(messages)

            # レスポンスオブジェクトからテキスト部分のみ表示
            st.write(result.content)

        else:
            st.error("質問を入力してください。")

    else:
        # OpenAI APIを使用して、幼児教育のアドバイスを取得
        if input_message:
            from langchain.chat_models import ChatOpenAI
            from langchain.schema import SystemMessage, HumanMessage

            llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

            messages = [
                SystemMessage(content="あなたは幼児教育の専門家です。子どもの教育に関するアドバイスを提供してください。"),
                HumanMessage(content=input_message),
            ]

            result = llm(messages)

            # レスポンスオブジェクトからテキスト部分のみ表示
            st.write(result.content)

        else:
            st.error("質問を入力してください。")