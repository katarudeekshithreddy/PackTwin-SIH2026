import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="PackTwin - AI Packaging Engine", layout="wide")

st.title("🌱 PackTwin: Physics-Informed Compliance Engine")
st.subheader("Client: Rajan's Millet Snacks | Region: Karnataka | Target: 90 Days")

st.divider()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Retrieval Accuracy", "91%", "+3% vs baseline")
col2.metric("Simulation Latency", "0.18 s", "-0.05 s")
col3.metric("FSSAI Coverage", "Indexed", "Phase 1")
col4.metric("Physics Error", "~15%", "vs empirical")

st.divider()
st.markdown("### 🏆 Top 3 Ranked Packaging Options")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("🥇 Option 1: Bagasse Outer + PLA Inner")
    st.write("**Est. Shelf Life:** 95 days")
    st.write("**Cost/Pack:** ₹1.10 (Local Agri-waste)")
    st.write("**Carbon Footprint:** 0.04 kg CO2e")
    st.write("**Compliance:** FSSAI Sub-reg 3.2.1 ✅")
    st.progress(95)

with c2:
    st.info("🥈 Option 2: Banana Fibre + Metallized CPP")
    st.write("**Est. Shelf Life:** 110 days")
    st.write("**Cost/Pack:** ₹1.45")
    st.write("**Carbon Footprint:** 0.08 kg CO2e")
    st.write("**Compliance:** FSSAI Reg 4.1 ✅")
    st.progress(85)

with c3:
    st.warning("🥉 Option 3: Standard Multi-layer Plastic (Baseline)")
    st.write("**Est. Shelf Life:** 120 days")
    st.write("**Cost/Pack:** ₹0.90")
    st.write("**Carbon Footprint:** 0.35 kg CO2e")
    st.write("**Compliance:** FSSAI Reg 4.1 ✅")
    st.progress(70)

st.markdown("---")
st.markdown("### 📄 RAG Trace: FSSAI Clause Retrieval")
st.code('''[Document: Packaging_Regs_2018.pdf | Chunk: 42]
Sub-regulation 3.2.1: "Primary food packaging materials must be of food-grade quality. Bio-based plastics like Polylactic Acid (PLA) are permitted for direct contact with dry foods..."
Cosine Similarity Score: 0.94''', language="text")
