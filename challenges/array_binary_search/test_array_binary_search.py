from .array_binary_search import binary_search

def test_this_file_works():
  pass

def test_binary_search_module_exists():
  return binary_search

def test_value_gets_found():
  expected = 1
  actual = binary_search([1,2,3,4],2)
  assert expected == actual

def test_returns_negative_one_if_not_in_array():
  expected = -1
  actual = binary_search([1,2,3,4],11)
  assert expected == actual

def test_works_with_odd_numbered_array():
  expected = 1
  actual = binary_search([1,2,3,4,5],2)
  assert expected == actual

def test_works_with_empty_list():
  expected = -1
  actual = binary_search([],9)
  assert expected == actual

def test_works_really_long_arrays():
  expected = 9
  array=[]
  for i in range(0,1000):
      array.append(i)
  actual = binary_search(array,9)
  assert expected == actual


