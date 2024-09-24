import tkinter as tk

def calculate_BMR_no_bodyfat_man_or_women(W, H, A):
    BMR = (13.397 * W) + (4.799 * H) - (5.677 * A) + 5 + 88.362
    return BMR

def calculate_BMR_bodyfat_man_(W, bf):
    lbm = (W * (bf * 0.01) - W) * -1
    BMR = 370 + (21.6 * lbm)
    return BMR

def calculate_womenBMR(W, H, A):
    BMR = 665.1 + (9.563 * W) + (1.85 * H) - (4.676 * A)
    return BMR

# Weight loss calculators
def easy_WL_calculator(weight_loss_entry):
    WL = float(weight_loss_entry.get())
    WL_C = WL * 3500
    SC = 500
    DTG = WL_C / SC
    DTG = round(DTG)
    return DTG, SC, WL

def medium_WL_calculator(weight_loss_entry):
    WL = float(weight_loss_entry.get())
    WL_C = WL * 3500
    SC = 750
    DTG = WL_C / SC
    DTG = round(DTG)
    return DTG, SC, WL

def hard_WL_calculator(weight_loss_entry):
    WL = float(weight_loss_entry.get())
    WL_C = WL * 3500
    SC = 1000
    DTG = WL_C / SC
    DTG = round(DTG)
    return DTG, SC, WL

# Weight gain calculators
def suggested_surplus_WG_calculator(BMR, weight_gain_entry):
    SCS = BMR * 0.10
    NC = BMR + SCS
    WG = float(weight_gain_entry.get())
    WG_CC = WG * 3500
    DTG = WG_CC / SCS
    DTG = round(DTG)
    return SCS, NC, WG, WG_CC, DTG

def aggressive_surplus_WG_calculator(BMR, weight_gain_entry):
    SCS = BMR * 0.15
    NC = BMR + SCS
    WG = float(weight_gain_entry.get())
    WG_CC = WG * 3500
    DTG = WG_CC / SCS
    DTG = round(DTG)
    return SCS, NC, WG, WG_CC, DTG

def reckless_surplus_WG_calculator(BMR, weight_gain_entry):
    SCS = BMR * 0.20
    NC = BMR + SCS
    WG = float(weight_gain_entry.get())
    WG_CC = WG * 3500
    DTG = WG_CC / SCS
    return SCS, NC, WG, WG_CC, DTG

def calculate_bmr():
    gender = gender_var.get()
    age = float(age_entry.get())
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bodyfat = bodyfat_var.get()

    if bodyfat == "yes" and gender == "male":
        BMR = calculate_BMR_bodyfat_man_(weight, float(bodyfat_level_entry.get()))
    elif bodyfat == "no" and gender == "male":
        BMR = calculate_BMR_no_bodyfat_man_or_women(weight, height, age)
    elif bodyfat == "no" and gender == "female":
        BMR = calculate_womenBMR(weight, height, age)
    else:
        BMR = calculate_BMR_no_bodyfat_man_or_women(weight, height, age)

    result_label.config(text=f"Your BMR: {BMR}")

def calculate_weight_loss():
    BMR = float(result_label.cget("text").split(": ")[1].strip())  # Extract BMR from the label
    AL = aggressive_loss_var.get()
    if AL == "Easy":
        DTG, SC, WL = easy_WL_calculator(weight_loss_entry)
    elif AL == "Medium":
        DTG, SC, WL = medium_WL_calculator(weight_loss_entry)
    elif AL == "Hard":
        DTG, SC, WL = hard_WL_calculator(weight_loss_entry)

    result_label.config(text=f"Maintain Current Weight: {BMR}\nMeet Weight Goal: {BMR - SC}\nIn order to lose {WL} lbs, "
                             f"considering your current BMR of {BMR} calories, your caloric intake at the {AL} "
                             f"progression level should be {BMR - SC} calories per day. At this rate, you will "
                             f"reach your goal in {DTG} days. If you use 500 calories for TDEE you would have to add that to this number in this case {BMR}\n")

def calculate_weight_gain():
    BMR = float(result_label.cget("text").split(": ")[1].strip())  # Extract BMR from the label
    AL = aggressive_gain_var.get()
    if AL == "Suggested":
        SCS, NC, WG, WG_CC, DTG = suggested_surplus_WG_calculator(BMR, weight_gain_entry)
    elif AL == "Aggressive":
        SCS, NC, WG, WG_CC, DTG = aggressive_surplus_WG_calculator(BMR, weight_gain_entry)
    elif AL == "Reckless":
        SCS, NC, WG, WG_CC, DTG = reckless_surplus_WG_calculator(BMR, weight_gain_entry)

    result_label.config(text=f"Maintain Current Weight: {BMR}\nMeet Weight Goal: {NC}\nIn order to gain {WG} lbs, "
                             f"considering your current BMR of {BMR} calories, your caloric intake at the {AL} "
                             f"progression level should be {NC} calories per day. At this rate, you will reach "
                             f"your goal in {DTG} days. If you use 500 calories for TDEE you would have to add that to this number in this case {NC+SCS}\n")

root = tk.Tk()
root.title("BMR Calculator")
root.configure(bg ="red")

gender_var = tk.StringVar()
bodyfat_var = tk.StringVar()
aggressive_loss_var = tk.StringVar()
aggressive_gain_var = tk.StringVar()

# GUI elements for collecting user information
gender_label = tk.Label(root, text="Gender:")
gender_label.pack()
gender_entry = tk.Entry(root, textvariable=gender_var)
gender_entry.pack()

age_label = tk.Label(root, text="Age:")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

weight_label = tk.Label(root, text="Weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

height_label = tk.Label(root, text="Height (cm):")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

bodyfat_label = tk.Label(root, text="Do you know your bodyfat level? (yes/no):")
bodyfat_label.pack()
bodyfat_entry = tk.Entry(root, textvariable=bodyfat_var)
bodyfat_entry.pack()

bodyfat_level_label = tk.Label(root, text="What's your bodyfat level? (if known):")
bodyfat_level_label.pack()
bodyfat_level_entry = tk.Entry(root)
bodyfat_level_entry.pack()

# Weight loss entry
weight_loss_label = tk.Label(root, text="How much weight would you like to lose?:")
weight_loss_label.pack()
weight_loss_entry = tk.Entry(root)
weight_loss_entry.pack()

# Buttons to calculate BMR and weight loss/gain
bmr_button = tk.Button(root, text="Calculate BMR", command=calculate_bmr)
bmr_button.pack()

loss_label = tk.Label(root, text="Choose weight loss aggressiveness:")
loss_label.pack()
loss_option = tk.OptionMenu(root, aggressive_loss_var, "Easy", "Medium", "Hard")
loss_option.pack()

loss_button = tk.Button(root, text="Calculate Weight Loss", command=calculate_weight_loss)
loss_button.pack()

# Weight gain entry
weight_gain_label = tk.Label(root, text="How much weight would you like to gain?:")
weight_gain_label.pack()
weight_gain_entry = tk.Entry(root)
weight_gain_entry.pack()

gain_label = tk.Label(root, text="Choose weight gain aggressiveness:")
gain_label.pack()
gain_option = tk.OptionMenu(root, aggressive_gain_var, "Suggested", "Aggressive", "Reckless")
gain_option.pack()

gain_button = tk.Button(root, text="Calculate Weight Gain", command=calculate_weight_gain)
gain_button.pack()

# Label to display the results
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
# Example of transitioning calculator into an interactive one