import CSP_6_01_Library_Basics as HW
def test_process_expenses():
    assert HW.process_expenses([10,20,30,40,50]) == [12, 23, 34, 46, 57]

def test_analyze_scores():
    assert HW.analyze_scores([77,81,86,87,90,94,95]) == (95,87)

def test_sanitize_usernames():
    assert HW.sanitize_usernames(["  Late  ", " Penalty  ", " Will  ", " Kill   ","   Me "]) == ["late","penalty","will","kill","me"]

def test_identify_outliers():
    assert HW.identify_outliers([1,2,3,4,5,1234]) == [1234]

def test_search_and_report():
    assert HW.search_and_report(["  MMMMmmmmm", " Large ", "Celery"], "Celery") == (["mmmmmmmmm","large","celery"], 1)