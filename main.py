from nyquist_calculator import calculate_data_rate
from input_handler import get_user_inputs
import sys

def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--cli':
        # Command-line interface
        print("Nyquist Theorem Data Rate Calculator (Noiseless Channel)")
        
        # Get inputs from the user
        bandwidth, levels = get_user_inputs()
        
        # Calculate data rate using Nyquist theorem
        try:
            data_rate = calculate_data_rate(bandwidth, levels)
            print(f"\nMaximum Data Rate: {data_rate:.2f} bits per second")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        # Launch GUI
        from gui import main as gui_main
        gui_main()

if __name__ == "__main__":
    main()
