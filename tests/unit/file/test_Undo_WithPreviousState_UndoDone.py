from File import File

def test_undo_WithPreviousState_UndoDone():
    test_file = File()
    test_file.read_excel('tests\dummy_sheet.xlsx')
    initial_state = test_file.get_file()

    test_file.delete_column('Region')
    test_file.undo()

    final_state = test_file.get_file()


    assert initial_state.equals(final_state) 