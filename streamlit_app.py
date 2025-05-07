import streamlit as st

# Custom CSS for updated theme
st.markdown("""
    <style>
    .main {
        background-color: #FFFFFF;
        
    }
    h1 {
        color: #000000;
        text-align: center;
        font-size: 2.5em;
    }
    h3 {
        color: #000000;
    }
    .stRadio > label, .stSelectbox > label {
        color: #00008B;
        font-size: 1.1em;
    }
    .stRadio > div > label, .stSelectbox > div > label {
        color: #000000;
    }
    .stRadio > div, .stSelectbox > div {
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
    </style>
""", unsafe_allow_html=True)

# Updated title with same emojis
st.title("💵 MOODS- The market App 💰")

# Add a decorative subheader
st.markdown("<h3 class='coin-animation'>Grow Your Riches with Smart Market Moves!</h3>", unsafe_allow_html=True)

# User type selection with dark blue label
user_type = st.radio("💎 Select Your Role:", ("Farmer", "Trader"))

# Month selection with dark blue label
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
selected_month = st.selectbox("📅 Select Month:", months)

# Farmer data
farmer_data = {
    "January": {
        "Price_Trend": "Stable prices",
        "Demand": "Moderate post-harvest demand",
        "Supply_Impact": "Erratic rain reduces yields",
        "Recommendation": [
            "Hold unless cash is urgent",
            "Wait for price rise in March-April"
        ]
    },
    "February": {
        "Price_Trend": "Slight price increase",
        "Demand": "Moderate demand",
        "Supply_Impact": "Heat stress lowers tillers",
        "Recommendation": [
            "Sell 10-20% if prices up 5-10% from January",
            "Hold rest for March"
        ]
    },
    "March": {
        "Price_Trend": "Significant price increase",
        "Demand": "High festival demand",
        "Supply_Impact": "Delayed rains shorten harvest",
        "Recommendation": [
            "Sell 20-30% if prices up 10-15% from February",
            "Target festival markets"
        ]
    },
    "April": {
        "Price_Trend": "High prices",
        "Demand": "Strong export demand",
        "Supply_Impact": "Dry spells reduce pod size",
        "Recommendation": [
            "Sell 20-30% if prices up 15-20% from March",
            "Focus on export buyers"
        ]
    },
    "May": {
        "Price_Trend": "Stable prices",
        "Demand": "Stable pre-monsoon demand",
        "Supply_Impact": "Waterlogging increases diseases",
        "Recommendation": [
            "Hold unless supply issues spike prices",
            "Monitor weather forecasts"
        ]
    },
    "June": {
        "Price_Trend": "Slight price increase",
        "Demand": "Moderate demand",
        "Supply_Impact": "Flooding damages plants",
        "Recommendation": [
            "Sell 10-15% if prices up 5-10% due to weather",
            "Hold rest for July"
        ]
    },
    "July": {
        "Price_Trend": "Peak prices",
        "Demand": "Strong demand",
        "Supply_Impact": "Landslides and pests cut yields",
        "Recommendation": [
            "Sell 30-40% if prices up 20-25% from June",
            "Act fast on high prices"
        ]
    },
    "August": {
        "Price_Trend": "High but stable prices",
        "Demand": "Strong demand",
        "Supply_Impact": "Wet spells delay maturation",
        "Recommendation": [
            "Sell 20-30% if prices remain high",
            "Prepare for harvest"
        ]
    },
    "September": {
        "Price_Trend": "Slight price decrease",
        "Demand": "Moderate demand",
        "Supply_Impact": "Unseasonal rains cause losses",
        "Recommendation": [
            "Sell remaining stock before harvest",
            "Avoid post-harvest price drop"
        ]
    },
    "October": {
        "Price_Trend": "Significant price decrease",
        "Demand": "Low demand",
        "Supply_Impact": "New harvest floods market",
        "Recommendation": [
            "Avoid selling unless prices spike",
            "Store for later months"
        ]
    },
    "November": {
        "Price_Trend": "Low prices",
        "Demand": "Low post-harvest demand",
        "Supply_Impact": "Heavy rain damages capsules",
        "Recommendation": [
            "Hold off unless urgent",
            "Wait for price recovery"
        ]
    },
    "December": {
        "Price_Trend": "Slight price recovery",
        "Demand": "Moderate demand",
        "Supply_Impact": "Warmer winters affect dormancy",
        "Recommendation": [
            "Sell 10-20% if prices up 5-10% from November",
            "Hold rest for March"
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
        "Demand": {"Score": 0, "Degree": 1, "Status": "Steady demand"},
        "Supply": {"Score": 0, "Degree": 1, "Status": "Steady supply"},
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
        "Demand": {"Score": -1, "Degree": 1, "Status": "Slight chance of demand decrease"},
        "Supply": {"Score": 1, "Degree": 1, "Status": "Slight chance of supply increase"},
        "Trader_Recommendation": "Buy inventory at lower prices. Target price-sensitive customers."
    },
    "Oct-Nov": {
        "Price": {"Score": -3, "Degree": 2, "Status": "Moderate chance of price decrease"},
        "Demand": {"Score": -2, "Degree": 1, "Status": "Slight chance of demand decrease"},
        "Supply": {"Score": 2, "Degree": 1, "Status": "Slight chance of supply increase"},
        "Trader_Recommendation": "Hold inventory; focus on competitive pricing."
    },
    "Nov-Dec": {
        "Price": {"Score": 0, "Degree": 1, "Status": "Stable prices expected"},
        "Demand": {"Score": 0, "Degree": 1, "Status": "Stable demand expected"},
        "Supply": {"Score": 0, "Degree": 1, "Status": "Stable supply expected"},
        "Trader_Recommendation": "Maintain inventory. Monitor holiday demand."
    },
    "Dec-Jan": {
        "Price": {"Score": 2, "Degree": 1, "Status": "Slight chance of price increase"},
        "Demand": {"Score": 4, "Degree": 2, "Status": "Moderate chance of demand increase"},
        "Supply": {"Score": 3, "Degree": 1, "Status": "Moderate chance of supply increase"},
        "Trader_Recommendation": "Stock up for demand spike. Prepare for seasonal sales."
    },
    "Jan-Feb": {
        "Price": {"Score": 1, "Degree": 1, "Status": "Slight chance of price increase"},
        "Demand": {"Score": 2, "Degree": 1, "Status": "Slight chance of demand increase"},
        "Supply": {"Score": 1, "Degree": 1, "Status": "Slight chance of supply increase"},
        "Trader_Recommendation": "Maintain inventory; focus on marketing."
    },
    "Feb-Mar": {
        "Price": {"Score": -1, "Degree": 1, "Status": "Slight chance of price decrease"},
        "Demand": {"Score": -3, "Degree": 2, "Status": "Moderate chance of demand decrease"},
        "Supply": {"Score": -2, "Degree": 1, "Status": "Slight chance of supply decrease"},
        "Trader_Recommendation": "Reduce stock. Offer promotions to clear inventory."
    },
    "Mar-Apr": {
        "Price": {"Score": 0, "Degree": 1, "Status": "Stable prices expected"},
        "Demand": {"Score": 0, "Degree": 1, "Status": "Stable demand expected"},
        "Supply": {"Score": 0, "Degree": 1, "Status": "Stable supply expected"},
        "Trader_Recommendation": "Maintain inventory. Monitor early season trends."
    }
}

# Helper functions
def get_next_month(current_month):
    month_index = months.index(current_month)
    next_month_index = (month_index + 1) % 12
    return months[next_month_index]

def get_month_pair(current_month):
    prev_month = months[(months.index(current_month) - 1) % 12]
    return f"{prev_month[:3]}-{current_month[:3]}"

# Updated button text with same emojis
if st.button("💸 GO DEEP 💸"):
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
            st.write("**Recommendation**: Hold until March, April, or July for best prices.")

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
            st.write("**Recommendation**: Hold until March, April, or July for best prices.")
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