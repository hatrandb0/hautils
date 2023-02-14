import streamlit as st

st.set_page_config(
    page_title="🌐 URL Generation",
    page_icon="🌐",
)

st.write("# URL Generation 🌐")

url_prefix = {
    "Shopee VN BI BD Jira Agent Portal": "https://jira.shopee.io/projects/SPVNBIBD/queues/custom/710/SPVNBIBD-",
    "Shopee VN BI BD Jira Customer Portal": "https://jira.shopee.io/servicedesk/customer/portal/52/SPVNBIBD-"

}

url_template = st.selectbox(
    "Choose a URL template",
    url_prefix.keys()
        )

post_fix = st.text_input("Enter ticket number here, e.g 5350")

requested_url = url_prefix[url_template] + post_fix


if post_fix:
    st.write("Your requested URL: ", requested_url)

