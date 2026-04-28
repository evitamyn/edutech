import pandas as pd
import numpy as np
import streamlit as st
import joblib

model = joblib.load('best_model.pkl')
preprocess = joblib.load('preprocessor.pkl')

st.set_page_config(page_title="Student Performance Predictor", layout='wide')

st.markdown("""
# 🏫 Jaya-Jaya Institution
## Student Performance Prediction System
""")
st.markdown("---")

st.markdown("## 🪪 Informasi Mahasiswa")

col1, col2, col3, col4 = st.columns(4)
with col1:
    
    Age_at_enrollment = st.number_input('Age at Enrollment', 
                                        min_value=17, max_value=70)
with col2:
    gender_map = {0: 'Female', 1: 'Male'}
    Gender = st.selectbox('Gender',
                          options=list(gender_map.keys()),
                          format_func=lambda x: gender_map[x])
with col3:
    marital_map = {1: 'Single',
                   2: 'Married',
                   3: 'Widower',
                   4: 'Divorced',
                   5: 'Facto Union',
                   6: 'Legally Separated'}
    Marital_status = st.selectbox("Marital Status",
                                   options=list(marital_map.keys()),
                                   format_func=lambda x: marital_map[x])
with col4:
    attendance_map = {0: 'Evening', 1: 'Daytime'}
    Daytime_evening_attendance = st.selectbox("Attendance",
                                              options=list(attendance_map.keys()),
                                              format_func=lambda x: attendance_map[x])
st.markdown("---")
st.markdown('## 💰 Finansial')
col5, col6, col7 = st.columns(3)
with col5:
    scholar_map = {0: 'No Scholarship',
                  1: 'Scholarship'}
    Scholarship_holder = st.selectbox("Scholarship Holder",
                                     options=list(scholar_map.keys()),
                                     format_func=lambda x: scholar_map[x])
with col6:  
    tuition_map = {0: 'No Update',
                   1: 'Update'}  
    Tuition_fees_up_to_date = st.selectbox("Tuition Fees",
                                           options=list(tuition_map.keys()),
                                           format_func=lambda x: tuition_map[x])
with col7:    
    debtor_map = {0: 'No',
                  1: 'Yes'}
    Debtor = st.selectbox("Debtor", 
                          options=list(debtor_map.keys()),
                          format_func=lambda x: debtor_map[x])
st.markdown("---")
st.markdown("## 🎓 Akademik")
st.markdown("### Semester 1")
col8, col9 = st.columns(2)
with col8:
    Curricular_units_1st_sem_approved = st.number_input("1st Sem Approved", min_value=0, max_value=26, value=0)
with col9:
    Curricular_units_1st_sem_enrolled = st.number_input("1st Sem Enrolled", min_value=0, max_value=26, value=0)

col10, col11 = st.columns(2)
with col10:
    Curricular_units_1st_sem_evaluations = st.number_input("1st Sem Evaluations", min_value=0, max_value=45, value=0)
with col11:
    Curricular_units_1st_sem_grade = st.number_input("1st Sem Grade", min_value=0, max_value=18.875, value=0)

st.markdown("### Semester 2")
col12, col13 = st.columns(2)
with col12:
    Curricular_units_2nd_sem_approved = st.number_input("2nd Sem Approved", min_value=0, max_value=20, value=0)
with col13:
    Curricular_units_2nd_sem_enrolled = st.number_input("2nd Sem Enrolled", min_value=0, max_value=23, value=0)

col14, col15 = st.columns(2)
with col14:
    Curricular_units_2nd_sem_evaluations = st.number_input("2nd Sem Evaluations", min_value=0, max_value=33, value=0)
with col15:
    Curricular_units_2nd_sem_grade = st.number_input("2nd Sem Grade", min_value=0, max_value=18.571429, value=0)

input_data = pd.DataFrame([{
    'Age_at_enrollment': Age_at_enrollment,
    'Gender': Gender,
    'Marital_status': Marital_status,
    'Daytime_evening_attendance': Daytime_evening_attendance,

    'Tuition_fees_up_to_date': Tuition_fees_up_to_date,
    'Debtor': Debtor,
    'Scholarship_holder': Scholarship_holder,

    'Curricular_units_1st_sem_approved': Curricular_units_1st_sem_approved,
    'Curricular_units_1st_sem_grade': Curricular_units_1st_sem_grade,
    'Curricular_units_1st_sem_evaluations': Curricular_units_1st_sem_evaluations,
    'Curricular_units_1st_sem_enrolled': Curricular_units_1st_sem_enrolled,

    'Curricular_units_2nd_sem_approved': Curricular_units_2nd_sem_approved,
    'Curricular_units_2nd_sem_grade': Curricular_units_2nd_sem_grade,
    'Curricular_units_2nd_sem_evaluations': Curricular_units_2nd_sem_evaluations,
    'Curricular_units_2nd_sem_enrolled': Curricular_units_2nd_sem_enrolled,
}])

for col in preprocess.feature_names_in_:
    if col not in input_data.columns:
        input_data[col] = 0

input_data = input_data[preprocess.feature_names_in_]

if st.button('Predict'): 
    X_input = preprocess.transform(input_data)
    prediction = model.predict(X_input)[0]

    label_map = {0: '🔴 Dropout',
                 1: '🟡 Enrolled',
                 2: '🟢 Graduate'}
    
    result = label_map[prediction]
    st.success(f'🎯 Prediksi Mahasiswa adalah: **{result}**')
