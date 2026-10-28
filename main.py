
import streamlit as st

st.title("Password Strength Checker")
st.write("Check your password strength and get suggestions.")

st.info("Use test passwords instead of real passwords.")

password = st.text_input(
    "Enter a test password:",
    type="password",
)

if password:

    length_check = False

    for char in password:
        if len(password) >= 8:
            length_check = True
            break

    uppercase_check = False

    for char in password:
        if char.isupper():
            uppercase_check = True
            break

    lowercase_check = False

    for char in password:
        if char.islower():
            lowercase_check = True
            break

    number_check = False

    for char in password:
        if char.isdigit():
            number_check = True
            break

    special_check = False

    for char in password:
        if not char.isalnum() and not char.isspace():
            special_check = True
            break

    checks = {
        "At least 8 characters": length_check,
        "At least one uppercase letter": uppercase_check,
        "At least one lowercase letter": lowercase_check,
        "At least one number": number_check,
        "At least one special character": special_check
    }

    score = 0
    for criterion, satisfied in checks.items():
        if satisfied:
            score = score + 1

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    st.subheader("Password Analysis")
    st.write("Password Strength Score:", str(score) + "/5")
    st.write("Password Strength:", strength)
    st.write("Strength Progress")
    st.progress(score / 5)
    st.subheader("Criteria Checklist")

    for criterion, satisfied in checks.items():
        if satisfied:
            st.success(criterion + ": Satisfied")
        else:
            st.error(criterion + ": Not satisfied")

    st.subheader("Suggestions")

    suggestions_found = False

    for criterion, satisfied in checks.items():
        if not satisfied:
            st.write("Improve your password: " + criterion)
            suggestions_found = True

    if not suggestions_found:
        st.success("All five criteria have been satisfied.")

else:
    st.write("Enter a password to begin the analysis.")
