import streamlit as st
import pickle

from utils import transform_text

st.set_page_config(
    page_title="SMS Spam Classifier",
    page_icon="📩",
    layout="centered"
)

st.title("📩 SMS spam Classifier")
st.caption("Classify SMS messages as Spam or Ham using Classical NLP and Machine Learning.")
st.divider()
st.write("Enter an SMS message below and click **predict** to classify it as Spam or Ham.")

message = st.text_area(
    "Enter your SMS message",
    placeholder="Example: Congratulations! You've won a FREE ticket. Claim now!"
    )


col1, col2, col3 = st.columns([1,2,1])

with col2:
    predict = st.button("Predict", use_container_width = True)


with st.sidebar:

    st.header("📌 About")

    st.write("""
    This application classifies SMS messages as **Spam** or **Ham** using a classical Natural Language Processing (NLP) pipeline.

    **Model**
    - Linear SVM

    **Vectorizer**
    - Bag of Words

    **Accuracy**
    - 98.36%
    """)


@st.cache_resource
def load_model():

    model = pickle.load(open("models/spam_model.pkl", "rb"))
    vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))
    return model, vectorizer

model, vectorizer = load_model()

if predict:

    if message.strip() == "":
        st.warning("Please enter an SMS message.")

    else:
        with st.spinner("⏳ Analyzing message..."):

            transformed_message = transform_text(message)
            vector = vectorizer.transform([transformed_message])
            prediction = model.predict(vector)[0]
            score = model.decision_function(vector)[0]

            st.subheader("Prediction")

            if prediction == 1:
                st.error("🚨 Spam")
            else:
                st.success("✅ Ham")

            
            st.caption(f"Decision Score: {score:.3f}")

            with st.expander("See preprocessing"):
                st.write(transformed_message)



st.divider()
st.caption(
    "Built with Streamlit | Scikit-learn | NLTK"
)


    