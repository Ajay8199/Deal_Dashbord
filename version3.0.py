import streamlit as st
import pandas as pd
import mysql.connector
from PIL import Image
from datetime import datetime
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

image = Image.open("/home/ajay/Videos/PubMatic.png")
# Rest of your code...
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user='root',
        password='Kumar@8199',
        database="test"
    )
def main():
    st.set_page_config(layout='wide', initial_sidebar_state='expanded')
    st.sidebar.image(image, caption='', use_column_width=True)
    st.sidebar.header('Dashboard `version 3`')
    st.sidebar.subheader('Deal Creator Name')
    Creator_Name = st.sidebar.text_input("Enter Creator Name")
    st.sidebar.subheader('Enter Start Date')
    start_date = st.sidebar.date_input("Select Start Date", max_value=datetime.now().date())
    st.sidebar.subheader('Enter End Date')
    end_date = st.sidebar.date_input("Select End Date", max_value=datetime.now().date())
    st.sidebar.markdown('''
        ---
        Created with ❤️ by Ajay Shinde | Technical Escalations Team.
        ''')

    # Row A
    col1 = st.columns(1)
    col1[0].title("Programmatic Deal Monitoring Dashboard:star:")
    # Rest of your code...

    try:
        connection = create_connection()
        if connection.is_connected():
            cursor = connection.cursor()

            if st.button("Fetch Metrics"):
                col_summary = st.columns(3)  # Create 3 columns for the Deal Summary

                # Total number of deals created by the user
                query_total_deals = f"""
                                SELECT COUNT(pub_deal_id) AS total_deals
                                FROM dd_troublshooting
                                WHERE creator_name = '{Creator_Name}'
                                AND DATE BETWEEN '{start_date}' AND '{end_date}'
                            """
                cursor.execute(query_total_deals)
                total_deals_result = cursor.fetchone()
                total_deals = total_deals_result[0] if total_deals_result else 0
                col_summary[0].metric("Total Deals", f"{total_deals}")

                # Total monetized deals
                query_monetized_deals = f"""
                                SELECT COUNT(pub_deal_id) AS total_monetized_deals
                                FROM dd_troublshooting
                                WHERE creator_name = '{Creator_Name}'
                                AND DATE BETWEEN '{start_date}' AND '{end_date}'
                                AND spend > 0
                            """
                cursor.execute(query_monetized_deals)
                monetized_deals_result = cursor.fetchone()
                total_monetized_deals = monetized_deals_result[0] if monetized_deals_result else 0
                col_summary[1].metric("Total Monetized Deals", f"{total_monetized_deals}")

                # Total non-monetized deals
                query_non_monetized_deals = f"""
                                SELECT COUNT(pub_deal_id) AS total_non_monetized_deals
                                FROM dd_troublshooting
                                WHERE creator_name = '{Creator_Name}'
                                AND DATE BETWEEN '{start_date}' AND '{end_date}'
                                AND spend = 0
                            """
                cursor.execute(query_non_monetized_deals)
                non_monetized_deals_result = cursor.fetchone()
                total_non_monetized_deals = non_monetized_deals_result[0] if non_monetized_deals_result else 0
                col_summary[2].metric("Total Non-Monetized Deals", f"{total_non_monetized_deals}")

                # Function to fetch deal summary for a specific deal type
                def fetch_deal_summary(deal_type):
                    # SQL query for total PG deals
                    query_total_pgdeals = f"""
                        SELECT COUNT(pub_deal_id) AS total_deals
                        FROM dd_troublshooting
                        WHERE creator_name = '{Creator_Name}'
                        AND DATE BETWEEN '{start_date}' AND '{end_date}'
                        AND deal_type = 'PG_Deal'
                    """
                    cursor.execute(query_total_pgdeals)
                    total_pgdeals_result = cursor.fetchone()
                    total_pg_deals = total_pgdeals_result[0] if total_pgdeals_result else 0

                    # SQL query for monetized PG deals
                    query_monetized_pg_deals = f"""
                        SELECT COUNT(pub_deal_id) AS total_monetized_deals
                        FROM dd_troublshooting
                        WHERE creator_name = '{Creator_Name}'
                        AND DATE BETWEEN '{start_date}' AND '{end_date}'
                        AND deal_type = 'PG_Deal' AND spend > 0
                    """
                    cursor.execute(query_monetized_pg_deals)
                    monetized_pg_deals_result = cursor.fetchone()
                    total_monetized_pg_deals = monetized_pg_deals_result[0] if monetized_pg_deals_result else 0

                    # SQL query for non-monetized PG deals
                    query_non_monetized_pg_deals = f"""
                        SELECT COUNT(pub_deal_id) AS total_non_monetized_deals
                        FROM dd_troublshooting
                        WHERE creator_name = '{Creator_Name}'
                        AND DATE BETWEEN '{start_date}' AND '{end_date}'
                        AND deal_type = 'PG_Deal' AND spend = 0
                    """
                    cursor.execute(query_non_monetized_pg_deals)
                    non_monetized_pg_deals_result = cursor.fetchone()
                    total_non_monetized_pg_deals = non_monetized_pg_deals_result[
                        0] if non_monetized_pg_deals_result else 0

                    # SQL query for total PMP deals
                    query_total_pmpdeals = f"""
                        SELECT COUNT(pub_deal_id) AS total_deals
                        FROM dd_troublshooting
                        WHERE creator_name = '{Creator_Name}'
                        AND DATE BETWEEN '{start_date}' AND '{end_date}'
                        AND deal_type = 'PMP'
                    """
                    cursor.execute(query_total_pmpdeals)
                    total_pmpdeals_result = cursor.fetchone()
                    total_pmp_deals = total_pmpdeals_result[0] if total_pmpdeals_result else 0

                    # SQL query for monetized PMP deals
                    query_monetized_pmp_deals = f"""
                        SELECT COUNT(pub_deal_id) AS total_monetized_deals
                        FROM dd_troublshooting
                        WHERE creator_name = '{Creator_Name}'
                        AND DATE BETWEEN '{start_date}' AND '{end_date}'
                        AND deal_type = 'PMP' AND spend > 0
                    """
                    cursor.execute(query_monetized_pmp_deals)
                    monetized_pmp_deals_result = cursor.fetchone()
                    total_monetized_pmp_deals = monetized_pmp_deals_result[0] if monetized_pmp_deals_result else 0

                    # SQL query for non-monetized PMP deals
                    query_non_monetized_pmp_deals = f"""
                        SELECT COUNT(pub_deal_id) AS total_non_monetized_deals
                        FROM dd_troublshooting
                        WHERE creator_name = '{Creator_Name}'
                        AND DATE BETWEEN '{start_date}' AND '{end_date}'
                        AND deal_type = 'PMP' AND spend = 0
                    """
                    cursor.execute(query_non_monetized_pmp_deals)
                    non_monetized_pmp_deals_result = cursor.fetchone()
                    total_non_monetized_pmp_deals = non_monetized_pmp_deals_result[0] if non_monetized_pmp_deals_result else 0

                    # SQL query for total preferred deals
                    query_total_preferred_deals = f"""
                        SELECT COUNT(pub_deal_id) AS total_deals
                        FROM dd_troublshooting
                        WHERE creator_name = '{Creator_Name}'
                        AND DATE BETWEEN '{start_date}' AND '{end_date}'
                        AND deal_type = 'Preferred'
                    """
                    cursor.execute(query_total_preferred_deals)
                    total_preferred_deals_result = cursor.fetchone()
                    total_preferred_deals = total_preferred_deals_result[0] if total_preferred_deals_result else 0

                    # SQL query for monetized preferred deals
                    query_monetized_preferred_deals = f"""
                        SELECT COUNT(pub_deal_id) AS total_monetized_deals
                        FROM dd_troublshooting
                        WHERE creator_name = '{Creator_Name}'
                        AND DATE BETWEEN '{start_date}' AND '{end_date}'
                        AND deal_type = 'Preferred' AND spend > 0
                    """
                    cursor.execute(query_monetized_preferred_deals)
                    monetized_preferred_deals_result = cursor.fetchone()
                    total_monetized_preferred_deals = monetized_preferred_deals_result[0] if monetized_preferred_deals_result else 0

                    # SQL query for non-monetized preferred deals
                    query_non_monetized_preferred_deals = f"""
                        SELECT COUNT(pub_deal_id) AS total_non_monetized_deals
                        FROM dd_troublshooting
                        WHERE creator_name = '{Creator_Name}'
                        AND DATE BETWEEN '{start_date}' AND '{end_date}'
                        AND deal_type = 'Preferred' AND spend = 0
                    """
                    cursor.execute(query_non_monetized_preferred_deals)
                    non_monetized_preferred_deals_result = cursor.fetchone()
                    total_non_monetized_preferred_deals = non_monetized_preferred_deals_result[0] if non_monetized_preferred_deals_result else 0

                    return total_pg_deals, total_monetized_pg_deals, total_non_monetized_pg_deals, total_pmp_deals, total_monetized_pmp_deals, total_non_monetized_pmp_deals, total_preferred_deals, total_monetized_preferred_deals, total_non_monetized_preferred_deals

                # PG Deal Summary
                total_pg_deals, total_monetized_pg_deals, total_non_monetized_pg_deals,total_pmp_deals, total_monetized_pmp_deals,total_non_monetized_pmp_deals,total_prefered_deals,total_monetized_preferred_deals,total_non_monetized_preferred_deals = fetch_deal_summary('deal_type')
                col_summary[0].metric("Total PG Deals", f"{total_pg_deals}")
                col_summary[0].metric("Total PMP Deals", f"{total_pmp_deals}")
                col_summary[0].metric("Total Preferred Deals", f"{total_prefered_deals}")

                # PMP Deal Summary
                #total_pmp_deals, total_monetized_pmp_deals, total_non_monetized_pmp_deals = fetch_deal_summary('PMP_Deal')
                col_summary[1].metric("Total Monetized PG Deals", f"{total_monetized_pg_deals}")
                col_summary[1].metric("Total Monetized PMP Deals", f"{total_monetized_pmp_deals}")
                col_summary[1].metric("Total Monetized Preferred Deals", f"{total_monetized_preferred_deals}")

                # Preferred Deal Summary
                #total_prefered_deals, total_monetized_prefered_deals, total_non_monetized_prefered_deals = fetch_deal_summary('Preferred_Deal')
                col_summary[2].metric("Total Non-Monetized PG Deals", f"{total_non_monetized_pg_deals}")
                col_summary[2].metric("Total Non-Monetized PMP Deals", f"{total_non_monetized_pmp_deals}")
                col_summary[2].metric("Total Non-Monetized Preferred Deals", f"{total_non_monetized_preferred_deals}")

