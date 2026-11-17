import re
import math
import time
from collections import Counter
import streamlit as st

# ==============================================================================
# 1. STREAMLIT PAGE SETUP
# ==============================================================================
st.set_page_config(page_title="CollegeGPT - SJCEM", page_icon="🎓", layout="centered")

st.title("🎓 CollegeGPT: SJCEM Assistant")
st.caption("Simple From-Scratch Language Model • All SJCEM Data Built Directly in Code")

# ==============================================================================
# 2. COMPLETE IN-CODE SJCEM DATASET (NO EXTERNAL FILES OR RAG NEEDED)
# ==============================================================================
SJCEM_DATA = [
    {
        "topic": "College Overview, NAAC Grade & Autonomy",
        "keywords": "what is sjcem overview about college naac grade autonomous aicte university mumbai aldel trust rank ranking",
        "response": (
            "St. John College of Engineering and Management (SJCEM) was established in 2008 in Palghar by the "
            "Aldel Education Trust (a Christian Religious Minority Institution). It is an UGC Autonomous institute "
            "accredited with NAAC Grade A+, approved by AICTE, and affiliated with the University of Mumbai (for Degree/PG) "
            "and MSBTE (for Diploma). SJCEM is ranked 10th overall among Engineering Colleges in the MMRDA region."
        )
    },
    {
        "topic": "Campus Location & Address",
        "keywords": "where is sjcem located address location reach palghar station highway campus size acres manor road vevoor",
        "response": (
            "SJCEM is situated on a 10-acre campus at St. John Technical Campus, Village Vevoor, Manor Road, "
            "Palghar (East), Palghar District - 401404, Maharashtra. It is located about 1.5 km from Palghar Railway Station "
            "and 18 km from Manor (Mastaan Naka) on the Mumbai-Ahmedabad Western Express Highway."
        )
    },
    {
        "topic": "Principal & Management",
        "keywords": "who is principal chairman director head management kamal shah albert dsouza trust",
        "response": (
            "The Principal of St. John College of Engineering and Management is Dr. Kamal Shah. "
            "The institution is governed by the Aldel Education Trust under Chairman Mr. Albert W. D'Souza."
        )
    },
    {
        "topic": "Courses, Branches & Seat Intake",
        "keywords": "courses branches offered seats intake btech be engineering diploma mba mms mca computer aiml it data science civil mechanical extc ecs",
        "response": (
            "SJCEM offers Undergraduate B.E., Postgraduate (MMS/MBA, MCA), and 3-year Diploma programs:\n"
            "- **B.E. Computer Engineering:** 120 seats\n"
            "- **B.E. Artificial Intelligence & Machine Learning (AIML):** 60–120 seats\n"
            "- **B.E. Information Technology (IT):** 60 seats\n"
            "- **B.E. Data Science:** 60 seats\n"
            "- **B.E. Electronics & Computer Science (ECS):** 60 seats\n"
            "- **B.E. Electronics & Telecommunication (EXTC):** 60 seats\n"
            "- **B.E. Civil Engineering:** 120 seats\n"
            "- **B.E. Mechanical Engineering:** 120 seats\n"
            "- **PG & Diploma:** MMS/MBA (60 seats), MCA (60 seats), and Diploma in Civil, Mechanical, IT, and EXTC (60 seats each)."
        )
    },
    {
        "topic": "Fee Structure",
        "keywords": "fee fees structure cost tuition amount be btech mba mms diploma annual total",
        "response": (
            "The total 4-year tuition fee for B.E. programs (such as Computer Engineering and AIML) at SJCEM is "
            "approximately ₹3.57 Lakhs as per regulatory norms. First-year Diploma fees are around ₹65,544, and "
            "the 2-year MMS (MBA) total fee is approximately ₹2.40 Lakhs."
        )
    },
    {
        "topic": "Admission Process & Eligibility",
        "keywords": "admission admissions eligibility apply entrance exam cet jee main mht cap acap il institute level cutoff",
        "response": (
            "Admissions to First Year B.E. at SJCEM require passing 10+2 (HSC) with Physics, Chemistry, and Mathematics "
            "(minimum 45% marks) and a valid positive score in MHT-CET or JEE Main. For MMS/MBA, MAH-MBA-CET is accepted, "
            "and for MCA, MAH-MCA-CET is accepted. Seats are filled through Centralised Admission Process (CAP) rounds, "
            "ACAP rounds, and Institute Level (IL) rounds."
        )
    },
    {
        "topic": "Documents Required for Admission",
        "keywords": "documents document required needed list certificates marksheet verification form",
        "response": (
            "According to the college information available, the required documents for admission at SJCEM include:\n"
            "1. SSC (10th) and HSC (12th) Marksheets\n"
            "2. MHT-CET or JEE Main Scorecard\n"
            "3. College Leaving / Transfer Certificate\n"
            "4. Domicile and Nationality Certificate\n"
            "5. Aadhaar Card & Passport-size Photographs\n"
            "6. CAP Seat Allotment Letter (and Minority/Caste certificate if applicable)."
        )
    },
    {
        "topic": "Placements, Packages & Recruiters",
        "keywords": "placement placements company companies recruiters salary package median highest job tcs infosys wipro",
        "response": (
            "SJCEM has an active Training and Placement Cell with a 68.63% placement rate and a median salary package "
            "of ₹3.50 LPA (with top packages reaching ₹7–8 LPA). Leading recruiters visiting SJCEM include TCS, Infosys, "
            "Wipro, Capgemini, Accenture, IBM, and Tech Mahindra."
        )
    },
    {
        "topic": "Campus Facilities & Infrastructure",
        "keywords": "facilities facility library hostel bus transport canteen labs computer lab medical sports infrastructure",
        "response": (
            "SJCEM provides a Central Library, high-tech Computer Labs, a dedicated Language Lab, Seminar Halls, "
            "Auditorium, Hygienic Canteen, Hostel facilities, Medical Room, Sports grounds, and College Bus service "
            "operating from Palghar Railway Station."
        )
    },
    {
        "topic": "College Events, Fests & Student Chapters",
        "keywords": "events event fest hackathon megaleio megahack prastut sih chapters clubs csi iste ieee nss cultural",
        "response": (
            "Major annual events at SJCEM include **Megaleio** (National Technical Fest), **Megahack** (National Hackathon), "
            "**Smart India Hackathon (SIH)**, **Prastut** (Paper Presentation), Science Fest, and Annual Cultural Day. "
            "Active student chapters include CSI, ISTE, IEEE, ITSA, ASCAI, SAE, ACE, ISHRAE, and NSS."
        )
    },
    {
        "topic": "Contact Numbers, Emails & Website",
        "keywords": "contact phone number email call helpline website official office",
        "response": (
            "You can contact SJCEM through the following official channels:\n"
            "- **Phone:** +91-7709177843 / 02525-297279\n"
            "- **Engineering Degree Email:** office@sjcem.edu.in\n"
            "- **Engineering Diploma Email:** office_diploma@sjcem.edu.in\n"
            "- **MBA / MMS Email:** office_mms@sjcem.edu.in\n"
            "- **Official Website:** https://sjcem.edu.in/"
        )
    }
]

