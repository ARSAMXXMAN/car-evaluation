import streamlit as st
import pickle
import numpy as np
with open('model_car.pkl', 'rb') as f:
    loaded_model = pickle.load(f)
st.title("مدل ارزیابی ماشین ها")
st.write("لطفا اطلاعات ماشین خود را وارد کنید")

dict_buy={'low':0,'med':1,'high':2,'vhigh':3}
buy=st.radio("میزان قیمت ماشین",dict_buy.keys())

dict_maint={'low':0,'med':1,'high':2,'vhigh':3}
maint=st.radio("میزان قیمت نگهداری ماشین",dict_maint.keys())

dict_doors={'2':0,'3':1,'4':2,'more5':3}
doors=st.radio("تعداد در های ماشین",dict_doors.keys())

dict_persons={'2':0,'4':1,'more':2}
persons=st.radio("ظرفیت ماشین",dict_persons.keys())

dict_lug_boot={'small':0,'med':1,'big':2}
lug_boot=st.radio("سایز صندوق عقب ماشین",dict_lug_boot.keys())

dict_safety={'low':0,'med':1,'high':2}
safety=st.radio("امنیت  ماشین",dict_safety.keys())


if st.button("پیش بینی کن"):
    data=np.array ([dict_buy[buy],dict_maint[maint],dict_doors[doors],dict_persons[persons],dict_lug_boot[lug_boot],dict_safety[safety]]).reshape(1, -1)
    predict=loaded_model.predict(data)
    dict_out={0:'نامناسب',1:'مناسب',2:'خوب',3:'خیلی خوب'}
    st.write("ماشین شما",dict_out[int(predict)],"است")