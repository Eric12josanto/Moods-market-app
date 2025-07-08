import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def get_next_month(current_month):
    month_index = months.index(current_month)
    next_month_index = (month_index + 1) % 12
    return months[next_month_index]

def get_month_pair(current_month):
    prev_month = months[(months.index(current_month) - 1) % 12]
    return f"{prev_month[:3]}-{current_month[:3]}"

# Farmer and trader data omitted for brevity (keep your existing dictionaries here)

st.set_page_config(page_title="MOODS- The Market App", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .main {
        background-color: #FFFFFF !important;
        color: #000000;
    }
    h1 {
        color: #000000;
        text-align: center;
        font-size: 2.5em;
    }
    h3 {
        color: #000000;
    }
    .stRadio > label, .stSelectbox > label, .stDateInput > label, .stSlider > label {
        color: #00008B;
        font-size: 1.1em;
    }
    .stRadio > div > label, .stSelectbox > div > label, .stSlider > div > label {
        color: #000000;
    }
    .stRadio > div, .stSelectbox > div, .stDateInput > div, .stSlider > div {
        background-color: #E0F7E0;
        border-radius: 8px;
        padding: 10px;
        color: #000000;
        box-shadow: 0 4px 16px 0 rgba(0,0,0,0.10), 0 1.5px 4px 0 rgba(0,0,0,0.08);
        border: none;
    }
    .stButton > button {
        background-color: #E0F7E0;
        color: #000000;
        padding: 10px 20px;
        font-size: 1.2em;
        border-radius: 8px;
        cursor: pointer;
        transition: transform 0.2s;
        box-shadow: 0 4px 16px 0 rgba(0,0,0,0.10), 0 1.5px 4px 0 rgba(0,0,0,0.08);
        border: none;
    }
    .stButton > button:hover {
        transform: scale(1.1);
    }
    .stButton > button:active {
        transform: scale(0.95);
    }
    .stMarkdown, .stText {
        color: #000000;
    }
    .coin-animation::before {
        content: '💰';
        font-size: 1.5em;
        margin-right: 8px;
    }
    .framed-image {
        border: none;
        border-radius: 10px;
        display: inline-block;
        box-shadow: 0 4px 16px 0 rgba(0,0,0,0.12), 0 1.5px 4px 0 rgba(0,0,0,0.10);
    }
    .stCheckbox > label {
        color: #00008B;
        font-size: 1.1em;
    }
    .stCheckbox > div {
        background-color: #E0F7E0;
        border-radius: 8px;
        padding: 10px;
        color: #000000;
        box-shadow: 0 4px 16px 0 rgba(0,0,0,0.10), 0 1.5px 4px 0 rgba(0,0,0,0.08);
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💵 MOODS- The Market App 💰")

menu_option = st.sidebar.selectbox("Select Feature", ["Market Insights", "Price Predictor"])

# Market Insights (unchanged, keep your logic here)

if menu_option == "Market Insights":
    st.markdown("<h3 class='coin-animation'>Don't know what to do with your cardamom? Let us handle it.</h3>", unsafe_allow_html=True)
    user_type = st.radio("💎 Select Your Role:", ("Farmer", "Trader"))
    selected_month = st.selectbox("📅 Select Month:", months)
    if st.button("💸 GO DEEP 💸"):
        col1, col2 = st.columns([1.5, 1])
        with col1:
            # ...existing Market Insights logic...
            pass
        with col2:
            st.markdown("""
                <div class="framed-image">
                    <img src="https://github.com/Eric12josanto/Moods-market-app/raw/main/graphy.png" 
                         width="450" alt="Market Insights">
                </div>
                <p style="text-align: center; color: #000000;">Market Insights</p>
                <p style="text-align: center; color: #000000;"><i><b>"The graph shows cardamom's month-on-month average price and quantity sold. Based on seasonal trends from 2015–2024 data."</b></i></p>
            """, unsafe_allow_html=True)

elif menu_option == "Price Predictor":
    st.markdown("<h3 class='coin-animation'>Check Cardamom Prices and Trends</h3>", unsafe_allow_html=True)

    # Load data from the new Excel file with actuals
    try:
        data = pd.read_excel('combined_prices_2015_2028.xlsx')
    except FileNotFoundError:
        st.error("Error: 'combined_prices_2015_2028.xlsx' not found in the project folder.")
        st.stop()

    # Prepare data
    expected_columns = ['Year', 'Month', 'Predicted_Price', 'Actual_Price']
    if not all(col in data.columns for col in expected_columns):
        st.error(f"Expected columns {expected_columns} not found. Actual columns: {data.columns.tolist()}")
        st.stop()
    
    data = data[expected_columns].copy()
    data['Year_Month'] = data['Year'] + (data['Month'] - 1) / 12
    data = data.sort_values(['Year', 'Month']).reset_index(drop=True)

    # Demand growth slider
    demand_growth_percent = st.slider(
        "📈 Select Annual Demand Growth Percentage:",
        min_value=0,
        max_value=50,
        value=5,
        step=1,
        format="%d%%"
    )
    demand_growth = demand_growth_percent / 100

    # Adjust predicted prices for demand growth
    data['Adjusted_Price'] = data['Predicted_Price'].copy()
    for idx, row in data.iterrows():
        if row['Year'] >= 2025:
            year = int(row['Year'])
            years_since_2024 = year - 2024
            cumulative_growth = demand_growth * years_since_2024
            data.at[idx, 'Adjusted_Price'] = row['Predicted_Price'] * (1 + cumulative_growth)

    # Date input
    selected_date = st.date_input(
        "📅 Select a Date (2015–2028):",
        value=datetime(2025, 6, 15),
        min_value=datetime(2015, 1, 1),
        max_value=datetime(2028, 12, 31)
    )

    if selected_date:
        year = selected_date.year
        month = selected_date.month

        price_row = data[(data['Year'] == year) & (data['Month'] == month)]
        if price_row.empty:
            st.write(f"No price data for {year}-{month:02d}.")
        else:
            st.markdown("**Predicted Increasing Demand of Cardamom**")
            price = price_row['Adjusted_Price'].iloc[0]
            st.markdown(f"**Price for {year}-{month:02d}: Rs. {price:.2f}/kg**")

            if 'show_actual_prices' not in st.session_state:
                st.session_state.show_actual_prices = False

            cutoff_year_month = 2024 + (11 - 1) / 12  # November 2024 = 2024.917

            train_data = data[(data['Year'] >= 2015) & (data['Year'] <= 2021)]
            actual_test_data = data[(data['Year'] >= 2022)]
            red_line_data = data[(data['Year'] >= 2022) & (data['Year_Month'] <= cutoff_year_month)]
            prediction_data = data[(data['Year'] >= 2022) & (data['Year'] <= year) & 
                                 ((data['Year'] < year) | (data['Month'] <= month))]

            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=train_data['Year_Month'],
                y=train_data['Predicted_Price'],
                mode='lines',
                name='Training Data (2015-2021)',
                line=dict(color='green', width=2),
                hovertemplate='Year: %{x:.1f}<br>Price: Rs. %{y:.2f}/kg<extra></extra>'
            ))

            if st.session_state.show_actual_prices and not actual_test_data.empty:
                fig.add_trace(go.Scatter(
                    x=actual_test_data['Year_Month'],
                    y=actual_test_data['Actual_Price'],
                    mode='lines',
                    name='Actual Prices (2022-2024)',
                    line=dict(color='brown', width=2, dash='dot'),
                    hovertemplate='Year: %{x:.1f}<br>Actual Price: Rs. %{y:.2f}/kg<extra></extra>'
                ))

            if not red_line_data.empty:
                fig.add_trace(go.Scatter(
                    x=red_line_data['Year_Month'],
                    y=red_line_data['Predicted_Price'],
                    mode='lines',
                    name='Base Prediction (2022-2024)',
                    line=dict(color='red', width=2),
                    hovertemplate='Year: %{x:.1f}<br>Base Price: Rs. %{y:.2f}/kg<extra></extra>'
                ))

            fig.add_trace(go.Scatter(
                x=prediction_data['Year_Month'],
                y=prediction_data['Adjusted_Price'],
                mode='lines',
                name='Predicted Prices with Demand Growth',
                line=dict(color='blue', width=2, dash='dot'),
                hovertemplate='Year: %{x:.1f}<br>Predicted Price: Rs. %{y:.2f}/kg<extra></extra>'
            ))

            fig.update_layout(
                title=f"Cardamom Price Analysis: Training, Testing & Prediction (2015 to {year}-{month:02d})",
                xaxis_title="Year",
                yaxis_title="Price (Rs./kg)",
                hovermode='x unified',
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1
                ),
                height=600,
                template="plotly_white"
            )

            fig.update_xaxes(
                tickvals=list(range(2015, year + 1)),
                ticktext=[str(y) for y in range(2015, year + 1)],
                range=[2015, year + (month / 12)]
            )

            st.plotly_chart(fig, use_container_width=True)

            show_actual_prices = st.checkbox(
                "📊 Show Actual Prices",
                value=st.session_state.show_actual_prices,
                help="Toggle to show/hide the actual price data from 2022-2024",
                key="actual_prices_toggle"
            )

            if show_actual_prices != st.session_state.show_actual_prices:
                st.session_state.show_actual_prices = show_actual_prices
                st.rerun()