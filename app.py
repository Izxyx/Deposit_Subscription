# Libraries
from pathlib import Path
import pickle
import streamlit as st
import gzip
import sklearn

# Paths
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir/'styles'/'main.css'


# Configuration
st.set_page_config(page_title='Prediction Bank Term Deposit Subscription',page_icon='chart_with_upwards_trend')


# Header
with open(css_file) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

# Main
def main():
    st.title('Prediction Bank Term Deposit Subscription')


    with st.expander("Project's Description"):
        st.write(''' 
            Understand if the client will subscribe a term deposit.
        ''')


def main2():
    st.header('Will client subscribe?...')

    if st.button('  PREDICT  '):

        result = model.predict([[
            age,
            job_x,
            marital_x,
            education_x,
            default_x,
            balance,
            housing_x,
            loan_x,
            contact_x,
            day,
            month_x,
            duration,
            campaign,
            pdays,
            previous,
            poutcome_x
            ]])

        def yes_no(x):
            if result[0] == 0:
                return 'No, try with another one.'
            else: 
                return 'Yes, you must call it.'
        
        response = yes_no(result)

        st.title('\n')
        st.title(response)
        st.title('\n')

if __name__ == '__main__':

    with gzip.open('random.pkl','rb') as f:
        model = pickle.load(f)
    
    main()

    st.header('Input client perfil:')
    
    age = st.slider('Age', 18,95)
        #st.write(age)

    job = option = st.selectbox('Job',
                    ['Blue-collar',
                    'Management',
                    'Technician',
                    'Administration',
                    'Services',
                    'Retired',
                    'Other'
                    ])
    # st.write(job)

    def job_to_int(x):
        if x == 'Blue-collar':
            return 0
        elif x == 'Management':
            return 1
        elif x == 'Technician':
            return 2
        elif x == 'Administration':
            return 3
        elif x == 'Services':
            return 4
        elif x == 'Retired':
            return 5
        else:
            return 6

    job_x =job_to_int(job)
    print(job_x)

    marital = option = st.selectbox('Marital',
                    ['Married',
                    'Single',
                    'Divorced'
                    ])
    #st.write(marital)

    def marital_to_int(x):
        if x == 'Married':
            return 0
        elif x == 'Single':
            return 1
        else:
            return 2

    marital_x =marital_to_int(marital)
    print(marital_x)

    education = option = st.selectbox('Education',
                    ['Primary',
                    'Secundary',
                    'Tertiary'
                    ])
     #st.write(education)

    def education_to_int(x):
        if x == 'Primary':
            return 0
        elif x == 'Secundary':
            return 1
        else:
            return 2

    education_x =education_to_int(education)
    print(education_x)

    default = option = st.selectbox('Default',
                    ['Yes',
                    'No'
                    ])
    #st.write(default)

    def default_to_int(x):
        if x == 'Yes':
            return 1
        else:
            return 0

    default_x =default_to_int(default)
    print(default_x)

    balance = st.slider('Balance', -3000,80000,step=100)
    #st.write(balance)

    housing = option = st.selectbox('Housing',
                    ['Yes',
                    'No'
                    ])
    #st.write(housing)

    def housing_to_int(x):
        if x == 'Yes':
            return 1
        else:
            return 0

    housing_x =housing_to_int(housing)
    print(housing_x)

    loan = option = st.selectbox('Loan',
                    ['Yes',
                    'No'
                    ])
    #st.write(loan)

    def loan_to_int(x):
        if x == 'Yes':
            return 1
        else:
            return 0

    loan_x =loan_to_int(loan)
    print(loan_x)
    
    contact = option = st.selectbox('Contact',
                    ['Cellular',
                    'Unknown',
                    'Telephone'
                    ])
    st.write(contact)

    def contact_to_int(x):
        if x == 'Cellular':
            return 0
        elif x == 'Unknown':
            return 1
        else:
            return 2

    contact_x =contact_to_int(contact)
    print(contact_x)

    day = st.slider('Day', 1,31)
    # st.write(day)
    
    month= option = st.selectbox('Month',
                    ['January',
                    'February',
                    'March',
                    'April',
                    'May',
                    'June',
                    'July',
                    'August',
                    'September',
                    'Octuber',
                    'November',
                    'December'
                    ])
    # st.write(month)

    def month_to_int(x):
        if x == 'January':
            return 0
        elif x == 'February':
            return 1
        elif x == 'March':
            return 2
        elif x == 'April':
            return 3
        elif x == 'May':
            return 4
        elif x == 'June':
            return 5
        elif x == 'July':
            return 6
        elif x == 'August':
            return 7
        elif x == 'September':
            return 8
        elif x == 'Octuber':
            return 9
        elif x == 'November':
            return 9
        else:
            return 11

    month_x =month_to_int(month)
    print(month_x)
    
    duration = st.slider('Duration (Seconds)', 0,4000,step=10)
    # st.write(duration)
    
    campaign = st.slider('Campaign', 1,32)
    # st.write(campaign)
    
    pdays = st.slider('Pdays', 0,900)
    # st.write(pdays)
    
    previous = st.slider('Previous', 0,20)
    # st.write(previous)
    
    poutcome= option = st.selectbox('Poutcome',
                    ['Unknown',
                    'Succes',
                    'Failure',
                    'Other'
                    ])
    # st.write(poutcome)

    def poutcome_to_int(x):
        if x == 'Unknown':
            return 0
        elif x == 'Succes':
            return 1
        elif x == 'Failure':
            return 2
        else:
            return 3

    poutcome_x =poutcome_to_int(poutcome)
    print(poutcome_x)

    main2()

    