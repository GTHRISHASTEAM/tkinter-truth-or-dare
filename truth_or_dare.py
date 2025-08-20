# Player list - replace or add new names as needed!
players = [
    {"name": "Player 1", "traits": ["Loves adventures", "Always late"]},
    {"name": "Player 2", "traits": ["Memes lover", "Good at pranks"]},
    {"name": "Player 3", "traits": ["Shy but wild", "Obsessed with gadgets"]},
    {"name": "Player 4", "traits": ["Sports fanatic", "Never says no to pizza"]},
    {"name": "Player 5", "traits": ["Bookworm", "Night owl"]},
    {"name": "Player 6", "traits": ["Fashionista", "Can't keep secrets"]},
    {"name": "Player 7", "traits": ["TikTok star", "Life of the party"]},
]

truths = [
    "{}: What's your most embarrassing moment? 😳",
    "{}: Who's your current crush? 👀",
    "{}: What's a habit you need to stop? 🚫",
    "{}: What's the weirdest food combo you've tried? 🍕+🍍?",
    "{}: If you had a secret power, what would it be? 🦸‍♀️",
]

dares = [
    "{}: Show the last photo in your gallery to everyone! 📸",
    "{}: Dance for 30 seconds without music. 🕺",
    "{}: Send 'I miss you' to a random contact in your phone. 📱",
    "{}: Post an embarrassing childhood photo on Instagram for 10 mins. 😂",
    "{}: Act like your favorite animal until the next turn. 🐒",
]

class TruthOrDareApp:
    def __init__(self, master):
        self.master = master
        self.master.title("🔥 Truth or Dare: Ultimate Fun 🔥")
        self.master.geometry("700x600")
        self.master.configure(bg="#ffe4e1")

        # Title
        self.title_label = tk.Label(
            master,
            text="✨ Truth or Dare: Gen Z Edition ✨",
            font=("Comic Sans MS", 22, "bold"),
            bg="#ffe4e1",
            fg="#ff4500",
        )
        self.title_label.pack(pady=20)

        # Pick Player Button
        self.player_button = tk.Button(
            master,
            text="🎲 Spin for a Player 🎲",
            font=("Comic Sans MS", 16),
            bg="#6a5acd",
            fg="white",
            command=self.pick_player,
        )
        self.player_button.pack(pady=20)

        # Player Display
        self.player_label = tk.Label(
            master,
            text="Waiting for a player... 🕺",
            font=("Comic Sans MS", 18),
            bg="#ffe4e1",
            fg="#2f4f4f",
        )
        self.player_label.pack(pady=20)

        # Truth Button
        self.truth_button = tk.Button(
            master,
            text="🧠 TRUTH 🧠",
            font=("Comic Sans MS", 14),
            bg="#1e90ff",
            fg="white",
            command=self.pick_truth,
        )
        self.truth_button.pack(pady=10)

        # Dare Button
        self.dare_button = tk.Button(
            master,
            text="🔥 DARE 🔥",
            font=("Comic Sans MS", 14),
            bg="#ff6347",
            fg="white",
            command=self.pick_dare,
        )
        self.dare_button.pack(pady=10)

        # Display Truth/Dare
        self.task_label = tk.Label(
            master,
            text="Waiting for Truth or Dare... 😎",
            font=("Comic Sans MS", 14),
            bg="#ffe4e1",
            fg="#4b0082",
            wraplength=600,
            justify="center",
        )
        self.task_label.pack(pady=20)

    def pick_player(self):
        """Randomly select a player."""
        self.current_player = random.choice(players)
        player_info = f"Player: {self.current_player['name']} 🌟\nTraits: {', '.join(self.current_player['traits'])}"
        self.player_label.config(text=player_info, fg="#008b8b")

    def pick_truth(self):
        """Assign a random truth to the current player."""
        if hasattr(self, "current_player"):
            task = random.choice(truths).format(self.current_player["name"])
            self.task_label.config(text=task, fg="#1e90ff")
        else:
            self.task_label.config(text="Pick a player first! 🎲", fg="red")

    def pick_dare(self):
        """Assign a random dare to the current player."""
        if hasattr(self, "current_player"):
            task = random.choice(dares).format(self.current_player["name"])
            self.task_label.config(text=task, fg="#ff4500")
        else:
            self.task_label.config(text="Pick a player first! 🎲", fg="red")


def main():
    root = tk.Tk()
    app = TruthOrDareApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

