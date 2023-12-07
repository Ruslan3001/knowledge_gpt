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
        par_temperature_input = st.text_input(
            "Temperature",
            type="default",
            placeholder="Значения от 0 до 2",
            disabled=False,
            label_visibility="visible",
            value=1,
            help="Более высокое значение делает вывод более случайным"  # noqa: E501
        )   
        st.markdown(
            "Температура выборки, значения от 0 до 2. Более высокие значения, такие как 1.8,\n"
            "сделают вывод более случайным, в то время как более низкие значения, такие как 0.2,\n"
            "сделают его более целенаправленным и детерминированным.\n"
            "Не рекомендуется использовать совместно с параметром top_p.\n"
        )

        # top_p:
        par_top_p_input = st.text_input(
            "top_p",
            type="default",
            placeholder="Значения от 0 до 1",
            disabled=False,
            label_visibility="visible",
            value="",
            help="Более высокое значение делает вывод более случайным"  # noqa: E501
        )   
        st.markdown(
            "Тальтернатива параметру temperature, где модель учитывает результаты токенов с\n"
            "вероятностной массой top_p. Таким образом, 0.1 означает, что учитываются только \n"
            "токены, составляющие верхнюю 10%-ную массу вероятности. Значения от 0 до 1.\n"
            "Не рекомендуется использовать совместно с параметром temperature.\n"
        )

        #n :
        par_n_input = st.text_input(
            "N-число вариантов ответов",
            type="default",
            placeholder="Значения от 1 до 4",
            disabled=False,
            label_visibility="visible",
            value="1",
            help="Значения от 1 до 4"  # noqa: E501
        )   
        st.markdown(
            "Число вариантов ответов модели, которые необходимо сгенерировать \n"
            "для каждого входного сообщения. Максимально возможное значение n=4.\n"
        )

        #max_tokens :
        par_max_tokens_input = st.text_input(
            "max_tokens",
            type="default",
            placeholder="Значения ????",
            disabled=False,
            label_visibility="visible",
            value="1",
            help="Мальное количество токенов для генерации ответов"  # noqa: E501
        )  

        
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
