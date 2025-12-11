# life_progress_bar.py
# A beginner-friendly Python project to visualize life progress with an aesthetic terminal bar.

import sys

# --- CONFIGURATION ---
DEFAULT_LIFESPAN = 80  # Default assumed average lifespan in years
BAR_LENGTH = 50        # Length of the progress bar in characters

# ANSI Color Codes for terminal output
COLOR_GREEN = "\033[92m"  # Light Green for progress
COLOR_GRAY = "\033[90m"   # Dark Gray for remaining
COLOR_RESET = "\033[0m"   # Reset color

# ASCII Characters
CHAR_FILLED = "█"
CHAR_EMPTY = "░"

# --- CORE FUNCTIONS ---

def get_valid_input(prompt, default_value=None):
    """
    Handles user input, ensuring it is a valid positive integer.
    Includes error handling for non-numeric and negative inputs.
    """
    while True:
        try:
            # Display prompt and default value if provided
            input_text = f"{prompt} ({default_value} years): " if default_value else f"{prompt}: "
            
            user_input = input(input_text).strip()
            
            # Use default value if input is empty and a default is provided
            if not user_input and default_value is not None:
                return default_value
            
            # Convert to integer
            value = int(user_input)
            
            # Validate for positive number
            if value <= 0:
                print(f"{COLOR_GRAY}Error: Please enter a positive number greater than zero.{COLOR_RESET}")
                continue
            
            return value
            
        except ValueError:
            print(f"{COLOR_GRAY}Error: Invalid input. Please enter a whole number.{COLOR_RESET}")
        except EOFError:
            # Handle Ctrl+D/Ctrl+Z gracefully
            print("\nExiting program.")
            sys.exit(0)

def calculate_progress(age, lifespan):
    """
    Calculates the percentage of life lived and the remaining percentage.
    """
    # Ensure age does not exceed lifespan for calculation purposes
    age_clamped = min(age, lifespan)
    
    # Calculate the percentage of life lived
    percentage_lived = (age_clamped / lifespan) * 100
    
    # Calculate the percentage remaining
    percentage_remaining = 100 - percentage_lived
    
    return percentage_lived, percentage_remaining

def generate_progress_bar(percentage):
    """
    Creates the aesthetic ASCII progress bar string with color.
    """
    # Calculate the number of filled characters
    filled_chars = int(round((percentage / 100) * BAR_LENGTH))
    
    # Calculate the number of empty characters
    empty_chars = BAR_LENGTH - filled_chars
    
    # Create the bar string with colors
    bar = (
        COLOR_GREEN + (CHAR_FILLED * filled_chars) + COLOR_RESET +
        COLOR_GRAY + (CHAR_EMPTY * empty_chars) + COLOR_RESET
    )
    
    return bar

# --- ENHANCEMENT FUNCTIONS (Optional but implemented) ---

def get_life_stage(age):
    """
    Provides a simple categorization of the user's life stage.
    """
    if age < 13:
        return "Childhood"
    elif age < 20:
        return "Teenage Years"
    elif age < 40:
        return "Young Adulthood"
    elif age < 65:
        return "Middle Age"
    elif age < 80:
        return "Elder Adulthood"
    else:
        return "Golden Years"

def get_motivational_message(percentage):
    """
    Provides a motivational or reflective message based on life progress.
    """
    if percentage < 15:
        return "The journey has just begun! Every day is a new adventure."
    elif percentage < 35:
        return "You're building the foundation of your life. Keep learning and growing!"
    elif percentage < 50:
        return "Halfway to the default finish line! Time to reflect and set new goals."
    elif percentage < 75:
        return "You have a wealth of experience. Share your wisdom and enjoy the ride."
    elif percentage < 100:
        return "Every moment is precious. Focus on what truly matters."
    else:
        return "A life well-lived! Celebrate your legacy and the moments that remain."

# --- DISPLAY FUNCTION ---

def display_results(age, lifespan, percentage_lived, percentage_remaining, bar):
    """
    Prints all the calculated and generated results in a clean, aesthetic format.
    """
    
    # Get enhancement data
    life_stage = get_life_stage(age)
    message = get_motivational_message(percentage_lived)
    
    print("\n" + "="*60)
    print(f"{COLOR_GREEN}✨ LIFE PROGRESS BAR GENERATOR ✨{COLOR_RESET}".center(68))
    print("="*60 + "\n")
    
    print(f"👤 Your Age: {age} years")
    print(f"🎯 Assumed Lifespan: {lifespan} years")
    print(f"🗓️ Life Stage: {life_stage}\n")
    
    # Display the progress bar and percentage
    print(f"Progress: {percentage_lived:.2f}% Lived | {percentage_remaining:.2f}% Remaining")
    print(f"[{bar}]")
    
    # Display the motivational message
    print("\n" + "-"*60)
    print(f"💡 Reflection: {message}")
    print("-"*60 + "\n")


# --- MAIN EXECUTION ---

def main():
    """
    The main function to run the Life Progress Bar Generator.
    """
    print("Welcome to the Life Progress Bar Generator!")
    print(f"The default assumed lifespan is {DEFAULT_LIFESPAN} years.")
    
    # 1. Get user's age
    age = get_valid_input("Please enter your current age", default_value=None)
    
    # 2. Get target lifespan (optional custom input)
    lifespan = get_valid_input("Enter the assumed lifespan (or press Enter for default)", default_value=DEFAULT_LIFESPAN)
    
    # 3. Check for invalid age/lifespan combination
    if age > lifespan:
        print(f"\n{COLOR_GRAY}Note: Your age ({age}) exceeds the assumed lifespan ({lifespan}).{COLOR_RESET}")
        print(f"{COLOR_GRAY}The progress bar will show 100% lived based on this lifespan.{COLOR_RESET}")
    
    # 4. Core calculation
    percentage_lived, percentage_remaining = calculate_progress(age, lifespan)
    
    # 5. Generate visual bar
    bar = generate_progress_bar(percentage_lived)
    
    # 6. Display results
    display_results(age, lifespan, percentage_lived, percentage_remaining, bar)

if __name__ == "__main__":
    main()


