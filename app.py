import streamlit as st
import pandas as pd

# Define the initial team members data
initial_data = {
    'Name': ['John Doe', 'Jane Smith', 'Alex Johnson', 'Emily Brown', 'Michael Davis',
             'Sarah Wilson', 'Chris Thompson', 'Emma Martinez', 'David Lee', 'Olivia White'],
    'Contact Info': ['john@example.com', 'jane@example.com', 'alex@example.com', 'emily@example.com', 'michael@example.com',
                     'sarah@example.com', 'chris@example.com', 'emma@example.com', 'david@example.com', 'olivia@example.com'],
    'Role': ['Manager', 'Developer', 'Designer', 'Manager', 'Developer',
             'Designer', 'Manager', 'Developer', 'Designer', 'Manager']
}

# Create a DataFrame from the initial data
team_df = pd.DataFrame(initial_data)

# Function to add a new team member
def add_team_member(name, contact_info, role):
    global team_df
    new_member = {'Name': name, 'Contact Info': contact_info, 'Role': role}
    team_df = team_df.append(new_member, ignore_index=True)

# Function to edit an existing team member
def edit_team_member(index, name, contact_info, role):
    global team_df
    team_df.at[index, 'Name'] = name
    team_df.at[index, 'Contact Info'] = contact_info
    team_df.at[index, 'Role'] = role

# Streamlit app
def main():
    st.title('Team Manager App')

    # Display the current team members
    st.write('## Current Team Members')
    st.write(team_df)

    # Add a new team member
    st.write('## Add New Team Member')
    new_name = st.text_input('Name')
    new_contact_info = st.text_input('Contact Info')
    new_role = st.selectbox('Role', ['Manager', 'Developer', 'Designer'])
    if st.button('Add Team Member'):
        add_team_member(new_name, new_contact_info, new_role)
        st.success('New team member added successfully!')

    # Edit an existing team member
    st.write('## Edit Team Member')
    member_index = st.number_input('Index of the member to edit', min_value=0, max_value=len(team_df)-1, value=0)
    edited_name = st.text_input('Name', team_df.iloc[member_index]['Name'])
    edited_contact_info = st.text_input('Contact Info', team_df.iloc[member_index]['Contact Info'])
    edited_role = st.selectbox('Role', ['Manager', 'Developer', 'Designer'], index=['Manager', 'Developer', 'Designer'].index(team_df.iloc[member_index]['Role']))
    if st.button('Edit Team Member'):
        edit_team_member(member_index, edited_name, edited_contact_info, edited_role)
        st.success('Team member edited successfully!')

if __name__ == '__main__':
    main()
