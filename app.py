import streamlit as st
import pandas as pd
import plotly.express as px

# Define the initial team members data
initial_team_data = {
    'Name': ['John Doe', 'Jane Smith', 'Alex Johnson', 'Emily Brown', 'Michael Davis',
             'Sarah Wilson', 'Chris Thompson', 'Emma Martinez', 'David Lee', 'Olivia White'],
    'Contact Info': ['john@example.com', 'jane@example.com', 'alex@example.com', 'emily@example.com', 'michael@example.com',
                     'sarah@example.com', 'chris@example.com', 'emma@example.com', 'david@example.com', 'olivia@example.com'],
    'Role': ['Manager', 'Developer', 'Designer', 'Manager', 'Developer',
             'Designer', 'Manager', 'Developer', 'Designer', 'Manager'],
    'Team Leader': [True, False, False, True, False, False, True, False, False, False],
    'Performance': [90, 85, 75, 92, 88, 78, 87, 84, 79, 91]
}

# Create a DataFrame for team data
team_df = pd.DataFrame(initial_team_data)

# Define the initial sales data
initial_sales_data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [20000, 25000, 30000, 28000, 32000]
}

# Create a DataFrame for sales data
sales_df = pd.DataFrame(initial_sales_data)

# Function to add a new team member
def add_team_member(name, contact_info, role, is_team_leader, performance):
    global team_df
    # Check if the name or contact info already exists
    if name in team_df['Name'].values or contact_info in team_df['Contact Info'].values:
        st.error("A team member with the same name or contact info already exists.")
        return
    new_member = {'Name': name, 'Contact Info': contact_info, 'Role': role, 'Team Leader': is_team_leader, 'Performance': performance}
    team_df = team_df.append(new_member, ignore_index=True)

# Function to edit an existing team member
def edit_team_member(index, name, contact_info, role, is_team_leader, performance):
    global team_df
    # Check if the name or contact info already exists (excluding the current member)
    if (name in team_df['Name'].values or contact_info in team_df['Contact Info'].values) and \
            (team_df.iloc[index]['Name'] != name or team_df.iloc[index]['Contact Info'] != contact_info):
        st.error("A team member with the same name or contact info already exists.")
        return
    team_df.at[index, 'Name'] = name
    team_df.at[index, 'Contact Info'] = contact_info
    team_df.at[index, 'Role'] = role
    team_df.at[index, 'Team Leader'] = is_team_leader
    team_df.at[index, 'Performance'] = performance

# Function to delete a team member
def delete_team_member(index):
    global team_df
    team_df.drop(index, inplace=True)

# Function to display the sales performance page
def sales_performance_page():
    st.title('Sales Performance Tracker')

    # Display the sales data
    st.write('## Sales Data')
    st.write(sales_df)

    # Visualization: Sales Performance
    st.write('## Sales Performance')
    fig = px.line(sales_df, x='Month', y='Sales', title='Monthly Sales Performance')
    st.plotly_chart(fig)

# Streamlit app
def main():
    st.sidebar.title('Navigation')
    page = st.sidebar.radio('Go to', ['Team Management', 'Sales Performance'])

    if page == 'Team Management':
        st.title('Team Management')

        # Display the current team members
        st.write('## Current Team Members')
        st.write(team_df)

        # Sidebar for team management options
        st.sidebar.title('Team Management Options')
        selected_option = st.sidebar.selectbox('Select an Option', ['Add Team Member', 'Edit Team Member', 'Delete Team Member', 'Export Team Data'])

        if selected_option == 'Add Team Member':
            # Add a new team member
            st.sidebar.subheader('Add New Team Member')
            new_name = st.text_input('Name')
            new_contact_info = st.text_input('Contact Info')
            new_role = st.selectbox('Role', ['Manager', 'Developer', 'Designer'])
            is_team_leader = st.checkbox('Team Leader')
            performance = st.slider('Performance', min_value=0, max_value=100, value=50, step=1)
            if st.button('Add Team Member'):
                add_team_member(new_name, new_contact_info, new_role, is_team_leader, performance)
                st.success('New team member added successfully!')

        elif selected_option == 'Edit Team Member':
            # Edit an existing team member
            st.sidebar.subheader('Edit Team Member')
            member_index = st.sidebar.number_input('Index of the member to edit', min_value=0, max_value=len(team_df)-1, value=0)
            edited_name = st.text_input('Name', team_df.iloc[member_index]['Name'])
            edited_contact_info = st.text_input('Contact Info', team_df.iloc[member_index]['Contact Info'])
            edited_role = st.selectbox('Role', ['Manager', 'Developer', 'Designer'], index=['Manager', 'Developer', 'Designer'].index(team_df.iloc[member_index]['Role']))
            is_team_leader = st.checkbox('Team Leader', team_df.iloc[member_index]['Team Leader'])
            edited_performance = st.slider('Performance', min_value=0, max_value=100, value=team_df.iloc[member_index]['Performance'], step=1)
            if st.button('Edit Team Member'):
                edit_team_member(member_index, edited_name, edited_contact_info, edited_role, is_team_leader, edited_performance)
                st.success('Team member edited successfully!')

        elif selected_option == 'Delete Team Member':
            # Delete a team member
            st.sidebar.subheader('Delete Team Member')
            delete_index = st.sidebar.number_input('Index of the member to delete', min_value=0, max_value=len(team_df)-1, value=0)
            if st.button('Delete Team Member'):
                delete_team_member(delete_index)
                st.success('Team member deleted successfully!')

        elif selected_option == 'Export Team Data':
            # Export team data to CSV
            st.sidebar.subheader('Export Team Data')
            if st.button('Export Team Data'):
                team_df.to_csv('team_data.csv', index=False)
                st.success('Team data exported to team_data.csv!')

    elif page == 'Sales Performance':
        sales_performance_page()

if __name__ == '__main__':
    main()
