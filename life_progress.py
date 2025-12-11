"""
Life Progress Bar Generator
A terminal-based tool to visualize your life progress
"""

import time
import sys

def validate_age(age_str, is_lifespan=False):
    """
    Validate age input
    Returns: (is_valid, error_message, age_int)
    """
    if not age_str:
        return False, "Input cannot be empty.", 0
    
    try:
        age = float(age_str)
    except ValueError:
        return False, "Please enter a valid number.", 0
    
    # Check if it's a whole number (for age)
    if not is_lifespan and age != int(age):
        return False, "Age should be a whole number (e.g., 25).", 0
    
    age_int = int(age) if not is_lifespan else age
    
    if age_int <= 0:
        return False, "Please enter a positive number.", 0
    
    if is_lifespan and age_int < 10:
        return False, "Lifespan should be at least 10 years.", 0
    
    if not is_lifespan and age_int > 150:
        return False, "Please enter a realistic age (max 150).", 0
    
    return True, "", age_int

def calculate_percentage(age, lifespan):
    """Calculate percentage of life lived"""
    return min((age / lifespan) * 100, 100)  # Cap at 100%

def create_progress_bar(percentage, bar_length=40):
    """
    Create ASCII progress bar
    Example: [███████-------------] 35%
    """
    filled_length = int(round(bar_length * percentage / 100))
    empty_length = bar_length - filled_length
    
    # Create bar with blocks and dashes
    bar = "█" * filled_length + "─" * empty_length
    
    # Add color based on percentage (ANSI escape codes)
    if percentage < 30:
        color = "\033[92m"  # Green
    elif percentage < 60:
        color = "\033[93m"  # Yellow
    elif percentage < 80:
        color = "\033[33m"  # Orange
    else:
        color = "\033[91m"  # Red
    
    reset_color = "\033[0m"
    
    return f"[{color}{bar}{reset_color}]"

def get_life_stage(age):
    """Determine life stage based on age"""
    if age < 13:
        return "Childhood 👶"
    elif age < 20:
        return "Teen Years 🧒"
    elif age < 30:
        return "Twenties 🌟"
    elif age < 40:
        return "Thirties 💼"
    elif age < 50:
        return "Forties 🏡"
    elif age < 65:
        return "Fifties 🎯"
    else:
        return "Golden Years 👴"

def get_motivational_message(percentage):
    """Get motivational message based on life percentage"""
    if percentage < 20:
        return [
            "🌟 Your adventure is just beginning!",
            "The whole world is ahead of you.",
            "Every day is a blank page to write your story."
        ]
    elif percentage < 40:
        return [
            "🚀 You're building momentum!",
            "This is where foundations are strengthened.",
            "Your experiences are shaping who you'll become."
        ]
    elif percentage < 60:
        return [
            "💪 You're in your prime!",
            "This is your time to make a real impact.",
            "Use your wisdom to guide your energy."
        ]
    elif percentage < 80:
        return [
            "🎯 You've gained valuable perspective!",
            "Your experience is your superpower.",
            "Now you know what truly matters."
        ]
    else:
        return [
            "👑 You are a treasure of wisdom!",
            "Every moment is precious and earned.",
            "Your legacy is being written every day."
        ]

def display_header():
    """Display project header"""
    print("\n" + "="*60)
    print(" " * 15 + "🌈 LIFE PROGRESS BAR GENERATOR")
    print("="*60)
    print("\nA visual representation of your life journey")
    print("Remember: This is just a tool, not a destiny predictor!")
    print("-"*60)

def animate_progress(percentage, bar_length=40):
    """Animate the progress bar filling up"""
    print("\n📊 Generating your life progress bar...")
    
    for i in range(0, int(percentage) + 1, 2):  # Animate in steps of 2%
        current_percentage = min(i, percentage)
        bar = create_progress_bar(current_percentage, bar_length)
        sys.stdout.write(f"\rProgress: {bar} {current_percentage:.1f}%")
        sys.stdout.flush()
        time.sleep(0.05)
    
    print()  # New line after animation

