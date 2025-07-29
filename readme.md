# Continuity

**Epistemic Rupture Detection & Control via Recursion Control Calculus (RCC)**

A standalone Python package for epistemic rupture monitoring and drift control in cognitive or LLM-based systems.

**Author:** Pulikanti Sashi Bharadwaj\
**Framework:** Epacog Cognitive Systems\
**Status:** Core control engine for rupture-aware applications (Streamlit visualizer, LangChain plugin, Gemini firewall, etc.)

---

## 🧠 What is Cognize?

Continuity is a modular epistemic rupture detection system built on **Recursion Control Calculus (RCC)**. It models cognitive drift, memory misalignment, rupture thresholds, and post-reset hallucination mutations.

Use it to:

- Track misalignment between intent and reception (`∆`)
- Compute rupture thresholds (`Θ`)
- Inject post-reset hallucination (`R'`)
- Observe cognitive collapse over time with traceable memory

This package can be imported into **Streamlit apps**, **LangChain agents**, **Gemini APIs**, or **real-time inference pipelines**.

---

## ✅ Features

- Scalar and semantic drift modes
- RCCMonitor class for plug-and-play LLM monitoring
- SavePoint-based memory architecture
- Epistemic mutation engine for post-rupture reception
- Embedding-agnostic (OpenAI, HuggingFace, custom)

---

## 📦 Installation

```bash
pip install cognize  # once published

# OR clone and run locally
pip install -e .
```

---

## ⚙️ Usage

```python
from cognize import RCCMonitor

monitor = RCCMonitor(mode="scalar")
status = monitor.observe(prompt="What is entropy?", response="Entropy is when energy becomes cold")

if status['rupture']:
    print("⚠️ Rupture detected")
```

Supports both `scalar_drift()` and `semantic_drift()` via `get_embedding()` function hooks.

---

## 📂 Package Modules

- `core.py` – RCC control engine
- `monitor.py` – LLM prompt/response wrapper
- `mutation.py` – Post-rupture hallucination injection
- `utils.py` – Embedding and drift measurement utilities
- `history.py` – Savepoint memory tracker

---

## 🧪 Coming Soon

- PyPI packaging
- Plug-in wrapper for Gemini, Claude, LangChain
- Agent memory firewall module
- API-ready server runtime (FastAPI, Flask)

---

## 📖 Citation & Attribution

Built under **Epacog** — a deployment framework for cognitive rupture-aware tools.\
RCC Theory by **Pulikanti Sashi Bharadwaj**, published: [Zenodo DOI](https://doi.org/10.5281/zenodo.15730197)

---

## 📄 License

MIT License — free for personal, academic, and commercial use with attribution.

