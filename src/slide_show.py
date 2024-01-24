import streamlit as st
import time
import datetime


def slide_show(page):
    # 前のページで設定したスライドショーの設定が無ければ、初期値を設定
    if "slide_enable_previous" not in st.session_state:
        st.session_state.slide_enable_previous = False

    if "slide_time_previous" not in st.session_state:
        st.session_state.slide_time_previous = 20

    # スライダーをサイドバーに表示し、スライドの表示時間を変更できるようにする
    st.sidebar.slider(
        label="スライドの表示時間（秒）",
        min_value=5,
        max_value=60,
        value=st.session_state.slide_time_previous,
        step=5,
        key="slide_time",
    )

    # チェックボックスをサイドバーに表示し、スライドショーの開始/停止を切り替えられるようにする
    st.sidebar.checkbox(
        label="スライドショーを開始する",
        value=st.session_state.slide_enable_previous,
        key="slide_enable",
    )

    # スライドショーが有効な場合は指定された時間だけページを表示し、進捗バーを更新
    if st.session_state.slide_enable:
        endtime = datetime.datetime.now() + datetime.timedelta(
            seconds=int(st.session_state.slide_time)
        )
        progress_bar = st.progress(
            0, f"スライドショー中... 0 / {st.session_state.slide_time} 秒"
        )
        while datetime.datetime.now() < endtime:
            time.sleep(1)
            progress_time = int(
                st.session_state.slide_time
                - (endtime - datetime.datetime.now()).total_seconds()
            )
            progress_value = progress_time / st.session_state.slide_time
            progress_bar.progress(
                progress_value,
                text=f"スライドショー中... {progress_time} / {st.session_state.slide_time} 秒",
            )

        # 設定時間が経過したら、指定されたページに切り替える
        # 次ページでスライドショーを継続するために、スライドショーの設定を保存
        st.session_state.slide_enable_previous = True
        st.session_state.slide_time_previous = st.session_state.slide_time
        st.switch_page(page)
    else:
        # スライドショーを止めて別ページに移動した場合に、スライドショーが勝手に再開しないようにする
        st.session_state.slide_enable_previous = False
