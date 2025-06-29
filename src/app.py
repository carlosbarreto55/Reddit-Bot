import streamlit as st
from reddit_searcher import RedditSearcher

st.title ("Reddit Search Bot")
st.write("Search for reddit posts!")

term = st.text_input ("Input the search term")
limit = st.slider("Whats the number of posts?",1,10,50)
if st.button("Buscar"):
    searcher = RedditSearcher()
    results = RedditSearcher.search_posts(term,limit)
    if results :
        for post in results:
            st.subheader(post['title'])
            st.write(f"Subreddit: {post['subreddit']}")
            st.write(f"Autor: {post['post_author']}")
            st.write(f"Comentários: {post['num_comments']}")
            st.markdown("---")
    else:
        st.warning("Nenhum resultado encontrado ou erro na busca.")