###########################################################################################################################
            # Row B
            st.markdown('### Deals Data created By User')
            col1, col2, col3, col4, col5 = st.columns(5)  # Create 5 columns here

            if col1.button("All Deals by User", help="All Deals data for Selected User and Date Range"):
                # Fetch all data from the table
                query_deals_data = f"""
                                SELECT DATE, deal_meta_id, pub_deal_id, deal_name, deal_status, deal_type, creator_name, 
                                creation_time, start_date, end_date, bid_request_send_to_dsp,non_zero_bid_recevied,paid_impressions, spend, 
                                lost_bid_auction_count,lost_bid_block_list_count,lost_bid_deal_allowlist_fl_count,lost_bid_floor_count,lost_bid_pub_auction_count 
                                FROM dd_troublshooting 
                                WHERE creator_name = '{Creator_Name}' 
                                AND DATE BETWEEN '{start_date}' AND '{end_date}' 
                                ORDER BY DATE DESC;
                            """
                cursor.execute(query_deals_data)
                deals_data = cursor.fetchall()
                # Display all data
                if deals_data:
                    st.subheader("User's All Deals")
                    df_all_data = pd.DataFrame(deals_data, columns=[col[0] for col in cursor.description])
                    st.dataframe(df_all_data)
                    # Download button for all data
                    csv_all_data = df_all_data.to_csv(index=False)
                    st.download_button(
                        label="Download All Deals Data",
                        data=csv_all_data,
                        file_name="all_data.csv",
                        mime="text/csv"
                    )
                else:
                    st.warning("No deals were found for the selected date range and user, Please fill the "
                               "correct name")
            ###############################################################################################################
            if col2.button("Non Monetized Deals", help="All Non Monetized Deals Data for Selected User and Date Range"):
                # Fetch data where spend is less than 1 for the selected creator name and date
                query_non_performing_deals = f"""
                                SELECT DATE,deal_meta_id, pub_deal_id, deal_name, deal_status, deal_type, creator_name,bid_request_send_to_dsp,non_zero_bid_recevied, 
                                spend AS total_spend 
                                FROM dd_troublshooting 
                                WHERE creator_name = '{Creator_Name}' 
                                AND DATE BETWEEN '{start_date}' AND '{end_date}' AND spend = 0 
                                ORDER BY total_spend ASC;
                            """
                cursor.execute(query_non_performing_deals)
                non_performing_deals = cursor.fetchall()

                # Display data where spend is less than 1 for the selected creator name and date
                if non_performing_deals:
                    st.subheader("Data for Non monetized Deals")
                    df_spend_less_than_1 = pd.DataFrame(non_performing_deals,
                                                        columns=[col[0] for col in cursor.description])
                    st.dataframe(df_spend_less_than_1)
                    # Download button for spend < 1 data
                    csv_spend_less_than_1 = df_spend_less_than_1.to_csv(index=False)
                    st.download_button(
                        label="Download Non monetized Deals",
                        data=csv_spend_less_than_1,
                        file_name="non_monetized_deals.csv",
                        mime="text/csv"
                    )
                else:
                    st.warning("No deals were found for the selected date range and user.")
            ###############################################################################################################################
            if col3.button("Monetized Deals", help="All Monetized Deals Data for Selected User and Date Range"):
                # Fetch data where spend is greater than or equal to 1 for the selected creator name and date
                query_top_deals = f"""
                                SELECT DATE,deal_meta_id, pub_deal_id, deal_name, deal_status, deal_type, creator_name, bid_request_send_to_dsp,non_zero_bid_recevied,
                                spend AS total_spend 
                                FROM dd_troublshooting 
                                WHERE creator_name = '{Creator_Name}' 
                                AND DATE BETWEEN '{start_date}' AND '{end_date}' AND spend > 0
                                ORDER BY total_spend DESC;
                            """
                cursor.execute(query_top_deals)
                top_deals = cursor.fetchall()
                # Display data where spend is greater than or equal to 1 for the selected creator name and date
                if top_deals:
                    st.subheader("Data for monetized Deals")
                    df_spend_greater_than_1 = pd.DataFrame(top_deals,
                                                           columns=[col[0] for col in cursor.description])
                    st.dataframe(df_spend_greater_than_1)
                    # Download button for monetized deals
                    csv_spend_greater_than_1 = df_spend_greater_than_1.to_csv(index=False)
                    st.download_button(
                        label="Download Monetized Deals",
                        data=csv_spend_greater_than_1,
                        file_name="monetized_deals.csv",
                        mime="text/csv"
                    )
                else:
                    st.warning(
                        "No deals were found for the selected date range and user.")
            ##########################################################################################################
            if col4.button("Deals Not Sending Bid Requests",
                           help="All Deals with No bidrequest to DSP for Selected User and Date Range"):
                # Fetch all data from the table
                no_bid_request_to_DSP = f"""
                                SELECT DATE,deal_meta_id, pub_deal_id, deal_status, deal_type, creator_name, bid_request_send_to_dsp, non_zero_bid_recevied
                                FROM dd_troublshooting
                                WHERE creator_name = '{Creator_Name}' AND `DATE` BETWEEN '{start_date}' AND '{end_date}'
                                AND bid_request_send_to_dsp <= 0;
                            """
                cursor.execute(no_bid_request_to_DSP)
                no_bid_request = cursor.fetchall()
                # Display no_bid_request Deals data
                if no_bid_request:
                    st.subheader("Deals Not Sending Bid Requests To DSP")
                    no_bid_request_data = pd.DataFrame(no_bid_request, columns=[col[0] for col in cursor.description])
                    st.dataframe(no_bid_request_data)
                    # Download button for all data
                    csv_nobidrequest_data = no_bid_request_data.to_csv(index=False)
                    st.download_button(
                        label="Download All Data",
                        data=csv_nobidrequest_data,
                        file_name="No_bidrequest_deals.csv",
                        mime="text/csv"
                    )
                else:
                    st.warning("No deals were found for the selected condition")

            ########################################################################################################
            if col5.button("Deals With No Response",
                           help="All Deals with No Bidresponse from DSP For Selected User and Date Range"):
                # Fetch deals with no bid responses
                NO_bid_response_deals = f"""
                                SELECT date, deal_meta_id, pub_deal_id, deal_status, deal_type, creator_name, bid_request_send_to_dsp,IFNULL(non_zero_bid_recevied, 0) AS non_zero_bid_recevied, paid_impressions, spend, lost_bid_auction_count, lost_bid_block_list_count, lost_bid_deal_allowlist_fl_count, lost_bid_floor_count, lost_bid_pub_auction_count
                                FROM dd_troublshooting
                                WHERE creator_name = '{Creator_Name}' AND date BETWEEN '{start_date}' AND '{end_date}'
                                AND bid_request_send_to_dsp > 0 AND non_zero_bid_recevied=0;
                            """
                cursor.execute(NO_bid_response_deals)
                no_bid_response = cursor.fetchall()
                # Display no_bid_response Deals data
                if no_bid_response:
                    st.subheader("Deals with no bid responses")
                    no_bid_response_data = pd.DataFrame(no_bid_response, columns=[col[0] for col in cursor.description])
                    st.dataframe(no_bid_response_data)
                    # Download button for all data
                    csv_nobidresponse_data = no_bid_response_data.to_csv(index=False)
                    st.download_button(
                        label="Download Deals with No Responses",
                        data=csv_nobidresponse_data,
                        file_name="No_bidresponse_deals.csv",
                        mime="text/csv"
                    )
                else:
                    st.warning("No deals were found for the selected date range and user.")
            connection.close()

            # Rest of your code...

    except Exception as e:
        st.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
