from .array_shift import insert_shift_array

def test_this_file_works():
  pass

def test_insert_shift_array_module_exists():
  return insert_shift_array

def test_value_gets_inserted():
  expected = [1,2,9,3,4]
  actual = insert_shift_array([1,2,3,4],9)
  assert expected == actual

def test_works_with_odd_number_of_elements():
  expected = [1,2,3,9,4,5]
  actual = insert_shift_array([1,2,3,4,5],9)
  assert expected == actual

def test_works_with_empty_list():
  expected = [9]
  actual = insert_shift_array([],9)
  assert expected == actual

def test_works_with_single_element_list():
  expected = [1,9]
  actual = insert_shift_array([1],9)
  assert expected == actual

def test_works_with_list_of_different_data_types():
  expected = ['string',[],3,3.14,{},'',26380746]
  actual = insert_shift_array(['string',[],3,{},'',26380746],3.14)
  assert expected == actual