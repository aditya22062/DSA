
def main():
    s=input()
    st=[]
    for i in s:
        if i==')' :
            if st[-1]=='(':
                print("true")
                return
            else:
                while st[-1]!='(':
                    st.pop()
                st.pop()
        else:
            st.append(i)

    print("false")

if __name__ == "__main__":
    main()
