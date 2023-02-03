#This code example uses the streamlit and pandas libraries to create a table of invoices issued and allow authorized users to create new invoices.
#The user can select a client from a drop-down list and then fill out a form with the relevant information to create a new invoice. 
#The new invoice is then appended to the table of invoices issued and a success message is displayed. 
#The code also includes a placeholder for generating a word invoice based on a pre-defined template.

import streamlit as st
import pandas as pd

# Data to store invoices
data = {"Invoice No": [0], "Client": ["TEST"], "Date": ["1/1/2023"], "Project": ["TestPrj"], "Amount": [0], "VAT": [0], "Description": ["First_Sample Invoice"]}
df = pd.DataFrame(data)

# List of authorized clients
clients = ["Client A", "Client B", "Client C"]

def new_invoice_form(client):
    invoice_no = len(df) + 1
    date = st.date_input("Date")
    project = st.text_input("Project")
    amount = st.number_input("Amount")
    vat = st.number_input("VAT")
    description = st.text_area("Description")
    create = st.button("Create")
    if create:
        df_new = pd.DataFrame({"Invoice No": [invoice_no], "Client": [client], "Date": [date], "Project": [project], "Amount": [amount], "VAT": [vat], "Description": [description]})
        df = df.append(df_new)
        st.success("Invoice created successfully!")
        # print the invoice in word based on the template
        # Code to generate the invoice based on the template goes here


client = st.selectbox("Select Client", clients)
if client:
  new_invoice_form(client)
st.write("Invoices Issued:", df)

#def main():
#    client = st.selectbox("Select Client", clients)
#    if client:
#        new_invoice_form(client)
#    st.write("Invoices Issued:", df)

#if __name__ == "__main__":
#    main()




