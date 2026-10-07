"""Interactive APC demonstration dashboard.

Run with: streamlit run app.py
The defaults are illustrative assumptions, not a valuation.
"""
import pandas as pd
import streamlit as st
from dcf_engine import DCFInputs, dcf_value, sensitivity_matrix, terminal_value

st.set_page_config(page_title="UK Commercial Property DCF Lab", page_icon="🏢", layout="wide")
st.title("UK Commercial Property DCF Lab")
st.caption("Transparent growth-explicit modelling • evidence-led assumptions • professional judgement")
st.warning("Educational decision-support model — not an RICS valuation or investment advice.")

with st.sidebar:
    st.header("Valuer assumptions")
    passing_rent = st.number_input("Year 1 net income (£)", 0, 10_000_000, 332_172, step=5_000)
    growth = st.slider("Annual income growth", 0.0, 6.0, 2.5, 0.1) / 100
    discount = st.slider("Discount rate", 3.0, 15.0, 8.0, 0.1) / 100
    exit_yield = st.slider("Exit yield", 3.0, 12.0, 6.5, 0.1) / 100
    years = st.slider("Explicit forecast (years)", 5, 15, 10)
    sale_cost = st.slider("Sale costs", 0.0, 5.0, 1.5, 0.1) / 100

cashflows=[passing_rent*((1+growth)**(y-1)) for y in range(1,years+1)]
terminal_erv=passing_rent*((1+growth)**years)
inputs=DCFInputs(cashflows,discount,terminal_erv,exit_yield,sale_cost)
value=dcf_value(inputs)
tv=terminal_value(terminal_erv,exit_yield,sale_cost)
pv_tv=tv/((1+discount)**years)
pv_income=value-pv_tv

a,b,c,d=st.columns(4)
a.metric("DCF indication",f"£{value:,.0f}")
b.metric("PV explicit income",f"£{pv_income:,.0f}")
c.metric("PV terminal value",f"£{pv_tv:,.0f}")
d.metric("Terminal value share",f"{pv_tv/value:.1%}")

st.subheader("Cash-flow transparency")
df=pd.DataFrame({"Year":range(1,years+1),"Net cash flow":cashflows})
df["Discount factor"]=[1/((1+discount)**y) for y in df["Year"]]
df["Present value"]=df["Net cash flow"]*df["Discount factor"]
st.dataframe(df.style.format({"Net cash flow":"£{:,.0f}","Discount factor":"{:.4f}","Present value":"£{:,.0f}"}),use_container_width=True)
st.line_chart(df.set_index("Year")[["Net cash flow","Present value"]])

st.subheader("Two-way sensitivity: discount rate × exit yield")
drs=[discount+x for x in (-.01,-.005,0,.005,.01)]
eys=[exit_yield+x for x in (-.01,-.005,0,.005,.01)]
matrix=sensitivity_matrix(cashflows,terminal_erv,drs,eys,sale_cost)
sens=pd.DataFrame(matrix).T
sens.index=[f"{x:.1%}" for x in sens.index]
sens.columns=[f"{x:.1%}" for x in sens.columns]
st.dataframe(sens.style.format("£{:,.0f}"),use_container_width=True)
st.caption("Rows: discount rate. Columns: exit yield. Sensitivity exposes model risk rather than hiding it.")

st.subheader("Valuer judgement checkpoint")
st.markdown("""
**Before adopting any conclusion, evidence should support:** ERV and rental growth; discount rate; exit yield;
lease events and void/reletting assumptions; purchaser/sale costs; and the forecast horizon.

**Market Value discipline:** inputs should reflect market-participant expectations and be reconciled to transaction evidence.
Investor-specific inputs may instead indicate Investment Value (worth).

> **The model calculates; the valuer concludes.**
""")