# ==============================================================================
# 3. SIMPLE FROM-SCRATCH LANGUAGE ENGINE (PURE PYTHON MATH - NO EXTERNAL LIBS)
# ==============================================================================
SYNONYMS = {
    "branch": "branches", "course": "courses", "program": "courses", "programs": "courses",
    "degree": "courses", "doc": "documents", "docs": "documents", "paper": "documents",
    "fee": "fees", "cost": "fees", "tuition": "fees", "job": "placements", "jobs": "placements",
    "package": "placements", "salary": "placements", "recruiter": "companies",
    "where": "located", "place": "located", "club": "chapters", "clubs": "chapters",
    "bus": "facilities", "hostel": "facilities", "library": "facilities", "canteen": "facilities",
    "number": "contact", "phone": "contact", "mail": "contact", "head": "principal"
}

def tokenize(text):
    words = re.findall(r"[a-z0-9]+", text.lower())
    return [SYNONYMS.get(w, w) for w in words]

def cosine_attention_score(query_tokens, doc_tokens):
    """Calculates pure-Python cosine similarity between question tokens and topic tokens."""
    q_counts = Counter(query_tokens)
    d_counts = Counter(doc_tokens)
    common = set(q_counts.keys()) & set(d_counts.keys())
    numerator = sum(q_counts[w] * d_counts[w] for w in common)
    sum_q = sum(v ** 2 for v in q_counts.values())
    sum_d = sum(v ** 2 for v in d_counts.values())
    denominator = math.sqrt(sum_q) * math.sqrt(sum_d)
    return numerator / denominator if denominator else 0.0

def generate_college_gpt_reply(user_question):
    """Finds the highest-attention SJCEM topic and generates the response token by token."""
    q_tokens = tokenize(user_question)
    best_score = -1.0
    best_item = SJCEM_DATA[0]

    for item in SJCEM_DATA:
        doc_tokens = tokenize(item["keywords"] + " " + item["topic"] + " " + item["response"])
        # Weight keyword matches higher for accurate topic selection
        kw_tokens = tokenize(item["keywords"])
        score = (cosine_attention_score(q_tokens, kw_tokens) * 0.75) + (cosine_attention_score(q_tokens, doc_tokens) * 0.25)
        if score > best_score:
            best_score = score
            best_item = item

    if best_score == 0:
        return (
            "I am **CollegeGPT for SJCEM, Palghar**. Please ask me about **courses, admission eligibility, "
            "required documents, fees, placements, facilities, events (Megaleio/Megahack), principal, or contact details**!",
            "General Help",
            0.0
        )

    return best_item["response"], best_item["topic"], round(best_score * 100, 1)

def stream_words(text):
    """Streams output word-by-word like a live GPT model."""
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)

# ==============================================================================
# 4. STREAMLIT SIDEBAR & CHAT INTERFACE
# ==============================================================================
with st.sidebar:
    st.header("⚡ Quick SJCEM Questions")
    st.caption("Click any button to test CollegeGPT:")
    sample_questions = [
        "What is SJCEM and its NAAC grade?",
        "What courses and seats are offered?",
        "What documents are required for admission?",
        "What is the fee structure at SJCEM?",
        "How are the placements and median salary?",
        "Where is SJCEM located?",
        "What are the college events and student chapters?",
        "What facilities are available on campus?",
        "Who is the Principal of SJCEM?",
        "How can I contact the college office?"
    ]
    clicked_question = None
    for q in sample_questions:
        if st.button(q, use_container_width=True):
            clicked_question = q

    st.divider()
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! I am **CollegeGPT** for **St. John College of Engineering and Management (SJCEM), Palghar**. Ask me anything about admissions, courses, fees, documents, placements, or campus life!"
        }
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask a question about SJCEM...")
active_prompt = clicked_question if clicked_question else user_input

if active_prompt:
    st.session_state.messages.append({"role": "user", "content": active_prompt})
    with st.chat_message("user"):
        st.markdown(active_prompt)

    reply_text, matched_topic, confidence = generate_college_gpt_reply(active_prompt)

    with st.chat_message("assistant"):
        st.write_stream(stream_words(reply_text))
        st.caption(f"Matched Topic: **{matched_topic}** | Token Attention Score: **{confidence}%**")

    st.session_state.messages.append({"role": "assistant", "content": reply_text})
    if clicked_question:
        st.rerun()