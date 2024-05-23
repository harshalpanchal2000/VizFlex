import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# App title and description
st.title('VizFlex: Your Data Visualization Tool')
st.write('Upload your CSV file and create insightful visualizations with ease.')

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    
    # Display the uploaded data
    if st.checkbox('Show raw data'):
        st.subheader('Raw Data')
        st.write(data)
    
    # Check if the dataset contains numerical columns
    numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
    
    if len(numerical_columns) > 0:
        # Sidebar options for visualizations
        st.sidebar.header('Visualization Settings')
        plot_type = st.sidebar.selectbox('Select plot type', ['Scatterplot', 'Histogram'])
        
        st.sidebar.markdown('---')
        x_axis = st.sidebar.selectbox('Select X-axis', numerical_columns)
        y_axis = st.sidebar.selectbox('Select Y-axis', numerical_columns)
        
        # Create plots based on user selection
        st.subheader('Visualization')
        if plot_type == 'Scatterplot':
            fig, ax = plt.subplots()
            sns.scatterplot(x=data[x_axis], y=data[y_axis], ax=ax)
            st.pyplot(fig)
        elif plot_type == 'Histogram':
            fig, ax = plt.subplots()
            sns.histplot(data[x_axis], kde=True, ax=ax)
            st.pyplot(fig)
    else:
        st.write("The uploaded dataset does not contain any numerical columns. Please upload a dataset with numerical data.")
else:
    st.write("Please upload a CSV file to get started.")
