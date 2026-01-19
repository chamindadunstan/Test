import tkinter as tk
from tkinter import ttk
import csv


def read_csv(filename):
    rows = []
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)

    return rows


def prepare_tree_data(rows, icon_male, icon_female):
    grouped_data = {}
    for row in rows:
        if row['Gender'] == 'Male':
            row['Icon'] = icon_male
        else:
            row['Icon'] = icon_female

        city = row['City']  # Assuming city is in the 5th column
        if city not in grouped_data:
            grouped_data[city] = []
        grouped_data[city].append(row)
    return grouped_data


def format_currency(value):
    try:
        return f"${int(value):,}"
    except ValueError:
        return value


def create_tree_view(root, employees, icons):

    frame = ttk.Frame(root)

    treeview = ttk.Treeview(frame, columns=("Salary", "Bonus"))

    treeview.heading("#0", text="Employee")
    treeview.heading("Salary", text="Salary")
    treeview.heading("Bonus", text="Bonus")

    employee_data = prepare_tree_data(
        employees, icons['female'], icons['male'])

    for city in employee_data.keys():
        # add city
        city_id = treeview.insert('', tk.END, text=city, image=icons['city'])

        # add employees in the city
        for employee in employee_data[city]:
            treeview.insert(
                city_id,
                tk.END,
                text=employee['First Name'] + ' ' + employee['Last Name'],
                values=(format_currency(employee['Salary']),
                        format_currency(employee['Bonus'])),
                image=employee['Icon']
            )
    # create a vertical scrollbar
    v_scrollbar = ttk.Scrollbar(
        frame, orient=tk.VERTICAL, command=treeview.yview)
    treeview.configure(yscrollcommand=v_scrollbar.set)

    # pack the treeview and scrollbar
    treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # package the frame
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


def main():
    root = tk.Tk()
    root.title("Employee List")

    icons = {
        'city': tk.PhotoImage(file="./assets/city_32x32.png"),
        'male': tk.PhotoImage(file="./assets/male_32x32.png"),
        'female': tk.PhotoImage(file="./assets/female_32x32.png"),
     }

    employees = read_csv("./assets/employees.csv")
    create_tree_view(root, employees, icons)

    root.mainloop()


if __name__ == '__main__':
    main()
