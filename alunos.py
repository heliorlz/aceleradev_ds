import streamlit as st


def main():
    st.title("Hello World")

    st.markdown("Botao")
    botao = st.button("Botao")
    if botao:
        st.markdown("Clicado")

    st.markdown("Checkbox")
    check_box = st.checkbox("Checkbox")
    if check_box:
        st.markdown("Checado")

    st.markdown("Radio")
    radio = st.radio("What's your favorite soccer team?",
                     ("Corinthians", "Palmeiras", "Sao Paulo"))
    if radio == "Corinthians":
        st.markdown("Vai Corinthians")
    elif radio == "Palmeiras":
        st.markdown("Porco")
    else:
        st.markdown("Bambi")

    st.markdown("Select Box")
    select_box = st.selectbox("What's your favorite soccer team?",
                              ("Corinthians", "Palmeiras", "Sao Paulo"))
    if select_box == "Corinthians":
        st.markdown("Vai Corinthians")
    elif select_box == "Palmeiras":
        st.markdown("Porco")
    else:
        st.markdown("Bambi")

    st.markdown("Multi Select")
    multi_select_box = st.multiselect(
        "Select your favorites colors:", ["Red", "Black", "Blue", "Yellow"])
    st.write(f"Your favorite color(s): {multi_select_box}")

    st.markdown("File uploader")
    file = st.file_uploader("Select your file: ", type="csv")
    if file is not None:
        st.markdown("File uploaded")


if __name__ == '__main__':
    main()
