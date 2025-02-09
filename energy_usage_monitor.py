import matplotlib.pyplot as plt
import streamlit as st

# power consumption per hour of appliances (in watts)
COMPUTER_POWER_PER_HOUR = 170
FAN_POWER_PER_HOUR = 50
LIGHT_POWER_PER_HOUR = {"Incandescent": 60, "CFL": 15, "LED": 10}

AC_TYPES = {
  'Window AC': 1500,
  'Split AC': 1200,
  'Inverter AC': 1000,
  'Portable AC': 1800,
  'Central AC': 2000
}
REFRIGERATOR_POWER_PER_HOUR = 180
WASHING_MACHINE_POWER_PER_HOUR = 500
TV_POWER_PER_HOUR = 100
############################################################################

st.set_page_config(layout="wide")

# Add a title to the sidebar
st.sidebar.title("Select Option")

# Get the selected option
selected_option = st.sidebar.radio(
  "Options", ("ABOUT SMART ENERGY MONITER", "GET STARTED", "TIPS TO REDUCE",
              "POWER SOURCES"))

# Show the selected analysis option
if selected_option == "ABOUT SMART ENERGY MONITER":
  st.markdown(
    "<h1 style='text-align: center; color: black; font-family: Arial, sans-serif; font-size: 50px;'>SMART ENERGY MONITOR</h1>",
    unsafe_allow_html=True)
  st.markdown(
    "<span   style='text-align: center;color: red; font-size: 35px;'>Empowering Efficiency and Awareness!</span>",
    unsafe_allow_html=True)
  st.markdown(
    "<span style='color: black; font-size: 28px;'>welcome to, </span><span   style='color: red; font-size: 35px;'>SMART ENERGY MONITER!</span>",
    unsafe_allow_html=True)
  #st.write("Please select an analysis option from the sidebar.")



  st.expander("▼ Introduction", expanded=True)
  with st.expander("▼ Introduction"):
    st.markdown(
      """
        <style>
        .custom-text {
            font-size: 24px;
            font-family: 'Times New Roman', Times, serif;
            color: black;
        }
        .custom-container {
            background-color: #f5f5f5;
            padding: 20px;
            border-radius: 5px;
        }
        </style>
        
        <div class='custom-container'>
            <p class='custom-text'>
            In today's fast-paced world, where energy consumption is on the rise and sustainability is a pressing concern, it becomes crucial to monitor and manage our energy usage effectively. The "Smart Energy Monitor" project is a cutting-edge solution designed to empower individuals and organizations with the tools and insights needed to optimize energy efficiency and foster a culture of awareness.
            </p>
        </div>
        """,
      unsafe_allow_html=True,
    )


  # Create two columns with equal width
  col1, col2 = st.columns(2)

  # Define the content of the first column
  with col1:
    with st.expander("▼ Empowering Energy Management"):
      st.markdown(
        """
        <div style='background-color: #f5f5f5; padding: 20px; border-radius: 5px;'>
            <h3 style='font-size: 30px; color: black;'>
                &#x1F50C; &#x1F341; Empowering Energy Management:
            </h3>
            <p style='font-size: 24px; color: black;'>
                The Smart Energy Monitor project revolutionizes energy management. It combines efficiency, intelligence, and awareness to empower individuals, households, and organizations. Users gain control over their energy usage, reduce waste, and contribute to a greener future. 
        </div>
        """,
        unsafe_allow_html=True,
      )

