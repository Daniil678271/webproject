import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import os
import webbrowser

# Настройки страницы
st.set_page_config(page_title="Калькулятор затрат на Premium Cars", layout="wide", page_icon="  ")

car_images = {
    "Lamborghini Revuelto": r"D:\1\orig-removebg-preview.png",
    "Lamborghini Huracan Tecnica": r"D:\1\unnamed-removebg-preview.png",
    "Lamborghini Urus": r"D:\1\lamborghini-urus-yellow-e1569794314548-removebg-preview.png",
    "Lamborghini Huracan Sterrato": r"D:\1\lamborghini-huracan-sterrato-6-removebg-preview.png",
    "Mclaren Artura": r"D:\1\2023_McLaren_Artura_4-removebg-preview.png",
    "Mclaren P1": r"D:\1\Vclarenp1-removebg-preview.png",
    "Mclaren 720s": r"D:\1\Макларен-720С-черный-цвет-removebg-preview.png",
    "Ferrari SF90": r"D:\1\ferrari_sf90__554581082f-removebg-preview.png",
    "Ferrari Daytona": r"D:\1\Ferrari_Daytona_SP3_front_side_at_CF_2022-removebg-preview.png",
    "Ferrari Roma": r"D:\1\ferrari_roma_1024955-removebg-preview.png",
    "Ferrari Purosange": r"D:\1\Purosange-removebg-preview.png",
    "Ferrari 812 Superfast": r"D:\1\uljvo0qtiw5ljuwyk1sg-removebg-preview.png",
    "Bentley Continental GT": r"D:\1\Bentley_Continental_GT__4th_gen.__IMG_0556-removebg-preview.png",
    "Aston Martin Vantage": r"D:\1\AM606_studio-removebg-preview.png",
    "Aston Martin DB 12": r"D:\1\db12-removebg-preview.png",
    "BMW M3CS": r"D:\1\m3cs-removebg-preview.png",
    "Rolls-Royce Spectre": r"D:\1\Spectre-removebg-preview.png",
    "Rolls-Royce Black Badge Wraith": r"D:\1\rolls-royce-black-badge-wraith-by-spofec-removebg-preview.png"
}
youtube_reviews = {"Lamborghini Revuelto": ["https://youtu.be/KBGJn0ogQuA?si=BWh4ACO-zyzyUW1H"],
                    "Lamborghini Huracan Tecnica": ["https://youtu.be/FjiF3wG5Oag?si=Mod_UeDY5U5xTaPt"],
                    "Lamborghini Urus": ["https://youtu.be/iG380_ycdgE?si=l7hLpobgImHg0knB"],
                    "Lamborghini Huracan Sterrato": ["https://youtube.com/shorts/a78E3tOFn68?si=oYUDRfqqRct2YlbN"],
                    "Mclaren Artura": ["https://youtu.be/8W1pZtujhwo?si=ZsGccQXzIePTH-_A"],
                    "Mclaren P1": ["https://youtu.be/q9HwQHHaeIM?si=vzD-PuLQUfFBo-kL"],
                    "Mclaren 720s": ["https://youtu.be/DnRUv-e09uU?si=QG2PaMaH8RCo1H93"],
                    "Ferrari SF90": ["https://youtu.be/g3_BkVJ_v9U?si=CiceKModKRjMe1Hh"],
                    "Ferrari Daytona": ["https://youtube.com/shorts/lzNtfBlQtA8?si=GMm3W9yQNzLm5jCb"],
                    "Ferrari Roma": ["https://youtu.be/JMdLlvpLw60?si=VO2k2fyhUrtCSufv"],
                    "Ferrari Purosange": ["https://youtu.be/hOKuqfIHin0?si=OrKbbowQ-8uRkbzX"],
                    "Ferrari 812 Superfast": ["https://youtube.com/shorts/tSbmRAgMr-8?si=pd41IGiJ06Krq9E-"],
                    "Bentley Continental GT": ["https://youtu.be/c5uiJCDCEOk?si=as0RcX7yzvSmboLs"],
                    "Aston Martin Vantage": ["https://youtu.be/DaqeBaK0-kk?si=NRSjb_fPZK1R1Hkw"],
                    "Aston Martin DB 12": ["https://youtu.be/rzK-VYf3VM8?si=QsQ2Ny0b9Cn8Gm8_"],
                    "BMW M3CS": ["https://youtu.be/Vc4cHeycVhg?si=Mf1W632yj6bkuNlh"],
                    "Rolls-Royce Spectre": ["https://youtu.be/eYiPRSzaJkg?si=P7VX1XukhT37m8pF"],
                    "Rolls-Royce Black Badge Wraith": ["https://youtu.be/-V3AgInFu2U?si=KrHB65FPMKUl7a51"]
                   }

