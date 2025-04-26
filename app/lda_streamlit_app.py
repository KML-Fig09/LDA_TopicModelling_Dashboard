import pandas as pd
import streamlit as st
import os
import re
import webbrowser

# Set up Streamlit
st.set_page_config(page_title="Topic Modelling Dashboard", page_icon="📊", layout="wide")

# Define base path relative to location of the app folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "topic_assignments.csv")
label_map_path = os.path.join(BASE_DIR, "topic_label_map.csv")
text_folder = os.path.join(BASE_DIR, "extracted_texts")
pyldavis_path = os.path.join(BASE_DIR, "lda_topic_dashboard.html")

# Data load
df = pd.read_csv(csv_path, encoding="utf-8")  # Force correct UTF-8 decoding for emoji characters

# Load labels
if os.path.exists(label_map_path):
    label_map = pd.read_csv(label_map_path)
else:
    label_map = None
    st.warning(f"Topic label map file not found: {label_map_path}")

# UI heading
st.title("📊 Topic Modelling Dashboard")
st.markdown("Explore topics discovered in synthetic documents.")

# Topic selection
selected_theme = st.selectbox("Select a topic to explore:", sorted(df['topic_label'].dropna().unique()))

# Theme filter
filtered_df = df[df['topic_label'] == selected_theme]

st.subheader(f"Topic: {selected_theme}")

if not filtered_df.empty:
    st.write(f"Showing {len(filtered_df)} documents related to this theme.")
    st.dataframe(filtered_df[['filename', 'topic_label']])
else:
    st.warning("🛑 No documents found for this theme.")

# KW search (an adapted vers of user Kaushik000raj's search code) ---
search_term = st.text_input("🔍 Search for a keyword or phrase inside all document contents (regex supported):")

if search_term:
    st.markdown(f"Searching for **'{search_term}'**...")
    matches = []

    for root, dirs, files in os.walk(text_folder):
        for fname in files:
            if fname.endswith(".txt"):
                full_path = os.path.join(root, fname)

                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        match = re.search(search_term, content, re.IGNORECASE)
                        if match:
                            snippet_start = max(0, match.start() - 100)
                            snippet = content[snippet_start:match.end() + 100]
                            highlighted = re.sub(search_term, f"**{match.group()}**", snippet, flags=re.IGNORECASE)

                            match_row = {
                                "filename": fname,  # match using .txt filename
                                "snippet": highlighted
                            }

                            topic_row = df[df['filename'] == fname]
                            if not topic_row.empty:
                                match_row["topic_label"] = topic_row.iloc[0]['topic_label']

                            matches.append(match_row)

                except Exception as e:
                    st.error(f"Error reading {fname}: {e}")

    # Search result display
    if matches:
        st.success(f"✅ Found {len(matches)} documents containing the term.")
        for row in matches:
            st.markdown(f"📄 **{row['filename']}** — _{row.get('topic_label', 'No label')}_")
            st.markdown(row["snippet"], unsafe_allow_html=True)
    else:
        st.warning("🛑 No matches found.")

# Sidebar ref for themes
if label_map is not None:
    st.sidebar.title("📘 Topic Theme Reference")
    for _, row in label_map.iterrows():
        st.sidebar.markdown(f"**Topic {row['topic_id']}**: {row['readable_title']}")

# Button to open pyLDAvis map
if st.button("Open pyLDAvis topic map in browser"):
    if os.path.exists(pyldavis_path):
        webbrowser.open_new_tab(pyldavis_path)
    else:
        st.error("Topic map file not found.")

