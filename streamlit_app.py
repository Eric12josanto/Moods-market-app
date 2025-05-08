import streamlit as st

# Define the months list first, as it's used by helper functions
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Helper functions
def get_next_month(current_month):
    month_index = months.index(current_month)
    next_month_index = (month_index + 1) % 12
    return months[next_month_index]

def get_month_pair(current_month):
    prev_month = months[(months.index(current_month) - 1) % 12]
    return f"{prev_month[:3]}-{current_month[:3]}"

# Farmer data (updated based on new tables)
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

# Trader data (updated directly from new tables)
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

# Disable Streamlit's theme override and set white background
st.set_page_config(page_title="MOODS- The market App", layout="wide", initial_sidebar_state="collapsed")
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

# Title
st.title("💵 MOODS- The market App 💰")

# Subheader
st.markdown("<h3 class='coin-animation'>Don’t know what to do with your cardamom? Let us handle it.</h3>", unsafe_allow_html=True)

# User type selection
user_type = st.radio("💎 Select Your Role:", ("Farmer", "Trader"))

# Month selection
selected_month = st.selectbox("📅 Select Month:", months)

# Button
if st.button("💸 GO DEEP 💸"):
    # Display the image after button press with reduced size
    st.image("https://github.com/Eric12josanto/Moods-market-app/raw/main/graphy.png", 
             caption="Your Cardamom Market Guide", 
             width=450)  # Set width to 450px (approximately half of default container width)

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