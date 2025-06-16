import streamlit as st

st.title("Cadastro de clientes")

nome = st.text_input("Digite o nome do cliente")
endereco = st.text_input("Digite o seu endereço")
data = st.date_input("Escolha a data de nascimento")
tipo_cliente = st.selectbox("Tipo do cliente" , ["Pessoa fisica", "Pessoa juridica"])

cadastrar = st.button("Cadastrar Cliente")

if cadastrar: 
    with open("cliente.csv", "a", encoding="utf8") as arquivos:
        arquivos.write(f"{nome}, {endereco}, {data}, {tipo_cliente}\n")
        st.success("Cliente cadastrado com sucesso")
