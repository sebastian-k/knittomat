import math
import tkinter as tk
from tkinter import ttk


def toggle_target_stitches_entry():
    if use_target_stitches.get():
        entry_target_stitches.grid(row=3, column=1, sticky="ew")
    else:
        entry_target_stitches.grid_remove()
        entry_target_stitches.delete(0, tk.END)  # Reset to default value


def toggle_angle_entry():
    if use_angle.get():
        entry_angle.grid(row=2, column=1, sticky="ew")
    else:
        entry_angle.grid_remove()
        entry_angle.delete(0, tk.END)  # Reset to default value


def calculate():
    current_stitches = int(entry_current_stitches.get())
    edgeangle = 45  # Default angle (45 degrees)

    if use_angle.get():
        edgeangle = float(entry_angle.get())

    # if the user entered a custom stitchcount we will use that,
    # otherwise we calculate it by using the sinus
    try:
        target_stitches = int(entry_target_stitches.get())  # use custom stitchcount
    except ValueError:
        target_stitches = round(current_stitches / math.sin(math.radians(edgeangle)))  # use sinus

    # main calculations
    # the EASY part
    # ###############

    # increases and gaps
    increases = target_stitches - current_stitches
    # the increases are typciall worked between two existing stitches.
    # so we have to leave out the very last stitch.
    gaps = current_stitches - 1

    # so far, so easy
    # let's display this in the GUI
    result_label.config(
        text=f'{target_stitches} - Target amount of stitches.\n'
        f'{gaps} - Available gaps between your existing stitches where you can work your increases.\n'
        f'{increases} - Amount of increase stitches.\n\n'
    )

    # the COMPLICATED part
    # ####################
    # disclaimer: for anyone who is looking into this:
    # i really suck at math. if there is a logical or mathematical error, let me know ;)

    # case 1: less increases than gaps, probably the more common part
    if increases < gaps:
        distribution = int(gaps / increases)
        rest = gaps % increases

        # phrase for UI
        if distribution == 1:
            phrase = ""
        else:
            phrase = f'{distribution}. '

        if rest <= 1:
            result_label.config(
                text=result_label.cget("text") + f'Make a new stitch after each {phrase}existing stitch.'
            )
        else:
            rest_distribution = round(increases / rest) + 1
            result_label.config(
                text=result_label.cget("text") +
                f'In theory, you could make an increase after every {phrase}stitch.\n'
                f'However, you would end up with {rest} stitches too much.\n'
                f'So, follow the pattern of an increase after each {phrase}stitch,\n'
                f'but after each {rest_distribution}. increase work one regular stitch more before you knit the next increase stitch.'
            )
    # case 2: more increases than gaps
    else:
        distribution = round(increases / gaps)
        theoretical_distribution = distribution * gaps
        rest = theoretical_distribution - increases

        if rest < 0:
            no_rest = False
            many_few = "few"
            more_less = "more"

        elif rest > 0:
            many_few = "many"
            more_less = "less"
            no_rest = False
        else:
            no_rest = True
        rest_phrase = abs(rest)

        # phrasing
        plural = ""
        if distribution > 1:
            plural = "es"
        increase_phrase = f'{distribution} new stitch{plural}'

        if no_rest:
            result_label.config(
                text=result_label.cget("text") + f'Make {increase_phrase} after each existing stitch.'
            )
        else:
            rest_distribution = abs(int(gaps / rest))
            remainder = gaps % rest
            if remainder == 0:
                last_stitch_phrase = ""
            else:
                last_stitch_phrase = f'...\n But ahh, too bad, there is still {remainder} left. Just work it anywhere you like :)'
            result_label.config(
                text=result_label.cget("text") +
                f'In theory, you could make {increase_phrase} after every existing stitch.\n'
                f'However, you would end up with {theoretical_distribution} stitches, which is {rest_phrase} too {many_few}.\n'
                f'So, follow the pattern of increasing {increase_phrase} after each existing stitch,\n'
                f'but work one increase stitch {more_less} after each {rest_distribution}. regular stitch. \n'
                f'{last_stitch_phrase}'
            )


