import re

def convert_word_list_to_frequency_table(word_list, exclude_stop_words=True):
  """
  Converts a list of words to a dictionary containing word frequencies. Optionally excludes stop words.

  Args:
      word_list: A list of words.
      exclude_stop_words: A boolean flag indicating whether to exclude stop words (default: True).

  Returns:
      A dictionary mapping words to their frequencies.
  """

  word_count = {}
  stop_words = set()

  # Load stop words from file if needed
  if exclude_stop_words:
    try:
      with open("stop_words.txt", "r") as stop_words_file:
        stop_words.update(word.lower() for word in stop_words_file.read().split())
    except FileNotFoundError:
      print("Error: Stop words file 'stop_words.txt' not found. Skipping stop words.")

  for word in word_list:
    if exclude_stop_words and word.lower() in stop_words:
      continue  # Skip stop words if enabled
    word_count[word.lower()] = word_count.get(word.lower(), 0) + 1

  return word_count

# Example usage
text = "This is an example text with some stop words like the and a."
word_list = re.split(r"\s+", text.lower())  # Split text into lowercase words

# Count frequencies with stop words excluded
frequency_table = convert_word_list_to_frequency_table(word_list)
print(frequency_table)

# Count frequencies with stop words included (optional)
frequency_table_all = convert_word_list_to_frequency_table(word_list, exclude_stop_words=False)
print(frequency_table_all)