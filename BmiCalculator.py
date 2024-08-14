import tkinter


def calculateBMI():
    weight = weight_input.get()
    cm_height = height_input.get()


    if cm_height == "" or weight == "":
        result_label.config(text="Enter both weight and height")
        return

    try:
        m_height = float(cm_height) / 100
        body_mass_index = float(weight) / (m_height * m_height)
    except ValueError:
        result_label.config(text="Enter a valid number!")
        return

    bmi_result = f"BMI: {body_mass_index:.2f}\n"

    if body_mass_index < 18.5:
        result_label.config(text=bmi_result + "You are underweight")
    elif 18.5 <= body_mass_index < 24.9:
        result_label.config(text=bmi_result + "You are of normal weight")
    elif 24.9 <= body_mass_index < 29.9:
        result_label.config(text=bmi_result + "You are overweight")
    elif 29.9 <= body_mass_index < 34.9:
        result_label.config(text=bmi_result + "You are obese")
    elif body_mass_index >= 34.9:
        result_label.config(text=bmi_result + "You are extremely obese")


my_window = tkinter.Tk()
my_window.title("BMI Calculator")
my_window.config(padx=30, pady=30)

height_input_label = tkinter.Label(text="Enter your height here (cm) :")
height_input_label.pack()

height_input = tkinter.Entry(width=10)
height_input.pack()



weight_input_label = tkinter.Label(text="Enter your weight here (kg) :")
weight_input_label.pack()

weight_input = tkinter.Entry(width=10)
weight_input.pack()

my_button = tkinter.Button(text="Calculate", width=10, command=calculateBMI)
my_button.pack()

result_label = tkinter.Label()
result_label.pack()

my_window.mainloop()
