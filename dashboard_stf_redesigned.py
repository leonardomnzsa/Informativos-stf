import streamlit as st
import pandas as pd
import plotly.express as px
import base64
from io import BytesIO
import random

# Configuração da página
st.set_page_config(
    layout="wide", 
    page_title="Dashboard Informativos STF - Prof. Leonardo Aquino",
    page_icon="⚖️"
)

# Função para aplicar o tema personalizado
def apply_custom_theme():
    # Cores baseadas no site do Prof. Leonardo Aquino
    custom_css = """
    <style>
        /* Cores principais */
        :root {
            --background-color: #0e0e0e;
            --text-color: #ffffff;
            --accent-color: #c9a227;
            --secondary-color: #333333;
            --card-bg-color: #1a1a1a;
        }
        
        /* Estilo geral da página */
        .main {
            background-color: var(--background-color);
            color: var(--text-color);
        }
        
        /* Cabeçalhos */
        h1, h2, h3, h4, h5, h6 {
            color: var(--text-color);
            font-family: 'Helvetica Neue', sans-serif;
            font-weight: 500;
        }
        
        h1 {
            font-size: 2.5rem;
            margin-bottom: 1.5rem;
            border-bottom: 2px solid var(--accent-color);
            padding-bottom: 0.5rem;
        }
        
        h2 {
            font-size: 1.8rem;
            margin-top: 2rem;
            margin-bottom: 1rem;
            color: var(--accent-color);
        }
        
        h3 {
            font-size: 1.4rem;
            margin-top: 1.5rem;
            margin-bottom: 0.8rem;
        }
        
        /* Sidebar */
        .css-1d391kg, .css-12oz5g7 {
            background-color: var(--secondary-color);
        }
        
        /* Cards para conteúdo */
        .stCard {
            background-color: var(--card-bg-color);
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            border-left: 3px solid var(--accent-color);
        }
        
        /* Botões */
        .stButton>button {
            background-color: var(--accent-color);
            color: black;
            font-weight: 500;
            border: none;
            border-radius: 4px;
            padding: 0.5rem 1rem;
            transition: all 0.3s;
        }
        
        .stButton>button:hover {
            background-color: #e0b62d;
            color: black;
        }
        
        /* Inputs e seletores */
        .stSelectbox>div>div, .stMultiSelect>div>div {
            background-color: var(--card-bg-color);
            border: 1px solid var(--accent-color);
            color: var(--text-color);
        }
        
        /* Tabelas e DataFrames */
        .dataframe {
            font-family: 'Helvetica Neue', sans-serif;
        }
        
        .dataframe th {
            background-color: var(--accent-color);
            color: black;
            font-weight: 500;
            text-align: left;
            padding: 8px;
        }
        
        .dataframe td {
            background-color: var(--card-bg-color);
            color: var(--text-color);
            padding: 8px;
            border-bottom: 1px solid #333;
        }
        
        /* Estilo para o resumo expandido */
        .resumo-card {
            background-color: var(--card-bg-color);
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            border-left: 3px solid var(--accent-color);
            line-height: 1.6;
        }
        
        .resumo-title {
            color: var(--accent-color);
            font-size: 1.3rem;
            margin-bottom: 0.8rem;
            font-weight: 500;
        }
        
        .resumo-content {
            color: var(--text-color);
            font-size: 1rem;
            text-align: justify;
            white-space: pre-line;
        }
        
        .resumo-meta {
            color: #999;
            font-size: 0.9rem;
            margin-top: 1rem;
            border-top: 1px solid #333;
            padding-top: 0.5rem;
        }
        
        /* Estilo para as assertivas */
        .assertiva-card {
            background-color: var(--card-bg-color);
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            border-left: 3px solid #3498db;
        }
        
        .assertiva-text {
            font-size: 1.1rem;
            margin-bottom: 1rem;
            line-height: 1.5;
        }
        
        .assertiva-options {
            margin-top: 1rem;
        }
        
        .assertiva-feedback-correct {
            background-color: rgba(46, 204, 113, 0.2);
            border-left: 3px solid #2ecc71;
            padding: 1rem;
            border-radius: 4px;
            margin-top: 1rem;
        }
        
        .assertiva-feedback-incorrect {
            background-color: rgba(231, 76, 60, 0.2);
            border-left: 3px solid #e74c3c;
            padding: 1rem;
            border-radius: 4px;
            margin-top: 1rem;
        }
        
        /* Estilo para a seção de perguntas */
        .pergunta-card {
            background-color: var(--card-bg-color);
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            border-left: 3px solid #9b59b6;
        }
        
        .resposta-card {
            background-color: rgba(155, 89, 182, 0.1);
            border-radius: 8px;
            padding: 1.5rem;
            margin-top: 1rem;
            border-left: 3px solid #9b59b6;
        }
        
        /* Logo no topo */
        .logo-container {
            text-align: center;
            margin-bottom: 1rem;
        }
        
        .logo-container img {
            max-width: 200px;
            margin-bottom: 0.5rem;
        }
        
        /* Footer */
        .footer {
            text-align: center;
            margin-top: 3rem;
            padding-top: 1rem;
            border-top: 1px solid #333;
            color: #777;
            font-size: 0.9rem;
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

# Função para carregar a imagem da logo
def get_logo_base64():
    with open("White on Transparent 2.png", "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Função para exibir a logo
def display_logo():
    logo_base64 = get_logo_base64()
    logo_html = f"""
    <div class="logo-container">
        <img src="data:image/png;base64,{logo_base64}" alt="Prof. Leonardo Aquino Logo">
    </div>
    """
    st.markdown(logo_html, unsafe_allow_html=True)

# Função para carregar os dados (com cache para performance)
@st.cache_data
def load_data(file_path):
    try:
        df = pd.read_excel(file_path)
        # Tratar valores nulos em colunas de texto para evitar erros nos filtros/buscas
        for col in ["Título", "Tese Julgado", "Resumo", "Ramo Direito", "Matéria"]:
            if col in df.columns:
                df[col] = df[col].fillna("Não informado")
        # Converter Informativo para string para melhor exibição em filtros
        if "Informativo" in df.columns:
            df["Informativo"] = df["Informativo"].astype(str)
        return df
    except FileNotFoundError:
        st.error(f"Erro: Arquivo não encontrado em {file_path}")
        return None
    except Exception as e:
        st.error(f"Erro ao carregar ou processar o arquivo Excel: {e}")
        return None

# Função para criar um card de resumo
def create_resumo_card(titulo, resumo, informativo, classe, ramo, repercussao):
    html = f"""
    <div class="resumo-card">
        <div class="resumo-title">{titulo}</div>
        <div class="resumo-content">{resumo}</div>
        <div class="resumo-meta">
            <strong>Informativo:</strong> {informativo} | 
            <strong>Classe:</strong> {classe} | 
            <strong>Ramo do Direito:</strong> {ramo} | 
            <strong>Repercussão Geral:</strong> {repercussao}
        </div>
    </div>
    """
    return st.markdown(html, unsafe_allow_html=True)

# Função para gerar assertivas de estudo
def generate_assertivas(df, num_assertivas=5):
    assertivas = []
    
    # Selecionar aleatoriamente alguns registros para criar assertivas
    if len(df) >= num_assertivas:
        sample_indices = random.sample(range(len(df)), num_assertivas)
        
        for idx in sample_indices:
            row = df.iloc[idx]
            
            # Tipos de assertivas
            assertiva_types = [
                # Tipo 1: Assertiva correta sobre o resumo
                {
                    "texto": f"De acordo com o Informativo {row['Informativo']} do STF, {row['Resumo'][:200]}...",
                    "correta": True,
                    "explicacao": f"A assertiva está correta e reproduz fielmente o conteúdo do Informativo {row['Informativo']} do STF."
                },
                # Tipo 2: Assertiva incorreta (invertendo o sentido)
                {
                    "texto": f"Segundo o STF, no julgamento que gerou o Informativo {row['Informativo']}, NÃO é correto afirmar que {row['Resumo'][:150]}...",
                    "correta": False,
                    "explicacao": f"A assertiva está incorreta. O Informativo {row['Informativo']} do STF afirma justamente o contrário."
                },
                # Tipo 3: Assertiva sobre a classe processual
                {
                    "texto": f"O Informativo {row['Informativo']} do STF trata de um julgamento da classe processual {row['Classe Processo']}.",
                    "correta": True,
                    "explicacao": f"A assertiva está correta. O Informativo {row['Informativo']} realmente se refere a um processo da classe {row['Classe Processo']}."
                }
            ]
            
            # Escolher aleatoriamente um tipo de assertiva
            assertiva = random.choice(assertiva_types)
            assertivas.append(assertiva)
    
    return assertivas

# Função para simular respostas da IA para perguntas sobre informativos
def simulate_ia_response(pergunta, df):
    # Esta é uma simulação simples. Em um ambiente real, seria integrado com uma API de IA.
    
    # Verificar se a pergunta contém palavras-chave relacionadas a informativos específicos
    informativos_mencionados = []
    for informativo in df['Informativo'].unique():
        if informativo in pergunta:
            informativos_mencionados.append(informativo)
    
    # Verificar se a pergunta menciona ramos do direito
    ramos_mencionados = []
    for ramo in df['Ramo Direito'].unique():
        if ramo.lower() in pergunta.lower():
            ramos_mencionados.append(ramo)
    
    # Construir uma resposta baseada nos elementos identificados
    if informativos_mencionados:
        # Filtrar o DataFrame para os informativos mencionados
        df_filtrado = df[df['Informativo'].isin(informativos_mencionados)]
        
        if not df_filtrado.empty:
            # Pegar o primeiro resultado como exemplo
            exemplo = df_filtrado.iloc[0]
            
            resposta = f"""
            Com base no Informativo {exemplo['Informativo']} do STF, posso informar que:
            
            **Título:** {exemplo['Título']}
            
            **Resumo:** {exemplo['Resumo']}
            
            **Classe Processual:** {exemplo['Classe Processo']}
            
            **Ramo do Direito:** {exemplo['Ramo Direito']}
            
            **Repercussão Geral:** {exemplo['Repercussão Geral']}
            
            Este informativo é frequentemente cobrado em concursos públicos, especialmente em provas que abordam {exemplo['Ramo Direito']}.
            
            Para se preparar adequadamente, recomendo estudar a fundamentação constitucional desta decisão e comparar com outros julgados similares.
            """
            return resposta
    
    elif ramos_mencionados:
        # Filtrar o DataFrame para os ramos mencionados
        df_filtrado = df[df['Ramo Direito'].str.contains('|'.join(ramos_mencionados), case=False)]
        
        if not df_filtrado.empty:
            # Contar os informativos por ramo
            contagem = len(df_filtrado)
            
            # Pegar alguns exemplos
            exemplos = df_filtrado.sample(min(3, len(df_filtrado)))
            
            exemplos_texto = ""
            for _, exemplo in exemplos.iterrows():
                exemplos_texto += f"- Informativo {exemplo['Informativo']}: {exemplo['Título']}\n"
            
            resposta = f"""
            Sobre {', '.join(ramos_mencionados)} nos informativos do STF (2021-2025):
            
            Encontrei {contagem} informativos relacionados a este ramo do direito. Alguns exemplos importantes:
            
            {exemplos_texto}
            
            Este é um tema recorrente em concursos públicos. Recomendo focar nos aspectos constitucionais e processuais destas decisões.
            
            Para uma preparação completa, analise também a jurisprudência relacionada e as súmulas vinculantes que tratam deste tema.
            """
            return resposta
    
    # Resposta genérica se não encontrar referências específicas
    resposta = """
    Para responder com precisão sobre informativos específicos do STF, preciso que você mencione:
    
    1. Números de informativos específicos, ou
    2. Ramos do direito de seu interesse, ou
    3. Classes processuais específicas
    
    Posso ajudar com informações sobre qualquer um dos informativos do STF entre 2021 e 2025 presentes neste dashboard.
    
    Exemplos de perguntas mais específicas:
    - "O que diz o Informativo 1173 do STF?"
    - "Quais são os principais julgados de Direito Constitucional?"
    - "Explique as decisões com repercussão geral em matéria tributária."
    """
    return resposta

# Aplicar o tema personalizado
apply_custom_theme()

# Exibir a logo
display_logo()

# Título do Dashboard
st.title("Dashboard Interativo - Informativos STF (2021-2025)")

# Carregar os dados
df = load_data("/home/ubuntu/Dados_InformativosSTF_filtrado.xlsx")

if df is not None:
    # Criar abas para as diferentes seções
    tab1, tab2, tab3, tab4 = st.tabs(["📚 Informativos", "📊 Estatísticas", "✅ Assertivas", "❓ Pergunte à Result"])
    
    # Sidebar com filtros
    st.sidebar.header("Filtros e Navegação")
    
    # Filtros na sidebar
    informativo_filter = st.sidebar.multiselect(
        "Filtrar por Informativo:",
        options=sorted(df["Informativo"].unique()),
    )

    ramo_direito_filter = st.sidebar.multiselect(
        "Filtrar por Ramo do Direito:",
        options=sorted(df["Ramo Direito"].unique()),
    )

    classe_processo_filter = st.sidebar.multiselect(
        "Filtrar por Classe Processual:",
        options=sorted(df["Classe Processo"].unique()),
    )

    repercussao_geral_filter = st.sidebar.multiselect(
        "Filtrar por Repercussão Geral:",
        options=sorted(df["Repercussão Geral"].unique()),
    )

    # Barra de busca na sidebar
    search_term = st.sidebar.text_input("Buscar termo (Título, Resumo, Matéria):")

    # Aplicar filtros
    df_filtered = df.copy()
    if informativo_filter:
        df_filtered = df_filtered[df_filtered["Informativo"].isin(informativo_filter)]
    if ramo_direito_filter:
        df_filtered = df_filtered[df_filtered["Ramo Direito"].isin(ramo_direito_filter)]
    if classe_processo_filter:
        df_filtered = df_filtered[df_filtered["Classe Processo"].isin(classe_processo_filter)]
    if repercussao_geral_filter:
        df_filtered = df_filtered[df_filtered["Repercussão Geral"].isin(repercussao_geral_filter)]

    # Aplicar busca textual
    if search_term:
        search_term_lower = search_term.lower()
        df_filtered = df_filtered[
            df_filtered["Título"].str.lower().str.contains(search_term_lower) |
            df_filtered["Resumo"].str.lower().str.contains(search_term_lower) |
            df_filtered["Matéria"].str.lower().str.contains(search_term_lower)
        ]
    
    # --- Aba 1: Visualização dos Informativos ---
    with tab1:
        st.header("Visualização dos Informativos")
        st.write(f"Exibindo {len(df_filtered)} de {len(df)} registros.")
        
        # Opção para visualizar como tabela ou cards
        view_mode = st.radio("Modo de visualização:", ["Tabela", "Cards de Leitura"], horizontal=True)
        
        if view_mode == "Tabela":
            # Exibir tabela de dados filtrados
            st.dataframe(df_filtered)
        else:
            # Exibir como cards para melhor leitura
            for i, row in df_filtered.iterrows():
                create_resumo_card(
                    row["Título"], 
                    row["Resumo"], 
                    row["Informativo"], 
                    row["Classe Processo"], 
                    row["Ramo Direito"], 
                    row["Repercussão Geral"]
                )

    # --- Aba 2: Estatísticas Interativas ---
    with tab2:
        st.header("Estatísticas Interativas")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Distribuição por Ramo do Direito (Top 15)")
            if "Ramo Direito" in df.columns:
                ramo_counts = df["Ramo Direito"].value_counts().nlargest(15).reset_index()
                ramo_counts.columns = ["Ramo Direito", "Contagem"]
                fig_ramo = px.bar(
                    ramo_counts, 
                    x="Contagem", 
                    y="Ramo Direito", 
                    title="Top 15 Ramos do Direito",
                    text_auto=True,
                    orientation='h',
                    color_discrete_sequence=["#c9a227"]
                )
                fig_ramo.update_layout(
                    plot_bgcolor="#1a1a1a",
                    paper_bgcolor="#0e0e0e",
                    font_color="#ffffff",
                    xaxis_title="Número de Julgados",
                    yaxis_title="Ramo do Direito",
                    margin=dict(l=10, r=10, t=40, b=10)
                )
                st.plotly_chart(fig_ramo, use_container_width=True)
            else:
                st.warning("Coluna 'Ramo Direito' não encontrada.")

        with col2:
            st.subheader("Distribuição por Repercussão Geral")
            if "Repercussão Geral" in df.columns:
                rg_counts = df["Repercussão Geral"].value_counts().reset_index()
                rg_counts.columns = ["Repercussão Geral", "Contagem"]
                fig_rg = px.pie(
                    rg_counts, 
                    names="Repercussão Geral", 
                    values="Contagem", 
                    title="Julgados com Repercussão Geral",
                    color_discrete_sequence=["#c9a227", "#555555"]
                )
                fig_rg.update_layout(
                    plot_bgcolor="#1a1a1a",
                    paper_bgcolor="#0e0e0e",
                    font_color="#ffffff",
                    margin=dict(l=10, r=10, t=40, b=10)
                )
                st.plotly_chart(fig_rg, use_container_width=True)
            else:
                st.warning("Coluna 'Repercussão Geral' não encontrada.")

        st.subheader("Distribuição por Classe Processual (Top 15)")
        if "Classe Processo" in df.columns:
            classe_counts = df["Classe Processo"].value_counts().nlargest(15).reset_index()
            classe_counts.columns = ["Classe Processo", "Contagem"]
            fig_classe = px.bar(
                classe_counts, 
                x="Classe Processo", 
                y="Contagem", 
                title="Top 15 Classes Processuais", 
                text_auto=True,
                color_discrete_sequence=["#c9a227"]
            )
            fig_classe.update_layout(
                plot_bgcolor="#1a1a1a",
                paper_bgcolor="#0e0e0e",
                font_color="#ffffff",
                xaxis_title="Classe Processual",
                yaxis_title="Número de Julgados",
                margin=dict(l=10, r=10, t=40, b=10)
            )
            st.plotly_chart(fig_classe, use_container_width=True)
        else:
            st.warning("Coluna 'Classe Processo' não encontrada.")

    # --- Aba 3: Assertivas para Estudo ---
    with tab3:
        st.header("Assertivas para Estudo")
        st.write("Teste seus conhecimentos com assertivas baseadas nos informativos do STF.")
        
        # Botão para gerar novas assertivas
        if st.button("Gerar Novas Assertivas"):
            # Gerar assertivas baseadas nos dados
            assertivas = generate_assertivas(df)
            
            # Armazenar as assertivas na sessão
            st.session_state.assertivas = assertivas
            st.session_state.respostas = {}
            st.session_state.feedback = {}
        
        # Verificar se já existem assertivas na sessão
        if 'assertivas' not in st.session_state:
            st.session_state.assertivas = generate_assertivas(df)
            st.session_state.respostas = {}
            st.session_state.feedback = {}
        
        # Exibir as assertivas
        for i, assertiva in enumerate(st.session_state.assertivas):
            st.markdown(f"""
            <div class="assertiva-card">
                <div class="assertiva-text">{i+1}. {assertiva['texto']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Opções para o usuário responder
            col1, col2 = st.columns(2)
            with col1:
                verdadeiro = st.button("Verdadeiro", key=f"v_{i}")
                if verdadeiro:
                    st.session_state.respostas[i] = True
                    if assertiva['correta'] == True:
                        st.session_state.feedback[i] = True
                    else:
                        st.session_state.feedback[i] = False
            
            with col2:
                falso = st.button("Falso", key=f"f_{i}")
                if falso:
                    st.session_state.respostas[i] = False
                    if assertiva['correta'] == False:
                        st.session_state.feedback[i] = True
                    else:
                        st.session_state.feedback[i] = False
            
            # Exibir feedback se o usuário já respondeu
            if i in st.session_state.feedback:
                if st.session_state.feedback[i]:
                    st.markdown(f"""
                    <div class="assertiva-feedback-correct">
                        ✅ <strong>Correto!</strong> {assertiva['explicacao']}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div class="assertiva-feedback-incorrect">
                        ❌ <strong>Incorreto.</strong> {assertiva['explicacao']}
                    </div>
                    """, unsafe_allow_html=True)
            
            st.markdown("<hr>", unsafe_allow_html=True)
        
        # Exibir pontuação se todas as assertivas foram respondidas
        if len(st.session_state.respostas) == len(st.session_state.assertivas):
            acertos = sum(st.session_state.feedback.values())
            total = len(st.session_state.assertivas)
            st.success(f"Você acertou {acertos} de {total} assertivas! ({acertos/total*100:.1f}%)")

    # --- Aba 4: Pergunte para a Result ---
    with tab4:
        st.header("Pergunte para a Result")
        st.markdown("Faça sua pergunta sobre os informativos do STF listados neste dashboard.")

        user_question = st.text_area("Digite sua pergunta aqui:")
        ask_button = st.button("Enviar Pergunta")

        if ask_button and user_question:
            # Simular uma resposta da IA
            resposta = simulate_ia_response(user_question, df)
            
            st.markdown("""
            <div class="resposta-card">
                <h3>Resposta da Result:</h3>
            """, unsafe_allow_html=True)
            
            st.markdown(resposta)
            
            st.markdown("</div>", unsafe_allow_html=True)
            
        elif ask_button:
            st.warning("Por favor, digite uma pergunta antes de enviar.")

    # Footer
    st.markdown("""
    <div class="footer">
        Dashboard desenvolvido para Prof. Leonardo Aquino | © 2025 | Todos os direitos reservados
    </div>
    """, unsafe_allow_html=True)

else:
    st.error("Não foi possível carregar os dados para o dashboard.")
