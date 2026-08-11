
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import requests
import random

class CloudWatchtowerStudio:
    def __init__(self, root):
        self.root = root
        self.root.title('Cloud Watchtower Studio')
        self.root.configure(bg='#2b2b2b')

        # Header frame
        self.header_frame = tk.Frame(self.root, bg='#2b2b2b')
        self.header_frame.pack(fill='x')
        self.title_icon = tk.Label(self.header_frame, text='Cloud Watchtower Studio', font=('Arial', 16), bg='#2b2b2b', fg='white')
        self.title_icon.pack(side='left')
        self.subtitle = tk.Label(self.header_frame, text='Visual Cloud Infrastructure Telemetry GUI', font=('Arial', 12), bg='#2b2b2b', fg='gray')
        self.subtitle.pack(side='left', padx=10)

        # Input controls frame
        self.input_frame = tk.Frame(self.root, bg='#2b2b2b')
        self.input_frame.pack(fill='x', padx=10, pady=10)
        selfcloud_provider = tk.StringVar()
        self.cloud_provider = ttk.Combobox(self.input_frame, textvariable=cloud_provider)
        self.cloud_provider['values'] = ('AWS', 'Azure', 'Google Cloud')
        self.cloud_provider.current(0)
        self.cloud_provider.pack(side='left')
        self.resource_type = tk.StringVar()
        self.resource_type = ttk.Combobox(self.input_frame, textvariable=resource_type)
        self.resource_type['values'] = ('EC2', 'S3', 'RDS')
        self.resource_type.current(0)
        self.resource_type.pack(side='left', padx=10)
        self.threshold = tk.IntVar()
        self.threshold_slider = tk.Scale(self.input_frame, from_=0, to=100, orient='horizontal', variable=threshold)
        self.threshold_slider.pack(side='left', padx=10)
        self.refresh_button = tk.Button(self.input_frame, text='Refresh', command=self.refresh_data, bg='#4b4b4b', fg='white')
        self.refresh_button.pack(side='left', padx=10)

        # Main visualization display frame
        self.display_frame = tk.Frame(self.root, bg='#2b2b2b')
        self.display_frame.pack(fill='both', expand=True, padx=10, pady=10)
        self.tree = ttk.Treeview(self.display_frame)
        self.tree['columns'] = ('Resource', 'Usage', 'Cost')
        self.tree.column('#0', width=0, stretch='no')
        self.tree.column('Resource', anchor='w', width=100)
        self.tree.column('Usage', anchor='w', width=100)
        self.tree.column('Cost', anchor='w', width=100)
        self.tree.heading('#0', text='', anchor='w')
        self.tree.heading('Resource', text='Resource', anchor='w')
        self.tree.heading('Usage', text='Usage', anchor='w')
        self.tree.heading('Cost', text='Cost', anchor='w')
        self.tree.pack(fill='both', expand=True)

        # Status message
        self.status_message = tk.Label(self.root, text='Waiting for data...', font=('Arial', 12), bg='#2b2b2b', fg='gray')
        self.status_message.pack(fill='x', padx=10, pady=10)

    def refresh_data(self):
        # Simulate data refresh
        self.status_message['text'] = 'Refreshing data...'
        self.tree.delete(*self.tree.get_children())
        for i in range(10):
            resource = f'Resource {i}'
            usage = random.randint(0, 100)
            cost = random.uniform(0, 100)
            self.tree.insert('', 'end', values=(resource, usage, cost))
        self.status_message['text'] = 'Data refreshed.'

if __name__ == '__main__':
    root = tk.Tk()
    app = CloudWatchtowerStudio(root)
    root.mainloop()
