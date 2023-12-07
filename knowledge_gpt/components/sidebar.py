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
        
        st.markdown("# Параметры:")
        
        # Орисание st.text_input: https://docs.streamlit.io/library/api-reference/widgets/st.text_input  
        # temperature:
   
      
        st.markdown("[Описание API GigaChat](https://developers.sber.ru/docs/ru/gigachat/api/reference)")    
        
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
