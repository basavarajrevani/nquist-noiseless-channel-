import tkinter as tk
from tkinter import ttk, messagebox
from nyquist_calculator import calculate_data_rate
from utils import validate_positive_float, validate_positive_int

class NyquistCalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Nyquist Calculator")
        self.root.geometry("800x700")  # Increased height for graphs
        
        # Unit conversion factors
        self.units = {
            'Hz': 1,
            'KHz': 1e3,
            'MHz': 1e6,
            'GHz': 1e9
        }
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Input frame
        input_frame = ttk.LabelFrame(main_frame, text="Input Parameters", padding="10")
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        # Bandwidth input with units
        bandwidth_frame = ttk.Frame(input_frame)
        bandwidth_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(bandwidth_frame, text="Channel Bandwidth:").grid(row=0, column=0, sticky=tk.W)
        self.bandwidth_var = tk.StringVar()
        self.bandwidth_entry = ttk.Entry(bandwidth_frame, textvariable=self.bandwidth_var, width=20)
        self.bandwidth_entry.grid(row=0, column=1, padx=5)
        
        # Unit selection
        self.unit_var = tk.StringVar(value='Hz')
        unit_combo = ttk.Combobox(bandwidth_frame, textvariable=self.unit_var, values=list(self.units.keys()), width=8, state='readonly')
        unit_combo.grid(row=0, column=2, sticky=tk.W)
        
        # Levels input
        ttk.Label(input_frame, text="Signal Levels:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.levels_var = tk.StringVar()
        self.levels_entry = ttk.Entry(input_frame, textvariable=self.levels_var)
        self.levels_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Buttons frame
        button_frame = ttk.Frame(input_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        calculate_button = ttk.Button(button_frame, text="Calculate", command=self.calculate)
        calculate_button.grid(row=0, column=0, padx=5)
        
        analyze_button = ttk.Button(button_frame, text="Analyze & Plot", command=self.analyze_range)
        analyze_button.grid(row=0, column=1, padx=5)
        
        # Result display
        result_frame = ttk.LabelFrame(main_frame, text="Result", padding="10")
        result_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=10)
        
        self.result_var = tk.StringVar(value="")
        result_label = ttk.Label(result_frame, textvariable=self.result_var, wraplength=350)
        result_label.grid(row=0, column=0)
        
        # Create notebook for graphs and analysis
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        
        # Analysis text frame
        self.analysis_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.analysis_frame, text="Text Analysis")
        
        # Create text widget for analysis
        self.analysis_text = tk.Text(self.analysis_frame, height=10, width=50)
        self.analysis_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(self.analysis_frame, orient="vertical", command=self.analysis_text.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.analysis_text.configure(yscrollcommand=scrollbar.set)
        
        # Graph frames with canvas
        self.bandwidth_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.bandwidth_frame, text="Bandwidth Graph")
        self.bandwidth_canvas = tk.Canvas(self.bandwidth_frame, width=600, height=300, bg='white')
        self.bandwidth_canvas.pack(pady=10)
        
        self.levels_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.levels_frame, text="Levels Graph")
        self.levels_canvas = tk.Canvas(self.levels_frame, width=600, height=300, bg='white')
        self.levels_canvas.pack(pady=10)
        
        # Configure grid weights
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
    def draw_graph(self, canvas, points, x_label, y_label):
        """Draw a simple line graph on the canvas"""
        canvas.delete("all")  # Clear canvas
        
        # Graph dimensions
        margin = 40
        width = 600 - 2 * margin
        height = 300 - 2 * margin
        
        # Find min/max values
        x_values = [p[0] for p in points]
        y_values = [p[1] for p in points]
        x_min, x_max = min(x_values), max(x_values)
        y_min, y_max = min(y_values), max(y_values)
        
        # Draw axes
        canvas.create_line(margin, height + margin, width + margin, height + margin, arrow=tk.LAST)  # X-axis
        canvas.create_line(margin, height + margin, margin, margin, arrow=tk.LAST)  # Y-axis
        
        # Draw labels
        canvas.create_text(width//2 + margin, height + margin + 20, text=x_label)
        canvas.create_text(margin - 30, height//2 + margin, text=y_label, angle=90)
        
        # Scale points to fit canvas
        scaled_points = []
        for x, y in points:
            x_scaled = margin + (x - x_min) * width / (x_max - x_min)
            y_scaled = height + margin - (y - y_min) * height / (y_max - y_min)
            scaled_points.append((x_scaled, y_scaled))
        
        # Draw lines between points
        for i in range(len(scaled_points) - 1):
            x1, y1 = scaled_points[i]
            x2, y2 = scaled_points[i + 1]
            canvas.create_line(x1, y1, x2, y2, fill='blue', width=2)
            canvas.create_oval(x1-3, y1-3, x1+3, y1+3, fill='blue')
        
        # Draw last point
        x, y = scaled_points[-1]
        canvas.create_oval(x-3, y-3, x+3, y+3, fill='blue')
        
    def analyze_range(self):
        try:
            # Get current values
            bandwidth = float(self.bandwidth_var.get())
            levels = int(self.levels_var.get())
            bandwidth_hz = self.convert_bandwidth(bandwidth, self.unit_var.get())
            
            # Clear previous analysis
            self.analysis_text.delete(1.0, tk.END)
            
            # Analyze bandwidth variation
            self.analysis_text.insert(tk.END, "=== Bandwidth Analysis ===\n")
            bandwidth_points = []
            for factor in [0.5, 0.75, 1.0, 1.25, 1.5]:
                b = bandwidth_hz * factor
                rate = calculate_data_rate(b, levels)
                b_display = b/self.units[self.unit_var.get()]
                self.analysis_text.insert(tk.END, 
                    f"Bandwidth: {b_display:.2f} {self.unit_var.get()} → Rate: {self.format_data_rate(rate)}\n")
                bandwidth_points.append((b_display, rate))
            
            # Draw bandwidth graph
            self.draw_graph(self.bandwidth_canvas, bandwidth_points, 
                          f"Bandwidth ({self.unit_var.get()})", "Data Rate (bps)")
            
            # Analyze levels variation
            self.analysis_text.insert(tk.END, "\n=== Signal Levels Analysis ===\n")
            levels_points = []
            for l in range(2, min(levels * 2, 9)):
                rate = calculate_data_rate(bandwidth_hz, l)
                self.analysis_text.insert(tk.END, 
                    f"Levels: {l} → Rate: {self.format_data_rate(rate)}\n")
                levels_points.append((l, rate))
            
            # Draw levels graph
            self.draw_graph(self.levels_canvas, levels_points, 
                          "Number of Signal Levels", "Data Rate (bps)")
                
        except ValueError as e:
            messagebox.showerror("Analysis Error", "Please enter valid values for bandwidth and levels first.")
    
    def convert_bandwidth(self, value, unit):
        """Convert bandwidth to Hz based on the selected unit"""
        return value * self.units[unit]
    
    def format_data_rate(self, bits_per_second):
        """Format data rate in appropriate units"""
        if bits_per_second >= 1e9:
            return f"{bits_per_second/1e9:.2f} Gbps"
        elif bits_per_second >= 1e6:
            return f"{bits_per_second/1e6:.2f} Mbps"
        elif bits_per_second >= 1e3:
            return f"{bits_per_second/1e3:.2f} Kbps"
        else:
            return f"{bits_per_second:.2f} bps"
    
    def calculate(self):
        try:
            # Get and validate inputs
            bandwidth = self.bandwidth_var.get()
            levels = self.levels_var.get()
            
            bandwidth = validate_positive_float(bandwidth, "Bandwidth must be a positive number.")
            levels = validate_positive_int(levels, "Levels must be a positive integer.")
            
            # Convert bandwidth to Hz
            bandwidth_hz = self.convert_bandwidth(bandwidth, self.unit_var.get())
            
            # Calculate result
            data_rate = calculate_data_rate(bandwidth_hz, levels)
            
            # Format and display result
            formatted_rate = self.format_data_rate(data_rate)
            input_bandwidth = f"{bandwidth} {self.unit_var.get()}"
            self.result_var.set(f"Input Bandwidth: {input_bandwidth}\nMaximum Data Rate: {formatted_rate}")
            
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

def main():
    root = tk.Tk()
    app = NyquistCalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()