car_model = st.sidebar.selectbox("Модель автомобиля", ["Lamborghini Revuelto", "Lamborghini Huracan Tecnica", "Lamborghini Urus", "Lamborghini Huracan Sterrato", "Mclaren Artura", "Mclaren P1", "Mclaren 720s",
"Ferrari SF90", "Ferrari Daytona", "Ferrari Roma", "Ferrari Purosange", "Ferrari 812 Superfast", "Bentley Continental GT", "Aston Martin Vantage", "Aston Martin DB 12", "BMW M3CS", "Rolls-Royce Spectre", "Rolls-Royce Black Badge Wraith"], index=0)
# Стили
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #000000, #3a3f44, #ffffff);
        min-height: 100vh;
        background-attachment: fixed;
        color: white;
    }
    label, .stTextInput label, .stPassword label {
        color: white !important;
    }
    input[type="text"], input[type="text"], input[type="password"], input[type="number"] {
        background-color: rgba(0,0,0,0.4);
        color: white !important;
        border: 1px solid #aaa;
        border-radius: 8px;
        padding: 8px;
    }
    input::placeholder {
        color: #cccccc;
    }
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e1e1e, #3c3c3c, #5a5a5a);
        color: white;
    }
    section[data-testid="stSidebar"] * {
        color: white !important;
    }
    .stButton>button {
        background: linear-gradient(90deg, #ff4b4b, #ff6f61);
        color: white;
        border-radius: 12px;
        padding: 12px 24px;
        font-weight: bold;
        border: none;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.5);
    }
    h1, h2, h3 {
        color: #ffffff;
        font-family: 'Arial Black', sans-serif;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    }
    </style>
    """, unsafe_allow_html=True)

# Инициализация session_state
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['Модель', 'Расстояние (км)', 'Расход (л/100км)', 'Цена топлива (грн/л)', 'Общие затраты (грн)'])
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

def calculate_cost(distance, fuel_consumption, fuel_price):
    try:
        total_fuel = (distance / 100) * fuel_consumption
        total_cost = total_fuel * fuel_price
        return total_fuel, total_cost
    except Exception as e:
        st.error(f"Ошибка при расчете: {e}")
        return None, None
    
def load_car_image(image_path):
    try:
        if os.path.exists(image_path):
            return Image.open(image_path)
        else:
            st.warning(f"Изображение не найдено по пути: {image_path}. Убедитесь, что файл находится в папке 'images'.")
            return None
    except Exception as e:
        st.error(f"Ошибка загрузки изображение: {e}")
        return None

def login_page():
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.title("🔐Вход в систему")
    st.markdown("Пожайлуста, введите учетные данные для доступа к сайту.")

    username = st.text_input("Имя пользователя", placeholder="Введите имя пользователя")
    password = st.text_input("Пароль", type="password", placeholder="Введите пароль")

    if st.button("Войти"):
        if username == "admin" and password == "heuytnij77":
            st.session_state.authenticated = True 
            st.success("Успешный вход! Перенапраление...")
            st.rerun()
        else:
            st.error("Неверное имя пользователя или пароль.")

    st.markdown("</div>", unsafe_allow_html=True)

def main_page():
    st.markdown("<div class='main'>", unsafe_allow_html=True)

# Заголовок
st.title("   Калькулятор затрат на Premium Cars")
st.markdown("Рассчитайте затраты на топливо для вашего суперкара в гривнах и наслаждайтесь стильной визуализацией!")

# Сайдбар
st.sidebar.header("🔧 Ввод данных")
distance = st.sidebar.slider("Расстояние (км)", min_value=0.0, max_value=1000.0, value=100.0, step=10.0)
fuel_consumption = st.sidebar.number_input("Расход топлива (л/100км)", min_value=0.0, value=15.0, step=0.5)
fuel_price = st.sidebar.number_input("Цена топлива (грн/л)", min_value=0.0, value=50.0, step=1.0)

if st.sidebar.button("Рассчитать 🚀"):
    total_fuel, total_cost = calculate_cost(distance, fuel_consumption, fuel_price)
    new_data = pd.DataFrame({
        'Модель': [car_model],
        'Расстояние (км)': [distance],
        'Расход (л/100км)': [fuel_consumption],
        'Цена топлива (грн/л)': [fuel_price],
        'Общие затраты (грн)': [total_cost]    
    })
    st.session_state.data = pd.concat([st.session_state.data, new_data], ignore_index=True)
    st.success(f"🏁 Расчет выполнен! Расход топлива: {total_fuel:.2f} л, Затраты: {total_cost:.2f} грн")
    st.sidebar.header("Посмотреть обзор на платформе Youtube")
    selected_review = st.sidebar.selectbox("Выберите обзор", youtube_reviews[car_model], index=0)
    if st.sidebar.button("Перейти на Youtube"):
        try:
            webbrowser.open_new_tab(selected_review)
            st.info(f"Открывается обзор для {car_model}...")
        except Exception as e:
            st.error(f"Ошибка открытия ссылки {e}")
# Колонки
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📈 Результаты расчетов")
    if not st.session_state.data.empty:
        styled_df = st.session_state.data.style.format({
            'Расстояние (км)': '{:.1f}',
            'Расход (л/100км)': '{:.1f}',
            'Цена топлива (грн/л)': '{:.1f}',
            'Общие затраты (грн)': '{:.2f}'
        }).set_properties(**{
            'background-color': '#3a3f44',
            'color': 'white',
            'border-color': '#ff4b4b',
            'border-radius': '8px',
            'padding': '10px'
        })
        st.dataframe(styled_df, use_container_width=True)

        if 'Общие затраты (грн)' in st.session_state.data.columns:
            st.subheader("📊 График затрат")
            fig_bar = go.Figure(data=[
                go.Bar(
                    x=st.session_state.data['Модель'],
                    y=st.session_state.data['Общие затраты (грн)'],
                    marker_color=['#ff4b4b', '#ff6f61', '#ff8a80'],
                    marker_line_color=['#d32f2f', '#e53935', '#ef5350'],
                    marker_line_width=2
                )
            ])
            fig_bar.update_layout(
                title="Затраты на топливо по моделям",
                xaxis_title="Модель",
                yaxis_title="Затраты (грн)",
                template="plotly_dark",
                title_font_color='#ff4b4b',
                font_color="white",
                showlegend=False,
                yaxis=dict(range=[0, st.session_state.data['Общие затраты (грн)'].max() * 1.2]),
                transition={"duration": 200, "easing": "cubic-in-out"}
            )
            st.plotly_chart(fig_bar, use_container_width=True)

            st.subheader("🔄 Анимированная зависимость затрат")
            fig_scatter = px.scatter(
                st.session_state.data,
                x='Расстояние (км)',
                y='Общие затраты (грн)',
                color='Модель',
                size='Расход (л/100км)',
                title="Зависимость затрат от расстояния",
                animation_frame='Модель',
                range_y=[0, st.session_state.data['Общие затраты (грн)'].max() * 1.2],
                template="plotly_dark"
            )
            fig_scatter.update_layout(title_font_color="#ff4b4b", font_color="white")
            st.plotly_chart(fig_scatter, use_container_width=True)
        else:
            st.warning("Нет данных для графика. Сначала нажмите 'Рассчитать 🚀'")
    else:
        st.warning("Нет данных для отображения. Сначала добавьте расчет.")

with col2:
    st.subheader(" Ваш суперкар")
    image_path = car_images.get(car_model)
    car_image = load_car_image(image_path)
    if car_image:
        st.image(car_image, caption=f"{car_model}", use_container_width=True)
    else:
        st.warning(f"Изображение для {car_model} не найдено.")

st.markdown("""
### Как пользоваться:
1. Выберите модель Premium Car и введите данные в боковой панели.
2. Нажмите **Рассчитать** для сохранения результата.
3. Просмотрите таблицу и графики для анализа затрат в гривнах.
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

if not st.session_state.authenticated:
    login_page()
else:
    main_page()
