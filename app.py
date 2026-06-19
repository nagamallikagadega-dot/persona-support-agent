import streamlit as st
import os
from src.classifier import classify_customer_persona
from src.generator import generate_response
from src.escalator import check_escalation

st.set_page_config(page_title="AI Customer Support Agent", page_icon="🤖")
st.title("🤖 Persona-Adaptive Customer Support Agent")
st.markdown("---")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    persona_result = classify_customer_persona(prompt)
    persona = persona_result.get("persona", "Frustrated User")
    
    escalation = check_escalation(prompt, persona)
    
    if escalation["should_escalate"]:
        response = f"🚨 **Escalating to Human Agent**\n\nI understand this is urgent. A human agent will assist you shortly.\n\n**Reason:** {escalation['reason']}"
    else:
        response = generate_response(prompt, persona)
    
    with st.chat_message("assistant"):
        st.markdown(f"**Detected Persona:** {persona}\n\n{response}")
    
    st.session_state.messages.append({"role": "assistant", "content": f"**Detected Persona:** {persona}\n\n{response}"})
