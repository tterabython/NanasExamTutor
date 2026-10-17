import streamlit as st
from PIL import Image
import random
import time
import os

# Page Configuration
st.set_page_config(
    page_title="Nana's Official ICF PCC Exam Simulator 💖", 
    page_icon="🧠", 
    layout="centered"
)

# Custom Styling (Pink Aesthetic)
st.markdown("""
    <style>
    .main, .stApp {
        background-color: #fff0f5 !important;
        color: #4a2e35 !important;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #d81b60 !important;
    }
    p, label, span {
        color: #4a2e35 !important;
        font-weight: 500;
    }
    div.row-widget.stRadio div[role="radiogroup"] label {
        color: #4a2e35 !important;
        background-color: transparent !important;
    }
    .stRadio label div[data-testid="stMarkdownContainer"] p {
        color: #4a2e35 !important;
        background-color: transparent !important;
    }
    input[type="radio"] {
        accent-color: #ff69b4 !important;
    }
    .stButton>button {
        background-color: #ff69b4 !important;
        color: white !important;
        border-radius: 20px;
        font-weight: bold;
        width: 100%;
        padding: 10px;
        border: none !important;
    }
    .stButton>button:hover {
        background-color: #ff1493 !important;
        color: white !important;
    }
    div.stFormSubmitButton > button, button[type="submit"] {
        background-color: #ff69b4 !important;
        color: white !important;
        border-radius: 20px !important;
        font-weight: bold !important;
        width: 100% !important;
        padding: 10px !important;
        border: none !important;
    }
    div.stFormSubmitButton > button:hover, button[type="submit"]:hover {
        background-color: #ff1493 !important;
        color: white !important;
    }
    .competency-box {
        background-color: #ffffff !important;
        color: #333333 !important;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #ff69b4;
        margin-bottom: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    .competency-box strong, .competency-box p, .competency-box em, .competency-box code {
        color: #333333 !important;
        background-color: transparent !important;
    }
    .bloom-tag {
        background-color: #fce4ec !important;
        color: #c2185b !important;
        padding: 3px 8px;
        border-radius: 5px;
        font-size: 0.85em;
        font-weight: bold;
    }
    .part-b-warning {
        background-color: #ffebee !important;
        color: #c62828 !important;
        padding: 12px;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
        border: 1px solid #ffcdd2;
    }
    .break-box {
        background-color: #ffffff !important;
        color: #333333 !important;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        border: 2px dashed #ff69b4;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    .timer-box {
        background-color: #e8f5e9 !important;
        color: #2e7d32 !important;
        padding: 12px;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        font-size: 1.2em;
        margin-bottom: 20px;
        border: 1px solid #c8e6c9;
    }
    </style>
""", unsafe_allow_html=True)

