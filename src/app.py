import streamlit as st
from reddit_searcher import RedditSearcher

st.set_page_config(page_title="Reddit Search Bot", page_icon=":mag:", layout="wide")

# Sidebar
st.sidebar.title("🔎 Reddit Search Bot")
st.sidebar.write("Search for Reddit posts by keyword and filter your results.")

term = st.sidebar.text_input("Search term", placeholder="e.g. Python, AI, Data Science")
limit = st.sidebar.slider("Number of posts", 1, 50, 10)
sort = st.sidebar.selectbox("Sort by", ["relevance", "new", "hot", "top", "comments"])
time_filter = st.sidebar.selectbox("Time filter", ["all", "day", "hour", "month", "week", "year"])
search_button = st.sidebar.button("Search")

st.title("Reddit Search Bot")
st.markdown("Find the most relevant Reddit posts for your interests. Powered by the Reddit public API.")

if search_button:
    if not term.strip():
        st.warning("Please enter a search term.")
    else:
        searcher = RedditSearcher()
        with st.spinner("Searching Reddit..."):
            results = searcher.search_posts(term, limit, sort, time_filter)
        if results:
            st.success(f"Found {len(results)} posts for '{term}'")
            for post in results:
                with st.container():
                    st.markdown(f"### [{post['title']}]({post['post_url']})")
                    st.write(f"**Subreddit:** :speech_balloon: `{post['subreddit']}` | **Author:** :bust_in_silhouette: `{post['post_author']}` | **Comments:** :speech_left: `{post['num_comments']}`")
                    # st.image(post['thumbnail'])  # Se disponível
                    st.markdown("---")
        else:
            st.error("No results found or an error occurred.")