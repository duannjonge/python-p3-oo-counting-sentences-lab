#!/usr/bin/env python3
import re
class MyString:
  def __init__(self,value="") -> None:
#value="" allows the attribute to be called with or without a value
    self._value=value

  def get_value(self):
     return self._value

    
  def set_value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

  def is_sentence(self):
       # Check if the value ends with a period
        return self._value.endswith('.')
  def is_question(self):
      return self._value.endswith('?')
  
  def is_exclamation(self):
      return self._value.endswith('!')
  
  def count_sentences(self):
        # Split the text based on sentence-ending punctuation marks
    sentences = [sentence.strip() for sentence in re.split(r'[.!?]', self._value) if sentence.strip()]
    return len(sentences)
  
  value=property(get_value,set_value)

my_string1 = MyString("Is this a question?")
my_string2 = MyString("This is not a question")

print(my_string1.is_question())  # True
print(my_string2.is_question())  # False


  
