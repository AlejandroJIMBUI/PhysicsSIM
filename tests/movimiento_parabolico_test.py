import sys
import numpy as np
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QDoubleSpinBox, QPushButton, QGroupBox
)
from PyQt6.QtCore import QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class ParabolicMotionSimulator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Parabolic Motion Simulator")
        self.setGeometry(100, 100, 1920, 1080)

        # Simulation parameters
        self.velocity = 20.0  # m/s
        self.angle = 45.0     # degrees
        self.gravity = 9.81   # m/s²
        self.time = 0
        self.max_time = 10
        self.trajectory = []

        self.init_ui()

    def init_ui(self):
        main_widget = QWidget()
        main_layout = QHBoxLayout()

        control_panel = QGroupBox("Simulation Parameters")
        control_layout = QVBoxLayout()

        self.velocity_spin = self.create_spinbox("Initial velocity (m/s):", 0, 100, self.velocity, 0.1)
        self.angle_spin = self.create_spinbox("Launch angle (degrees):", 0, 90, self.angle, 1)
        self.gravity_spin = self.create_spinbox("Gravity (m/s²):", 1, 20, self.gravity, 0.1)

        self.start_button = QPushButton("Start Simulation")
        self.start_button.clicked.connect(self.start_simulation)
        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_simulation)

        control_layout.addWidget(self.velocity_spin)
        control_layout.addWidget(self.angle_spin)
        control_layout.addWidget(self.gravity_spin)
        control_layout.addWidget(self.start_button)
        control_layout.addWidget(self.reset_button)
        control_layout.addStretch()
        control_panel.setLayout(control_layout)

        graph_panel = QWidget()
        graph_layout = QVBoxLayout()

        self.figure = Figure(figsize=(10, 8), dpi=100)
        self.canvas = FigureCanvas(self.figure)

        self.ax1 = self.figure.add_subplot(211)
        self.ax2 = self.figure.add_subplot(212)

        graph_layout.addWidget(self.canvas)
        graph_panel.setLayout(graph_layout)

        main_layout.addWidget(control_panel, stretch=1)
        main_layout.addWidget(graph_panel, stretch=3)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_simulation)

    def create_spinbox(self, label, min_val, max_val, default, step):
        container = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(QLabel(label))
        spinbox = QDoubleSpinBox()
        spinbox.setRange(min_val, max_val)
        spinbox.setValue(default)
        spinbox.setSingleStep(step)
        layout.addWidget(spinbox)
        container.setLayout(layout)

        key = label.split(" ")[0].lower() + "_spinbox"
        setattr(self, key, spinbox)
        return container

    def start_simulation(self):
        self.velocity = self.initial_spinbox.value()
        self.angle = np.radians(self.launch_spinbox.value())
        self.gravity = self.gravity_spinbox.value()

        self.max_time = 2 * self.velocity * np.sin(self.angle) / self.gravity
        self.time = 0
        self.trajectory = []

        self.ax1.clear()
        self.ax1.set_title("Projectile Trajectory")
        self.ax1.set_xlabel("Distance (m)")
        self.ax1.set_ylabel("Height (m)")
        self.ax1.grid(True)

        self.ax2.clear()
        self.ax2.set_title("Height vs Time")
        self.ax2.set_xlabel("Time (s)")
        self.ax2.set_ylabel("Height (m)")
        self.ax2.grid(True)

        self.timer.start(50)

    def update_simulation(self):
        if self.time > self.max_time:
            self.timer.stop()
            return

        x = self.velocity * np.cos(self.angle) * self.time
        y = self.velocity * np.sin(self.angle) * self.time - 0.5 * self.gravity * self.time**2

        self.trajectory.append((self.time, x, y))

        times = [t for t, _, _ in self.trajectory]
        xs = [x for _, x, _ in self.trajectory]
        ys = [y for _, _, y in self.trajectory]

        self.ax1.clear()
        self.ax1.plot(xs, ys, 'b-')
        self.ax1.set_title(f"Projectile Trajectory (v₀={self.velocity:.1f} m/s, θ={np.degrees(self.angle):.1f}°)")
        self.ax1.set_xlabel("Distance (m)")
        self.ax1.set_ylabel("Height (m)")
        self.ax1.grid(True)

        self.ax2.clear()
        self.ax2.plot(times, ys, 'r-')
        self.ax2.set_title("Height vs Time")
        self.ax2.set_xlabel("Time (s)")
        self.ax2.set_ylabel("Height (m)")
        self.ax2.grid(True)

        self.canvas.draw()
        self.time += 0.05

    def reset_simulation(self):
        self.timer.stop()
        self.time = 0
        self.trajectory = []
        self.ax1.clear()
        self.ax2.clear()
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ParabolicMotionSimulator()
    window.show()
    sys.exit(app.exec())
