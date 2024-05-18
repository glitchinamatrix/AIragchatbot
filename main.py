import streamlit as st
import requests


def fetch_ai_news(api_key):
    url = f"https://newsapi.org/v2/everything?q=artificial intelligence&apiKey={api_key}"
    #To fetch te ai news over a time
    response = requests.get(url)
    data = response.json()
    #the articles fetched are returned
    if 'articles' in data:
        return data['articles']
    else:
        return None


def main():
    st.title("AI Trends in India")
    st.sidebar.title("Settings")

    api_key = st.sidebar.text_input("Enter News API Key", type="password")
#the news api key is accessed
    if st.sidebar.button("Get AI Trends"):
        if api_key:
            ai_news = fetch_ai_news(api_key)
            if ai_news:
                st.header("Latest AI Trends in India")
                for article in ai_news:
                    st.markdown(f"**{article['title']}**")
                    st.write(article['description'])
                    st.write(article['url'])
                    st.write("---")
            else:
                st.error("Failed to fetch AI trends. Check your API key or try again later.") #if it fails to fetch te news
        else:
            st.warning("Please enter your News API key.")


if __name__ == "__main__":
    main()
