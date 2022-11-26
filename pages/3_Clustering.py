import streamlit as st


st.set_page_config(layout="centered")

st.title("K-means clustering")


st.markdown("<b>Кластеризация</b> (англ. <i>cluster analysis</i>) — задача группировки множества объектов на подмножества (<b>кластеры</b>) таким образом, чтобы объекты из одного кластера были более похожи друг на друга, чем на объекты из других кластеров по какому-либо критерию.", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2,6,2])

with col2:
    st.image('static/icons/clustering.png')


st.subheader("Алгоритм K-means (k-средних)")

st.markdown("Основная идея алгоритма k-means заключается в том, что данные произвольно разбиваются на кластеры, после чего итеративно перевычисляется центр масс для каждого кластера, полученного на предыдущем шаге, затем векторы разбиваются на кластеры вновь в соответствии с тем, какой из новых центров оказался ближе по выбранной метрике.")

st.markdown("Цель алгоритма заключается в разделении n наблюдений на k кластеров таким образом, чтобы каждое наблюдение принадлежало ровно одному кластеру, расположенному на наименьшем расстоянии от наблюдения.")

st.markdown("<b>Reference:</b>", unsafe_allow_html=True)

st.write('\t1. http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html')


