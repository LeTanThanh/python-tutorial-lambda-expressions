if __name__ == "__main__":
  # What are Python lambda expressions

  """
  Python lambda expressions allow you to define anonymous functions.

  Anonymous functions are functions without names.
  The anonymous functions are useful when you neef to use them once.

  A lambda expression typically contains one or more arguments, but it can have only one expression.

  The following shows the lambda expression syntax:

  lambda parameters: expression

  It's equivalent to the following function with the "anonymous" name:

  def anonymous(parameters):
    return expression
  """

  # Functions that accept a function example

  def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)

  """
  The get_ful_name() function accepts three arguments:
  - first_name
  - last_name
  - A function that will format the full name (formater).
  In turn, the formatter function accepts two arguments first name and last name.
  """

  def first_last(first_name, last_name):
    return f"{first_name} {last_name}"

  def last_first(first_name, last_name):
    return f"{last_name} {first_name}"

  print(get_full_name("John", "Doe", first_last))
  print(get_full_name("John", "Doe", last_first))

  lambda_first_last = lambda first_name, last_name: f"{first_name} {last_name}"
  lambda_last_first = lambda first_name, last_name: f"{last_name} {first_name}"

  print(get_full_name("John", "Doe", lambda_first_last))
  print(get_full_name("John", "Doe", lambda_last_first))

  # Functions that return a function example

  def times(n):
    return lambda x: x * n

  double = times(2)
  print(type(double)) # <class 'function'>
  print(double(10))   # 20

  triple = times(3)
  print(type(triple)) # <class 'function'>
  print(triple(10))   # 30
