#** start of main.py **

full_dot = '●'
empty_dot = '○'

def create_character(char_name, strength, intelligence, charisma):
    # --- Name validation ---
    if not isinstance(char_name, str):
        return "The character name should be a string"
    if len(char_name) > 10:
        return "The character name is too long"
    if " " in char_name:
        return "The character name should not contain spaces"

    # --- Stats validation (no loop, check each one) ---
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return "All stats should be integers"
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"

    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"

    # --- Build output ---
    def stat_line(label, value):
        return f"{label} {full_dot * value}{empty_dot * (10 - value)}"

    return (
        char_name + "\n" +
        stat_line("STR", strength) + "\n" +
        stat_line("INT", intelligence) + "\n" +
        stat_line("CHA", charisma)
    )


#** end of main.py **

