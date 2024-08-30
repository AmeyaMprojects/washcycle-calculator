import sys
import datetime as dt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

today = dt.datetime.today()
curr_year = today.year
semester_start_date = dt.datetime(curr_year, 8, 19)
semester_end_date = dt.datetime((curr_year + 1), 6, 15)


def get_no_of_loads(no_of_washes):
    if 30 >= no_of_washes >= 0:
        return True
    else:
        return False


def no_of_days_left():
    no_of_days_left = (semester_end_date - today)   
    return no_of_days_left.days


class WashScheduleTracker(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Wash Schedule Tracker")

        # Set font for the entire application
        font = QFont("Helvetica", 12)
        self.setFont(font)

        # Create widgets
        self.label_washes = QLabel("Number of Washes Done (0-30):")
        self.entry_washes = QLineEdit()
        self.button_calculate = QPushButton("Calculate")
        self.output_text = QTextEdit()

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_washes)
        layout.addWidget(self.entry_washes)
        layout.addWidget(self.button_calculate)
        layout.addWidget(self.output_text)

        # Set layout
        self.setLayout(layout)

        # Connect button to function
        self.button_calculate.clicked.connect(self.calculate_schedule)

    def calculate_schedule(self):
        try:
            no_of_washes = int(self.entry_washes.text())
            if get_no_of_loads(no_of_washes):
                # Calculate remaining washes and days
                no_of_washes_left = 30 - no_of_washes
                total_days_left = no_of_days_left()
                increment = total_days_left / no_of_washes_left

                # Display results
                self.output_text.clear()
                self.output_text.append(f"You have {no_of_washes_left} washes left.")
                for i in range(0, int(no_of_washes_left)):
                    wash_day = today + dt.timedelta(days=i * increment)
                    self.output_text.append(f"Wash day {i+1} is {wash_day.strftime('%Y-%m-%d')}")
            else:
                self.output_text.clear()
                self.output_text.append("Please enter a number between 0 and 30.")
        except ValueError:
            self.output_text.clear()
            self.output_text.append("Please enter a valid number.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WashScheduleTracker()
    window.resize(600, 400)
    window.show()
    sys.exit(app.exec_())