# Define the content of the second column
  with col2:
    # Add any additional content or widgets you want to display in the second column
    with st.expander("▼ User-Friendly Interface and Real-Time Monitoring:"):
      st.markdown(
        """
        <div style='background-color: #f5f5f5; padding: 20px; border-radius: 5px;'>
            <h3 style='font-size: 30px; color: black;'>
                &#x1F4BB; &#x23F1; User-Friendly Interface and Real-Time Monitoring:
            </h3>
            <p style='font-size: 24px; color: black;'>
                The project offers a user-friendly interface for easy navigation and interaction. Real-time monitoring capabilities provide up-to-date information on energy consumption. Users can make informed decisions and take immediate action to optimize energy usage.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
      )

  with st.expander("▼ Paving the Way for Sustainability:"):
    st.markdown("""
        <div style='background-color: #f5f5f5; padding: 20px; border-radius: 5px;'>
        <style>
        .expander-text {
            font-size: 24px;
        }
        </style>

        - 🛣️ <span class="expander-text">Paving the Way for Sustainability:</span>
            - ♻️ <span class="expander-text">The Smart Energy Monitor project promotes a more sustainable and energy-conscious society.</span>
            - 💡 <span class="expander-text">It provides actionable insights to help users adopt energy-efficient practices.</span>
            - 🚀 <span class="expander-text">By embracing smart technology, we can create a brighter and more efficient future.</span>
        """,
                unsafe_allow_html=True)

  st.markdown(
    "<p style='font-size: 24px; font-family: Times New Roman, serif;'>Let us embark on this journey together, embracing the power of smart technology to create a brighter and more efficient tomorrow.</p>",
    unsafe_allow_html=True)
  st.markdown(
    "<p style='font-size: 24px; font-family: Times New Roman, serif;'>Together, we can leverage the power of smart technology to make a positive impact on our planet and create a better future for generations to come.</p>",
    unsafe_allow_html=True)
  st.markdown("<p style='font-size: 24px;'>🌍🔌🌱</p>", unsafe_allow_html=True)

  st.markdown("""
    <p style='font-size: 24px; color: red;'>
        🚀 Ready to embark on an energy-saving adventure? Click "<span style='color: black;'>Get Started</span>" and unlock a world of efficiency and sustainability. Let's make a positive impact together! 💡🌱
    </p>
""",
              unsafe_allow_html=True)
elif selected_option == "GET STARTED":
  st.empty()  # Clear the main area
  st.title("Weekly Analysis")
  # Add your weekly analysis code here
  # Power consumption per hour of appliances (in watts)
  COMPUTER_POWER_PER_HOUR = 170
  FAN_POWER_PER_HOUR = 50
  LIGHT_POWER_PER_HOUR = {"Incandescent": 60, "CFL": 15, "LED": 10}
  AC_TYPES = {
    'Window AC': 1500,
    'Split AC': 1200,
    'Inverter AC': 1000,
    'Portable AC': 1800,
    'Central AC': 2000
  }
  REFRIGERATOR_POWER_PER_HOUR = 200
  WASHING_MACHINE_POWER_PER_HOUR = 500
  TV_POWER_PER_HOUR = 100

  #analysis_option = st.sidebar.radio("Select analysis option", ("Weekly", "Daily"))

  # Input
  st.sidebar.header("Weekly Usage Analysis")
  days_of_week = [
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
    'Sunday'
  ]
  weekly_bill = 0
  weekly_energy = 0
  weekly_usage = {}
  daily_bill = 0
  # State selection
  state = st.sidebar.selectbox(
    "Select your state",
    ("Select State", "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar",
     "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh",
     "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
     "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
     "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
     "Uttar Pradesh", "Uttarakhand", "West Bengal"))

  if state == "Select State":
    st.warning("Please select a state.")
  else:
    plots = []
    for day in days_of_week:
      st.sidebar.subheader(f"{day}'s Usage")
      st.sidebar.subheader("Number of Appliances")

      num_computers = st.sidebar.number_input(f"Number of Computers ({day})",
                                              value=1,
                                              key=f"computers-{day}",
                                              min_value=0)

      num_fans = st.sidebar.number_input(f"Number of Fans ({day})",
                                         value=1,
                                         key=f"fans-{day}",
                                         min_value=0)
      light_type = st.sidebar.selectbox(f"Type of Light ({day})",
                                        ("Incandescent", "CFL", "LED"),
                                        key=f"light_type-{day}")

      num_lights = st.sidebar.number_input(f"Number of Lights ({day})",
                                           value=1,
                                           key=f"lights-{day}",
                                           min_value=0)
      ac_type = st.sidebar.selectbox(f"AC Type ({day})",
                                     list(AC_TYPES.keys()),
                                     key=f"ac_type-{day}")

      num_acs = st.sidebar.number_input(f"Number of ACs ({day})",
                                        value=1,
                                        key=f"acs-{day}",
                                        min_value=0)
      num_refrigerators = st.sidebar.number_input(
        f"Number of Refrigerators ({day})",
        value=1,
        key=f"refrigerators-{day}",
        min_value=0)
      num_washing_machines = st.sidebar.number_input(
        f"Number of Washing Machines ({day})",
        value=1,
        key=f"washing_machines-{day}",
        min_value=0)
      num_tvs = st.sidebar.number_input(f"Number of TVs ({day})",
                                        value=1,
                                        key=f"tvs-{day}",
                                        min_value=0)

      st.sidebar.subheader("Usage Hours")
      computer_hours = st.sidebar.slider(f"Computer ({day})",
                                         0.0,
                                         24.0,
                                         0.0,
                                         step=0.25,
                                         key=f"computer_hours-{day}")

      fan_hours = st.sidebar.slider(f"Fan ({day})",
                                    0.0,
                                    24.0,
                                    0.0,
                                    step=0.25,
                                    key=f"fan_hours-{day}")
      light_hours = st.sidebar.slider(f"Light ({day})",
                                      0.0,
                                      24.0,
                                      0.0,
                                      step=0.25,
                                      key=f"light_hours-{day}")
      ac_hours = st.sidebar.slider(f"AC ({day})",
                                   0.0,
                                   24.0,
                                   0.0,
                                   step=0.25,
                                   key=f"ac_hours-{day}")
      refrigerator_hours = st.sidebar.slider(f"Refrigerator ({day})",
                                             0.0,
                                             24.0,
                                             0.0,
                                             step=0.25,
                                             key=f"refrigerator_hours-{day}")
      washing_machine_hours = st.sidebar.slider(
        f"Washing Machine ({day})",
        0.0,
        24.0,
        0.0,
        step=0.25,
        key=f"washing_machine_hours-{day}")
      tv_hours = st.sidebar.slider(f"TV ({day})",
                                   0.0,
                                   24.0,
                                   0.0,
                                   step=0.25,
                                   key=f"tv_hours-{day}")

      # Calculate usage
      computer_energy = num_computers * COMPUTER_POWER_PER_HOUR * computer_hours
      fan_energy = num_fans * FAN_POWER_PER_HOUR * fan_hours
      light_power = num_lights * LIGHT_POWER_PER_HOUR[light_type] * light_hours
      ac_power = AC_TYPES[ac_type]
      ac_energy = num_acs * ac_power * ac_hours
      refrigerator_energy = num_refrigerators * REFRIGERATOR_POWER_PER_HOUR * refrigerator_hours
      washing_machine_energy = num_washing_machines * WASHING_MACHINE_POWER_PER_HOUR * washing_machine_hours
      tv_energy = num_tvs * TV_POWER_PER_HOUR * tv_hours
      total_power_consumption = (computer_energy + fan_energy + light_power +
                                 ac_energy + refrigerator_energy +
                                 washing_machine_energy + tv_energy) / 1000

      bill_amount = 0
      if state == "Andhra Pradesh":
        if total_power_consumption <= 100:
          bill_amount = total_power_consumption * 1.00
        elif total_power_consumption <= 200:
          bill_amount = 100 + (total_power_consumption - 50) * 1.50
        elif total_power_consumption <= 500:
          bill_amount = 550 + (total_power_consumption - 200) * 2.00
        else:
          bill_amount = 1550 + (total_power_consumption - 400) * 2.0
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )

      elif state == "Arunachal Pradesh":
        if total_power_consumption <= 50:
          bill_amount = total_power_consumption * 2.00
        elif total_power_consumption <= 200:
          bill_amount = 100 + (total_power_consumption - 50) * 3.00
        elif total_power_consumption <= 400:
          bill_amount = 550 + (total_power_consumption - 200) * 4.00
        else:
          bill_amount = 1550 + (total_power_consumption - 400) * 5.00
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )
      elif state == "Assam":
        if total_power_consumption <= 120:
          bill_amount = total_power_consumption * 2.00
        elif total_power_consumption <= 240:
          bill_amount = 240 + (total_power_consumption - 120) * 3.00
        elif total_power_consumption <= 360:
          bill_amount = 600 + (total_power_consumption - 240) * 3.50
        elif total_power_consumption <= 480:
          bill_amount = 1020 + (total_power_consumption - 360) * 4.00
        elif total_power_consumption <= 600:
          bill_amount = 1620 + (total_power_consumption - 480) * 4.50
        else:
          bill_amount = 2520
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )
      elif state == "Bihar":
        if total_power_consumption <= 50:
          bill_amount = total_power_consumption * 2.50
        elif total_power_consumption <= 100:
          bill_amount = 125 + (total_power_consumption - 50) * 3.00
        elif total_power_consumption <= 200:
          bill_amount = 275 + (total_power_consumption - 100) * 3.50
        elif total_power_consumption <= 300:
          bill_amount = 725 + (total_power_consumption - 200) * 4.00
        else:
          bill_amount = 1125 + (total_power_consumption - 300) * 5.00
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )
      elif state == "Chhattisgarh":
        if total_power_consumption <= 50:
          bill_amount = total_power_consumption * 2.60
        elif total_power_consumption <= 100:
          bill_amount = 130 + (total_power_consumption - 50) * 3.10
        elif total_power_consumption <= 200:
          bill_amount = 340 + (total_power_consumption - 100) * 3.60
        elif total_power_consumption <= 400:
          bill_amount = 760 + (total_power_consumption - 200) * 4.10
        elif total_power_consumption <= 800:
          bill_amount = 1560 + (total_power_consumption - 400) * 4.60
        else:
          bill_amount = 3960 + (total_power_consumption - 800) * 5.10
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )
      elif state == "Goa":
        if total_power_consumption <= 100:
          bill_amount = total_power_consumption * 3.00
        elif total_power_consumption <= 200:
          bill_amount = 300 + (total_power_consumption - 100) * 4.00
        elif total_power_consumption <= 300:
          bill_amount = 700 + (total_power_consumption - 200) * 5.00
        else:
          bill_amount = 1200 + (total_power_consumption - 300) * 5.75
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )
      elif state == "Gujarat":
        if total_power_consumption <= 50:
          bill_amount = total_power_consumption * 2.75
        elif total_power_consumption <= 100:
          bill_amount = 137.50 + (total_power_consumption - 50) * 3.25
        elif total_power_consumption <= 200:
          bill_amount = 325 + (total_power_consumption - 100) * 3.75
        elif total_power_consumption <= 300:
          bill_amount = 700 + (total_power_consumption - 200) * 4.25
        else:
          bill_amount = 1150 + (total_power_consumption - 300) * 4.75
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )
      elif state == "Jharkhand":
        if total_power_consumption <= 50:
          bill_amount = total_power_consumption * 2.60
        elif total_power_consumption <= 100:
          bill_amount = 130 + (total_power_consumption - 50) * 3.10
        elif total_power_consumption <= 200:
          bill_amount = 340 + (total_power_consumption - 100) * 3.60
        elif total_power_consumption <= 400:
          bill_amount = 760 + (total_power_consumption - 200) * 4.10
        elif total_power_consumption <= 800:
          bill_amount = 1560 + (total_power_consumption - 400) * 4.60
        else:
          bill_amount = 3960 + (total_power_consumption - 800) * 5.10
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )
      elif state == "Karnataka":
        if total_power_consumption <= 30:
          bill_amount = total_power_consumption * 3.50
        elif total_power_consumption <= 100:
          bill_amount = 105 + (total_power_consumption - 30) * 4.00
        elif total_power_consumption <= 200:
          bill_amount = 385 + (total_power_consumption - 100) * 5.00
        elif total_power_consumption <= 500:
          bill_amount = 885 + (total_power_consumption - 200) * 6.00
        else:
          bill_amount = 3085 + (total_power_consumption - 500) * 6.50
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )
      elif state == "Kerala":
        if total_power_consumption <= 40:
          bill_amount = total_power_consumption * 2.50
        elif total_power_consumption <= 100:
          bill_amount = 100 + (total_power_consumption - 40) * 3.00
        elif total_power_consumption <= 200:
          bill_amount = 220 + (total_power_consumption - 100) * 3.50
        elif total_power_consumption <= 300:
          bill_amount = 670 + (total_power_consumption - 200) * 4.00
        else:
          bill_amount = 1170 + (total_power_consumption - 300) * 4.50
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )
      elif state == "Madhya Pradesh":
        if total_power_consumption <= 50:
          bill_amount = total_power_consumption * 2.75
        elif total_power_consumption <= 100:
          bill_amount = 137.50 + (total_power_consumption - 50) * 3.25
        elif total_power_consumption <= 200:
          bill_amount = 325 + (total_power_consumption - 100) * 3.75
        elif total_power_consumption <= 300:
          bill_amount = 700 + (total_power_consumption - 200) * 4.25
        else:
          bill_amount = 1150 + (total_power_consumption - 300) * 4.75
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )
      elif state == "Maharashtra":
        if total_power_consumption <= 100:
          bill_amount = total_power_consumption * 3.80
        elif total_power_consumption <= 300:
          bill_amount = 380 + (total_power_consumption - 100) * 4.50
        elif total_power_consumption <= 500:
          bill_amount = 1280 + (total_power_consumption - 300) * 6.00
        else:
          bill_amount = 3280 + (total_power_consumption - 500) * 7.30
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )
      elif state == "Odisha":
        if total_power_consumption <= 50:
          bill_amount = total_power_consumption * 2.50
        elif total_power_consumption <= 200:
          bill_amount = 125 + (total_power_consumption - 50) * 3.15
        elif total_power_consumption <= 400:
          bill_amount = 632.50 + (total_power_consumption - 200) * 4.15
        elif total_power_consumption <= 500:
          bill_amount = 1490 + (total_power_consumption - 400) * 4.30
        else:
          bill_amount = 2115 + (total_power_consumption - 500) * 5.30
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )
      elif state == "Punjab":
        if total_power_consumption <= 50:
          bill_amount = total_power_consumption * 2.50
        elif total_power_consumption <= 100:
          bill_amount = 125 + (total_power_consumption - 50) * 3.75
        elif total_power_consumption <= 200:
          bill_amount = 362.50 + (total_power_consumption - 100) * 4.25
        elif total_power_consumption <= 300:
          bill_amount = 837.50 + (total_power_consumption - 200) * 5.00
        else:
          bill_amount = 1637.50 + (total_power_consumption - 300) * 6.20
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )
      elif state == "Rajasthan":
        if total_power_consumption <= 50:
          bill_amount = total_power_consumption * 3.50
        elif total_power_consumption <= 150:
          bill_amount = 175 + (total_power_consumption - 50) * 4.00
        elif total_power_consumption <= 300:
          bill_amount = 575 + (total_power_consumption - 150) * 5.00
        elif total_power_consumption <= 500:
          bill_amount = 1325 + (total_power_consumption - 300) * 6.00
        else:
          bill_amount = 3125 + (total_power_consumption - 500) * 6.50
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )

      elif state == "Tamil Nadu":
        if total_power_consumption <= 100:
          bill_amount = total_power_consumption * 3.00
        elif total_power_consumption <= 200:
          bill_amount = 300 + (total_power_consumption - 100) * 3.50
        elif total_power_consumption <= 500:
          bill_amount = 650 + (total_power_consumption - 200) * 4.60
        else:
          bill_amount = 2570 + (total_power_consumption - 500) * 6.60
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )
      elif state == "Telangana":
        if total_power_consumption <= 50:
          bill_amount = total_power_consumption * 2.60
        elif total_power_consumption <= 100:
          bill_amount = 130 + (total_power_consumption - 50) * 3.10
        elif total_power_consumption <= 200:
          bill_amount = 335 + (total_power_consumption - 100) * 3.60
        elif total_power_consumption <= 400:
          bill_amount = 815 + (total_power_consumption - 200) * 4.00
        else:
          bill_amount = 1815 + (total_power_consumption - 400) * 4.50
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )
      elif state == "Tripura":
        if total_power_consumption <= 50:
          bill_amount = total_power_consumption * 3.75
        elif total_power_consumption <= 200:
          bill_amount = 187.50 + (total_power_consumption - 50) * 4.25
        elif total_power_consumption <= 500:
          bill_amount = 750 + (total_power_consumption - 200) * 5.50
        else:
          bill_amount = 3050 + (total_power_consumption - 500) * 6.50
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )
      elif state == "Uttar Pradesh":
        if total_power_consumption <= 100:
          bill_amount = total_power_consumption * 4.00
        elif total_power_consumption <= 200:
          bill_amount = 400 + (total_power_consumption - 100) * 4.50
        elif total_power_consumption <= 500:
          bill_amount = 850 + (total_power_consumption - 200) * 5.00
        else:
          bill_amount = 2350 + (total_power_consumption - 500) * 6.00
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )
      elif state == "Himachal Pradesh":
        if total_power_consumption <= 50:
          bill_amount = total_power_consumption * 3.75
        elif total_power_consumption <= 150:
          bill_amount = 187.50 + (total_power_consumption - 50) * 4.25
        else:
          bill_amount = 562.50 + (total_power_consumption - 150) * 5.00
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )
      elif state == "Haryana":
        if total_power_consumption <= 40:
          bill_amount = total_power_consumption * 2.50
        elif total_power_consumption <= 100:
          bill_amount = 100 + (total_power_consumption - 40) * 3.70
        elif total_power_consumption <= 150:
          bill_amount = 350 + (total_power_consumption - 100) * 4.80
        elif total_power_consumption <= 200:
          bill_amount = 670 + (total_power_consumption - 150) * 5.50
        else:
          bill_amount = 1120 + (total_power_consumption - 200) * 6.50
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )
      elif state == "Manipur":
        if total_power_consumption <= 30:
          bill_amount = total_power_consumption * 4.00
        elif total_power_consumption <= 100:
          bill_amount = 120 + (total_power_consumption - 30) * 5.00
        elif total_power_consumption <= 200:
          bill_amount = 470 + (total_power_consumption - 100) * 6.00
        elif total_power_consumption <= 300:
          bill_amount = 1070 + (total_power_consumption - 200) * 6.50
        else:
          bill_amount = 1870 + (total_power_consumption - 300) * 7.00
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )
      elif state == "Nagaland":
        if total_power_consumption <= 100:
          bill_amount = total_power_consumption * 4.00
        elif total_power_consumption <= 200:
          bill_amount = 400 + (total_power_consumption - 100) * 5.50
        elif total_power_consumption <= 300:
          bill_amount = 1150 + (total_power_consumption - 200) * 6.50
        elif total_power_consumption <= 400:
          bill_amount = 1900 + (total_power_consumption - 300) * 7.50
        else:
          bill_amount = 3150 + (total_power_consumption - 400) * 8.50
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )
      elif state == "Mizoram":
        if total_power_consumption <= 50:
          bill_amount = total_power_consumption * 3.50
        elif total_power_consumption <= 100:
          bill_amount = 175 + (total_power_consumption - 50) * 4.00
        elif total_power_consumption <= 200:
          bill_amount = 475 + (total_power_consumption - 100) * 5.50
        elif total_power_consumption <= 300:
          bill_amount = 1275 + (total_power_consumption - 200) * 6.00
        else:
          bill_amount = 2475 + (total_power_consumption - 300) * 7.50
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )
      elif state == "Sikkim":
        if total_power_consumption <= 50:
          bill_amount = total_power_consumption * 3.50
        elif total_power_consumption <= 150:
          bill_amount = 175 + (total_power_consumption - 50) * 4.00
        elif total_power_consumption <= 300:
          bill_amount = 575 + (total_power_consumption - 150) * 4.50
        else:
          bill_amount = 1300 + (total_power_consumption - 300) * 5.00
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )
      elif state == "Uttarakhand":
        if total_power_consumption <= 100:
          bill_amount = total_power_consumption * 3.75
        elif total_power_consumption <= 150:
          bill_amount = 375 + (total_power_consumption - 100) * 4.25
        elif total_power_consumption <= 200:
          bill_amount = 637.50 + (total_power_consumption - 150) * 5.00
        elif total_power_consumption <= 300:
          bill_amount = 1125 + (total_power_consumption - 200) * 5.75
        else:
          bill_amount = 1900 + (total_power_consumption - 300) * 6.50
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )
      elif state == "West Bengal":
        if total_power_consumption <= 75:
          bill_amount = total_power_consumption * 4.00
        elif total_power_consumption <= 150:
          bill_amount = 337.50 + (total_power_consumption - 75) * 5.00
        elif total_power_consumption <= 300:
          bill_amount = 812.50 + (total_power_consumption - 150) * 5.50
        elif total_power_consumption <= 500:
          bill_amount = 1625 + (total_power_consumption - 300) * 6.00
        else:
          bill_amount = 3625 + (total_power_consumption - 500) * 6.50
        st.write(
          f"Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )
      elif state == "Meghalaya":
        if total_power_consumption <= 100:
          bill_amount = total_power_consumption * 5.00
        elif total_power_consumption <= 200:
          bill_amount = 500 + (total_power_consumption - 100) * 6.00
        elif total_power_consumption <= 300:
          bill_amount = 1100 + (total_power_consumption - 200) * 7.00
        else:
          bill_amount = 1900 + (total_power_consumption - 300) * 8.00
        st.write(
          f" Your {day}'s electricity bill for {total_power_consumption} kWh is Rs. {bill_amount:.2f}"
        )
      # Add daily usage and bill to weekly totals
      weekly_usage[day] = total_power_consumption
      weekly_bill += bill_amount
      weekly_energy += total_power_consumption
      formatted_bill = round(weekly_bill, 4)



      fig, ax = plt.subplots(figsize=(8, 6))
      energy_usage = {
        'Computer': computer_energy,
        'Fan': fan_energy,
        'Light': light_power,
        'AC': ac_energy,
        'Refrigerator': refrigerator_energy,
        'Washing Machine': washing_machine_energy,
        'TV': tv_energy
      }

      colours = [
        'blue', 'orange', 'red', 'teal', 'fuchsia', 'cornflowerblue', 'bisque'
      ]
      #col1, col2 = st.columns(2)

      ax.bar(energy_usage.keys(),
             energy_usage.values(),
             color=colours,
             alpha=0.5)
      ax.set_title(f"{day}'s Energy Usage")
      ax.set_xlabel("Appliance")
      ax.set_ylabel("Energy Consumption (Watts)")
      ax.tick_params(axis='x', rotation=45)

      # Add the plot to the list
      plots.append(fig)
    col1, col2 = st.columns(2)
    for i, day in enumerate(days_of_week):
      # Display the plot in each column
      col = col1 if i % 2 == 0 else col2
      col.pyplot(plots[i])
    st.subheader("Total Weekly Energy Consumption")
    st.write(f"{weekly_energy:.4f} kilowatts")
    st.subheader("Total Weekly Bill")
    st.write(f"Rs. {formatted_bill:.4f}")

    # Store the daily usage in the weekly_usage dictionary
    plt.figure(figsize=(10, 6))
    plt.bar(weekly_usage.keys(), weekly_usage.values(), color='blue')
    # Find the highest day usage
    highest_day = max(weekly_usage, key=weekly_usage.get)
    # Highlight the highest day usage with a different color
    highest_index = list(weekly_usage.keys()).index(highest_day)
    plt.bar(highest_day, weekly_usage[highest_day], color='red')

    plt.xlabel("Day of the Week")
    plt.ylabel("Power Consumption (kWh)")
    plt.title("Weekly Power Consumption")
    st.pyplot(plt)
    plt.show()
    st.subheader("monthly bill based on the above weekly analysis is")
    st.write(f"Rs. {formatted_bill*4.28:.4f}")

elif selected_option == "TIPS TO REDUCE":
  st.empty()
  st.title("Electricity Consumption Reduction Tips")

  with st.expander("Computer"):

    st.subheader("Tips to reduce computer electricity consumption:")
    st.write(
      "1. Turn off your computer and monitor when not in use, especially overnight."
    )
    st.write(
      "2. Enable power-saving features to put the computer to sleep or hibernate after a period of inactivity."
    )
    st.write(
      "3. Consider using a laptop instead of a desktop, as laptops generally consume less power."
    )
    st.write(
      "4. Use more energy-efficient computer components and peripherals.")

  with st.expander("Fan"):
    st.subheader("Tips to reduce fan electricity consumption:")
    st.write(
      "1. Use fans only in occupied rooms, and turn them off when leaving.")
    st.write(
      "2. Consider using ceiling fans instead of air conditioners whenever possible."
    )
    st.write(
      "3. Clean and maintain your fans regularly to ensure optimal performance."
    )

  with st.expander("Lighting"):
    st.subheader("Tips to reduce lighting electricity consumption:")
    st.write(
      "1. Switch from incandescent bulbs to energy-efficient CFL or LED bulbs."
    )
    st.write("2. Turn off lights in unoccupied rooms.")
    st.write(
      "3. Make use of natural light during the day by opening curtains and blinds."
    )

  with st.expander("Air Conditioner"):
    st.subheader("Tips to reduce air conditioner electricity consumption:")
    st.write(
      "1. Set the temperature to an energy-efficient level (around 24-26°C or 75-78°F)."
    )
    st.write(
      "2. Use fans along with the AC to help circulate cool air more effectively."
    )
    st.write(
      "3. Seal any gaps or leaks around windows and doors to prevent cool air from escaping."
    )
    st.write("4. Service and clean your AC regularly for better efficiency.")

  with st.expander("Refrigerator"):
    st.subheader("Tips to reduce refrigerator electricity consumption:")
    st.write(
      "1. Set the refrigerator temperature to the recommended levels (around 3-5°C or 37-41°F) and the freezer at -18°C (0°F)."
    )
    st.write(
      "2. Keep the refrigerator well-organized to minimize door openings and cold air loss."
    )
    st.write("3. Ensure the door seals are tight and in good condition.")

  with st.expander("Washing Machine"):
    st.subheader("Tips to reduce washing machine electricity consumption:")
    st.write(
      "1. Use the washing machine with a full load to maximize efficiency.")
    st.write(
      "2. Use cold water for washing when possible, and avoid using the dryer by hanging clothes to dry."
    )

  with st.expander("TV"):
    st.subheader("Tips to reduce TV electricity consumption:")
    st.write("1. Enable power-saving features on your TV.")
    st.write(
      "2. Turn off the TV when not actively watching, instead of leaving it on standby."
    )

  with st.expander("General Tips"):
    st.subheader("General tips to reduce electricity consumption:")
    st.write(
      "- Unplug chargers, power strips, and other electronics when they're not in use, as they can draw power even when idle."
    )
    st.write(
      "- Use power strips to easily turn off multiple devices at once, preventing standby power consumption."
    )
    st.write(
      "- Consider investing in energy-efficient appliances with a high ENERGY STAR rating."
    )
    st.write(
      "- Conduct an energy audit of your home to identify areas where energy efficiency can be improved."
    )
    st.write(
      "- Use smart plugs or home automation systems to schedule and control the operation of appliances."
    )

elif selected_option == "POWER SOURCES":
  st.empty()
  import streamlit as st
  import matplotlib.pyplot as plt
  import numpy as np

  # Data
  labels = [
    'Thermal Power', 'Wind Power', 'Solar Power', 'Hydropower',
    'Biomass/Others', 'Nuclear Power'
  ]
  ranges = [(65, 70), (10, 15), (5, 10), (10, 15), (3, 7), (2, 4)]
  colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

  # Extracting ranges
  lower_bounds = [r[0] for r in ranges]
  upper_bounds = [r[1] for r in ranges]

  # Create a horizontal bar graph
  fig, ax = plt.subplots(figsize=(8, 6))

  # Styling the graph
  bar_list = ax.barh(labels, upper_bounds, color=colors)
  ax.barh(labels,
          np.subtract(upper_bounds, lower_bounds),
          left=lower_bounds,
          color='white')

  # Title and labels
  ax.set_title('Electricity Generation Sources in India', fontweight='bold')
  ax.set_xlabel('Percentage Range')

  # Gridlines
  ax.xaxis.grid(True, linestyle='--', linewidth=0.5)

  # Function to highlight the button on hover
  def highlight_button(index):
    for i, bar in enumerate(bar_list):
      if i == index:
        bar.set_color('red')
      else:
        bar.set_color('grey')

  # Streamlit app
  st.set_option('deprecation.showPyplotGlobalUse', False)  # To avoid warning
  st.title('Electricity Generation Sources in India')

  # Display buttons side by side with red style
  col1, col2 = st.columns(2)
  with col1:
    button_1 = st.button(labels[0])
    button_2 = st.button(labels[1])
    button_3 = st.button(labels[2])
  with col2:
    button_4 = st.button(labels[3])
    button_5 = st.button(labels[4])
    button_6 = st.button(labels[5])

  # Highlight the selected button
  if button_1:
    highlight_button(0)
  elif button_2:
    highlight_button(1)
  elif button_3:
    highlight_button(2)
  elif button_4:
    highlight_button(3)
  elif button_5:
    highlight_button(4)
  elif button_6:
    highlight_button(5)

  # Display the chart using Streamlit
  st.pyplot(fig)

  import streamlit as st

  # Part 1: Power Sources in India
  part1_text = '''
  ## <span style="font-family: Times New Roman; color: #3366ff; font-size: 24px;">Part 1: Power Sources in India</span>
  
  India relies on a diverse mix of power sources to meet its electricity demands. The major power sources in India include:
  
  1. <span style="font-family: Times New Roman; color: #ff3300; font-size: 18px;">Thermal Power</span>: Thermal power plants primarily use coal as a fuel source to generate electricity. They contribute a significant portion of India's power generation but also contribute to air pollution and greenhouse gas emissions.
  
  2. <span style="font-family: Times New Roman; color: #33cc33; font-size: 18px;">Wind Power</span>: India has vast wind energy potential, and wind power has been harnessed through wind turbines installed in various regions. It is a clean and renewable energy source.
  
  3. <span style="font-family: Times New Roman; color: #ff9900; font-size: 18px;">Solar Power</span>: With abundant sunlight, India has seen rapid growth in solar power installations. Solar panels capture sunlight and convert it into electricity, making it a clean and sustainable energy option.
  
  4. <span style="font-family: Times New Roman; color: #ffcc99; font-size: 18px;">Hydropower</span>: Hydropower plants utilize the energy of flowing water to generate electricity. India has several large and small hydropower projects, offering a reliable and renewable energy source.
  
  5. <span style="font-family: Times New Roman; color: #990099; font-size: 18px;">Biomass/Others</span>: Biomass power plants use organic matter, such as agricultural residues and municipal waste, to produce electricity. It helps in waste management and utilizes renewable resources.
  
  6. <span style="font-family: Times New Roman; color: #cc33cc; font-size: 18px;">Nuclear Power</span>: Nuclear power plants generate electricity through nuclear fission. Nuclear energy provides a significant share of India's electricity and contributes to a low-carbon energy mix.
  '''

  # Part 2: Reasons to Reduce Power Consumption
  part2_text = '''
  ## <span style="font-family: Times New Roman; color: #3366ff; font-size: 24px;">Part 2: Reasons to Reduce Power Consumption</span>
  
  While these power sources contribute to meeting India's growing energy demands, it is crucial to reduce power consumption for several reasons:
  
  1. <span style="font-family: Times New Roman; color: #ff9900; font-size: 18px;">Environmental Impact</span>: Energy production, especially from fossil fuels, contributes to air pollution, greenhouse gas emissions, and climate change. By reducing power consumption, we can minimize these environmental impacts and work towards a cleaner and healthier environment.
  
  2. <span style="font-family: Times New Roman; color: #ff3300; font-size: 18px;">Conservation of Resources</span>: Power generation requires the utilization of natural resources such as coal, oil, and gas. By reducing power consumption, we can conserve these finite resources and ensure their availability for future generations.
  
  3. <span style="font-family: Times New Roman; color: #cc33cc; font-size: 18px;">Cost Savings</span>: Reducing power consumption can lead to lower electricity bills for individuals, businesses, and industries. Energy-efficient practices and technologies help save money and increase financial sustainability.
  
  4. <span style="font-family: Times New Roman; color: #33cc33; font-size: 18px;">Energy Security</span>: By reducing power consumption, we can reduce our dependence on imported energy sources and enhance energy security. This can be achieved through energy conservation measures and promoting the use of renewable energy sources.
  
  5. <span style="font-family: Times New Roman; color: #990099; font-size: 18px;">Sustainable Development</span>: Reducing power consumption aligns with the goal of sustainable development. It helps in achieving a balance between economic growth, social well-being, and environmental protection, ensuring a better future for generations to come.
  
  To achieve these objectives, it is essential to promote energy conservation and efficiency measures, adopt renewable energy technologies, raise awareness about power consumption patterns, and encourage responsible energy consumption habits at the individual, community, and national levels.
  '''

  # Streamlit app
  st.title('Power Sources in India')

  # Create expandable sections for each part
  with st.expander('Part 1: Power Sources in India', expanded=False):
    st.markdown(part1_text, unsafe_allow_html=True)

  st.title('Reasons to reduce')

  with st.expander('Part 2: Reasons to Reduce Power Consumption',
                   expanded=False):
    st.markdown(part2_text, unsafe_allow_html=True)
