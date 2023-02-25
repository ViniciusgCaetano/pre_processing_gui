from File import File

def test_Undo_WithoutPreviousState_MakesNothing():
    test_file = File()
    test_file.read_excel('tests\dummy_sheet.xlsx')
    initial_state = test_file.get_file()
    test_file.undo()
    final_state = test_file.get_file()


    assert initial_state.equals(final_state) 