import pandas as pd

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = self.load_data()

    def load_data(self):
        try:
            return pd.read_csv(self.file_path)
        except FileNotFoundError:
            print("File not found. Please give the correct input path.")
            return None

    def display_data(self):
        print("Current Data:")
        print(self.df)

    def add_data(self):
        new_data = {}
        print("Enter new set of data:")
        for column in self.df.columns:
            new_data[column] = input(f"Enter {column}: ")
        print("NEW DATA", new_data)
        self.df = pd.concat([self.df, pd.DataFrame([new_data])], ignore_index=True)
        self.df.to_csv(self.file_path, index=False)
        print("The data has been added successfully. Please check the latest file for the new data")

    def edit_data(self):
        self.display_data()
        try:
            row_id = int(input("Enter the row index to edit: "))
            if not isinstance(row_id, int):
                raise ValueError("Row Id is not a numerical value")
            column_required = input(f"Enter the column name that you want to edit: ")
            if row_id in self.df.index and column_required in self.df.columns:
                for column in self.df.columns:
                    if column_required.lower() == column.lower():
                        new_value = input(f"Enter new value for {column} (current: {self.df.at[row_id, column]}): ")
                        self.df.at[row_id, column] = new_value
                self.df.to_csv(self.file_path, index=False)
                print("Data updated successfully. Please check the latest file for new updates")
            else:
                if row_id not in self.df.index:
                    print("Please enter a valid row index")
                elif column_required not in self.df.columns:
                    print("Please enter a valid Column name")

        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    def delete_data(self):
        self.display_data()
        try:
            row_id = int(input("Enter the row index to delete: "))
            if not isinstance(row_id, int):
                raise ValueError("Row Id is not a numerical value")
            if row_id in self.df.index:
                self.df = self.df.drop(index=row_id)
                self.df.to_csv(self.file_path, index=False)
                print("Data deleted successfully.")
            else:
                print("Invalid row index.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    def calculate_statistics(self):
        print("Mean Values:")
        print(self.df.mean(numeric_only=True))
        print("\nMedian Values:")
        print(self.df.median(numeric_only=True))

    def filter_by_revenue(self):
        try:
            threshold = int(input("Enter the Revenue threshold: "))
            filtered_df = self.df[self.df['Revenue'] > threshold]
            print(filtered_df)
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    def filter_by_product_name(self):
        product_name = input("Enter the product name to filter ")
        filtered_df = self.df[self.df['Product'] == product_name]
        print(filtered_df)


class DataManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataManager, cls).__new__(cls)
            # Initialize fields or perform other setup here
        return cls._instance

    def process_data(self, data):
        # Perform any data processing logic here
        return data


class ApplicationDriver:
    def __init__(self, data_processor):
        self.data_processor = data_processor

    def run_application(self):
        while True:
            print("\nMenu:")
            print("1. Display Data")
            print("2. Add Data")
            print("3. Edit Data")
            print("4. Delete Data")
            print("5. Calculate Mean and Median")
            print("6. Filter by Revenue")
            print("7. Filter by Product Name")
            print("8. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.data_processor.display_data()
            elif choice == '2':
                self.data_processor.add_data()
            elif choice == '3':
                self.data_processor.edit_data()
            elif choice == '4':
                self.data_processor.delete_data()
            elif choice == '5':
                self.data_processor.calculate_statistics()
            elif choice == '6':
                self.data_processor.filter_by_revenue()
            elif choice == '7':
                self.data_processor.filter_by_product_name()
            elif choice == '8':
                print("Exiting application.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    file_path = 'data_input.csv'  # Replace with the actual file path
    data_processor = DataProcessor(file_path)
    data_manager = DataManager()
    app_driver = ApplicationDriver(data_processor)
    app_driver.run_application()