import tkinter as tk  # Library for the graphical interface
import time           # Library to get the current system time
import math           # Library for mathematical calculations (trigonometry)

# Step 2: Create the main window and canvas

# Create the main window
root = tk.Tk()
root.title("Analog Clock")

# Set the window size (optional)
root.geometry("400x400")

# Create a canvas where we will draw the clock
canvas = tk.Canvas(root, width=400, height=400, bg='dark gray')
canvas.pack()

# Draw the outer circle for the clock face (the clock boundary)
canvas.create_oval(50, 50, 350, 350, outline="black", width=4)

# Draw the inner circle (the "mirror" of the clock) in gray
canvas.create_oval(60, 60, 340, 340, outline="black", fill="gray", width=2)

# Draw the hour markers around the clock face
for i in range(12):
	# Calculate the angle for each hour marker (30 degrees apart)
	angle = math.radians(i * 30)
	
	# Calculate the start and end points for the hour markers
	x_start = 200 + 130 * math.sin(angle)
	y_start = 200 - 130 * math.cos(angle)
	x_end = 200 + 150 * math.sin(angle)
	y_end = 200 - 150 * math.cos(angle)
	
	# Draw the hour marker lines
	canvas.create_line(x_start, y_start, x_end, y_end, width=2)

# Function to draw the clock hands with improved style
def update_clock():
	# Clear the previous hands
	canvas.delete('hands')

	# Get the current time
	t = time.localtime()
	hours = t.tm_hour % 12  # 12-hour format for analog clock
	minutes = t.tm_min
	seconds = t.tm_sec

	# Calculate the angles for the hands
	second_angle = math.radians(seconds * 6)  # 360° / 60 seconds = 6° per second
	minute_angle = math.radians(minutes * 6)  # 360° / 60 minutes = 6° per minute
	hour_angle = math.radians((hours + minutes / 60) * 30)  # 360° / 12 hours = 30° per hour

	# Coordinates for the center of the clock
	center_x, center_y = 200, 200

	# --- Style the Hour Hand (thicker and shorter) ---
	hour_x = center_x + 90 * math.sin(hour_angle)
	hour_y = center_y - 90 * math.cos(hour_angle)
	canvas.create_line(center_x, center_y, hour_x, hour_y, fill="black", width=6, tags='hands')

	# --- Style the Minute Hand (slightly thinner and longer) ---
	minute_x = center_x + 130 * math.sin(minute_angle)
	minute_y = center_y - 130 * math.cos(minute_angle)
	canvas.create_line(center_x, center_y, minute_x, minute_y, fill="black", width=4, tags='hands')

	# --- Style the Second Hand (thin and red, longer than minute hand) ---
	second_x = center_x + 140 * math.sin(second_angle)
	second_y = center_y - 140 * math.cos(second_angle)
	canvas.create_line(center_x, center_y, second_x, second_y, fill="red", width=2, tags='hands')

	# Update the clock every 1000 ms (1 second)
	canvas.after(1000, update_clock)

# Call the function to start the clock
update_clock()

# Start the Tkinter main loop
root.mainloop()