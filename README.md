# 📩 SMS Spam Classifier using Classical NLP

An end-to-end Natural Language Processing (NLP) project that classifies SMS messages as **Spam** or **Ham** using classical machine learning techniques.

The project demonstrates the complete NLP workflow, from raw text preprocessing to model selection and deployment-ready serialization.

---

## 🎯 Project Objective

The goal of this project is to build an accurate SMS spam detection system while exploring different text representation techniques and machine learning algorithms.

The project focuses on:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Text Preprocessing
- Feature Engineering
- Classical NLP
- Machine Learning Model Comparison
- Model Serialization

---

## 📂 Dataset

The project uses the **SMS Spam Collection Dataset**, which contains over **5,500 real SMS messages** labeled as either:

- **Ham** (Legitimate messages)
- **Spam** (Unwanted promotional/scam messages)

---

## ⚙️ Workflow

The complete pipeline is shown below.

```
Raw SMS
    │
    ▼
Data Cleaning
    │
    ▼
Exploratory Data Analysis
    │
    ▼
Text Preprocessing
    │
    ▼
Feature Engineering
    │
    ▼
Bag of Words / TF-IDF
    │
    ▼
Model Training
    │
    ▼
Model Evaluation
    │
    ▼
Best Model Selection
    │
    ▼
Save Model & Vectorizer
```

---

## 🧹 Text Preprocessing

Each SMS message undergoes the following preprocessing steps:

- Convert text to lowercase
- Tokenization
- Remove non-alphanumeric characters
- Remove stopwords
- Porter Stemming

Example:

**Original Message**

```
Congratulations! You've won $1000.
```

↓

**Processed Message**

```
congratul won 1000
```

---

## 📊 Exploratory Data Analysis

The following analyses were performed:

- Class distribution analysis
- Character count
- Word count
- Sentence count
- Correlation analysis
- Word Clouds
- Most Frequent Spam Words
- Most Frequent Ham Words

---

## 🧠 Text Representation Techniques

Two feature extraction techniques were compared:

- Bag of Words (BoW)
- TF-IDF

---

## 🤖 Machine Learning Models

The following classifiers were evaluated:

- Multinomial Naive Bayes
- Logistic Regression
- Linear Support Vector Machine (Linear SVM)
- Decision Tree
- Random Forest

---

## 📈 Model Performance

| Model | Text Representation | Accuracy | Precision | Recall | F1 Score |
|------|----------------|---------:|----------:|---------:|----------:|
| Linear SVM | **Bag of Words** | **98.36%** | **99.23%** | **88.97%** | **93.82%** |
| Linear SVM | TF-IDF | 98.26% | 97.74% | 89.66% | 93.53% |
| Naive Bayes | Bag of Words | 97.97% | 94.93% | 90.34% | 92.58% |
| Logistic Regression | Bag of Words | 97.78% | 97.66% | 86.21% | 91.58% |
| Random Forest | TF-IDF | 96.62% | 99.11% | 76.55% | 86.38% |

---

## 🏆 Best Performing Model

**Vectorizer**

- CountVectorizer (Bag of Words)

**Classifier**

- Linear Support Vector Machine (Linear SVM)

Performance:

- Accuracy: **98.36%**
- Precision: **99.23%**
- Recall: **88.97%**
- F1 Score: **93.82%**

---

## 💾 Saved Files

The trained artifacts are stored inside the `models/` directory.

```
models/
├── spam_model.pkl
└── vectorizer.pkl
```

These files can be directly used for inference without retraining.

---

## 🚀 Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- NLTK
- Scikit-learn
- WordCloud
- Jupyter Notebook

---

## 📁 Project Structure

```
spam-classifier/
│
├── data/
├── models/
├── notebooks/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔮 Future Improvements

Some possible extensions to this project include:

- Hyperparameter tuning
- Streamlit web application
- Transformer-based models (BERT)
- Larger and more recent spam datasets
- Model deployment on the cloud

---

## 👨‍💻 Author

Roshan Chouhan