# FULL CONSOLIDATED QUESTION POOL (Consolidated from all study modules)
ALL_QUESTIONS_POOL = [
    # SECTION A: ETHICS, AGREEMENTS & FOUNDATION
    {
        "section": "Part A",
        "question": "A coach is working with a client through a third-party coaching platform. The platform stores session recordings and shares performance analytics with sponsors. What is the BEST course of action for the coach?",
        "options": [
            "A) Inform the client about the platform’s data policies and obtain informed consent before proceeding.",
            "B) Proceed with coaching assuming the platform has already handled all legal and ethical disclosures.",
            "C) Ask the platform to anonymize data but do not inform the client.",
            "D) Share only general feedback with the sponsor without discussing data handling."
        ],
        "answer": 0,
        "competency": "Ethical Standard 2.5 – Technology and Confidentiality",
        "bloom": "Evaluating",
        "feedback": "Best: Inform the client and obtain informed consent. (Worst: Proceeding assuming the platform handled disclosures)."
    },
    {
        "section": "Part A",
        "question": "A coach is also a certified nutritionist. During a coaching session, the client asks for dietary advice. What is the WORST way for the coach to respond?",
        "options": [
            "A) Provide detailed nutritional advice without clarifying the shift in role.",
            "B) Explain the distinction between coaching and nutrition advice, and re-contract if the client wants to proceed.",
            "C) Refer the client to a separate nutrition session and document the change.",
            "D) Ask the client if they’d prefer to explore their goals through coaching or receive expert advice."
        ],
        "answer": 0,
        "competency": "Ethical Standard 3.7 – Role Clarity and Boundaries",
        "bloom": "Analyzing",
        "feedback": "Worst: Providing direct advice without role clarity. (Best: Explaining the distinction and re-contracting)."
    },
    {
        "section": "Part A",
        "question": "A client expresses discomfort and wants to end the coaching engagement immediately. What is the BEST response from the coach?",
        "options": [
            "A) Respect the client’s decision and offer a voluntary closure session.",
            "B) Insist on one final session to discuss the coach’s perspective.",
            "C) Delay termination until the coach has had a chance to review the contract.",
            "D) Ask the client to reconsider and continue for at least one more session."
        ],
        "answer": 0,
        "competency": "Ethical Standard 1.2 – Termination Rights",
        "bloom": "Applying",
        "feedback": "Best: Respect the client's decision and offer a voluntary closure session."
    },
    {
        "section": "Part A",
        "question": "A coach refers a client to a leadership assessment tool from which the coach receives a commission. What is the BEST ethical practice?",
        "options": [
            "A) Disclose the referral benefit to the client and allow them to make an informed decision.",
            "B) Recommend the tool without mentioning the commission.",
            "C) Mention the tool as an option but avoid discussing compensation.",
            "D) Use the tool and include the cost in the coaching fee without explanation."
        ],
        "answer": 0,
        "competency": "Ethical Standard 3.8 – Referral Disclosure",
        "bloom": "Evaluating",
        "feedback": "Best: Disclose the referral benefit fully to enable an informed decision."
    },
    {
        "section": "Part A",
        "question": "Coach Alex is working with a client who begins to share details about their mental health diagnosis. Alex is not a licensed therapist. What is the BEST response?",
        "options": [
            "A) Continue coaching and offer advice based on personal experience.",
            "B) Refer the client to a licensed mental health professional and clarify coaching boundaries.",
            "C) Ignore the mental health disclosure and proceed with the session.",
            "D) Ask the client to stop discussing mental health topics completely."
        ],
        "answer": 1,
        "competency": "ICF Ethics Standard 1.06, 1.07 – Scope & Boundaries",
        "bloom": "Evaluating",
        "feedback": "Best: Refer the client to a licensed professional while maintaining clear boundaries."
    },
    {
        "section": "Part A",
        "question": "Coach Jamie is coaching a team and also serves as their HR manager. During a session, a team member shares concerns about job security. What is the BEST action?",
        "options": [
            "A) Report the concern to upper management immediately.",
            "B) Clarify the dual role and revisit confidentiality agreements.",
            "C) Assure the team member their job is safe.",
            "D) Ignore the concern to avoid conflict."
        ],
        "answer": 1,
        "competency": "ICF Ethics Standard 3.1, 3.2 – Dual Roles & Conflicts",
        "bloom": "Analyzing",
        "feedback": "Best: Clarify dual roles and revisit confidentiality agreements transparently."
    },
    {
        "section": "Part A",
        "question": "Coach Morgan notices that a client is no longer making progress and seems disengaged during sessions. What is the BEST action?",
        "options": [
            "A) Continue coaching and hope engagement improves naturally.",
            "B) Discuss the shift in value and explore alternatives or termination.",
            "C) Terminate the coaching relationship immediately without discussion.",
            "D) Reduce session frequency without discussion."
        ],
        "answer": 1,
        "competency": "ICF Ethics Standard 4.3 – Value & Effectiveness",
        "bloom": "Evaluating",
        "feedback": "Best: Openly discuss the shift in value and explore alternatives with the client."
    },
    {
        "section": "Part A",
        "question": "Coach Dana uses AI transcription tools during sessions but hasn’t informed clients. What is the BEST ethical action?",
        "options": [
            "A) Continue using the tools without disclosure.",
            "B) Inform clients and obtain explicit informed consent before using tools.",
            "C) Stop using the tools entirely and delete everything secretly.",
            "D) Use the tools only for internal review."
        ],
        "answer": 1,
        "competency": "ICF Ethics Standard 2.5 – Informed Consent & AI",
        "bloom": "Applying",
        "feedback": "Best: Inform clients and obtain consent regarding data storage and technology usage."
    },

    # SECTION B: ADVANCED SCENARIOS & TOOLS
    {
        "section": "Part B",
        "question": "A coach is working with a senior executive facing pressure from their board. The client discloses confidential information about potential layoffs affecting thousands. The coach also coaches another executive in the same company. What is the BEST course of action?",
        "options": [
            "A) Disclose the information to the second client to prepare them.",
            "B) Seek supervision and reflect on how to manage the situation without breaching confidentiality.",
            "C) Terminate both coaching relationships immediately.",
            "D) Ignore the issue and continue coaching both clients as if nothing was disclosed."
        ],
        "answer": 1,
        "competency": "ICF Code of Ethics Standard 2.1, 2.3, 3.1 – Complex Confidentiality",
        "bloom": "Evaluating",
        "feedback": "Best: Seek supervision to reflect and maintain strict confidentiality between individual clients."
    },
    {
        "section": "Part B",
        "question": "When considering referring a client to therapy due to signs of mental health distress, what should be the FIRST step?",
        "options": [
            "A) Terminate the coaching contract instantly.",
            "B) Discuss concerns collaboratively with the client and explore readiness.",
            "C) Contact a therapist directly on their behalf.",
            "D) Document the behavior and say nothing."
        ],
        "answer": 1,
        "competency": "Referral Best Practice – Competency 1",
        "bloom": "Applying",
        "feedback": "Best: Discuss concerns transparently and collaboratively with the client."
    },
    {
        "section": "Part B",
        "question": "A coach uses the Wheel of Life with a client who becomes visibly distressed when rating their relationships. The coach suspects unresolved trauma. What should the coach do?",
        "options": [
            "A) Push further with intense questioning.",
            "B) Pause, hold space, and refer the client to a trauma-informed therapist if appropriate.",
            "C) Avoid the topic in all future sessions.",
            "D) Use visualization to force a positive mood."
        ],
        "answer": 1,
        "competency": "Tool Usage & Boundaries – Competency 1 & 4",
        "bloom": "Evaluating",
        "feedback": "Best: Hold space safely and assess if referral to a trauma specialist is needed."
    },
    {
        "section": "Part B",
        "question": "A client is overly focused on their MBTI 'Thinking' preference to dismiss emotional intelligence at work. What is the coach's best response?",
        "options": [
            "A) Invite the client to explore the value and integration of emotional awareness.",
            "B) Ban personality assessments from future sessions.",
            "C) Refer the client to therapy.",
            "D) Agree that emotion has no place in leadership."
        ],
        "answer": 0,
        "competency": "Competency 7: Evokes Awareness & Assessment Literacy",
        "bloom": "Analyzing",
        "feedback": "Best: Invite the client to reflect on how emotional awareness enhances their effective leadership."
    },
    {
        "section": "Part B",
        "question": "A coach notices that a client frequently deflects questions about their goals and focuses entirely on external office gossip. Which competency should be prioritized?",
        "options": [
            "A) Establishes and Maintains Agreements",
            "B) Evokes Awareness",
            "C) Facilitates Client Growth",
            "D) Listens Actively"
        ],
        "answer": 1,
        "competency": "Competency 7: Evokes Awareness",
        "bloom": "Analyzing",
        "feedback": "Best: Evokes Awareness helps the client notice the pattern of deflection and connect back to their goal."
    },
    {
        "section": "Part B",
        "question": "A client shares a breakthrough insight during a session. Which competency guides the coach to help the client translate this insight into tangible next steps?",
        "options": [
            "A) Facilitates Client Growth",
            "B) Evokes Awareness",
            "C) Establishes Agreements",
            "D) Listens Actively"
        ],
        "answer": 0,
        "competency": "Competency 8: Facilitates Client Growth",
        "bloom": "Applying",
        "feedback": "Best: Facilitates Client Growth transforms insights into actionable learning and sustainable progress."
    },
    {
        "section": "Part B",
        "question": "A corporate sponsor hires you to coach a senior leader and demands monthly updates on 'leadership weaknesses discussed in coaching.' The client hasn't consented. What is the BEST action?",
        "options": [
            "A) Negotiate with both client and sponsor to clarify confidentiality boundaries upfront.",
            "B) Provide the weakness reports as requested to maintain the contract.",
            "C) Refuse to work with the sponsor and terminate immediately.",
            "D) Secretly share general weaknesses without names."
        ],
        "answer": 0,
        "competency": "Competency 3 & Ethics 2.2 – Stakeholder Alignment",
        "bloom": "Evaluating",
        "feedback": "Best: Revisit agreements and clarify strict confidentiality boundaries with all stakeholders."
    },
    {
        "section": "Part B",
        "question": "During a virtual coaching session, a client's spouse unexpectedly joins the call and begins contributing to the session without prior notice. What should the coach do?",
        "options": [
            "A) Pause the conversation and renegotiate confidentiality and session agreements.",
            "B) Allow the spouse to participate without mentioning boundaries.",
            "C) Ignore the spouse and speak only to the client.",
            "D) End the video call abruptly."
        ],
        "answer": 0,
        "competency": "Competency 3 & Ethics 2.4 – Agreement & Privacy Boundaries",
        "bloom": "Applying",
        "feedback": "Best: Pause and renegotiate agreements regarding attendance and confidentiality."
    }
]

