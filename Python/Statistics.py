import os
import matplotlib.pyplot as plt

usernames = ["new_account", "old_account", "another_account", "account4"]  # Replace with your usernames

accuracies = []
accuracy_labels = []
sum = 0
mean = 0

for i in range(20):
    games = 0
    lower = i * 5
    upper = (i + 1) * 5
    accuracy_labels.append((lower + upper)/2)
    for user in usernames:
        directory = "Records/" + user + "/"
        txt_file = os.path.join(directory, str(float(lower)) + "-" + str(float(upper)) + ".txt")
        if os.path.exists(txt_file):
            with open(txt_file, "r") as file:
                games = games + len(file.readlines())
    accuracies.append(games)
    sum = sum + games
    mean = mean + games*(lower + upper)/2
mean = mean / sum

median_index = 0
median_number = sum / 2
while median_number > 0:
    print(median_index)
    median_number = median_number - accuracies[median_index]
    median_index += 1

median = median_index * 5 + 2.5

mode_frequencies = max(accuracies)
mode_indices = [i for i, v in enumerate(accuracies) if v == mode_frequencies]
modes = [i*5 + 2.5 for i in mode_indices]

print(accuracies)
print(f"Total games analyzed: {sum}")
print(f"Mean accuracy: {mean:.2f}")
print(f"Median accuracy: {median:.2f}")
print(f"Mode accuracy: {modes}")

x_values = [i * 5 + 2.5 for i in range(20)]

plt.figure(figsize=(14, 5))
plt.plot(x_values, accuracies, marker='o')

plt.axvline(x=mean, color='r', linestyle='--', label=f"Mean: {mean:.2f}%")
plt.axvline(x=median, color='g', linestyle='-.', label=f"Median: {median:.2f}%")
for mode in modes:
    plt.axvline(x=mode, color='b', linestyle=':', label=f"Mode: {mode:.2f}%")

plt.xticks(x_values, accuracy_labels)

handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())

plt.gcf().canvas.manager.set_window_title("Accuracies")
plt.subplots_adjust(left=0.05, right=0.98, top=0.93, bottom=0.1)
plt.title("Accuracies")
plt.xlabel("Accuracy (%)")
plt.ylabel("Number of Games")
plt.grid(True)
plt.show()