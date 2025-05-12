import streamlit as st
import re

def check_password(password):
    score = 0
    tips = []

    if len(password) >= 8:
        score += 1
    else:
        tips.append("🔢 Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        tips.append("🔠 Include at least one uppercase letter (A-Z).")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        tips.append("🔡 Include at least one lowercase letter (a-z).")

    if re.search(r"\d", password):
        score += 1
    else:
        tips.append("🔢 Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        tips.append("✨ Include at least one special character (!@#$%^&*).")

    return score, tips

def main():
    st.title("🔐 Password Strength Meter")
    st.markdown("🛡️ Check how secure your password is!")

    password = st.text_input("🔑 Enter your password:", type="password")

    if password:
        score, tips = check_password(password)

        if score == 5:
            st.success("✅ **Strong Password!** 🔥 You're all set!")
        elif score == 3 or score == 4:
            st.warning("⚠️ **Moderate Password** – Could be improved. 🧰")
        else:
            st.error("❌ **Weak Password!** ❗ Try the tips below to strengthen it:")

        if tips:
            st.markdown("💡 **Tips to Improve Your Password:**")
            for tip in tips:
                st.write("👉 " + tip)

main()