def load_nana_image():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    possible_names = [
        "nana.jpg", "Nana.jpg", "NANA.JPG", "nana.JPG", 
        "nana.jpeg", "Nana.jpeg", "NANA.JPEG", "nana.JPEG"
    ]
    for name in possible_names:
        full_path = os.path.join(script_dir, name)
        if os.path.exists(full_path):
            try:
                return Image.open(full_path)
            except Exception:
                continue
    return None

def main():
    st.title("💖 Nana's Official ICF Exam Simulator 💖")
    st.markdown("<h4 style='text-align: center; color: #880e4f;'>Master Question Bank (Randomized 60-Question Challenge) 🚀✨</h4>", unsafe_allow_html=True)
    st.markdown("---")

    # Initialize Session States & Dynamic Selection
    if "stage" not in st.session_state:
        st.session_state.stage = "part_a"
        
        part_a_pool = [q for q in ALL_QUESTIONS_POOL if q["section"] == "Part A"]
        part_b_pool = [q for q in ALL_QUESTIONS_POOL if q["section"] == "Part B"]
        
        random.shuffle(part_a_pool)
        random.shuffle(part_b_pool)
        
        # Pull 30 from each pool to form a complete 60-question test
        st.session_state.part_a_q = part_a_pool[:30] if len(part_a_pool) >= 30 else part_a_pool
        st.session_state.part_b_q = part_b_pool[:30] if len(part_b_pool) >= 30 else part_b_pool
        
        st.session_state.exam_start_time = time.time()

    if "part_a_answers" not in st.session_state:
        st.session_state.part_a_answers = []
    if "part_b_answers" not in st.session_state:
        st.session_state.part_b_answers = []
    if "score" not in st.session_state:
        st.session_state.score = 0

    # Live Timer
    elapsed_seconds = int(time.time() - st.session_state.exam_start_time)
    remaining_seconds = max(0, (2 * 3600) - elapsed_seconds)
    hours_left = remaining_seconds // 3600
    minutes_left = (remaining_seconds % 3600) // 60
    seconds_left = remaining_seconds % 60

    # --- PART A (Section 1) ---
    if st.session_state.stage == "part_a":
        st.markdown(f"<div class='timer-box'>⏳ Time Remaining: {hours_left:02d}:{minutes_left:02d}:{seconds_left:02d} | Section 1: Part A ({len(st.session_state.part_a_q)} Questions)</div>", unsafe_allow_html=True)
        
        with st.form("part_a_form"):
            user_answers = []
            for i, q in enumerate(st.session_state.part_a_q):
                st.markdown(f"**Question {i+1}:** {q['question']}")
                st.markdown(f"<span class='bloom-tag'>🧠 Level: {q['bloom']}</span>", unsafe_allow_html=True)
                choice = st.radio(
                    "Select the best coaching action:", 
                    q['options'], 
                    key=f"pa_q_{i}",
                    index=None
                )
                user_answers.append(choice)
                st.markdown("---")
            
            submit_a = st.form_submit_button("Submit Part A & Take Break ☕")

            if submit_a:
                if any(ans is None for ans in user_answers):
                    st.warning("⚠️ Please answer every question before proceeding, Nana! 💕")
                else:
                    st.session_state.part_a_answers = user_answers
                    st.session_state.stage = "break"
                    st.rerun()

    # --- BREAK ---
    elif st.session_state.stage == "break":
        st.subheader("☕ Scheduled Break")
        st.markdown(f"<div class='timer-box'>⏳ Total Time Remaining: {hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}</div>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class='break-box'>
            <h3>Awesome job completing Part A! 🎉</h3>
            <p>Take a breath, grab a coffee or water, and click below when you're ready to tackle <b>Part B</b> (Advanced Scenarios)!</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("---")
        
        if st.button("🚀 Start Part B (Advanced Case Scenarios)"):
            st.session_state.stage = "part_b"
            st.rerun()

    # --- PART B (Section 2) ---
    elif st.session_state.stage == "part_b":
        st.markdown(f"<div class='timer-box'>⏳ Time Remaining: {hours_left:02d}:{minutes_left:02d}:{seconds_left:02d} | Section 2: Part B ({len(st.session_state.part_b_q)} Questions)</div>", unsafe_allow_html=True)
        st.markdown("<div class='part-b-warning'>⚠ Section 2: Advanced Case Scenarios & Ethical Dilemmas</div>", unsafe_allow_html=True)
        
        with st.form("part_b_form"):
            user_answers = []
            for i, q in enumerate(st.session_state.part_b_q):
                st.markdown(f"**Question {i+1}:** {q['question']}")
                st.markdown(f"<span class='bloom-tag'>🧠 Level: {q['bloom']}</span>", unsafe_allow_html=True)
                choice = st.radio(
                    "Select the best coaching action:", 
                    q['options'], 
                    key=f"pb_q_{i}",
                    index=None
                )
                user_answers.append(choice)
                st.markdown("---")
            
            submit_b = st.form_submit_button("Submit Exam & View Final Score 🏆")

            if submit_b:
                if any(ans is None for ans in user_answers):
                    st.warning("⚠️ Please complete all questions in Part B! 💕")
                else:
                    st.session_state.part_b_answers = user_answers
                    
                    total_score = 0
                    feedback_log = []
                    
                    for i, q in enumerate(st.session_state.part_a_q):
                        selected_idx = q['options'].index(st.session_state.part_a_answers[i])
                        is_correct = (selected_idx == q['answer'])
                        if is_correct:
                            total_score += 1
                        feedback_log.append(("Part A", i+1, is_correct, q['competency'], q['bloom'], q['feedback']))
                    
                    for i, q in enumerate(st.session_state.part_b_q):
                        selected_idx = q['options'].index(st.session_state.part_b_answers[i])
                        is_correct = (selected_idx == q['answer'])
                        if is_correct:
                            total_score += 1
                        feedback_log.append(("Part B", i+1, is_correct, q['competency'], q['bloom'], q['feedback']))
                    
                    st.session_state.score = total_score
                    st.session_state.feedback_log = feedback_log
                    st.session_state.stage = "results"
                    st.rerun()

    # --- RESULTS ---
    else:
        score = st.session_state.score
        total = len(st.session_state.part_a_q) + len(st.session_state.part_b_q)
        percentage = int((score / total) * 100) if total > 0 else 0

        st.subheader("📊 Official Mock Exam Results")
        
        col1, col2 = st.columns([1, 2])
        with col1:
            img = load_nana_image()
            if img:
                st.image(img, caption="Nana, Certified Coach! 🌟", use_container_width=True)
            else:
                st.info("💡 Saved image `nana.jpeg` will appear here!")
        
        with col2:
            if percentage >= 75:
                st.balloons()
                st.success(f"🏆 Final Score: {score}/{total} ({percentage}%)!\n\n**Incredible job!** You have fully mastered the ICF PCC Competencies!")
            elif percentage >= 50:
                st.snow()
                st.info(f"✨ Final Score: {score}/{total} ({percentage}%)!\n\n**Solid effort!** Review the feedback breakdown below to sharpen your edge!")
            else:
                st.warning(f"🌱 Final Score: {score}/{total} ({percentage}%)!\n\n**Great practice run!** Use the breakdown below to review key ethics and competencies.")

        st.markdown("---")
        st.markdown("### 📝 Mentorship Feedback Breakdown:")
        
        for section, q_num, is_correct, comp, bloom_level, feedback_text in st.session_state.feedback_log:
            status = "✅ Correct" if is_correct else "💡 Key Learning:"
            st.markdown(f"""
            <div class="competency-box">
                <strong>{section} - Q{q_num} — {status}</strong> <span class="bloom-tag">🧠 {bloom_level}</span><br>
                <em>Focus Area:</em> <code>{comp}</code><br>
                <p style="margin-top: 8px;">{feedback_text}</p>
            </div>
            """, unsafe_allow_html=True)

        if st.button("🔄 Retake Full Exam (Pulls Fresh Random Shuffled Questions!)"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

if __name__ == "__main__":
    main()
    
