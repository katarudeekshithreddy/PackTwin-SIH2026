# 🌱 PackTwin: Physics-Informed Compliance Engine

**Smart India Hackathon 2026 — Idea Submission**
**Team:** Debuggers_IIITDh

## Overview
PackTwin is an AI-powered packaging recommendation engine designed for Indian food MSMEs. It bridges the gap between complex regulatory texts (FSSAI) and practical packaging physics (Arrhenius kinetics).

## Technical Architecture
*   **Physics Core:** SciPy ODE solver for Arrhenius shelf-life decay and WVTR moisture ingress.
*   **Compliance Agent:** LangChain + ChromaDB for FSSAI clause retrieval (RAG).
*   **Dashboard:** Built with Streamlit for MSME accessibility.

## Repository Contents
*   `packtwin_mockup.py` - The Streamlit UI dashboard prototype.
*   `PackTwin_PS26236_SIH2026.pdf` - Our official SIH presentation.

## How to run the UI Prototype
```bash
pip install streamlit
streamlit run packtwin_mockup.py
```
