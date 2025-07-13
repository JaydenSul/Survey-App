import streamlit as st
import csv
import os
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
filename = "apple_surveys.csv"

survey_number = 1
if os.path.exists(filename):
    with open(filename, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)
        existing_rows = [row for row in reader if row]
        if existing_rows and existing_rows[-1][0].isdigit():
            last_survey = int(existing_rows[-1][0])
            survey_number = last_survey + 1

name = st.text_input("Enter your name")

if "devices_list" not in st.session_state:
    st.session_state.devices_list = []

device = st.text_input("Enter one favorite Apple device")

if st.button("Add device"):
    if device:
        st.session_state.devices_list.append(device)

st.write(f"Thanks, {name}! You have added these devices:")
for i, d in enumerate(st.session_state.devices_list):
    col1, col2 = st.columns([8, 1])
    col1.write(f"- {d}")
    if col2.button("X", key=f"remove_{i}"):
        st.session_state.devices_list.pop(i)
        st.experimental_rerun()

if st.button("Submit Survey"):
    write_header = not os.path.exists(filename) or os.path.getsize(filename) == 0
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        if write_header:
            writer.writerow(["SurveyNumber", "Name", "Device", "Timestamp"])
        for device in st.session_state.devices_list:
            writer.writerow([survey_number, name, device, timestamp])
    st.success(f"Survey #{survey_number} saved to {filename}")