def display_results(age, lifespan, percentage, life_stage, messages):
    """Display all results in a clean format"""
    print("\n" + "="*60)
    print("📈 YOUR LIFE PROGRESS REPORT")
    print("="*60)
    
    print(f"\n📅 Age: {age} years")
    print(f"🎯 Assumed Lifespan: {lifespan} years")
    print(f"🏷️  Life Stage: {life_stage}")
    print(f"📊 Percentage Lived: {percentage:.1f}%")
    
    bar = create_progress_bar(percentage)
    print(f"\n{bar} {percentage:.1f}%\n")
    
    print("💭 REFLECTION:")
    for message in messages:
        print(f"  • {message}")
    
    # Display time left
    if percentage < 100:
        years_left = lifespan - age
        print(f"\n⏳ You have approximately {years_left} years ahead!")
        print(f"   That's about {years_left * 365:,} more days to make count!")
    
    print("\n" + "="*60)

def save_to_file(age, lifespan, percentage, life_stage):
    """Save results to a text file"""
    try:
        filename = f"life_progress_{age}.txt"
        with open(filename, 'w') as file:
            file.write("="*50 + "\n")
            file.write("       LIFE PROGRESS REPORT\n")
            file.write("="*50 + "\n\n")
            file.write(f"Age: {age} years\n")
            file.write(f"Lifespan: {lifespan} years\n")
            file.write(f"Life Stage: {life_stage}\n")
            file.write(f"Percentage Lived: {percentage:.1f}%\n\n")
            
            bar = create_progress_bar(percentage).replace("\033[92m", "")\
                                                .replace("\033[93m", "")\
                                                .replace("\033[33m", "")\
                                                .replace("\033[91m", "")\
                                                .replace("\033[0m", "")
            file.write(f"{bar} {percentage:.1f}%\n")
            
            if percentage < 100:
                years_left = lifespan - age
                file.write(f"\nYou have {years_left} years and {years_left * 365} days ahead!\n")
            
            file.write("\nRemember: Every day is a new opportunity!\n")
            file.write("="*50)
        
        print(f"\n💾 Results saved to '{filename}'")
        return True
    except Exception as e:
        print(f"\n⚠️  Could not save file: {e}")
        return False

def main():
    """Main function - runs the entire program"""
    
    # Display header
    display_header()
    
    # Get user's age
    while True:
        age_input = input("\n🎂 How old are you? ")
        is_valid, error_msg, age = validate_age(age_input)
        
        if is_valid:
            break
        else:
            print(f"❌ {error_msg} Please try again.")
    
    # Ask for custom lifespan
    print("\n" + "-"*60)
    print("💡 By default, we use 80 years as average lifespan.")
    use_default = input("Would you like to use a different lifespan? (y/n): ").lower()
    
    if use_default == 'y':
        while True:
            lifespan_input = input("Enter your expected lifespan (years): ")
            is_valid, error_msg, lifespan = validate_age(lifespan_input, is_lifespan=True)
            
            if is_valid:
                if lifespan <= age:
                    print("⚠️  Lifespan should be greater than your current age. Try again.")
                else:
                    break
            else:
                print(f"❌ {error_msg}")
    else:
        lifespan = 80
        print(f"Using default lifespan: {lifespan} years")
    
    # Calculate percentage
    percentage = calculate_percentage(age, lifespan)
    
    # Get life stage and messages
    life_stage = get_life_stage(age)
    messages = get_motivational_message(percentage)
    
    # Animate the progress bar
    animate_progress(percentage)
    
    # Display results
    display_results(age, lifespan, percentage, life_stage, messages)
    
    # Ask to save results
    save_option = input("\n💾 Would you like to save these results to a file? (y/n): ").lower()
    if save_option == 'y':
        save_to_file(age, lifespan, percentage, life_stage)
    
    # Final message
    print("\n" + "✨" * 30)
    print("Thank you for using the Life Progress Bar Generator!")
    print("Remember: It's not about the years in your life,")
    print("          but the life in your years! 🌟")
    print("✨" * 30 + "\n")

# Run the program
if __name__ == "__main__":
    main()