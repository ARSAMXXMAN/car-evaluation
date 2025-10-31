import streamlit as st
import pickle
import numpy as np

with open('model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)
st.title("مدل ارزیابی ماشین ها نسخه ی فارسی")
st.write("لطفا اطلاعات ماشین خود را وارد کنید")

dict_buy={'کم':0,'متوسط':1,'زیاد':2,'خیلی زیاد':3}
buy=st.radio("میزان قیمت ماشین",dict_buy.keys())

dict_maint={'کم':0,'متوسط':1,'زیاد':2,'خیلی زیاد':3}
maint=st.radio("میزان قیمت نگهداری ماشین",dict_maint.keys())

dict_doors={'۲':0,'۳':1,'۴':2,'بیشتر از ۵':3}
doors=st.radio("تعداد در های ماشین",dict_doors.keys())

dict_persons={'۲':0,'۴':1,'بیشتراز۴':2}
persons=st.radio("ظرفیت ماشین",dict_persons.keys())

dict_lug_boot={'کوچک':0,'متوسط':1,'بزرگ':2}
lug_boot=st.radio("سایز صندوق عقب ماشین",dict_lug_boot.keys())

dict_safety={'کم':0,'متوسط':1,'زیاد':2}
safety=st.radio("امنیت  ماشین",dict_safety.keys())


if st.button("پیش بینی کن"):
    data=np.array ([dict_buy[buy],dict_maint[maint],dict_doors[doors],dict_persons[persons],dict_lug_boot[lug_boot],dict_safety[safety]]).reshape(1, -1)
    predict=loaded_model.predict(data)
    dict_out={0:'نامناسب',1:'مناسب',2:'خوب',3:'خیلی خوب'}
    st.write("ماشین شما",dict_out[int(predict)],"است")