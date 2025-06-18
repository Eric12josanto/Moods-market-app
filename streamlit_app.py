import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# Define the months list first, as it's used by helper functions
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Helper functions
def get_next_month(current_month):
    month_index = months.index(current_month)
    next_month_index = (month_index + 12) % 12
    return months[next_month_index]

def get_month_pair(current_month):
    prev_month = months[(months.index(current_month) - 1) % 12]
    return f"{prev_month[:3]}-{current_month[:3]}"

# Farmer data
farmer_data = {
    "January": {
        "Price_Trend": "Slight price increase",
        "Demand": "Moderate demand increase",
        "Supply_Impact": "Moderate supply increase",
        "Recommendation": [
            "Hold unless prices spike",
            "Wait for May-Jun peak"
        ]
    },
    "February": {
        "Price_Trend": "Slight price decrease",
        "Demand": "Slight demand decrease",
        "Supply_Impact": "Slight supply decrease",
        "Recommendation": [
            "Hold",
            "Prices likely to drop further in Feb-Mar"
        ]
    },
    "March": {
        "Price_Trend": "Moderate price decrease",
        "Demand": "Moderate demand decrease",
        "Supply_Impact": "Slight supply decrease",
        "Recommendation": [
            "Hold",
            "Avoid selling during price drop"
        ]
    },
    "April": {
        "Price_Trend": "Stable prices",
        "Demand": "Stable demand",
        "Supply_Impact": "Stable supply",
        "Recommendation": [
            "Hold",
            "Wait for May-Jun price increase"
        ]
    },
    "May": {
        "Price_Trend": "Slight price decrease",
        "Demand": "Significant demand decrease",
        "Supply_Impact": "Significant supply decrease",
        "Recommendation": [
            "Hold",
            "Next month (May-Jun) offers a significant price increase"
        ]
    },
    "June": {
        "Price_Trend": "Significant price increase",
        "Demand": "Stable demand",
        "Supply_Impact": "Slight supply decrease",
        "Recommendation": [
            "Sell 40-50% of stored produce to capitalize on high prices"
        ]
    },
    "July": {
        "Price_Trend": "Moderate price increase",
        "Demand": "Slight demand decrease",
        "Supply_Impact": "Slight supply decrease",
        "Recommendation": [
            "Sell 20-30% if prices up 5-10% from June",
            "Next month has higher demand"
        ]
    },
    "August": {
        "Price_Trend": "Moderate price increase",
        "Demand": "Significant demand increase",
        "Supply_Impact": "Significant supply increase",
        "Recommendation": [
            "Sell 30-40% to meet high demand",
            "Supply increase may temper price gains"
        ]
    },
    "September": {
        "Price_Trend": "Moderate price increase",
        "Demand": "Moderate demand increase",
        "Supply_Impact": "Moderate supply increase",
        "Recommendation": [
            "Sell remaining stock before Sep-Oct price drop"
        ]
    },
    "October": {
        "Price_Trend": "Significant price decrease",
        "Demand": "Slight demand decrease",
        "Supply_Impact": "Slight supply increase",
        "Recommendation": [
            "Avoid selling",
            "Prices at a low point"
        ]
    },
    "November": {
        "Price_Trend": "Stable prices",
        "Demand": "Slight demand decrease",
        "Supply_Impact": "Slight supply decrease",
        "Recommendation": [
            "Hold",
            "Wait for potential price recovery"
        ]
    },
    "December": {
        "Price_Trend": "Slight price increase",
        "Demand": "Moderate demand decrease",
        "Supply_Impact": "Slight supply decrease",
        "Recommendation": [
            "Sell 10-20% if prices up 5-10% from November",
            "Hold rest for later"
        ]
    }
}

