import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="Joshni Currency Converter",
    page_icon="💱",
    layout="centered"
)

# Title
st.title("💱 Joshni Currency Converter")
st.write("Convert money easily from one currency to another.")

# Currency options
currencies = {
    "Indian Rupee (INR)": "INR",
    "US Dollar (USD)": "USD",
    "Euro (EUR)": "EUR",
    "British Pound (GBP)": "GBP",
    "Japanese Yen (JPY)": "JPY",
    "Australian Dollar (AUD)": "AUD",
    "Canadian Dollar (CAD)": "CAD",
    "Singapore Dollar (SGD)": "SGD",
    "Swiss Franc (CHF)": "CHF"
}

# Amount input
amount = st.number_input(
    "Enter Amount",
    min_value=0.0,
    value=1.0,
    step=1.0
)

# Currency selection
from_currency_name = st.selectbox(
    "From Currency",
    list(currencies.keys())
)

to_currency_name = st.selectbox(
    "To Currency",
    list(currencies.keys()),
    index=1
)

from_currency = currencies[from_currency_name]
to_currency = currencies[to_currency_name]

# Convert button
if st.button("💱 Convert Currency", use_container_width=True):

    if amount <= 0:
        st.warning("⚠️ Please enter an amount greater than 0.")

    elif from_currency == to_currency:
        st.success(
            f"{amount:.2f} {from_currency} = "
            f"{amount:.2f} {to_currency}"
        )

    else:
        try:
            # Free exchange-rate API
            url = (
                f"https://api.frankfurter.app/latest"
                f"?amount={amount}"
                f"&from={from_currency}"
                f"&to={to_currency}"
            )

            response = requests.get(url, timeout=10)
            data = response.json()

            converted_amount = data["rates"][to_currency]

            st.success(
                f"✅ {amount:.2f} {from_currency} = "
                f"{converted_amount:.2f} {to_currency}"
            )

            st.info(
                f"Conversion: {from_currency} → {to_currency}"
            )

        except Exception:
            st.error(
                "❌ Unable to get the exchange rate. "
                "Please check your internet connection and try again."
            )

st.divider()

st.caption("💱 Created using Python and Streamlit")