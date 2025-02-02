import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Importing PIL for image handling

class BananaDNAExperiment:
    def __init__(self, master):
        self.master = master
        self.master.title("Banana DNA Experiment")
        self.master.geometry("800x600")
        self.master.configure(bg="#ffefd5")  # Light peach background

        # Welcome Label
        self.welcome_label = tk.Label(
            master, 
            text="🍌 Welcome to the DNA Laboratory,Today we are Going to Extract DNA from a Banana! 🍌", 
            font=("Comic Sans MS", 20, "bold"), 
            bg="#ffefd5", 
            fg="#ff4500"
        )
        self.welcome_label.pack(pady=20)

        # Load and display the PNG image
        self.image = Image.open("Banana.png")  # Replace with your image path
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(master, image=self.photo, bg="#ffefd5")
        self.image_label.pack(pady=10)

        # Name Entry Section
        self.name_label = tk.Label(
            master, 
            text="What is your name?", 
            font=("Arial", 14), 
            bg="#ffefd5", 
            fg="#8b0000"
        )
        self.name_label.pack()
        
        self.name_entry = tk.Entry(master, font=("Arial", 14), width=30)
        self.name_entry.pack(pady=10)

        # Ready Button
        self.ready_button = tk.Button(
            master, 
            text="Start Experiment 🚀", 
            command=self.ask_ready, 
            bg="#32cd32", 
            fg="white", 
            font=("Arial Black", 16), 
            width=20, 
            height=2
        )
        self.ready_button.pack(pady=20)

    def ask_ready(self):
        person = self.name_entry.get()
        if person:
            response = messagebox.askyesno(
                "Ready to Begin?", f"Hi {person}! Are you ready to find the DNA from a Banana? 🧬"
            )
            if response:
                self.start_experiment(person)
            else:
                messagebox.showinfo("Goodbye!", "Maybe next time! 👋")
                self.master.quit()
        else:
            messagebox.showwarning("Input Error", "Please enter your name to proceed.")

    def start_experiment(self, person):
        # Clear the screen for the experiment
        for widget in self.master.winfo_children():
            widget.destroy()

        # Experiment Title
        title_label = tk.Label(
            self.master, 
            text=f"Let's Begin the Experiment, {person}!", 
            font=("Comic Sans MS", 18, "bold"), 
            bg="#ffefd5", 
            fg="#ff4500"
        )
        title_label.pack(pady=20)

        # Equipment Button
        equipment_button = tk.Button(
            self.master, 
            text="Show Equipment Needed 🧪", 
            command=self.show_equipment, 
            bg="#1e90ff", 
            fg="white", 
            font=("Arial Black", 16), 
            width=25, 
            height=2
        )
        equipment_button.pack(pady=10)

        # Process Button
        process_button = tk.Button(
            self.master, 
            text="Start the Banana Process 🍌", 
            command=lambda: self.show_process(person), 
            bg="#ffa500", 
            fg="white", 
            font=("Arial Black", 16), 
            width=25, 
            height=2
        )
        process_button.pack(pady=10)

    def show_equipment(self):
        equipment_needed = [
            "Beaker 🧴", "Knife 🔪", "Mortar ⚗️", "Test Tube 🧪",
            "Wooden Splint 🪵", "Refrigerator ❄️", "Coffee Filter ☕"
        ]
        
        more_equipment = [
            "Dishwashing Liquid 🧼", "1/2 Banana 🍌",
            "Salt 🧂", "Isopropyl Alcohol 🍶"
        ]
        
        equipment_message = (
            f"Basic Equipment:\n- {', '.join(equipment_needed)}\n\n"
            f"Additional Items:\n- {', '.join(more_equipment)}"
        )
        
        messagebox.showinfo("Equipment Needed 🛠️", equipment_message)

    def show_process(self, person):
        process_steps = [
            "1. Pour the dishwashing liquid into your beaker.",
            "2. Slice the banana and mush it into the mortar.",
            "3. Cover the banana with 10% of the dishwashing liquid.",
            "4. Add a pinch of salt.",
            "5. Add the salt, banana, and dishwashing liquid into a beaker.",
            "6. Filter the contents using a coffee filter into a test tube.",
            f"7. Now comes the fun part {person}, pour chilled isopropyl alcohol (rubbing alcohol) into the test tube.",
            f"8. What do you see {person}? You should see a cloud of white on the side of the test tube.",
            f"🎉 Congratulations {person}, you have just created Banana DNA! 🎉"
        ]

        # Display each step interactively
        for step in process_steps:
            messagebox.showinfo("Process Step 🔬", step)

if __name__ == "__main__":
    root = tk.Tk()
    app = BananaDNAExperiment(root)
    root.mainloop()
