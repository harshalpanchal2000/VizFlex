import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(
    page_title="VizFlex",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# App title and description
st.title('VizFlex: Your Ultimate Data Visualization Tool')
st.subheader('Effortlessly visualize your data with intuitive and interactive plots.')

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    
    # Display the uploaded data
    if st.checkbox('Show raw data'):
        st.subheader('Raw Data')
        st.write(data)
    
    # Check if the dataset contains numerical columns
    numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
    categorical_columns = data.select_dtypes(include=['object']).columns.tolist()

    if len(numerical_columns) > 0:
        # Sidebar options for visualizations
        st.sidebar.header('Visualization Settings')
        plot_type = st.sidebar.selectbox('Select plot type', ['Scatterplot', 'Histogram', 'Line Plot', 'Box Plot', 'Bar Plot'])
        
        st.sidebar.markdown('---')
        x_axis = st.sidebar.selectbox('Select X-axis', numerical_columns + categorical_columns if plot_type != 'Box Plot' else categorical_columns)
        y_axis = st.sidebar.selectbox('Select Y-axis', numerical_columns)
        
        # Button to generate plot
        if st.sidebar.button('Show Visualization'):
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
            elif plot_type == 'Line Plot':
                fig, ax = plt.subplots()
                sns.lineplot(x=data[x_axis], y=data[y_axis], ax=ax)
                st.pyplot(fig)
            elif plot_type == 'Box Plot':
                fig, ax = plt.subplots()
                sns.boxplot(x=data[x_axis] if x_axis in categorical_columns else None, y=data[y_axis], ax=ax)
                st.pyplot(fig)
            elif plot_type == 'Bar Plot':
                fig, ax = plt.subplots()
                sns.barplot(x=data[x_axis], y=data[y_axis], ax=ax)
                st.pyplot(fig)
    else:
        st.write("The uploaded dataset does not contain any numerical columns. Please upload a dataset with numerical data.")
else:
    st.write("Please upload a CSV file to get started.")

# Footer
st.markdown(
    """
    <div style='text-align: center; padding: 10px 0;'>
        <p>Built by <a href="https://www.linkedin.com/in/harshal-panchal/" target="_blank">Harshal Panchal</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
