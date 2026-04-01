import streamlit as st
import pandas as pd
import random
import time
from datetime import datetime
import os

st.set_page_config(page_title="ML Quiz", layout="centered")

# ---------------- MODERN MOBILE UI ----------------

st.markdown("""
<style>

body{
background: linear-gradient(135deg,#1f4037,#99f2c8);
}

.title{
text-align:center;
font-size:32px;
font-weight:bold;
}

.card{
background:white;
padding:20px;
border-radius:12px;
box-shadow:0 5px 20px rgba(0,0,0,0.2);
margin-bottom:15px;
}

.timer{
font-size:26px;
font-weight:bold;
color:red;
text-align:center;
}

button[kind="primary"]{
background:linear-gradient(90deg,#ff512f,#dd2476);
color:white;
font-weight:bold;
border-radius:8px;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">🧠 Machine Learning Quiz</p>', unsafe_allow_html=True)

QUIZ_TIME = 600

# ---------------- REGISTER NUMBERS ----------------

register_numbers = [
"23K81A7201","23K81A7202","23K81A7203","23K81A7204","23K81A7205","23K81A7206","23K81A7207",
"23K81A7208","23K81A7210","23K81A7211","23K81A7212","23K81A7213","23K81A7214","23K81A7215",
"23K81A7216","23K81A7218","23K81A7219","23K81A7220","23K81A7222","23K81A7223","23K81A7224",
"23K81A7225","23K81A7226","23K81A7227","23K81A7228","23K81A7229","23K81A7230","23K81A7231",
"23K81A7232","23K81A7233","23K81A7234","23K81A7235","23K81A7236","23K81A7237","23K81A7238",
"23K81A7239","23K81A7240","23K81A7241","23K81A7242","23K81A7243","23K81A7244","23K81A7245",
"23K81A7246","23K81A7247","23K81A7249","23K81A7250","23K81A7251","23K81A7252","23K81A7253",
"23K81A7254","23K81A7255","23K81A7256","23K81A7257","23K81A7258","23K81A7259","23K81A7260",
"23K81A7261","23K81A7262","23K81A7263","23K81A7264","24K85A7201","24K85A7202","24K85A7203",
"24K85A7204","24K85A7205","24K85A7206"
]

# ---------------- SESSION ----------------

if "page" not in st.session_state:
    st.session_state.page = "login"

if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

# ---------------- QUESTIONS ----------------

questions = [

{"q":"Which method combines multiple classifiers to improve accuracy?",
"options":["Clustering","Ensemble Method","Regression","Sampling"],
"answer":"Ensemble Method"},

{"q":"Which distribution is used in GMM?",
"options":["Uniform","Normal","Poisson","Binomial"],
"answer":"Normal"},

{"q":"Dimensionality reduction helps in:",
"options":["Increasing features","Reducing features","Sorting data","Encrypting data"],
"answer":"Reducing features"},

{"q":"PCA stands for:",
"options":["Principal Component Analysis","Partial Component Analysis","Primary Cluster Analysis","Predictive Component Algorithm"],
"answer":"Principal Component Analysis"},

{"q":"LDA is mainly used for:",
"options":["Regression","Classification","Clustering","Sampling"],
"answer":"Classification"},

{"q":"Factor Analysis is used to:",
"options":["Reduce variables","Increase noise","Sort data","Encode labels"],
"answer":"Reduce variables"},

{"q":"Reinforcement learning is based on:",
"options":["Labels","Rewards","Features","Noise"],
"answer":"Rewards"},

{"q":"Markov process depends on:",
"options":["Past states","Future states","Present state","All states"],
"answer":"Present state"},

{"q":"MCMC stands for:",
"options":["Markov Chain Monte Carlo","Mean Cluster Monte Carlo","Model Chain Mapping Code","Multi Chain Method Calculation"],
"answer":"Markov Chain Monte Carlo"},

{"q":"Bayesian Networks are:",
"options":["Undirected graphs","Directed graphs","Trees","Lists"],
"answer":"Directed graphs"},

{"q":"K-means belongs to:",
"options":["Supervised","Reinforcement","Unsupervised","Semi-supervised"],
"answer":"Unsupervised"},

{"q":"ICA stands for:",
"options":["Independent Component Analysis","Internal Cluster Analysis","Integrated Component Algorithm","Indexed Cluster Analysis"],
"answer":"Independent Component Analysis"},

{"q":"Isomap is used for:",
"options":["Linear mapping","Non-linear dimensionality reduction","Sorting","Encoding"],
"answer":"Non-linear dimensionality reduction"},

{"q":"Genetic algorithms are inspired by:",
"options":["Physics","Chemistry","Biology","Mathematics"],
"answer":"Biology"},

{"q":"Markov Random Fields are:",
"options":["Directed","Undirected","Linear","Trees"],
"answer":"Undirected"}

]

fill_questions = [

{"q":"K-means algorithm groups data into ______ clusters.","answer":"K"},
{"q":"Nearest Neighbor depends on ______ distance.","answer":"Euclidean"},
{"q":"Genetic algorithms use ______ selection.","answer":"Natural"},
{"q":"Mutation is a genetic ______.","answer":"Operator"},
{"q":"Factor Analysis identifies ______ variables.","answer":"Latent"},
{"q":"LLE preserves ______ structure.","answer":"Local"},
{"q":"HMM has ______ states.","answer":"Hidden"},
{"q":"Proposal distribution is used in ______ sampling.","answer":"MCMC"},
{"q":"MRF are ______ graphs.","answer":"Undirected"},
{"q":"Tracking methods estimate ______ over time.","answer":"States"},
{"q":"Ensemble learning combines ______ classifiers.","answer":"Multiple"},
{"q":"GMM is based on ______ distribution.","answer":"Normal"},
{"q":"PCA finds ______ components.","answer":"Principal"},
{"q":"LDA maximizes class ______.","answer":"Separation"},
{"q":"ICA assumes components are ______.","answer":"Independent"},
{"q":"Isomap preserves ______ distance.","answer":"Geodesic"},
{"q":"Reinforcement learning uses ______ signals.","answer":"Reward"},
{"q":"Markov property depends on ______ state.","answer":"Present"},
{"q":"MCMC is used for ______ sampling.","answer":"Probabilistic"},
{"q":"Bayesian networks use ______ probability.","answer":"Conditional"}

]

all_questions = questions + fill_questions

# ---------------- LOGIN PAGE ----------------

if st.session_state.page == "login":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Student Login")

    reg = st.selectbox("Select Register Number", register_numbers)

    if st.button("Start Quiz"):

        st.session_state.reg = reg
        st.session_state.start_time = time.time()

        random.shuffle(all_questions)
        st.session_state.quiz = all_questions

        st.session_state.page = "quiz"
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- QUIZ PAGE ----------------

elif st.session_state.page == "quiz":

    elapsed = int(time.time() - st.session_state.start_time)
    remaining = QUIZ_TIME - elapsed

    if remaining <= 0:
        st.session_state.page = "result"
        st.rerun()

    minutes = remaining // 60
    seconds = remaining % 60

    st.markdown(
    f'<p class="timer">⏱ Time Remaining: {minutes}:{seconds:02d}</p>',
    unsafe_allow_html=True
    )

    quiz = st.session_state.quiz
    i = st.session_state.q_index
    q = quiz[i]

    st.progress((i+1)/len(quiz))

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader(f"Question {i+1} of {len(quiz)}")
    st.write(q["q"])

    if "options" in q:
        ans = st.radio("Choose answer", q["options"], index=None)
    else:
        ans = st.text_input("Your answer")

    if ans:
        st.session_state.answers[i] = ans

    col1,col2,col3 = st.columns(3)

    with col1:
        if st.button("⬅ Previous") and i>0:
            st.session_state.q_index -=1
            st.rerun()

    with col2:
        if st.button("Next ➡") and i < len(quiz)-1:
            st.session_state.q_index +=1
            st.rerun()

    with col3:
        if st.button("Submit Quiz"):
            st.session_state.page = "result"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- RESULT PAGE ----------------

elif st.session_state.page == "result":

    quiz = st.session_state.quiz
    answers = st.session_state.answers

    score = 0

    for i,q in enumerate(quiz):

        correct = q["answer"].lower().strip()
        student = str(answers.get(i,"")).lower().strip()

        if correct == student:
            score +=1

    st.success(f"🎯 Your Score: {score} / {len(quiz)}")

    result = {
        "Register":st.session_state.reg,
        "Score":score,
        "Total":len(quiz),
        "Time":datetime.now()
    }

    df = pd.DataFrame([result])

    try:
        old = pd.read_excel("quiz_results.xlsx")
        df = pd.concat([old,df])
    except:
        pass

    df.to_excel("quiz_results.xlsx",index=False)

    # ---------------- LEADERBOARD ----------------

    st.subheader("🏆 Leaderboard")

    leaderboard = df.sort_values("Score",ascending=False)

    st.dataframe(leaderboard)

    # ---------------- CLEAR LEADERBOARD ----------------

    if st.button("🗑 Clear Leaderboard"):

        if os.path.exists("quiz_results.xlsx"):
            os.remove("quiz_results.xlsx")

        st.success("Leaderboard cleared!")

    st.balloons()