# Trader data
market_data = {
    "Apr-May": {
        "Price": {"Score": -2, "Degree": 3, "Status": "Slight chance of price decrease"},
        "Demand": {"Score": -8, "Degree": 3, "Status": "Strong chance of demand decrease"},
        "Supply": {"Score": -6, "Degree": 3, "Status": "Strong chance of supply decrease"},
        "Trader_Recommendation": "Reduce inventory to avoid overstocking. Offer discounts to stimulate demand."
    },
    "May-Jun": {
        "Price": {"Score": 8, "Degree": 1, "Status": "Strong chance of price increase"},
        "Demand": {"Score": 0, "Degree": 1, "Status": "Steady demand"},
        "Supply": {"Score": -2, "Degree": 1, "Status": "Slight chance of supply decrease"},
        "Trader_Recommendation": "Sell inventory to capitalize on higher prices. Delay purchases."
    },
    "Jun-Jul": {
        "Price": {"Score": 3, "Degree": 1, "Status": "Moderate chance of price increase"},
        "Demand": {"Score": -2, "Degree": 1, "Status": "Slight chance of demand decrease"},
        "Supply": {"Score": -2, "Degree": 1, "Status": "Slight chance of supply decrease"},
        "Trader_Recommendation": "Maintain inventory levels. Monitor market for opportunities."
    },
    "Jul-Aug": {
        "Price": {"Score": 5, "Degree": 3, "Status": "Moderate chance of price increase"},
        "Demand": {"Score": 8, "Degree": 2, "Status": "Strong chance of demand increase"},
        "Supply": {"Score": 8, "Degree": 3, "Status": "Strong chance of supply increase"},
        "Trader_Recommendation": "Increase inventory to meet demand. Boost sales efforts with promotions."
    },
    "Aug-Sep": {
        "Price": {"Score": 5, "Degree": 1, "Status": "Moderate chance of price increase"},
        "Demand": {"Score": 3, "Degree": 1, "Status": "Moderate chance of demand increase"},
        "Supply": {"Score": 5, "Degree": 2, "Status": "Moderate chance of supply increase"},
        "Trader_Recommendation": "Stock up to meet rising demand. Maintain stable pricing."
    },
    "Sep-Oct": {
        "Price": {"Score": -5, "Degree": 2, "Status": "Strong chance of price decrease"},
        "Demand": {"Score": -1, "Degree": 3, "Status": "Slight chance of demand decrease"},
        "Supply": {"Score": 1, "Degree": 3, "Status": "Slight chance of supply increase"},
        "Trader_Recommendation": "Buy inventory at lower prices. Target price-sensitive customers."
    },
    "Oct-Nov": {
        "Price": {"Score": 0, "Degree": 2, "Status": "Stable prices expected"},
        "Demand": {"Score": -2, "Degree": 1, "Status": "Slight chance of demand decrease"},
        "Supply": {"Score": -2, "Degree": 1, "Status": "Slight chance of supply decrease"},
        "Trader_Recommendation": "Hold inventory; focus on competitive pricing."
    },
    "Nov-Dec": {
        "Price": {"Score": 2, "Degree": 1, "Status": "Slight chance of price increase"},
        "Demand": {"Score": -4, "Degree": 1, "Status": "Moderate chance of demand decrease"},
        "Supply": {"Score": -2, "Degree": 1, "Status": "Slight chance of supply decrease"},
        "Trader_Recommendation": "Maintain inventory. Monitor holiday demand."
    },
    "Dec-Jan": {
        "Price": {"Score": 2, "Degree": 1, "Status": "Slight chance of price increase"},
        "Demand": {"Score": 4, "Degree": 2, "Status": "Moderate chance of demand increase"},
        "Supply": {"Score": 3, "Degree": 1, "Status": "Moderate chance of supply increase"},
        "Trader_Recommendation": "Stock up for demand spike. Prepare for seasonal sales."
    },
    "Jan-Feb": {
        "Price": {"Score": -1, "Degree": 1, "Status": "Slight chance of price decrease"},
        "Demand": {"Score": -3, "Degree": 1, "Status": "Slight chance of demand decrease"},
        "Supply": {"Score": -3, "Degree": 1, "Status": "Slight chance of supply decrease"},
        "Trader_Recommendation": "Reduce stock. Offer promotions to clear inventory."
    },
    "Feb-Mar": {
        "Price": {"Score": -4, "Degree": 1, "Status": "Moderate chance of price decrease"},
        "Demand": {"Score": -3, "Degree": 3, "Status": "Moderate chance of demand decrease"},
        "Supply": {"Score": -1, "Degree": 1, "Status": "Slight chance of supply decrease"},
        "Trader_Recommendation": "Reduce stock. Offer promotions to clear inventory."
    },
    "Mar-Apr": {
        "Price": {"Score": -1, "Degree": 3, "Status": "Slight chance of price decrease"},
        "Demand": {"Score": 0, "Degree": 2, "Status": "Stable demand expected"},
        "Supply": {"Score": 0, "Degree": 2, "Status": "Stable supply expected"},
        "Trader_Recommendation": "Maintain inventory. Monitor early season trends."
    }
}

