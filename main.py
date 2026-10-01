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

# Cute Custom Styling (Fixed Form Buttons, Radio Accents, and Dark Overrides)
st.markdown("""
    <style>
    /* Global background override for consistency */
    .main, .stApp {
        background-color: #fff0f5 !important;
        color: #4a2e35 !important;
    }
    
    /* Force crisp headers */
    h1, h2, h3, h4, h5, h6 {
        color: #d81b60 !important;
    }
    
    /* Force visible labels, paragraphs, and text */
    p, label, span {
        color: #4a2e35 !important;
        font-weight: 500;
    }
    
    /* Ensure radio button text and container backgrounds stay clean and transparent */
    div.row-widget.stRadio div[role="radiogroup"] label {
        color: #4a2e35 !important;
        background-color: transparent !important;
    }
    .stRadio label div[data-testid="stMarkdownContainer"] p {
        color: #4a2e35 !important;
        background-color: transparent !important;
    }
    
    /* Fix radio button selection dot color (makes them pink instead of solid black) */
    input[type="radio"] {
        accent-color: #ff69b4 !important;
    }
    
    /* Standard Buttons */
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
    
    /* Form Submit Buttons (Fixes the black submit button block) */
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
    
    /* Results feedback cards - forced clean white background with dark readable text */
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
    
    /* Bloom tags */
    .bloom-tag {
        background-color: #fce4ec !important;
        color: #c2185b !important;
        padding: 3px 8px;
        border-radius: 5px;
        font-size: 0.85em;
        font-weight: bold;
    }
    
    /* Part B warning banner */
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
    
    /* Break screen box */
    .break-box {
        background-color: #ffffff !important;
        color: #333333 !important;
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        border: 2px dashed #ff69b4;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    .break-box h3, .break-box p {
        color: #333333 !important;
    }
    
    /* Timer box */
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

# FULL 60-QUESTION MASTER BANK (30 Part A + 30 Part B)
MASTER_QUESTION_BANK = [
    # ==========================================
    # PART A: FOUNDATIONAL & ETHICAL APPLICATIONS (30 Questions)
    # ==========================================
    {
        "section": "Part A",
        "question": "During a session, a client spends 15 minutes talking about a messy corporate restructuring that has nothing to do with their stated coaching goal. According to ICF Competency 3, what should Nana do?",
        "options": [
            "A) Let them finish completely because building rapport and empathy is always the top priority.",
            "B) Gently interrupt, acknowledge their sharing, and partner with them to manage time and reconnect it back to the coaching agreement.",
            "C) Tell them firmly that time is limited and order them to get back on track immediately.",
            "D) Change the subject yourself to the original goal without interrupting them."
        ],
        "answer": 1,
        "competency": "Competency 3: Establishes and Maintains Agreements",
        "bloom": "Evaluating",
        "feedback": "Spot on, Nana! PCC coaches manage time and focus by partnering with the client rather than taking control."
    },
    {
        "section": "Part A",
        "question": "A client accepts a new coaching engagement with Nana and values her past industry expertise. What is the best action for Nana to take?",
        "options": [
            "A) Offer direct advice based on her industry work experience whenever asked.",
            "B) Clarify the distinction between coaching and consulting to maintain professional boundaries.",
            "C) Provide her credentials and past project wins to build confidence.",
            "D) Suggest engagement goals based on her industry experience."
        ],
        "answer": 1,
        "competency": "Competency 1: Demonstrates Ethical Practice",
        "bloom": "Analyzing",
        "feedback": "Brilliant! Maintaining clear distinctions between coaching, consulting, and other professions is essential for ethics."
    },
    {
        "section": "Part A",
        "question": "A client says: 'I just keep failing at every leadership initiative I launch.' Which response best aligns with ICF Competency 7 (Evokes Awareness)?",
        "options": [
            "A) 'Have you tried making a step-by-step project timeline template?'",
            "B) 'Why do you think you keep failing?'",
            "C) 'What are you learning about yourself and your leadership through these experiences?'",
            "D) 'Don't be so hard on yourself, everyone fails sometimes. What's next?'"
        ],
        "answer": 2,
        "competency": "Competency 7: Evokes Awareness",
        "bloom": "Applying",
        "feedback": "You nailed it! Powerful questions shift perspective and invite internal learning rather than advice-giving."
    },
    {
        "section": "Part A",
        "question": "A client comes to a coaching session without a specific topic or agenda. According to ICF Competency 3, what is the coach's best approach?",
        "options": [
            "A) Pick a topic for them based on what you discussed last time.",
            "B) Partner with the client to explore what they want to achieve or take away from today's conversation.",
            "C) Cancel the session since there is no structured agenda.",
            "D) Give them a personality test to fill the time."
        ],
        "answer": 1,
        "competency": "Competency 3: Establishes and Maintains Agreements",
        "bloom": "Applying",
        "feedback": "Spot on! The coach partners with the client to establish what they want and need from the session."
    },
    {
        "section": "Part A",
        "question": "During a session, Nana notices the client's tone changes and they become defensive when asked about their timeline. Which competency guides Nana to address this shift?",
        "options": [
            "A) Competency 5: Maintains Presence",
            "B) Competency 6: Listens Actively",
            "C) Competency 7: Evokes Awareness",
            "D) Competency 2: Embodies a Coaching Mindset"
        ],
        "answer": 1,
        "competency": "Competency 6: Listens Actively",
        "bloom": "Analyzing",
        "feedback": "Excellence! Active listening involves noticing shifts in tone, energy, or behavior."
    },
    {
        "section": "Part A",
        "question": "A client asks Nana to tell them exactly what career path they should choose because Nana is more experienced. How should Nana respond?",
        "options": [
            "A) Give them a direct recommendation based on market trends.",
            "B) Decline to give advice and invite the client to explore their own values, strengths, and desired direction.",
            "C) Ask another coach what they would recommend and relay it.",
            "D) Tell them to pick whatever pays the most money."
        ],
        "answer": 1,
        "competency": "Competency 2: Embodies a Coaching Mindset",
        "bloom": "Evaluating",
        "feedback": "Correct! Coaches maintain client autonomy and do not assume the role of an expert advisor."
    },
    {
        "section": "Part A",
        "question": "What is the primary purpose of establishing a coaching agreement at the beginning of an individual session?",
        "options": [
            "A) To ensure the coach gets paid on time.",
            "B) To outline what the client wants to accomplish and what success looks like for that specific conversation.",
            "C) To create a legally binding contract for employment.",
            "D) To set the homework assignments for the week."
        ],
        "answer": 1,
        "competency": "Competency 3: Establishes and Maintains Agreements",
        "bloom": "Applying",
        "feedback": "Spot on! Session agreements clarify the focus and measure of success for that specific meeting."
    },
    {
        "section": "Part A",
        "question": "When is it appropriate for a PCC coach to use intuition during a session?",
        "options": [
            "A) To tell the client what their hidden motives are as absolute fact.",
            "B) To share observations or hunches openly with the client, holding them lightly without attachment so the client can explore them.",
            "C) To diagnose mental health conditions.",
            "D) Never; intuition has no place in professional coaching."
        ],
        "answer": 1,
        "competency": "Competency 7: Evokes Awareness",
        "bloom": "Evaluating",
        "feedback": "Brilliant! Intuition can be offered as an observation, but the client always remains the expert on their own experience."
    },
    {
        "section": "Part A",
        "question": "A client achieves their goal halfway through a 6-month coaching engagement. What is the best next step?",
        "options": [
            "A) Automatically stop all remaining sessions.",
            "B) Partner with the client to re-evaluate the agreement, celebrate progress, and establish new goals for the remainder of the engagement.",
            "C) Keep talking about the old goal until the 6 months are up.",
            "D) Double the frequency of sessions without telling the client."
        ],
        "answer": 1,
        "competency": "Competency 3: Establishes and Maintains Agreements",
        "bloom": "Analyzing",
        "feedback": "Correct! Agreements are living frameworks that can be updated as the client evolves."
    },
    {
        "section": "Part A",
        "question": "Which of the following best demonstrates ICF Competency 4 (Cultivates Trust and Safety)?",
        "options": [
            "A) Sharing stories about other clients to make the current client feel normal.",
            "B) Respecting the client's boundaries, honoring their vulnerability, and creating a safe, supportive environment.",
            "C) Telling the client what mistakes they made in their previous job.",
            "D) Avoiding challenging questions so the client never feels uncomfortable."
        ],
        "answer": 1,
        "competency": "Competency 4: Cultivates Trust and Safety",
        "bloom": "Applying",
        "feedback": "Spot on! Trust and safety are built by respecting vulnerability and maintaining safety."
    },
    {
        "section": "Part A",
        "question": "A client says they want to improve their public speaking, but their body language and tone sound completely unenthusiastic. What should Nana do?",
        "options": [
            "A) Ignore their tone and move straight into public speaking drills.",
            "B) Acknowledge the discrepancy between their words and their energy, inviting them to explore what is really going on.",
            "C) Tell them they clearly don't want to improve and cancel the session.",
            "D) Give them an inspiring pep talk about confidence."
        ],
        "answer": 1,
        "competency": "Competency 6: Listens Actively",
        "bloom": "Evaluating",
        "feedback": "Exceptional! Active listening looks beyond mere words to notice energy shifts, tone, and body language."
    },
    {
        "section": "Part A",
        "question": "How should a coach handle client confidentiality when working within an organizational setting?",
        "options": [
            "A) Keep everything completely secret, even from the sponsor who pays for it, regardless of prior agreements.",
            "B) Clarify confidentiality parameters clearly with both client and sponsor upfront, adhering strictly to those agreed boundaries.",
            "C) Share full audio recordings with the manager whenever requested.",
            "D) Gossip about the client's weaknesses with HR."
        ],
        "answer": 1,
        "competency": "Competency 1: Demonstrates Ethical Practice",
        "bloom": "Analyzing",
        "feedback": "Correct! Ethical practice requires clear upfront agreements regarding stakeholder confidentiality."
    },
    {
        "section": "Part A",
        "question": "What is the primary difference between open-ended and closed-ended questions in coaching?",
        "options": [
            "A) Open-ended questions require a 'yes' or 'no' answer, while closed-ended questions invite broad reflection.",
            "B) Open-ended questions invite exploration, reflection, and deeper thinking, while closed-ended questions usually yield single-word answers.",
            "C) Closed-ended questions are forbidden in ICF coaching.",
            "D) There is no difference."
        ],
        "answer": 1,
        "competency": "Competency 7: Evokes Awareness",
        "bloom": "Applying",
        "feedback": "Spot on! Open-ended questions open doors for deeper client discovery."
    },
    {
        "section": "Part A",
        "question": "During a session, Nana feels triggered by a political opinion the client expresses. Under Competency 5 (Maintains Presence), what should Nana do?",
        "options": [
            "A) Argue with the client to correct their worldview.",
            "B) Notice her internal reaction, manage her own emotions, and remain fully present and open for the client.",
            "C) End the coaching relationship immediately.",
            "D) Pretend to agree even if she doesn't."
        ],
        "answer": 1,
        "competency": "Competency 5: Maintains Presence",
        "bloom": "Evaluating",
        "feedback": "Masterclass! Maintaining presence means staying grounded and objective even when personally triggered."
    },
    {
        "section": "Part A",
        "question": "A client asks Nana for her personal opinion on a delicate life choice. What is the PCC-level response?",
        "options": [
            "A) Give her personal opinion right away since she is wise.",
            "B) Explore what the client's own thoughts and inner wisdom are before considering outside perspectives.",
            "C) Tell the client what she would do in their shoes.",
            "D) Refuse to speak for the rest of the session."
        ],
        "answer": 1,
        "competency": "Competency 2: Embodies a Coaching Mindset",
        "bloom": "Applying",
        "feedback": "Correct! A coaching mindset centers on empowering the client's own internal resourcefulness."
    },
    {
        "section": "Part A",
        "question": "What does ICF Competency 8 (Facilitates Client Growth) require of the coach at the end of a session?",
        "options": [
            "A) Assigning mandatory reading material and tests.",
            "B) Partnering with the client to design actions, learnings, and accountability measures that support their growth.",
            "C) Telling them what their goals for next week must be.",
            "D) Ending abruptly as soon as the clock hits 60 minutes."
        ],
        "answer": 1,
        "competency": "Competency 8: Facilitates Client Growth",
        "bloom": "Applying",
        "feedback": "Spot on! Client growth is fostered by partnering on client-designed action and accountability."
    },
    {
        "section": "Part A",
        "question": "A client is talking at a very fast pace, jumping from topic to topic with high anxiety. How should Nana apply Competency 5 (Maintains Presence)?",
        "options": [
            "A) Speak even faster to match their frantic energy.",
            "B) Slow her own pace, remain calm and grounded, and invite a pause to help ground the client.",
            "C) Interrupt them and tell them to calm down.",
            "D) Take notes and say nothing until the session ends."
        ],
        "answer": 1,
        "competency": "Competency 5: Maintains Presence",
        "bloom": "Analyzing",
        "feedback": "Excellent! A coach's grounded presence helps anchor and calm an overwhelmed client."
    },
    {
        "section": "Part A",
        "question": "What should Nana do if she realizes she has a dual relationship or conflict of interest with a prospective coaching client?",
        "options": [
            "A) Proceed anyway without mentioning it.",
            "B) Disclose the conflict transparently and ethically decline or manage the engagement to protect professional integrity.",
            "C) Hide it from the ICF.",
            "D) Charge them double to offset the risk."
        ],
        "answer": 1,
        "competency": "Competency 1: Demonstrates Ethical Practice",
        "bloom": "Evaluating",
        "feedback": "Correct! Ethical practice demands transparency and avoiding or managing conflicts of interest."
    },
    {
        "section": "Part A",
        "question": "When a client has a major realization, what is the coach's role under Competency 7?",
        "options": [
            "A) Take credit for the insight.",
            "B) Allow the client to articulate their awareness and integrate what they have learned.",
            "C) Move immediately to the next question without letting them process.",
            "D) Correct minor flaws in their realization."
        ],
        "answer": 1,
        "competency": "Competency 7: Evokes Awareness",
        "bloom": "Applying",
        "feedback": "Spot on! Supporting client integration of their own awareness is key to evoking lasting change."
    },
    {
        "section": "Part A",
        "question": "What does active listening (Competency 6) entail beyond hearing the words spoken?",
        "options": [
            "A) Listening for what is unsaid, including shifts in emotion, pacing, body language, and underlying values.",
            "B) Memorizing every single detail to quiz the client later.",
            "C) Translating their words into psychological jargon.",
            "D) Figuring out your next question while they speak."
        ],
        "answer": 0,
        "competency": "Competency 6: Listens Actively",
        "bloom": "Analyzing",
        "feedback": "Brilliant! Active listening captures the holistic experience of the client."
    },
    {
        "section": "Part A",
        "question": "How should Nana handle a client who consistently arrives 15 minutes late to every session?",
        "options": [
            "A) Quietly adjust and give them extra time at the end without saying anything.",
            "B) Partner with the client to examine the pattern, discuss the agreement, and address the impact on coaching time.",
            "C) Cancel all future sessions immediately.",
            "D) Charge them a fine."
        ],
        "answer": 1,
        "competency": "Competency 3: Establishes and Maintains Agreements",
        "bloom": "Evaluating",
        "feedback": "Correct! Addressing logistical agreements and patterns is part of maintaining professional standards."
    },
    {
        "section": "Part A",
        "question": "What is meant by 'partnering' with the client in ICF coaching?",
        "options": [
            "A) The coach makes the final decisions while the client does the work.",
            "B) Working collaboratively as equals where the client drives the agenda and the coach facilitates the process.",
            "C) The coach acts as the manager of the client's career.",
            "D) Splitting profits from the client's business ventures."
        ],
        "answer": 1,
        "competency": "Competency 2: Embodies a Coaching Mindset",
        "bloom": "Applying",
        "feedback": "Spot on! Partnership means honoring the client as the expert in their life while holding the coaching process."
    },
    {
        "section": "Part A",
        "question": "Why is cultural awareness important under ICF Competency 1 and 2?",
        "options": [
            "A) It allows the coach to stereotype clients efficiently.",
            "B) It ensures the coach respects diverse backgrounds, avoids bias, and adapts to the client's unique worldview.",
            "C) It is only required for international coaches.",
            "D) It helps the coach decide what language to speak."
        ],
        "answer": 1,
        "competency": "Competency 1 & 2: Ethics & Mindset",
        "bloom": "Analyzing",
        "feedback": "Correct! Cultural awareness safeguards against bias and honors the client's full identity."
    },
    {
        "section": "Part A",
        "question": "When is a coach expected to engage in reflective practice (Competency 2)?",
        "options": [
            "A) Only when renewing their ICF credential every three years.",
            "B) Regularly, by evaluating their own coaching presence, biases, and continuous professional growth.",
            "C) Never, once PCC is achieved.",
            "D) Only when a client complains."
        ],
        "answer": 1,
        "competency": "Competency 2: Embodies a Coaching Mindset",
        "bloom": "Applying",
        "feedback": "Spot on! Continuous reflective practice is a hallmark of a mature coaching mindset."
    },
    {
        "section": "Part A",
        "question": "What is the primary focus when designing actions with a client (Competency 8)?",
        "options": [
            "A) Giving them tasks that the coach knows will work.",
            "B) Empowering the client to design their own action steps that align with their goals and values.",
            "C) Giving homework that takes at least 5 hours to complete.",
            "D) Letting the client skip action planning entirely."
        ],
        "answer": 1,
        "competency": "Competency 8: Facilitates Client Growth",
        "bloom": "Applying",
        "feedback": "Correct! Client autonomy is honored when clients design their own action steps."
    },
    {
        "section": "Part A",
        "question": "How should Nana respond if a client expresses gratitude and gives her an expensive luxury gift?",
        "options": [
            "A) Accept it gladly as a token of appreciation.",
            "B) Ethically decline or navigate the gift policy according to professional standards to avoid conflicts of interest or boundary blurring.",
            "C) Sell it and split the cash.",
            "D) Refuse to speak to the client ever again."
        ],
        "answer": 1,
        "competency": "Competency 1: Demonstrates Ethical Practice",
        "bloom": "Evaluating",
        "feedback": "Spot on! Professional boundaries must be maintained regarding gifts and rewards."
    },
    {
        "section": "Part A",
        "question": "What is the primary objective of powerful questioning (Competency 7)?",
        "options": [
            "A) To test how smart the coach is.",
            "B) To provoke discovery, insight, commitment, or action.",
            "C) To cross-examine the client like a lawyer.",
            "D) To fill awkward silences."
        ],
        "answer": 1,
        "competency": "Competency 7: Evokes Awareness",
        "bloom": "Applying",
        "feedback": "Correct! Powerful questions serve to shift perspective and evoke deep awareness."
    },
    {
        "section": "Part A",
        "question": "How does a coach support client autonomy during session closures?",
        "options": [
            "A) By telling them what they must achieve before next week.",
            "B) By asking what insights they are taking away and how they choose to hold themselves accountable.",
            "C) By summarizing everything for them without their input.",
            "D) By assigning mandatory reading."
        ],
        "answer": 1,
        "competency": "Competency 8: Facilitates Client Growth",
        "bloom": "Applying",
        "feedback": "Spot on! Accountability belongs to the client."
    },
    {
        "section": "Part A",
        "question": "What should Nana do if she notices she is talking more than 30% of the time during a session?",
        "options": [
            "A) Keep talking because her advice is valuable.",
            "B) Recognize she is over-functioning, step back, and shift the floor back to the client through powerful inquiry.",
            "C) Ask the client to talk faster.",
            "D) Charge half price."
        ],
        "answer": 1,
        "competency": "Competency 5 & 6: Presence & Listening",
        "bloom": "Evaluating",
        "feedback": "Correct! Coaches manage their own urge to speak and let the client lead."
    },
    {
        "section": "Part A",
        "question": "Why is establishing clear session goals crucial under Competency 3?",
        "options": [
            "A) It prevents the session from wandering aimlessly and ensures purposeful use of time.",
            "B) It allows the coach to grade the client's performance.",
            "C) It is a formality required by insurance companies.",
            "D) It ensures the session ends early."
        ],
        "answer": 0,
        "competency": "Competency 3: Establishes and Maintains Agreements",
        "bloom": "Applying",
        "feedback": "Spot on! Clear agreements keep coaching focused and impactful."
    },

    # ==========================================
    # PART B: ADVANCED CASE SCENARIOS (30 Questions)
    # ==========================================
    {
        "section": "Part B",
        "question": "[Complex Case] A corporate sponsor who pays for the coaching calls Nana privately to ask how the client is progressing and whether they are addressing their anger issues at work. What is the PCC-level response?",
        "options": [
            "A) Share a general overview of the client's progress to keep the corporate sponsor happy and funding the sessions.",
            "B) Maintain strict confidentiality per stakeholder agreements, remind the sponsor of confidentiality boundaries, and encourage the sponsor to discuss feedback directly with the client.",
            "C) Tell the sponsor everything the client said in confidence because the sponsor is paying the bills.",
            "D) Refuse to speak with the sponsor entirely under any circumstances."
        ],
        "answer": 1,
        "competency": "Competency 1 & 3: Ethics & Agreements",
        "bloom": "Evaluating",
        "feedback": "Masterclass coaching! Sub-competency 1.05 requires maintaining confidentiality per stakeholder agreements while managing sponsor expectations professionally."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] A client suddenly starts crying deeply and goes quiet after describing a major career failure. Following ICF Competency 5 (Maintains Presence), what should Nana do?",
        "options": [
            "A) Quickly fill the silence with comforting words to make the client feel less awkward.",
            "B) Suggest taking a 5-minute break to calm down and reset their emotions.",
            "C) Remain grounded, display confidence in handling strong emotions, and hold space for silence, pause, or reflection without rescuing.",
            "D) Ask an analytical question immediately to find out what triggered the tears."
        ],
        "answer": 2,
        "competency": "Competency 5: Maintains Presence",
        "bloom": "Analyzing",
        "feedback": "Exceptional! PCC coaches are comfortable in the space of not knowing, managing their own emotions, and allowing powerful silence."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] At the end of a session, Nana is excited because a huge breakthrough happened, but there are only two minutes left. How should Nana handle the conclusion per ICF Competency 8?",
        "options": [
            "A) Rapidly talk over the client to summarize all the breakthroughs and assign homework.",
            "B) Extend the session by 15 minutes because breakthroughs cannot be rushed.",
            "C) Partner with the client to summarize their key learnings, design their own accountability measures, and formally close the session on time.",
            "D) Tell the client to figure out their own action steps via email later."
        ],
        "answer": 2,
        "competency": "Competency 3 & 8: Closing & Client Growth",
        "bloom": "Evaluating",
        "feedback": "Spot on! Partnering with the client to summarize insights and honoring client autonomy in accountability is the hallmark of a PCC coach."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] A client repeatedly brings up deep psychological trauma during coaching sessions that significantly impairs their daily functioning. What is the most ethical PCC response?",
        "options": [
            "A) Attempt to heal the trauma using advanced therapeutic questioning techniques.",
            "B) Recognize the limits of coaching, discuss the boundary with the client, and ethically refer them to a licensed mental health professional.",
            "C) Ignore the trauma and focus strictly on corporate KPIs.",
            "D) Advise the client on what specific medications they should ask their doctor for."
        ],
        "answer": 1,
        "competency": "Competency 1: Demonstrates Ethical Practice",
        "bloom": "Evaluating",
        "feedback": "Spot on! Ethical practice requires knowing when coaching is no longer appropriate and referring clients to other professionals."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] A client continually avoids talking about their primary goal, instead using the entire session to complain about office gossip. When Nana attempts to refocus, the client pushes back angrily. What is the PCC-level response?",
        "options": [
            "A) Back down completely and let them gossip for the rest of the hour.",
            "B) Partner with the client to examine what is happening in the room, holding space for their frustration while maintaining the integrity of the coaching agreement.",
            "C) Scold the client for being uncooperative.",
            "D) Terminate the contract instantly."
        ],
        "answer": 1,
        "competency": "Competency 3 & 4: Agreements & Trust",
        "bloom": "Evaluating",
        "feedback": "Brilliant! PCC coaches navigate resistance by partnering with the client and addressing what is happening in the present moment."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] Nana notices that a client is looking for reassurance and validation from Nana after every decision they make. How should Nana respond to foster autonomy?",
        "options": [
            "A) Give them validation and tell them they are making the right choice.",
            "B) Partner with the client to explore where their need for external validation comes from and anchor their trust in their own inner authority.",
            "C) Tell them to stop asking for validation.",
            "D) Refer them to a therapist immediately."
        ],
        "answer": 1,
        "competency": "Competency 7: Evokes Awareness",
        "bloom": "Analyzing",
        "feedback": "Exceptional! Evoking awareness around patterns like external validation fosters deep client growth."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] A client says: 'I know I need to confront my boss, but I am terrified they will fire me.' Which response demonstrates advanced PCC presence and inquiry?",
        "options": [
            "A) 'Don't worry, bosses rarely fire people over feedback.'",
            "B) 'What is the worst that could happen, and what strength do you have within you to navigate whatever unfolds?'",
            "C) 'You shouldn't confront your boss yet; wait another year.'",
            "D) 'Let's roleplay right now where I pretend to be your boss.'"
        ],
        "answer": 1,
        "competency": "Competency 5 & 7: Presence & Awareness",
        "bloom": "Evaluating",
        "feedback": "Spot on! This question invites deep reflection while building internal resilience."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] During a team coaching session, two executives begin shouting at each other over budget allocations. According to PCC competencies, what should Nana do?",
        "options": [
            "A) Join in and take sides with the higher-ranking executive.",
            "B) Remain calm and grounded, acknowledge the intense energy in the room, and partner with the team to examine what this conflict reveals about their collective agreement.",
            "C) Panic and leave the room.",
            "D) Mute their microphones and wait for them to stop."
        ],
        "answer": 1,
        "competency": "Competency 4 & 5: Trust & Presence",
        "bloom": "Evaluating",
        "feedback": "Masterclass! Staying grounded in high-conflict moments models presence and maintains safety."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] A client makes rapid progress and wants to end the coaching engagement 3 months early. However, the prepaid package has 6 sessions remaining. What is the best ethical action?",
        "options": [
            "A) Force the client to use up the remaining sessions so you keep the money.",
            "B) Honor client autonomy, celebrate their success, and discuss options regarding the remaining agreement per your contract terms.",
            "C) Keep booking sessions without talking to them.",
            "D) Sue them for breach of contract."
        ],
        "answer": 1,
        "competency": "Competency 1 & 3: Ethics & Agreements",
        "bloom": "Analyzing",
        "feedback": "Correct! Client autonomy and clear upfront contract terms govern this scenario."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] A client shares a brilliant breakthrough that completely changes the direction of their career in the last 10 minutes of the session. How should Nana handle this?",
        "options": [
            "A) Rush them out the door so you aren't late for your next appointment.",
            "B) Acknowledge the magnitude of the breakthrough, partner with them on how to anchor this insight, and discuss how they want to handle support moving forward.",
            "C) Start a brand-new 60-minute session on the spot.",
            "D) Tell them they should have thought of it earlier."
        ],
        "answer": 1,
        "competency": "Competency 8: Facilitates Client Growth",
        "bloom": "Evaluating",
        "feedback": "Spot on! Respecting time while honoring major shifts is a PCC hallmark."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] Nana realizes halfway through a coaching engagement that her personal values clash significantly with the client's business ethics. What should Nana do?",
        "options": [
            "A) Lecture the client on morality during every session.",
            "B) Reflect on her ability to remain objective; if personal bias impairs her coaching presence, ethically refer the client to another coach.",
            "C) Sabotage the client's business projects.",
            "D) Pretend nothing is wrong."
        ],
        "answer": 1,
        "competency": "Competency 1 & 2: Ethical Practice & Mindset",
        "bloom": "Evaluating",
        "feedback": "Brilliant! Recognizing when personal bias impairs objectivity and stepping away ethically is true professionalism."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] A client is overly intellectualizing their problem, talking entirely in abstract business jargon without any personal connection or emotion. What should Nana do?",
        "options": [
            "A) Join in using even more corporate jargon.",
            "B) Invite the client to connect with their lived experience or feelings beneath the abstract concepts.",
            "C) Tell them they are being too smart.",
            "D) Give them a vocabulary test."
        ],
        "answer": 1,
        "competency": "Competency 6 & 7: Listening & Awareness",
        "bloom": "Analyzing",
        "feedback": "Correct! Moving clients from head to heart evokes deeper self-awareness."
    },
    {
        "section": "Part B",
        "question": "[Complex Line of Inquiry] A client comes to session 4 stating they changed their mind entirely about their goal from session 1. How should Nana respond?",
        "options": [
            "A) Refuse to change goals because you already signed a paper.",
            "B) Partner with the client to explore what shifted and update the coaching agreement to match their current reality.",
            "C) Scold them for being indecisive.",
            "D) End the coaching engagement."
        ],
        "answer": 1,
        "competency": "Competency 3: Establishes and Maintains Agreements",
        "bloom": "Applying",
        "feedback": "Spot on! Agreements can and should evolve as the client gains clarity."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] Nana notices she feels a strong urge to 'rescue' a client who is describing a difficult family crisis. What does Competency 5 require Nana to do?",
        "options": [
            "A) Act like their parent and solve the problem for them.",
            "B) Notice her own emotional reactivity, let go of the need to rescue, and hold space for the client's resourcefulness.",
            "C) Cry along with the client.",
            "D) Call the client's family members directly."
        ],
        "answer": 1,
        "competency": "Competency 5: Maintains Presence",
        "bloom": "Evaluating",
        "feedback": "Exceptional! Managing the inner rescuer is a core part of maintaining coaching presence."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] A client reports they are taking massive action every week, but results never materialize, and their tone sounds exhausted and cynical. What should Nana do?",
        "options": [
            "A) Push them to work even harder and double their action items.",
            "B) Partner with the client to explore what lies beneath the constant action, addressing energy, alignment, and being rather than just doing.",
            "C) Tell them they are lazy.",
            "D) Fire them as a client."
        ],
        "answer": 1,
        "competency": "Competency 7 & 8: Awareness & Growth",
        "bloom": "Evaluating",
        "feedback": "Spot on! PCC coaches look beneath the surface of frantic action to explore alignment and being."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] During a session, a client asks Nana: 'If you were in my position, would you quit your job?' How should Nana respond?",
        "options": [
            "A) 'Yes, absolutely, your boss sounds terrible.'",
            "B) 'No, never quit a job.'",
            "C) 'As your coach, my role isn't to give you my answer, but to help you uncover what is truly right for you. What does your intuition say?'",
            "D) 'Let me flip a coin for you.'"
        ],
        "answer": 2,
        "competency": "Competency 2 & 7: Mindset & Awareness",
        "bloom": "Analyzing",
        "feedback": "Correct! Redirecting the client back to their own inner wisdom preserves coaching boundaries."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] A client successfully achieves every action item assigned, yet expresses feeling completely empty and unfulfilled. What is the coaching opportunity here?",
        "options": [
            "A) Give them harder action items next time.",
            "B) Explore what values are being honored or neglected, shifting awareness from task execution to deeper purpose.",
            "C) Tell them they should be happy because they finished their homework.",
            "D) Conclude coaching immediately."
        ],
        "answer": 1,
        "competency": "Competency 7: Evokes Awareness",
        "bloom": "Evaluating",
        "feedback": "Spot on! True coaching explores deeper values and fulfillment beyond mere task completion."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] A client consistently arrives at coaching sessions intoxicated or under the influence of substances. What is the PCC ethical response?",
        "options": [
            "A) Ignore it and coach them anyway.",
            "B) Address the observation with care and safety, pause the coaching engagement, and refer them to appropriate medical support.",
            "C) Join them in having a drink to build rapport.",
            "D) Report them to the police immediately."
        ],
        "answer": 1,
        "competency": "Competency 1 & 4: Ethics & Safety",
        "bloom": "Evaluating",
        "feedback": "Correct! Safety and ethical boundaries require pausing coaching when a client is unable to engage safely."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] A client is paralyzed by perfectionism and refuses to take any action unless it is flawless. How should Nana partner with them?",
        "options": [
            "A) Tell them perfectionism is stupid and order them to move faster.",
            "B) Partner with the client to explore their relationship with perfectionism and design small, experimental steps that embrace learning over flawlessness.",
            "C) Do the work for them.",
            "D) Lower your standards as a coach."
        ],
        "answer": 1,
        "competency": "Competency 7 & 8: Awareness & Growth",
        "bloom": "Applying",
        "feedback": "Spot on! Partnering on safe experimentation helps dismantle perfectionism."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] Nana notices she feels bored and checked out during a session. According to Competency 5 and 6, what is the best internal reflection?",
        "options": [
            "A) Blame the client for being boring.",
            "B) Notice the disconnection, check in with her presence, and explore whether this dynamic mirrors what the client experiences with others.",
            "C) Fall asleep on the video call.",
            "D) End the session early."
        ],
        "answer": 1,
        "competency": "Competency 5 & 6: Presence & Listening",
        "bloom": "Evaluating",
        "feedback": "Masterclass! A coach's internal state can often provide powerful systemic data about the client's wider world."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] A client says they want to work on 'everything in their life' during a 45-minute session. How should Nana apply Competency 3?",
        "options": [
            "A) Try to rush through all topics in 45 minutes.",
            "B) Partner with the client to prioritize and choose one specific, meaningful focus for today's session.",
            "C) Tell them they are asking for too much and reject them.",
            "D) Extend the session to 5 hours."
        ],
        "answer": 1,
        "competency": "Competency 3: Establishes and Maintains Agreements",
        "bloom": "Applying",
        "feedback": "Correct! Establishing a focused agreement for the session prevents overwhelm."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] A client experiences a severe emotional outburst of anger directed at Nana during a session. How should Nana maintain presence?",
        "options": [
            "A) Scream back at the client.",
            "B) Stay calm, maintain clear boundaries without taking it personally, and hold a safe space to explore what triggered the reaction.",
            "C) Block their email and block their phone number.",
            "D) Cry and apologize for existing."
        ],
        "answer": 1,
        "competency": "Competency 4 & 5: Trust & Presence",
        "bloom": "Evaluating",
        "feedback": "Spot on! Unshakable presence means holding a safe boundary even amidst intense client emotion."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] A client comes to session boasting about how successful they are, but their voice tone is fragile and defensive. What does active listening require Nana to hear?",
        "options": [
            "A) Only the words about how successful they are.",
            "B) The underlying vulnerability and defensive tone beneath the boastful words.",
            "C) That they don't need coaching anymore.",
            "D) That they are lying."
        ],
        "answer": 1,
        "competency": "Competency 6: Listens Actively",
        "bloom": "Analyzing",
        "feedback": "Brilliant! Active listening captures the emotional nuance behind the literal words."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] A client asks Nana to act as their mentor-consultant for half the session and their coach for the other half. How should Nana handle this?",
        "options": [
            "A) Do whatever the client wants without clarifying.",
            "B) Clearly distinguish between mentoring/consulting and coaching, and explicitly contract with the client on which modality is being used at any given time.",
            "C) Refuse mentoring completely and lecture them.",
            "D) Mix them together seamlessly without telling anyone."
        ],
        "answer": 1,
        "competency": "Competency 1 & 3: Ethics & Agreements",
        "bloom": "Evaluating",
        "feedback": "Correct! Ethical practice requires transparent boundaries when shifting between professional roles."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] A client has achieved all their engagement goals ahead of schedule and asks to renew for another year just because they like talking to Nana. What is the PCC stance?",
        "options": [
            "A) Take their money indefinitely without new goals.",
            "B) Celebrate their success, evaluate whether ongoing coaching serves a distinct developmental purpose, and contract intentionally for new outcomes if renewal proceeds.",
            "C) Fire them immediately.",
            "D) Turn them into a personal friend."
        ],
        "answer": 1,
        "competency": "Competency 3: Establishes and Maintains Agreements",
        "bloom": "Evaluating",
        "feedback": "Spot on! Coaching must remain purposeful and goal-oriented rather than turning into casual chatting."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] Nana realizes she made a mistake during a powerful questioning moment and interrupted the client's train of thought. What should Nana do?",
        "options": [
            "A) Pretend it never happened and blame the client.",
            "B) Own the interruption transparently and invite the client back to where their thoughts were.",
            "C) Apologize profusely for 20 minutes.",
            "D) End the session immediately out of embarrassment."
        ],
        "answer": 1,
        "competency": "Competency 2 & 5: Mindset & Presence",
        "bloom": "Applying",
        "feedback": "Correct! A coaching mindset includes humility, transparency, and honoring the client's flow."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] A client is fearful of making a wrong decision and asks Nana to make the choice for them. How should Nana respond?",
        "options": [
            "A) Make the choice for them.",
            "B) Partner with the client to examine their decision-making process, values, and trust in themselves.",
            "C) Flip a coin.",
            "D) Tell them they are incompetent."
        ],
        "answer": 1,
        "competency": "Competency 2 & 7: Mindset & Awareness",
        "bloom": "Applying",
        "feedback": "Spot on! Coaches build client resourcefulness rather than acting as decision-makers."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] A client completes their action items with resentment, stating they felt forced by Nana. What went wrong under Competency 8?",
        "options": [
            "A) The client is just lazy.",
            "B) The action items were coach-assigned or lacked client ownership rather than being authentically client-designed.",
            "C) Nana didn't charge enough money.",
            "D) Nothing went wrong."
        ],
        "answer": 1,
        "competency": "Competency 8: Facilitates Client Growth",
        "bloom": "Analyzing",
        "feedback": "Correct! Client growth is hindered when actions are imposed rather than autonomously designed."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] At the completion of a long-term coaching agreement, what is the best practice for closing per Competency 8?",
        "options": [
            "A) Disappear without saying goodbye.",
            "B) Partner with the client to celebrate overall progress, summarize learning across the engagement, and discuss future sustainability.",
            "C) Send them an invoice and block their number.",
            "D) Give them a final test."
        ],
        "answer": 1,
        "competency": "Competency 8: Facilitates Client Growth",
        "bloom": "Applying",
        "feedback": "Spot on! Formal closing celebrates growth and solidifies learning for the future."
    },
    {
        "section": "Part B",
        "question": "[Complex Case] Nana notices her own mental fatigue is causing her to miss key details in the client's story. What should Nana do to uphold professional standards?",
        "options": [
            "A) Push through blindly and fake it.",
            "B) Transparently acknowledge her focus dip, regroup, or gently recalibrate the session energy to ensure full presence.",
            "C) Start scrolling on her phone.",
            "D) Yell at the client."
        ],
        "answer": 1,
        "competency": "Competency 5: Maintains Presence",
        "bloom": "Evaluating",
        "feedback": "Masterclass! Maintaining presence requires self-management and honesty about one's energetic capacity."
    }
]

def load_nana_image():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Expanded list to look for both .jpg and .jpeg in various capitalizations
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
    st.markdown("<h4 style='text-align: center; color: #880e4f;'>Official 60-Question Mock Test (30 Part A / 30 Part B) • Fully Styled & Fixed! 🚀✨</h4>", unsafe_allow_html=True)
    st.markdown("---")

    # Initialize Session States
    if "stage" not in st.session_state:
        st.session_state.stage = "part_a"
    if "part_a_q" not in st.session_state:
        part_a_pool = [q for q in MASTER_QUESTION_BANK if q["section"] == "Part A"]
        part_b_pool = [q for q in MASTER_QUESTION_BANK if q["section"] == "Part B"]
        
        random.shuffle(part_a_pool)
        random.shuffle(part_b_pool)
        
        st.session_state.part_a_q = part_a_pool[:30]
        st.session_state.part_b_q = part_b_pool[:30]
        
        st.session_state.exam_start_time = time.time()

    if "part_a_answers" not in st.session_state:
        st.session_state.part_a_answers = []
    if "part_b_answers" not in st.session_state:
        st.session_state.part_b_answers = []
    if "score" not in st.session_state:
        st.session_state.score = 0

    # Live 2-Hour Timer Calculation
    elapsed_seconds = int(time.time() - st.session_state.exam_start_time)
    remaining_seconds = max(0, (2 * 3600) - elapsed_seconds)
    hours_left = remaining_seconds // 3600
    minutes_left = (remaining_seconds % 3600) // 60
    seconds_left = remaining_seconds % 60

    # --- PART A (Section 1: 30 Questions) ---
    if st.session_state.stage == "part_a":
        st.markdown(f"<div class='timer-box'>⏳ Simulated Exam Time Remaining: {hours_left:02d}:{minutes_left:02d}:{seconds_left:02d} | Section 1: Part A (30 Questions)</div>", unsafe_allow_html=True)
        
        with st.form("part_a_form"):
            user_answers = []
            for i, q in enumerate(st.session_state.part_a_q):
                st.markdown(f"**Question {i+1}:** {q['question']}")
                st.markdown(f"<span class='bloom-tag'>🧠 Bloom's Level: {q['bloom']}</span>", unsafe_allow_html=True)
                choice = st.radio(
                    "Choose the best coaching action:", 
                    q['options'], 
                    key=f"pa_q_{i}",
                    index=None
                )
                user_answers.append(choice)
                st.markdown("---")
            
            submit_a = st.form_submit_button("Submit Part A & Take Scheduled Break ☕️")

            if submit_a:
                if any(ans is None for ans in user_answers):
                    st.warning("⚠️ Don't leave any blanks, Nana! Answer every question before moving on. 😘")
                else:
                    st.session_state.part_a_answers = user_answers
                    st.session_state.stage = "break"
                    st.rerun()

    # --- OPTIONAL BREAK (10 Minutes Midway) ---
    elif st.session_state.stage == "break":
        st.subheader("☕ Scheduled 10-Minute Break")
        st.markdown(f"<div class='timer-box'>⏳ Total Exam Time Remaining: {hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}</div>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class='break-box'>
            <h3>Great job completing Part A, Nana! 🎉</h3>
            <p>You've cleared the first 30 questions. Next up is <b>Part B</b> (the advanced case scenarios section). Take a deep breath, stretch, and click below when you're ready!</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("---")
        
        if st.button("🚀 Enter Part B (Advanced Case Scenarios)! Let's Go!"):
            st.session_state.stage = "part_b"
            st.rerun()

    # --- PART B (Section 2: 30 Questions) ---
    elif st.session_state.stage == "part_b":
        st.markdown(f"<div class='timer-box'>⏳ Simulated Exam Time Remaining: {hours_left:02d}:{minutes_left:02d}:{seconds_left:02d} | Section 2: Part B (30 Questions)</div>", unsafe_allow_html=True)
        st.markdown("<div class='part-b-warning'>⚠️ Part B Notice: These are complex, multi-variable scenarios requiring rigorous PCC evaluation. Think deeply, Nana!</div>", unsafe_allow_html=True)
        
        with st.form("part_b_form"):
            user_answers = []
            for i, q in enumerate(st.session_state.part_b_q):
                st.markdown(f"**Question {i+1}:** {q['question']}")
                st.markdown(f"<span class='bloom-tag'>🧠 Bloom's Level: {q['bloom']}</span>", unsafe_allow_html=True)
                choice = st.radio(
                    "Choose the best coaching action:", 
                    q['options'], 
                    key=f"pb_q_{i}",
                    index=None
                )
                user_answers.append(choice)
                st.markdown("---")
            
            submit_b = st.form_submit_button("Finish Entire Exam & See Final Results! 🏆")

            if submit_b:
                if any(ans is None for ans in user_answers):
                    st.warning("⚠️ Almost done, Nana! Answer the remaining questions! 💕")
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

    # --- RESULTS SCREEN ---
    else:
        score = st.session_state.score
        total = len(st.session_state.part_a_q) + len(st.session_state.part_b_q)
        percentage = int((score / total) * 100)

        st.subheader("📊 Official Mock Exam Results & Breakdown")
        
        col1, col2 = st.columns([1, 2])
        with col1:
            img = load_nana_image()
            if img:
                st.image(img, caption="Our Star Coach, Nana! 🌟", use_container_width=True)
            else:
                st.warning("💡 (Tip: Make sure your image is saved as `nana.jpeg` right inside your `NanasExamTutor` folder!)")
        
        with col2:
            if percentage >= 75:
                st.balloons()
                st.success(f"🏆 Final Score: {score}/{total} ({percentage}%)!\n\n**ICF is literally shaking right now!** Master Certified Coach energy right here. Good job, Nana!! 🎉🔥")
            elif percentage >= 50:
                st.snow()
                st.info(f"✨ Final Score: {score}/{total} ({percentage}%)!\n\n**So close to total mastery!** Just a tiny review on the core competencies and you'll clear it easily. Good job, Nana! 💪💖")
            else:
                st.warning(f"🌱 Final Score: {score}/{total} ({percentage}%)!\n\n**Hey, practice makes perfect!** Time to brush up and bounce back stronger. You've got this, Nana! ☕️💕")

        st.markdown("---")
        st.markdown("### 📝 Detailed Mentorship Feedback:")
        
        for section, q_num, is_correct, comp, bloom_level, feedback_text in st.session_state.feedback_log:
            status = "✅ Nailed it!" if is_correct else "💡 Growth Opportunity:"
            with st.container():
                st.markdown(f"""
                <div class="competency-box">
                    <strong>{section} - Q{q_num} — {status}</strong> <span class="bloom-tag">🧠 {bloom_level}</span><br>
                    <em>Core Focus:</em> <code>{comp}</code><br>
                    <p style="margin-top: 8px;">{feedback_text}</p>
                </div>
                """, unsafe_allow_html=True)

        if st.button("🔄 Retake Full Exam (New Shuffled Questions), Nana!"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

if __name__ == "__main__":
    main()
