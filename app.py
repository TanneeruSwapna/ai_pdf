import streamlit as st
import requests

# Backend URL
server_loc = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Weather Forecast Agent",
    page_icon="🌦️"
)

st.title("🌦️ Weather Forecast Agent")

st.write("Ask about the weather before going outside.")

city = st.text_input(
    "Enter City Name",
    placeholder="Hyderabad"
)

if st.button("Check Weather"):

    if city:

        try:
            response = requests.post(
                f"{server_loc}/weather",
                json={"city": city}
            )

            # Show full response if something goes wrong
            if response.status_code != 200:
                st.error(f"Backend Error: {response.status_code}")
                st.write(response.text)

            else:
                result = response.json()

                if "answer" in result:
                    st.success(result["answer"])
                else:
                    st.write(result)

        except Exception as e:
            st.error(f"Connection Error: {e}")

    else:
        st.warning("Please enter a city name")