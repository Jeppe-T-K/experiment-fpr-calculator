import streamlit as st

def Navbar():
    # builds the sidebar menu
    st.sidebar.page_link('main.py', label='Home', icon='🔥')
    st.sidebar.page_link('pages/p_value_calc.py', label='P-value calculator', icon='🛡️')
    st.sidebar.page_link('pages/estimating_false_positive_risk.py', label='Estimating the false positive risk', icon='🛡️')
    st.sidebar.page_link('pages/p_value_calc.py', label='Estimating the success rate', icon='🛡️')

    st.sidebar.markdown("# Your decided-upon experiment parameters:")
    alpha = st.sidebar.slider("α", 0.0, 0.20, 0.025, 0.001, format="%f")
    beta = 1 - st.sidebar.slider("Power (1-β)", 0.0, 1.0, 0.80)
    return (alpha, beta)