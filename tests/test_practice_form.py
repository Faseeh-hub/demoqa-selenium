# tests/test_practice_form.py
import os
from .pages.practice_form_page import PracticeFormPage

def test_practice_form(browser):
    form = PracticeFormPage(browser)
    form.open_form()
    sample = os.path.abspath("tests/artifacts/sample.png")
    # ensure tests/artifacts/sample.png exists (create one or put any image)
    form.fill_form("Razi", "Sohail", "razi@example.com", "3001234567", sample)
    assert form.submitted()
