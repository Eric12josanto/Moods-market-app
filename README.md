# Moods-market-app
https://moods-market-app.streamlit.app/

**MOODS- The Market App** is a Streamlit-based tool for cardamom farmers and traders, delivering market insights to guide selling decisions. It provides tailored recommendations on selling or holding produce, using historical price trends, demand, and supply data (2015–2024). With a graph of month-on-month price and quantity trends, the app empowers users to make informed decisions to maximize profits.


The workflow of the **MOODS- The Market App** begins with users accessing the Streamlit interface, where they select their role as either a "Farmer" or "Trader" and choose a month from a dropdown menu. Upon clicking the "GO DEEP" button, the app processes the input using predefined data: `farmer_data` for farmers (with monthly price trends, demand, supply, and recommendations) or `market_data` for traders (with month-pair trends and inventory advice). The app then displays a two-column layout: the left column shows tailored recommendations for the selected month and the next month (e.g., "Hold" or "Sell 40-50%"), while the right column presents a graph of cardamom’s month-on-month price and quantity trends (2015–2024), helping users make informed decisions to maximize profits.
