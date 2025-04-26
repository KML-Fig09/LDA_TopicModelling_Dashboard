# 📚 LDA Topic Modelling Dashboard

An interactive NLP application for exploring document themes using **Latent Dirichlet Allocation (LDA)**.  
Built with **Streamlit**, **Gensim**, **NLTK**, and **pyLDAvis**.

---

## 🚀 Project Overview

This project automatically extracts text from documents, identifies key latent topics via topic modelling, and presents results through an intuitive web dashboard.

Users can:

- 🔍 Filter documents by human-readable topics
- 📂 Search inside full-text content (regex supported)
- 📊 Visualize topic relationships interactively (pyLDAvis)
- 📝 Explore document snippets linked to each theme

---

## 🛠 Technologies Used

- [Gensim](https://radimrehurek.com/gensim/) — LDA Topic Modelling
- [Streamlit](https://streamlit.io/) — Web App Framework
- [pyLDAvis](https://github.com/bmabey/pyLDAvis) — Topic Visualization
- [NLTK](https://www.nltk.org/) — Text Tokenization and Cleaning
- Python Standard Libraries (`os`, `re`, `pandas`, `subprocess`)

---

## 📂 Project Structure

```
lda-topic-modelling-dashboard/
├── app/
│   ├── lda_streamlit_app.py
│   ├── topic_assignments.csv
│   ├── topic_label_map.csv
│   ├── extracted_texts/
│   └── lda_topic_dashboard.html
├── run.py
├── requirements.txt
├── README.md
```

---

## 🖥️ How to Run the App

### 1. Clone the Repository

```bash
git clone https://github.com/KML-Fig09/LDA_TopicModelling_Dashboard.git
cd LDA_TopicModelling_Dashboard
```

### 2. Install Dependencies

```bash
python -m venv venv
venv\Scripts\activate    # On Windows
# or
source venv/bin/activate # On macOS/Linux

pip install -r requirements.txt
```

### 3. Launch the Dashboard

```bash
python run.py
```

- The app will open automatically at `http://localhost:8501`.

---

## 🎨 Features

- **Preprocessing**: Lowercasing, stopword removal, tokenization
- **LDA Topic Modeling**: Train unsupervised topic models on document sets
- **Interactive Dashboard**: 
  - Filter documents by topic
  - Search full-text contents for keywords
  - Preview text snippets
- **Topic Visualization**:
  - Explore topic importance and keyword clusters via pyLDAvis

---

## 📚 Data Source

> _Dataset used for topic modelling was sourced from Dataset of PDF files available [here](https://www.kaggle.com/datasets/manisha717/dataset-of-pdf-files?resource=download)
> _Documents were pre-converted into `.txt` format for analysis._

---

## 🙏 Acknowledgments

This project was made possible thanks to:

- [Gensim Developers](https://radimrehurek.com/gensim/)
- [Streamlit Community](https://discuss.streamlit.io/)
- [pyLDAvis Team](https://github.com/bmabey/pyLDAvis)
- [kaushik000raj](https://github.com/kaushik000raj) for their inspiring recursive text search script
- [Stack Overflow](https://stackoverflow.com/) for having the answers to every question
- And many others!

---

## 📃 License

This project is licensed under the GNU General Public License, V. 3.

---

## ✨ Future Improvements

- 🔧 Deploy publicly via **Streamlit Cloud** or **AWS EC2**
- 📈 Integrate document statistics and word clouds
- 🔒 Add authentication for restricted document collections
- 🎛️ Allow users to dynamically select the number of LDA topics

---


