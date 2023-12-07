import streamlit as st

from knowledge_gpt.components.faq import faq
from dotenv import load_dotenv
import os

load_dotenv()

def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) below🔑\n"  # noqa: E501
            "2. Upload a pdf, docx, or txt file📄\n"
            "3. Ask a question about the document💬\n"
        )
        api_key_input = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="Paste your OpenAI API key here (sk-...)",
            help="You can get your API key from https://platform.openai.com/account/api-keys.",  # noqa: E501
            value=os.environ.get("OPENAI_API_KEY", None)
            or st.session_state.get("OPENAI_API_KEY", ""),
        )

        st.session_state["OPENAI_API_KEY"] = api_key_input

        st.markdown("---")
        st.markdown("# Параметры:")

        st.markdown("temperature:")
        st.markdown(
            "temperature:"
            "Температура выборки, значения от 0 до 2. Более высокие значения, такие как 1.8,\n"
            "сделают вывод более случайным, в то время как более низкие значения, такие как 0.2,\n"
            "сделают его более целенаправленным и детерминированным.\n"
            "Не рекомендуется использовать совместно с параметром top_p\n"
        )

       
       
        St.markdown("[Описание API GigaChat](https://developers.sber.ru/docs/ru/gigachat/api/reference)")    
        
        st.markdown("---")
        st.markdown("# О программе")
        st.markdown(
            "После загрузки документа можно задавать вопросы и получеть ответы от GigaChat"
        )
        st.markdown(
            "Данное приложение находится в разработке и может содержать ошибки"
        )
        st.markdown("Made by YR")
        st.markdown("---")

       # faq()
