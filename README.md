# CollegeGPT: SJCEM Virtual Assistant

CollegeGPT is an intelligent, lightweight campus assistant tailored specifically for **St. John College of Engineering and Management (SJCEM)** in Palghar. Built with **Streamlit** and powered by a pure-Python cosine-attention matching mechanism, it answers queries regarding college admissions, departments, placements, cutoffs, campus facilities, and more — without requiring external LLM API keys or cloud dependencies.

---

## Key Features

- **Built-in SJCEM Knowledge Base**: Comprehensive data on NAAC Grade A+ accreditation, UGC autonomy, engineering & diploma branches, MMS, admissions, fees, hostel, canteen, and sports facilities.
- **Pure-Python Attention Mechanism**: Uses keyword & context tokenization with cosine similarity scoring to match user queries to the best relevant topic.
- **Interactive Streamlit Interface**: Clean chat UI with streaming token-by-token response simulation.
- **Confidence & Matching Metrics**: Displays the matched topic and token attention score with each answer.
- **Colab & Local Ready**: Run directly in your local terminal or via Google Colab with Cloudflare tunneling.

---

## Repository Structure

```text
College_GPT/
├── app.py              # Main Streamlit web application
├── CollegeGPT.ipynb    # Jupyter / Google Colab notebook
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

---

## Getting Started

### Prerequisites

Make sure you have **Python 3.8+** installed on your system.

### 1. Clone the Repository

```bash
git clone https://github.com/prathamore8806/College_GPT.git
cd College_GPT
```

### 2. Create and Activate a Virtual Environment (Recommended)

**On Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

Open your browser and navigate to `http://localhost:8501`.

---

## Running on Google Colab

If you want to run the project in the cloud:
1. Upload `CollegeGPT.ipynb` to [Google Colab](https://colab.research.google.com/).
2. Run the cells sequentially.
3. The notebook will automatically launch Streamlit and provide a public Cloudflare tunnel link to access the web app.

---

## Built With

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [pycloudflared](https://github.com/zen-audio/pycloudflared)

---

## License

This project is licensed under the [MIT License](LICENSE) (or Open Source).
