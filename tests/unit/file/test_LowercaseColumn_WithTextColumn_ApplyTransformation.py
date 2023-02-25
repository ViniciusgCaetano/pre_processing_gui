from File import File

def test_LowercaseColumn_WithTextColumn_ApplyTransformation():
    test_file = File()
    test_file.read_excel('tests\dummy_sheet.xlsx')
    test_file.apply_lowercase('Item')
    table = test_file.get_file()

    
    assert table['Item'].equals(table['Lowercase Column']) 