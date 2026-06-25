import streamlit as st
import pandas as pd

st.set_page_config(page_title="Laboratório do Leite - SAC", layout="wide")

st.title("🧪 Sistema de Atendimento - Laboratório do Leite")

# Inicialização
if "clientes" not in st.session_state:
    st.session_state.clientes = []

if "atendimentos" not in st.session_state:
    st.session_state.atendimentos = []

# Cadastro de Cliente
st.header("Cadastro de Clientes")

with st.form("cliente_form"):
    nome = st.text_input("Nome do Cliente")
    telefone = st.text_input("Telefone")
    email = st.text_input("E-mail")

    cadastrar = st.form_submit_button("Cadastrar Cliente")

    if cadastrar:
        st.session_state.clientes.append({
            "Nome": nome,
            "Telefone": telefone,
            "Email": email
        })
        st.success("Cliente cadastrado com sucesso!")

# Registro de Solicitações
st.header("Registro de Solicitações")

with st.form("atendimento_form"):
    cliente = st.text_input("Nome do Cliente")
    protocolo = st.text_input("Número do Protocolo")

    status = st.selectbox(
        "Status do Laudo",
        ["Pendente", "Em andamento", "Concluído"]
    )

    responsavel = st.text_input("Responsável pelo Atendimento")

    registrar = st.form_submit_button("Registrar Solicitação")

    if registrar:
        st.session_state.atendimentos.append({
            "Cliente": cliente,
            "Protocolo": protocolo,
            "Status": status,
            "Responsável": responsavel
        })
        st.success("Solicitação registrada!")

# Indicadores
st.header("Indicadores")

total = len(st.session_state.atendimentos)

pendentes = len([
    x for x in st.session_state.atendimentos
    if x["Status"] == "Pendente"
])

andamento = len([
    x for x in st.session_state.atendimentos
    if x["Status"] == "Em andamento"
])

concluidos = len([
    x for x in st.session_state.atendimentos
    if x["Status"] == "Concluído"
])

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total", total)
col2.metric("Pendentes", pendentes)
col3.metric("Em andamento", andamento)
col4.metric("Concluídos", concluidos)

# Lista de Atendimentos
st.header("Lista de Atendimentos")

if st.session_state.atendimentos:
    df = pd.DataFrame(st.session_state.atendimentos)
    st.dataframe(df, use_container_width=True)
else:
    st.info("Nenhum atendimento registrado.")