# HELp


def display_help():
    # Create a new window for help text
    help_window = tk.Toplevel(app)
    help_window.title("Help")

    help_text = '''
    Case 1:
    You have knitted a triangle shape with a 45° angle and want to pick up stitches along the 45° angle side,
    and then continue knitting parallel to that edge, but maintaining the same overall height.
    (Effectively creating a trapezoid.)

    A bit of trigonometry: the long side of a right-angled triangle is C, the other 2 sides are a and b.
    (Or you have half a triangle with one 90° angle and one 45° angle. Let's call that side still b)
    So let's say you want to knit into b.
    To maintain the same height of the triangle (h) you need to increase the stitch count along b.

    In a triangle with a 45° angle you have to increase by dividing the edge stitches of b by the sinus of 45°, which is about 0.707.
    That will give you the amount of needed stitches.
    The script will also try to calculate the pattern for how to distribute the increases.

    Case 2:
    Your used a different decrease pattern, so the angle between C and b is not 45°.
    -> Enable the checkbox where you can enter a custom angle.

    Case 3:
    You just want to know how to increase evenly from stitch count A to stitch count B.
    -> Enable the checkbox to enter a custom target stitch count.
    '''

    help_label = ttk.Label(help_window, text=help_text, justify="left")
    help_label.pack()


# UI

# Create the main application window
app = tk.Tk()
app.title("Knittomat")

# Create a frame for padding
padding_frame = ttk.Frame(app, padding=20)
padding_frame.grid(row=0, column=0)

# Create labels, entry fields, and a result label within the frame
style = ttk.Style()
style.configure("TLabel", padding=(10, 2))
style.configure("TEntry", padding=(10, 2))
style.configure("TCheckbutton", padding=(10, 2))

# Current Stitches
label_current_stitches = ttk.Label(padding_frame, text="Amount of bound off edge stitches:")
entry_current_stitches = ttk.Entry(padding_frame)
entry_current_stitches.insert(0, 10)  # Set default value

# Target Stitches
label_target_stitches = ttk.Label(padding_frame, text="Target amount of stitches:")
entry_target_stitches = ttk.Entry(padding_frame)

# Angle
label_angle = ttk.Label(padding_frame, text="Angle (in degrees):")
entry_angle = ttk.Entry(padding_frame)

# Layout
label_current_stitches.grid(row=0, column=0, sticky="w")
entry_current_stitches.grid(row=0, column=1, sticky="ew")

# Checkbox for custom angle
use_angle = tk.IntVar()
use_angle_check = ttk.Checkbutton(
    padding_frame,
    text="Use a custom angle (in degrees):",
    variable=use_angle,
    command=toggle_angle_entry,
)
use_angle_check.grid(row=2, column=0, columnspan=2, sticky="w")

# Initially, hide the angle input field
entry_angle.grid_remove()
# Checkbox to enable/disable target stitches input
use_target_stitches = tk.IntVar()
use_target_stitches_check = ttk.Checkbutton(
    padding_frame,
    text="Use a custom target stitch count:",
    variable=use_target_stitches,
    command=toggle_target_stitches_entry,
)
use_target_stitches_check.grid(row=3, column=0, columnspan=2, sticky="w")

# Initially, hide the target stitches input field
entry_target_stitches.grid_remove()

calculate_button = ttk.Button(
    padding_frame,
    text="Calculate",
    command=calculate,
)
calculate_button.grid(row=4, column=0, columnspan=2, sticky="w")
# "Help" button to display help text

help_button = ttk.Button(padding_frame, text="Help / Instructions", command=display_help)
help_button.grid(row=4, column=1, columnspan=2)

result_label = ttk.Label(
    padding_frame,
    text="",
)
result_label.grid(row=5, column=0, columnspan=2, sticky="w")

padding_frame.grid_rowconfigure(4, minsize=100)

app.mainloop()
