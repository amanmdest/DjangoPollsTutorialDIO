import pytest

from django.utils import timezone
from polls.models import Question


@pytest.mark.django_db
def test_question_was_published_recently_returns_true():
    pub_date = timezone.now()

    question = Question.objects.create(question_text="naniii?", pub_date=pub_date, active=True)

    assert question.was_published_recently() is True
    assert str(question) == "naniii?"