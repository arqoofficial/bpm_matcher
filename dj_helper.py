import streamlit as st


st.set_page_config(
    "BPM Matcher 🎧",
    layout="centered"
)

st.markdown("# BPM Matcher 🎧")
st.markdown(
    (
        "С помощью данного сервиса вы сможете идеально "
        "подобрать процент изменения скорости вашего "
        "трека и сводить без единого коня 🐴🐴🐴"
    )
)

st.sidebar.markdown("## Точность ввода")
precise = st.sidebar.selectbox(
    "Выберите точность вашего BPM",
    [
        "Целый BPM (128)",
        "До десятых (128.1)",
        "До сотых (128.11)"
    ]
)

st.sidebar.markdown("## Диапазон BPM")
diapasone = st.sidebar.selectbox(
    "Выберите диапазон изменения вашего BPM",
    [
        "88-175",
        "70-180",
        "108-215"
    ]
)

diapasone_split = diapasone.split("-")
if precise == "Целый BPM (128)":
    start_bpm = int(diapasone_split[0])
    end_bpm = int(diapasone_split[1])
    FIRST_SPEED_VALUE = 128
    SECOND_SPEED_VALUE = 130
    CHANGE_SPEED = 1
    ROUND_VALUE = 1
    
elif precise == "До десятых (128.1)":
    start_bpm = float(diapasone_split[0])
    end_bpm = float(diapasone_split[1])
    FIRST_SPEED_VALUE = 128.0
    SECOND_SPEED_VALUE = 130.0
    CHANGE_SPEED = 0.1
    ROUND_VALUE = 2
else:
    start_bpm = float(diapasone_split[0])
    end_bpm = float(diapasone_split[1])
    FIRST_SPEED_VALUE = 128.00
    SECOND_SPEED_VALUE = 130.00
    CHANGE_SPEED = 0.01
    ROUND_VALUE = 2
    st.sidebar.warning("Не понимаю, зачем тебе такая точность, но ладно)))")

INST_LINK = "https://instagram.com/arqoofficial?igshid=OGQ5ZDc2ODk2ZA=="
GH_LINK = "https://github.com/arqoofficial"
st.sidebar.markdown("#### Made by Arqo 😎")
st.sidebar.markdown(f"[Instagram]({INST_LINK})")
st.sidebar.markdown(f"[GitHub]({GH_LINK})")

st.markdown("#### Первый трек (тот, что играет)")
first_speed = st.slider(
    "First BPM",
    start_bpm,
    end_bpm,
    FIRST_SPEED_VALUE,
    CHANGE_SPEED
)

st.markdown("#### Второй трек (который хочешь свести)")
second_speed = st.slider(
    "Second BPM",
    start_bpm,
    end_bpm,
    SECOND_SPEED_VALUE,
    CHANGE_SPEED
)

result = round(
    (100 / second_speed) * (first_speed - second_speed), 
    ROUND_VALUE
)
if result > 0:
    result_str = f"+{abs(result)}%"
    hint = f"Повысь скорость второго трека на {abs(result)}%"
elif result < 0:
    result_str = f"-{abs(result)}%"
    hint = f"Понизь скорость второго трека на {abs(result)}%"
else:
    result_str = "0%"
    hint = "Зачем ты это считаешь? Треки идеально сведутся)))"

st.markdown("## Результат")
st.markdown("Измени скорость второго трека на этот процент:")
st.success(result_str)

hint_button = st.button("Подсказка 🆘")
if hint_button:
    st.markdown(f"*{hint}*")
    st.markdown("___")
    st.write(
        (
            "В боковом меню можешь выбрать точность ввода/расчёта BPM. "
            "Там же можешь выбрать твой любимый диапазон BPM. "
            "Ну и еще можешь подписаться на мои аккаунты в инсте и гитхабе 😁 "
            "Для обратной связи пиши в директ 🥰"
        )
    )
    st.markdown("#### Своди без коней и играй классную музыку 📀🕺")
