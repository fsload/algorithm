for t in range(10):
    a, st = input().split()
    a = int(a)
    cnt = 0
    while True:
        st = st.replace('00', '')
        st = st.replace('11', '')
        st = st.replace('22', '')
        st = st.replace('33', '')
        st = st.replace('44', '')
        st = st.replace('55', '')
        st = st.replace('66', '')
        st = st.replace('77', '')
        st = st.replace('88', '')
        st = st.replace('99', '')
        cnt += 1
        if cnt >= a:
            break
 
    print('#' + str(t+1), st)
