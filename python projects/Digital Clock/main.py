# Importing the tkinter module for GUI development
import tkinter as tk  

 # Importing strftime to format the time
from time import strftime 
# Create the main window of the application
root = tk.Tk()  
# Set the title of the window
root.title("Digital Clock")  

# Define a function to update the time on the clock
def time():
    # Get the current time and date as a formatted string
    string = strftime("%H:%M:%S %p \n %D") 
      # Update the label with the new time
     # Format: Hours:Minutes:Seconds AM/PM and Date
    label.config(text=string)
     # Schedule the `time` function to run again after 1000 ms (1 second)
    label.after(1000, time) 

# Create a label widget to display the time
label = tk.Label(
    # Add the label to the main window
    root,  
        # Set font to Calibri, size 50, bold
    font=("calibri", 50, 'bold'),
      # Set the background color to black
    background='black', 
      # Set the text color to white
    foreground='white' 
)

 # Position the label in the center of the window
label.pack(anchor='center') 

# Call the `time` function to start the clock
time()

# Run the main event loop of the application
root.mainloop()
