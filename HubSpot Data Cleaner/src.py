import pandas as pd
import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image

ctk.set_appearance_mode("system")  
ctk.set_default_color_theme(r"debrbr.github.io\HubSpot Data Cleaner\orange.json")  


def browse_csv():
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    csv_path_entry.delete(0, ctk.END)
    csv_path_entry.insert(0, file_path)


def convert_csv_to_excel():
    try:
     
        csv_path = csv_path_entry.get()
        campaign_name = campaign_entry.get()  

    
        if not csv_path:
            messagebox.showerror("Error", "Please provide the CSV file path.")
            return

        if not campaign_name:
            messagebox.showerror("Error", "Please provide a First Marketing Campaign name.")
            return

       
        save_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
            title="Save Excel File As"
        )

        if not save_path:  
            messagebox.showinfo("Cancelled", "Save operation cancelled.")
            return

        excel_file = save_path

       
        columns_to_import = [
            'First Name', 'Last Name', 'Email', 'Job Title',
            'Company Name', 'Website', 'Country', "Mobile",
            "Direct", "Office", "HQ", 'Seniority', 'Lead Source'
        ]

  
        data = pd.read_csv(csv_path, encoding='latin1', usecols=columns_to_import)

       
        row_count = data['First Name'].notna().sum()

       
        data['Practice'] = [practice_var.get() if i < row_count else '' for i in range(len(data))]
        data['Subsidiary'] = [subsidiary_var.get() if i < row_count else '' for i in range(len(data))]
        data['Owner'] = [owner_var.get() if i < row_count else '' for i in range(len(data))]
        data['Life Cycle Stage'] = [lifecycle_var.get() if i < row_count else '' for i in range(len(data))]
        data['First Marketing Campaign'] = [campaign_name if i < row_count else '' for i in range(len(data))]

        
        data.to_excel(excel_file, index=False, engine='openpyxl')

      
        messagebox.showinfo("Success", f"Excel file created successfully: {excel_file}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


app = ctk.CTk()
app.title("HubSpot Data Cleaner")
app.geometry("800x600")


logo_img = ctk.CTkImage(light_image=Image.open(r"debrbr.github.io\HubSpot Data Cleaner\Catalyst IT Icon.png'), 
                        dark_image=Image.open(r"debrbr.github.io\HubSpot Data Cleaner\Catalyst IT Icon.png'),
                        size=(100,100))
logo_label = ctk.CTkLabel(app, text="", image=logo_img)
logo_label.pack(pady=(80,0))


logo = ctk.CTkLabel(app, text="HubSpot Data Cleaner", font=("Helvetica", 48, "bold"))
logo.pack(pady=(15,15))


csv_path_label = ctk.CTkLabel(app, text="CSV File Path:", font=("Helvetica", 15, "bold"))
csv_path_label.pack(pady=5)
csv_path_entry = ctk.CTkEntry(app, width=400)
csv_path_entry.pack(pady=5)
browse_button = ctk.CTkButton(app, text="Browse", command=browse_csv, font=("Helvetica", 13))
browse_button.pack(pady=5)


practice_var = ctk.StringVar(value="Practice")
subsidiary_var = ctk.StringVar(value="Subsidary")
owner_var = ctk.StringVar(value="Owner")
lifecycle_var = ctk.StringVar(value="Lifecycle")

practice_label = ctk.CTkLabel(app, text="Practice:", font=("Helvetica", 15, "bold"))
practice_label.pack(pady=5)
practice_dropdown = ctk.CTkComboBox(app, values=["BI", "Coeus SEP", "ERP", "Horsa"], variable=practice_var)
practice_dropdown.pack(pady=5)

subsidiary_label = ctk.CTkLabel(app, text="Subsidiary:", font=("Helvetica", 15, "bold"))
subsidiary_label.pack(pady=5)
subsidiary_dropdown = ctk.CTkComboBox(app, values=["Catalyst BI", "Catalyst Cloud ", "Catalyst ERP"], variable=subsidiary_var)
subsidiary_dropdown.pack(pady=5)

owner_label = ctk.CTkLabel(app, text="Owner:", font=("Helvetica", 15, "bold"))
owner_label.pack(pady=5)
owner_dropdown = ctk.CTkComboBox(app, values=["Ruban Sivalingam", "Sam Abear", "Abu Subhan", "Netta Mills", "David Snelson", "Marcus Adams", "Dan Packer", "Mike Cawthorn"], variable=owner_var)
owner_dropdown.pack(pady=5)

lifecycle_label = ctk.CTkLabel(app, text="Life Cycle Stage:", font=("Helvetica", 15, "bold"))
lifecycle_label.pack(pady=5)
lifecycle_dropdown = ctk.CTkComboBox(app, values=["Lead", "Opportunity", "Customer"], variable=lifecycle_var)
lifecycle_dropdown.pack(pady=5)


campaign_label = ctk.CTkLabel(app, text="First Marketing Campaign:", font=("Helvetica", 13, "bold"))
campaign_label.pack(pady=5)
campaign_entry = ctk.CTkEntry(app, width=400, placeholder_text="Enter First Marketing Campaign")
campaign_entry.pack(pady=5)


convert_button = ctk.CTkButton(app, text="Convert", command=convert_csv_to_excel, font=("Helvetica", 13))
convert_button.pack(pady=20)


creator = ctk.CTkLabel(app, text="created by Brendan de Bruyn 2024", font=("Helvetica", 10))
creator.pack(pady=10)


app.mainloop()
