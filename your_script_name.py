import streamlit as st
import pandas as pd
import openai

# Set Streamlit page configuration
st.set_page_config(
    page_title="Fashion Sales Dashboard",
    page_icon="🛍️",
    layout="wide"
)

# Dummy data for demonstration
@st.cache_data
def load_dummy_data():
    return pd.DataFrame({
        'Month_Name': ['January', 'February', 'March', 'April'],
        'Brand': ['Brand A', 'Brand B', 'Brand C', 'Brand D'],
        'Quantity_Sold': [120, 80, 150, 100],
        'Quantity_In_Stock': [60, 40, 30, 20],
        'Marketing_Group': ['Group 1', 'Group 2', 'Group 1', 'Group 2'],
        'Classified_Category': ['Category 1', 'Category 2', 'Category 1', 'Category 2'],
        'Category': ['Men', 'Women', 'Kids', 'Men']
    })

data = load_dummy_data()

# Sidebar for navigation
st.sidebar.title("Navigation")
pages = {
    "Sales Dashboard": "dashboard",
    "Inventory Management": "inventory",
    "Executive Insights": "insights"
}
page = st.sidebar.radio("Go to", list(pages.keys()))

# Define each page function
def sales_dashboard():
    st.title("📊 Sales Dashboard")
    st.markdown("### Analyze sales trends and performance metrics.")

    # Filter data
    marketing_group = st.sidebar.selectbox("Select Marketing Group", data['Marketing_Group'].unique())
    classified_category = st.sidebar.selectbox("Select Classified Category", data['Classified_Category'].unique())
    filtered_data = data[
        (data['Marketing_Group'] == marketing_group) &
        (data['Classified_Category'] == classified_category)
    ]
    st.dataframe(filtered_data)

    # Sales Trend Analysis
    st.subheader("Sales Trend Analysis")
    monthly_sales = filtered_data.groupby(['Month_Name', 'Brand'])['Quantity_Sold'].sum().reset_index()
    if not monthly_sales.empty:
        st.line_chart(monthly_sales.pivot(index='Month_Name', columns='Brand', values='Quantity_Sold').fillna(0))
    else:
        st.write("No data available for the selected filters.")

def inventory_management():
    st.title("📦 Inventory Management")
    st.markdown("### Monitor stock levels and inventory turnover.")
    
    # Dummy inventory stats
    st.subheader("Inventory Overview")
    inventory_stats = pd.DataFrame({
        "Brand": ["Brand A", "Brand B", "Brand C", "Brand D"],
        "Stock Level": [100, 50, 75, 20],
        "Turnover Rate": [1.2, 0.8, 1.5, 0.7]
    })
    st.dataframe(inventory_stats)

    st.subheader("Stock-Out Alerts")
    st.warning("No stock-outs detected.")

def executive_insights():
    st.title("💡 Executive Insights")
    st.markdown("### Gain insights and recommendations powered by AI.")
    
    questions = [
        "Which items reach 75% and 50% sold?",
        "Identify best-selling items by category.",
        "Describe slow-moving products.",
    ]
    for i, question in enumerate(questions, start=1):
        st.subheader(f"Insight {i}: {question}")
        st.text("Generated AI-driven recommendations would appear here (requires OpenAI API key).")

        # Placeholder for AI integration
        st.info("AI integration is currently mocked for this demo.")

# Page routing
if page == "Sales Dashboard":
    sales_dashboard()
elif page == "Inventory Management":
    inventory_management()
elif page == "Executive Insights":
    executive_insights()

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("### About")
st.sidebar.info("This is a multi-page Streamlit application for fashion sales analytics.")
