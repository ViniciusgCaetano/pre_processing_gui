from File import File

def test_LowercaseColumn_WithNonTextColumn_MakesNothing():
    test_file = File()
    test_file.read_excel('tests\dummy_sheet.xlsx')
    initial_table = test_file.get_file()
    test_file.apply_lowercase('Units') # A numeric column
    final_table = test_file.get_file()

    
    assert initial_table.equals(final_table) 