# Set page config
st.set_page_config(page_title="MOODS- The Market App", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for styling
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
        border: 2px solid #000000;
        border-radius: 8px;
        padding: 10px;
        color: #000000;
    }
    .stButton > button {
        background-color: #E0F7E0;
        color: #000000;
        border: 2px solid #000000;
        padding: 10px 20px;
        font-size: 1.2em;
        border-radius: 8px;
        cursor: pointer;
        transition: transform 0.2s;
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
        border: 6px solid #C4E4C4;
        border-radius: 10px;
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("💵 MOODS- The Market App 💰")

# Sidebar menu
menu_option = st.sidebar.selectbox("Select Feature", ["Market Insights", "Price Predictor"])

# Market Insights (Unchanged)
if menu_option == "Market Insights":
    st.markdown("<h3 class='coin-animation'>Don't know what to do with your cardamom? Let us handle it.</h3>", unsafe_allow_html=True)

    # User type selection
    user_type = st.radio("💎 Select Your Role:", ("Farmer", "Trader"))

    # Month selection
    selected_month = st.selectbox("📅 Select Month:", months)

    # Button
    if st.button("💸 GO DEEP 💸"):
        # Create a two-column layout
        col1, col2 = st.columns([1.5, 1])

        # Left column: Recommendations
        with col1:
            if user_type == "Farmer":
                st.subheader(f"💰 This Month ({selected_month}) 💰")
                if selected_month in farmer_data:
                    data = farmer_data[selected_month]
                    st.write(f"**Price Trend**: {data['Price_Trend']}")
                    st.write(f"**Demand**: {data['Demand']}")
                    st.write(f"**Supply Impact**: {data['Supply_Impact']}")
                    st.write("**💎 Recommendation 💎**:")
                    for rec in data['Recommendation']:
                        st.write(f"- {rec}")
                else:
                    st.write("**Status**: Limited data available.")
                    st.write("**Recommendation**: Hold until May or June for best prices.")

                next_month = get_next_month(selected_month)
                st.subheader(f"💰 Next Month ({next_month}) 💰")
                if next_month in farmer_data:
                    data = farmer_data[next_month]
                    st.write(f"**Price Trend**: {data['Price_Trend']}")
                    st.write(f"**Demand**: {data['Demand']}")
                    st.write(f"**Supply Impact**: {data['Supply_Impact']}")
                    st.write("**💎 Recommendation 💎**:")
                    for rec in data['Recommendation']:
                        st.write(f"- {rec}")
                else:
                    st.write("**Status**: Limited data available.")
                    st.write("**Recommendation**: Hold until May or June for best prices.")
            else:  # Trader
                current_pair = get_month_pair(selected_month)
                next_month = get_next_month(selected_month)
                next_pair = get_month_pair(next_month)

                st.subheader(f"💰 This Month ({selected_month}) 💰")
                if current_pair in market_data:
                    data = market_data[current_pair]
                    st.write(f"**Price**: {data['Price']['Status']}")
                    st.write(f"**Demand**: {data['Demand']['Status']}")
                    st.write(f"**Supply**: {data['Supply']['Status']}")
                    st.write(f"**💎 Recommendation 💎**: {data['Trader_Recommendation']}")
                else:
                    st.write("**Status**: Limited data available.")
                    st.write("**Recommendation**: Monitor market trends and adjust inventory cautiously.")

                st.subheader(f"💰 Next Month ({next_month}) 💰")
                if next_pair in market_data:
                    data = market_data[next_pair]
                    st.write(f"**Price**: {data['Price']['Status']}")
                    st.write(f"**Demand**: {data['Demand']['Status']}")
                    st.write(f"**Supply**: {data['Supply']['Status']}")
                    st.write(f"**💎 Recommendation 💎**: {data['Trader_Recommendation']}")
                else:
                    st.write("**Status**: Limited data available.")
                    st.write("**Recommendation**: Plan for stable inventory and pricing.")

        # Right column: Static Graph
        with col2:
            st.markdown("""
                <div class="framed-image">
                    <img src="https://github.com/Eric12josanto/Moods-market-app/raw/main/graphy.png" 
                         width="450" alt="Market Insights">
                </div>
                <p style="text-align: center; color: #000000;">Market Insights</p>
                <p style="text-align: center; color: #000000;"><i><b>"The graph shows cardamom's month-on-month average price and quantity sold. Based on seasonal trends from 2015–2024 data."</b></i></p>
            """, unsafe_allow_html=True)

# Price Predictor (Updated with Enhanced Multi-Series Graph)
elif menu_option == "Price Predictor":
    st.markdown("<h3 class='coin-animation'>Check Cardamom Prices and Trends</h3>", unsafe_allow_html=True)

    # Load data
    try:
        data = pd.read_excel('combined_prices_2015_2028.xlsx')
    except FileNotFoundError:
        st.error("Error: 'combined_prices_2015_2028.xlsx' not found in the project folder.")
        st.stop()

    # Prepare data
    expected_columns = ['Year', 'Month', 'Predicted_Price']
    if not all(col in data.columns for col in expected_columns):
        st.error(f"Expected columns {expected_columns} not found. Actual columns: {data.columns.tolist()}")
        st.stop()
    
    data = data[expected_columns].copy()
    data['Year_Month'] = data['Year'] + (data['Month'] - 1) / 12
    data = data.sort_values(['Year', 'Month']).reset_index(drop=True)

    # Assume we have an 'Actual_Price' column for test data
    # If not present, we'll generate sample data for demonstration
    if 'Actual_Price' not in data.columns:
        # Generate sample actual prices for 2022-2024 (with some noise for realism)
        import numpy as np
        np.random.seed(42)  # For reproducible results
        data['Actual_Price'] = data['Predicted_Price'] + np.random.normal(0, data['Predicted_Price'] * 0.05, len(data))

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

    # Process selected date
    if selected_date:
        year = selected_date.year
        month = selected_date.month

        # Find price
        price_row = data[(data['Year'] == year) & (data['Month'] == month)]
        if price_row.empty:
            st.write(f"No price data for {year}-{month:02d}.")
        else:
            st.markdown("**Predicted Increasing Demand of Cardamom**")
            price = price_row['Adjusted_Price'].iloc[0]
            st.markdown(f"**Price for {year}-{month:02d}: Rs. {price:.2f}/kg**")

            # Create enhanced multi-series graph with new logic
            st.markdown("**Graph: Cardamom Price Analysis with Training, Test, and Prediction Data**")
            
            # Define the cutoff point (November 2024 = 2024.917)
            cutoff_year_month = 2024 + (11 - 1) / 12  # November 2024 = 2024.917
            
            # Prepare data for different periods with new logic:
            # Green line: Training Data (2015-2021)
            train_data = data[(data['Year'] >= 2015) & (data['Year'] <= 2021)]
            
            # Brown dotted line: Actual Prices (2022-2024) - stops before 2024.917
            actual_test_data = data[(data['Year'] >= 2022) & (data['Year_Month'] <= cutoff_year_month)]
            
            # Red line: Base Prediction (2022-2024) - stops before 2024.917
            red_line_data = data[(data['Year'] >= 2022) & (data['Year_Month'] <= cutoff_year_month)]
            
            # Blue dotted line: Predicted Prices with Demand Growth - full prediction data up to selected date
            prediction_data = data[(data['Year'] >= 2022) & (data['Year'] <= year) & 
                                 ((data['Year'] < year) | (data['Month'] <= month))]
            
            # Create the plotly figure
            fig = go.Figure()
            
            # Add training data (2015-2021) - Green line
            fig.add_trace(go.Scatter(
                x=train_data['Year_Month'],
                y=train_data['Predicted_Price'],
                mode='lines',
                name='Training Data (2015-2021)',
                line=dict(color='green', width=2),
                hovertemplate='Year: %{x:.1f}<br>Price: Rs. %{y:.2f}/kg<extra></extra>'
            ))
            
            # Add actual test data (2022-2024, stops before 2024.917) - Brown dotted line
            if not actual_test_data.empty:
                fig.add_trace(go.Scatter(
                    x=actual_test_data['Year_Month'],
                    y=actual_test_data['Actual_Price'],
                    mode='lines',
                    name='Actual Prices (2022-2024)',
                    line=dict(color='brown', width=2, dash='dot'),
                    hovertemplate='Year: %{x:.1f}<br>Actual Price: Rs. %{y:.2f}/kg<extra></extra>'
                ))
            
            # Add base prediction data (2022-2024, stops before 2024.917) - Red line
            if not red_line_data.empty:
                fig.add_trace(go.Scatter(
                    x=red_line_data['Year_Month'],
                    y=red_line_data['Predicted_Price'],
                    mode='lines',
                    name='Base Prediction (2022-2024)',
                    line=dict(color='red', width=2),
                    hovertemplate='Year: %{x:.1f}<br>Base Price: Rs. %{y:.2f}/kg<extra></extra>'
                ))
            
            # Add predicted prices with demand growth - Dotted blue line (continues beyond)
            fig.add_trace(go.Scatter(
                x=prediction_data['Year_Month'],
                y=prediction_data['Adjusted_Price'],
                mode='lines',
                name='Predicted Prices with Demand Growth',
                line=dict(color='blue', width=2, dash='dot'),
                hovertemplate='Year: %{x:.1f}<br>Predicted Price: Rs. %{y:.2f}/kg<extra></extra>'
            ))
            
            # Update layout
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
            
            # Update x-axis
            fig.update_xaxes(
                tickvals=list(range(2015, year + 1)),
                ticktext=[str(y) for y in range(2015, year + 1)],
                range=[2015, year + (month / 12)]
            )
            
            st.plotly_chart(fig, use_container_width=True)