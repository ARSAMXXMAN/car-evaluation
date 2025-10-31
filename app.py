import streamlit as st
import pickle
import numpy as np

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Language switcher
language = st.radio("Select Language / انتخاب زبان", ["English", "فارسی"])

# Dictionaries
if language == "English":
    st.title("Car Evaluation Model - English Version")
    st.write("Please enter your car information")

    dict_buy = {'Low': 0, 'Medium': 1, 'High': 2, 'Very High': 3}
    buy = st.radio("Car Price Level", dict_buy.keys())

    dict_maint = {'Low': 0, 'Medium': 1, 'High': 2, 'Very High': 3}
    maint = st.radio("Maintenance Cost Level", dict_maint.keys())

    dict_doors = {'2': 0, '3': 1, '4': 2, 'More than 5': 3}
    doors = st.radio("Number of Doors", dict_doors.keys())

    dict_persons = {'2': 0, '4': 1, 'More than 4': 2}
    persons = st.radio("Seating Capacity", dict_persons.keys())

    dict_lug_boot = {'Small': 0, 'Medium': 1, 'Large': 2}
    lug_boot = st.radio("Trunk Size", dict_lug_boot.keys())

    dict_safety = {'Low': 0, 'Medium': 1, 'High': 2}
    safety = st.radio("Safety Level", dict_safety.keys())

    dict_out = {0: 'Unacceptable', 1: 'Acceptable', 2: 'Good', 3: 'Very Good'}
    predict_button = "Predict"

else:
    st.title("مدل ارزیابی ماشین‌ها - نسخه فارسی")
    st.write("لطفاً اطلاعات ماشین خود را وارد کنید")

    dict_buy = {'کم': 0, 'متوسط': 1, 'زیاد': 2, 'خیلی زیاد': 3}
    buy = st.radio("میزان قیمت ماشین", dict_buy.keys())

    dict_maint = {'کم': 0, 'متوسط': 1, 'زیاد': 2, 'خیلی زیاد': 3}
    maint = st.radio("هزینه نگهداری ماشین", dict_maint.keys())

    dict_doors = {'۲': 0, '۳': 1, '۴': 2, 'بیشتر از ۵': 3}
    doors = st.radio("تعداد درهای ماشین", dict_doors.keys())

    dict_persons = {'۲': 0, '۴': 1, 'بیشتراز۴': 2}
    persons = st.radio("ظرفیت ماشین", dict_persons.keys())

    dict_lug_boot = {'کوچک': 0, 'متوسط': 1, 'بزرگ': 2}
    lug_boot = st.radio("اندازه صندوق عقب", dict_lug_boot.keys())

    dict_safety = {'کم': 0, 'متوسط': 1, 'زیاد': 2}
    safety = st.radio("سطح ایمنی ماشین", dict_safety.keys())

    dict_out = {0: 'نامناسب', 1: 'مناسب', 2: 'خوب', 3: 'خیلی خوب'}
    predict_button = "پیش‌بینی کن"

# Prediction
if st.button(predict_button):
    data = np.array([
        dict_buy[buy],
        dict_maint[maint],
        dict_doors[doors],
        dict_persons[persons],
        dict_lug_boot[lug_boot],
        dict_safety[safety]
    ]).reshape(1, -1)

    predict = model.predict(data)
    st.write(dict_out[int(predict)])