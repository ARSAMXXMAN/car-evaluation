import streamlit as st
import pickle
import numpy as np

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

language = st.radio("Select Language / انتخاب زبان", ["فارسی", "English", "Deutsch", "Français", "العربية", "Русский", "Schwiizerdütsch"])

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

elif language=="فارسی":
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

elif language == "Deutsch":
    st.title("Auto-Bewertungsmodell - Deutsch")
    st.write("Bitte geben Sie Ihre Fahrzeugdaten ein")

    dict_buy = {'Niedrig': 0, 'Mittel': 1, 'Hoch': 2, 'Sehr hoch': 3}
    buy = st.radio("Fahrzeugpreis", dict_buy.keys())

    dict_maint = {'Niedrig': 0, 'Mittel': 1, 'Hoch': 2, 'Sehr hoch': 3}
    maint = st.radio("Wartungskosten", dict_maint.keys())

    dict_doors = {'2': 0, '3': 1, '4': 2, 'Mehr als 5': 3}
    doors = st.radio("Anzahl der Türen", dict_doors.keys())

    dict_persons = {'2': 0, '4': 1, 'Mehr als 4': 2}
    persons = st.radio("Sitzplätze", dict_persons.keys())

    dict_lug_boot = {'Klein': 0, 'Mittel': 1, 'Groß': 2}
    lug_boot = st.radio("Kofferraumgröße", dict_lug_boot.keys())

    dict_safety = {'Niedrig': 0, 'Mittel': 1, 'Hoch': 2}
    safety = st.radio("Sicherheitsstufe", dict_safety.keys())

    dict_out = {0: 'Ungeeignet', 1: 'Akzeptabel', 2: 'Gut', 3: 'Sehr gut'}
    predict_button = "Vorhersagen"

elif language == "Français":
    st.title("Modèle d'évaluation de voiture - Français")
    st.write("Veuillez entrer les informations de votre voiture")

    dict_buy = {'Faible': 0, 'Moyen': 1, 'Élevé': 2, 'Très élevé': 3}
    buy = st.radio("Prix de la voiture", dict_buy.keys())

    dict_maint = {'Faible': 0, 'Moyen': 1, 'Élevé': 2, 'Très élevé': 3}
    maint = st.radio("Coût d'entretien", dict_maint.keys())

    dict_doors = {'2': 0, '3': 1, '4': 2, 'Plus de 5': 3}
    doors = st.radio("Nombre de portes", dict_doors.keys())

    dict_persons = {'2': 0, '4': 1, 'Plus de 4': 2}
    persons = st.radio("Capacité de sièges", dict_persons.keys())

    dict_lug_boot = {'Petit': 0, 'Moyen': 1, 'Grand': 2}
    lug_boot = st.radio("Taille du coffre", dict_lug_boot.keys())

    dict_safety = {'Faible': 0, 'Moyen': 1, 'Élevé': 2}
    safety = st.radio("Niveau de sécurité", dict_safety.keys())

    dict_out = {0: 'Inacceptable', 1: 'Acceptable', 2: 'Bon', 3: 'Très bon'}
    predict_button = "Prédire"

elif language == "العربية":
    st.title("نموذج تقييم السيارات - عربي")
    st.write("يرجى إدخال معلومات سيارتك")

    dict_buy = {'منخفض': 0, 'متوسط': 1, 'مرتفع': 2, 'مرتفع جداً': 3}
    buy = st.radio("سعر السيارة", dict_buy.keys())

    dict_maint = {'منخفض': 0, 'متوسط': 1, 'مرتفع': 2, 'مرتفع جداً': 3}
    maint = st.radio("تكلفة الصيانة", dict_maint.keys())

    dict_doors = {'2': 0, '3': 1, '4': 2, 'أكثر من 5': 3}
    doors = st.radio("عدد الأبواب", dict_doors.keys())

    dict_persons = {'2': 0, '4': 1, 'أكثر من 4': 2}
    persons = st.radio("عدد المقاعد", dict_persons.keys())

    dict_lug_boot = {'صغير': 0, 'متوسط': 1, 'كبير': 2}
    lug_boot = st.radio("حجم الصندوق الخلفي", dict_lug_boot.keys())

    dict_safety = {'منخفض': 0, 'متوسط': 1, 'مرتفع': 2}
    safety = st.radio("مستوى الأمان", dict_safety.keys())

    dict_out = {0: 'غير مناسب', 1: 'مقبول', 2: 'جيد', 3: 'جيد جداً'}
    predict_button = "تنبؤ"

elif language == "Русский":
    st.title("Модель оценки автомобиля - Русский")
    st.write("Пожалуйста, введите информацию о вашем автомобиле")

    dict_buy = {'Низкая': 0, 'Средняя': 1, 'Высокая': 2, 'Очень высокая': 3}
    buy = st.radio("Цена автомобиля", dict_buy.keys())

    dict_maint = {'Низкая': 0, 'Средняя': 1, 'Высокая': 2, 'Очень высокая': 3}
    maint = st.radio("Стоимость обслуживания", dict_maint.keys())

    dict_doors = {'2': 0, '3': 1, '4': 2, 'Более 5': 3}
    doors = st.radio("Количество дверей", dict_doors.keys())

    dict_persons = {'2': 0, '4': 1, 'Более 4': 2}
    persons = st.radio("Вместимость", dict_persons.keys())

    dict_lug_boot = {'Маленький': 0, 'Средний': 1, 'Большой': 2}
    lug_boot = st.radio("Размер багажника", dict_lug_boot.keys())

    dict_safety = {'Низкий': 0, 'Средний': 1, 'Высокий': 2}
    safety = st.radio("Уровень безопасности", dict_safety.keys())

    dict_out = {0: 'Неприемлемо', 1: 'Приемлемо', 2: 'Хорошо', 3: 'Очень хорошо'}
    predict_button = "Предсказать"

elif language == "Schwiizerdütsch":
    st.title("Auto-Bewärtigsmodell - Schwiizerdütsch")
    st.write("Bitte gib d'Informatione zu dim Auto ii")

    dict_buy = {'Wenig': 0, 'Mittel': 1, 'Viel': 2, 'Sehr viel': 3}
    buy = st.radio("Autopreis", dict_buy.keys())

    dict_maint = {'Wenig': 0, 'Mittel': 1, 'Viel': 2, 'Sehr viel': 3}
    maint = st.radio("Unterhaltskostä", dict_maint.keys())

    dict_doors = {'2': 0, '3': 1, '4': 2, 'Meh als 5': 3}
    doors = st.radio("Aazahl vo Türe", dict_doors.keys())

    dict_persons = {'2': 0, '4': 1, 'Meh als 4': 2}
    persons = st.radio("Sitzplätz", dict_persons.keys())

    dict_lug_boot = {'Chli': 0, 'Mittel': 1, 'Gross': 2}
    lug_boot = st.radio("Grössi vom Chofferraum", dict_lug_boot.keys())

    dict_safety = {'Niedrig': 0, 'Mittel': 1, 'Hoch': 2}
    safety = st.radio("Sicherheitslevel", dict_safety.keys())

    dict_out = {0: 'Unbrauchbar', 1: 'Akzeptabel', 2: 'Guet', 3: 'Sehr guet'}
    predict_button = "Vorhersage"

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
    st.write("Dini Auto isch", dict_out[int(predict)])