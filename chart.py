import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import threading

class Chart:
    def __init__(self, labels: list, values: list):
        self.labels = labels
        self.values = values
        self.exps = [0.03, 0.05, 0.09]
        self.fig, self.ax = None, None
        self.ani = None

        input_thread = threading.Thread(target=self.input_data)
        input_thread.start()

        self.create_pie_chart()

    def create_pie_chart(self) -> None:
        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        exp = [random.choice(self.exps) for i in range(len(self.values))]
        self.ax.pie(self.values, labels=self.labels, autopct=f'%.1fч', explode=exp, shadow=True)
        self.ani = animation.FuncAnimation(fig=self.fig, func=self.animate, interval=1000, save_count=100)
        plt.show()

    def animate(self, i) -> None:
        plt.cla()
        if len(self.labels) != len(self.values):
            raise IOError('Length input data is uncorrect')
        exp = [random.choice(self.exps) for i in range(len(self.values))]
        self.ax.axis('equal')
        self.ax.pie(self.values, labels=self.labels, autopct=f'%.1fч', shadow=True)
        if len(self.values) > 0:
            self.ax.legend(loc='best')

    def input_data(self) -> None:
        while True:
            category = input("Введите категорию: ")
            try:
                value = float(input("Введите число: "))
            except ValueError:
                print('Нужно ввести число!')
                continue
            self.labels.append(category)
            self.values.append(value)

def start_app() -> None:
    Chart([], [])
